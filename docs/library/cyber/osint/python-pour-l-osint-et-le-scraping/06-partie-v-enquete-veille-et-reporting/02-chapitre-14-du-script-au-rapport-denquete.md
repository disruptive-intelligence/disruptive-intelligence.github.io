---
title: Chapitre 14 — Du script au rapport d’enquête
source: Cyber/02 OSINT/Python pour l'OSINT et le scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie V — Enquête, veille et reporting
  - index.md
---

Une enquête se termine **toujours** par un rapport lisible par un humain. Pas par un CSV brut, pas par un JSON imbriqué. Ce chapitre te fait passer de la donnée structurée au **livrable**.

## Le minimum à savoir

### Donnée ≠ rapport

|Donnée                |Rapport                          |
|----------------------|---------------------------------|
|`CSV`, `JSON`, `JSONL`|Markdown, HTML, PDF              |
|Lit par un programme  |Lu par un humain                 |
|Brut, exhaustif       |Synthétique, hiérarchisé         |
|Pas de contexte       |Source, méthode, dates, auteur   |
|Pas d’interprétation  |Conclusion bornée par la collecte|

Tu ne **publies** jamais le CSV. Tu publies un rapport qui s’**appuie** sur le CSV.

> **Rappel minimisation :** le rapport ne contient que **ce qui sert la conclusion**. Le dataset complet reste dans `data/processed/` (ou en annexe), pas dans le corps du rapport. C’est cohérent avec la minimisation appliquée à la collecte (chapitre 2) : on collecte le minimum nécessaire, on rapporte le minimum nécessaire.

### Anatomie d’un rapport OSINT

```
1. Métadonnées (qui, quand, quoi, sur quelle base)
2. Résumé exécutif (3-5 lignes maximum)
3. Périmètre et limites (ce que le rapport couvre, ce qu’il ne couvre pas)
4. Méthode (sources, outil, version, run_id)
5. Résultats
   5.1 Vue d’ensemble (chiffres clés, top-N)
   5.2 Détails (tableaux, échantillons, anomalies)
6. Conclusion (bornée à ce que la collecte autorise)
7. Reproductibilité (commande exacte pour régénérer)
```


Cette structure n’est pas négociable pour un rapport d’enquête sérieux. Elle protège contre les deux dérives classiques : conclusions trop larges et résultat irreproductible.

### Le bloc de métadonnées (obligatoire)

```markdown
---
title: Inventaire des publications — site exemple.fr
author: A. Dupont (osint-projet@example.org)
date: 2026-05-17
run_id: 20260517T140000Z
tool: mon-collecteur/0.3.1
sources:
  - https://exemple.fr/publications
data: data/processed/20260517T140000Z_publications.json
base_legale: Veille publique défensive (intérêt légitime)
limites: |
  Collecte ponctuelle d’une seule section du site,
  pendant 2 minutes, le 17 mai 2026 à 14:00 UTC.
  Ne reflète pas les changements ultérieurs.
---
```


Au format Markdown, on utilise un **front matter YAML**. C’est parsable par les outils standards (Pandoc, etc.) et lisible humainement.

### Générer du Markdown depuis Python

```python
from datetime import datetime, timezone

def generate_report(items, source_url, run_id, tool, output_path):
    """Génère un rapport Markdown simple à partir d’un dataset."""
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    auteurs = sorted({it.get("auteur", "(inconnu)") for it in items})

    lines = [
        "---",
        f"title: Rapport de collecte — {source_url}",
        f"date: {date}",
        f"run_id: {run_id}",
        f"tool: {tool}",
        f"source: {source_url}",
        f"count: {len(items)}",
        "---",
        "",
        f"# Rapport de collecte — {source_url}",
        "",
        "## Résumé",
        "",
        f"- **{len(items)}** items collectés",
        f"- **{len(auteurs)}** auteurs distincts",
        f"- Date de collecte : {date} (UTC)",
        "",
        "## Métadonnées",
        "",
        f"- `run_id` : `{run_id}`",
        f"- Outil : `{tool}`",
        f"- Source : <{source_url}>",
        "",
        "## Top 5 auteurs",
        "",
    ]

    from collections import Counter
    top = Counter(it.get("auteur", "(inconnu)") for it in items).most_common(5)
    lines.append("| Auteur | Nombre |")
    lines.append("|---|---|")
    for auteur, n in top:
        lines.append(f"| {auteur} | {n} |")

    lines += [
        "",
        "## Limites",
        "",
        "Ce rapport reflète une collecte ponctuelle à la date indiquée. ",
        "Il ne reflète pas les éventuelles modifications ultérieures de la source. ",
        "Pour rejouer la collecte, voir la section *Reproductibilité*.",
        "",
        "## Reproductibilité",
        "",
        "```bash",
        f"python -m src.main --target {source_url} --max-pages 50",
        "```",
        "",
    ]

    output_path.write_text("\n".join(lines), encoding="utf-8")
```


### Générer un tableau Markdown depuis une liste de dicts

```python
def md_table(rows, columns=None, max_rows=None):
    """Renvoie une table Markdown à partir de dicts."""
    if not rows:
        return "*(aucune donnée)*"
    columns = columns or list(rows[0].keys())
    if max_rows:
        rows = rows[:max_rows]
    out = ["| " + " | ".join(columns) + " |"]
    out.append("|" + "|".join(["---"] * len(columns)) + "|")
    for r in rows:
        vals = [str(r.get(c, "")).replace("|", "\\|") for c in columns]
        out.append("| " + " | ".join(vals) + " |")
    return "\n".join(out)
```


Note le `\\|` : les pipes dans une cellule Markdown doivent être échappés, sinon ils cassent le tableau.

### Statistiques basiques utiles

```python
from collections import Counter

def stats(items):
    """Statistiques minimales sur un dataset."""
    domains = Counter(it.get("domain", "") for it in items)
    auteurs = Counter(it.get("auteur", "") for it in items)
    return {
        "count": len(items),
        "domains_uniques": len([d for d in domains if d]),
        "top_domains": domains.most_common(5),
        "auteurs_uniques": len([a for a in auteurs if a]),
        "top_auteurs": auteurs.most_common(5),
        "premier_horodatage": min((it.get("collected_at") for it in items), default=None),
        "dernier_horodatage": max((it.get("collected_at") for it in items), default=None),
    }
```


Ces 6-7 chiffres suffisent pour la majorité des rapports. Inutile de calculer dix indicateurs si ton lecteur en regardera trois.

## Très utile en pratique

### Borner les conclusions à la collecte

C’est **la** règle d’or du rapport OSINT :

> Tout ce qu’on écrit doit être étayé par la collecte. Tout ce qui n’est pas étayé doit être explicitement formulé comme une hypothèse, une question, ou un angle mort.

|❌ Conclusion non bornée                     |✅ Conclusion bornée                                                                                          |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
|« L’entreprise X a réorienté sa stratégie. »|« Au cours des 12 dernières semaines, 8 des 10 nouvelles offres d’emploi publiées portent sur le domaine Y. »|
|« Personne ne parle de ce sujet. »          |« Aucune des 250 publications collectées sur le site Z entre A et B ne mentionne ce sujet. »                 |

La nuance est constante : on parle de **ce qu’on a vu**, pas de **ce qui existe**. C’est ce qui fait la différence entre un rapport solide et une opinion habillée.

### Conservation des preuves

Le rapport vit dans `reports/`. Mais il **pointe** vers les preuves :

```
reports/
├── 20260517_inventaire_publications.md
├── 20260517_inventaire_publications.html  (export)
└── ...

data/raw/                    ← intouché (preuves brutes)
data/processed/              ← intouché (datasets exploités)
logs/                        ← intouché (journal d’exécution)
```


Un lecteur sceptique doit pouvoir :

1. lire ton rapport,
1. ouvrir le dataset cité dans les métadonnées,
1. ouvrir le HTML brut correspondant,
1. relire ton journal d’exécution,
1. relancer ta commande pour comparer.

Si l’un de ces cinq éléments manque, le rapport est invérifiable.

### Minimisation, jusque dans le rapport

Tu as collecté avec minimisation (chapitre 2). Tu **rapportes** avec minimisation aussi :

- Ne mets pas de données personnelles dans le rapport si elles ne sont pas indispensables à la conclusion.
- Ne reproduis pas des textes longs : résume, cite court, lie vers la source.
- Ne mets pas dans le rapport ce que tu as collecté « au cas où ».

### Conversion Markdown → HTML / PDF (en bonus)

Pour livrer à un destinataire non technique :

```bash
# Markdown -> HTML simple
pip install markdown
python -c "import markdown, pathlib; print(markdown.markdown(pathlib.Path('reports/x.md').read_text()))" > reports/x.html

# Markdown -> HTML stylé / PDF (avec Pandoc, installé séparément)
pandoc reports/x.md -o reports/x.html
pandoc reports/x.md -o reports/x.pdf
```


Pandoc n’est pas un package Python ; il s’installe via le système. C’est l’outil de référence pour les conversions de documents.

## Bonus

### Génération depuis un template

Quand les rapports deviennent récurrents, un moteur de templates est plus propre :

```bash
pip install jinja2
```


```python
from jinja2 import Template

TEMPLATE = """\
# Rapport de veille — {{ titre }}

**Période** : {{ debut }} → {{ fin }}
**run_id** : `{{ run_id }}`

## Résumé

- {{ nb_items }} items collectés
- {{ nb_changements }} changements détectés

## Changements

{% for c in changements %}
- {{ c.titre }} ({{ c.date }})
{% endfor %}
"""

rapport = Template(TEMPLATE).render(
    titre="exemple.fr",
    debut="2026-05-10", fin="2026-05-17",
    run_id=run_id, nb_items=len(items), nb_changements=len(changements),
    changements=changements,
)
```


Pratique dès que la même structure se répète à chaque exécution.

### Indicateurs visuels

Pour les rapports lus en ligne, des indicateurs simples améliorent la lecture :

```
✓ Collecte réussie sur 12/12 sources
⚠ 2 sources avec un avertissement (timeouts ponctuels)
✗ 0 source en échec total
```


À utiliser avec parcimonie — ne transforme pas un rapport en sapin de Noël.

## ❌ Erreur classique

```
# Rapport sans métadonnées
"# Analyse rapide
Ces données montrent que..."

❌ Pas de date, pas de source, pas de méthode. Invérifiable, donc inutile.
✅ Front matter YAML obligatoire en tête.

# Conclusions plus larges que la collecte
"L'entreprise X investit massivement dans Y."

❌ Sur quelle base ? Combien de signaux ? Sur quelle période ?
✅ Borner précisément : "Sur la période A-B, sur la source C,
   X publications mentionnent Y."

# Inclure des données personnelles inutiles
Tableau avec nom, email, téléphone, adresse — alors que seul le nom
sert l'analyse.

❌ Violation de la minimisation, surface RGPD inutile.
✅ Ne garder que les colonnes qui servent la conclusion.

# Rapport non reproductible
"Voir les pièces jointes."

❌ Quelles pièces ? Quelle version ? Quelle commande ?
✅ Bloc "Reproductibilité" avec commande exacte et run_id.

# Copier-coller massif du dataset
Le rapport contient 300 lignes d’un tableau collé tel quel.

❌ Pas de hiérarchie, pas de synthèse.
✅ Mettre les chiffres clés et un échantillon de 10 lignes max ;
   joindre le dataset complet en annexe.
```


## Exercices

**Guidé :**

1. Reprends le dataset produit par le mini-projet « Collecteur d’articles publics » (Partie IV).
1. Écris `src/report.py` qui produit un rapport Markdown contenant :
- front matter complet,
- résumé (3-5 lignes),
- tableau top-5 auteurs,
- tableau top-5 domaines (si pertinent),
- 5 derniers articles avec titre + date + URL,
- bloc « Reproductibilité » avec la commande exacte.
1. Génère le rapport dans `reports/<run_id>_articles.md`.

**Autonome :**

1. Ajoute à ton veilleur (mini-projet Partie V 1/2) la génération d’un rapport hebdomadaire.
1. Le rapport `reports/<semaine>_veille.md` couvre les 7 derniers jours et liste :
- tous les snapshots de la semaine,
- les ajouts/retraits/modifications par jour,
- une synthèse globale (X ajouts, Y modifications, Z retraits).
1. Inclus un graphique ASCII très simple (ex. nombre de changements par jour avec `▆▂▅█▃`).

## 🧩 Mini-projet de Partie V (2/2) — *Synthétiseur de veille hebdomadaire*

**Objectif :** consolider les snapshots d’une semaine en un rapport unique exploitable.

**Entrée :** le dossier `data/snapshots/` produit par le veilleur de la Partie V (1/2).

**Cahier des charges :**

1. **Configuration** (`config/synth.yaml`) :
- nombre de jours à couvrir (défaut : 7),
- format de sortie (`md`, `html`),
- dossier de sortie,
- chemins des snapshots.
1. **Module** `src/synth.py` :
- charge tous les snapshots sur la période,
- calcule les diffs jour par jour,
- agrège : ajouts cumulés, retraits cumulés, modifications,
- identifie les **items revus** (modifiés plus d’une fois) — signal d’activité.
1. **Sortie** : `reports/<periode>_synthese.md` avec :
- front matter complet,
- résumé exécutif,
- tableau des changements par jour,
- liste des items les plus actifs,
- section « Limites » (sources non couvertes, jours manquants),
- bloc reproductibilité.
1. **Bonus** : générer aussi un export HTML lisible dans un navigateur.

## ✅ Tu sais maintenant…

- Distinguer **donnée** (CSV/JSON) et **rapport** (livrable humain)
- Structurer un rapport OSINT : métadonnées → résumé → méthode → résultats → limites → reproductibilité
- Inclure systématiquement un front matter YAML (date, run_id, tool, source, base légale)
- Générer du Markdown depuis Python (tableaux, statistiques)
- Borner les conclusions à ce que la collecte autorise
- Appliquer la minimisation **jusque dans le rapport**
- Lier le rapport à ses preuves (`data/raw/`, `data/processed/`, `logs/`)
- Convertir en HTML/PDF avec Pandoc en bonus

-----

> **🎯 Tu as terminé la Partie V.**
> 
> Tu sais maintenant **surveiller dans le temps**, **détecter des changements** et **produire un rapport** exploitable par un humain. C’est l’aboutissement d’un cycle OSINT complet : collecter, structurer, comparer, restituer.
> 
> Il ne reste qu’une étape : **mettre tout ça ensemble** dans un véritable petit outil OSINT. C’est l’objet de la Partie VI.

-----
