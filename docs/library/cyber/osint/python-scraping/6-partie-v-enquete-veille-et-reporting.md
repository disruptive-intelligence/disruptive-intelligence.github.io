---
title: PARTIE V — ENQUÊTE, VEILLE ET REPORTING
source: Cyber/02_OSINT/Python_Scraping.md
note: Python & scraping
chapter: 6
chapters: 7
---

> **Objectif de la partie :** dépasser la collecte ponctuelle. Apprendre à **surveiller dans le temps**, à **détecter les changements**, et à transformer des données en **rapport exploitable par un humain**.
> 
> Cette partie te fait basculer du « script qui collecte » à l’**outil d’enquête**.

-----


## Chapitre 13 — Veille et détection de changements

Une collecte unique te donne un instantané. Une veille te donne un **mouvement**. C’est souvent ce qui compte vraiment : qu’est-ce qui a changé, depuis quand, et dans quel sens ?

### Le minimum à savoir

#### Le principe : snapshots et comparaison

```
T0 : collecte n°1 → snapshot_T0
T1 : collecte n°2 → snapshot_T1
                       ↓
          comparer(snapshot_T0, snapshot_T1)
                       ↓
        ajouts / retraits / modifications
```

Chaque exécution de ton veilleur produit un **snapshot** complet (dataset propre), horodaté et conservé. La veille consiste à comparer deux snapshots successifs et à isoler les différences.

#### Hasher pour comparer rapidement

Comparer deux datasets dict par dict est coûteux. On préfère calculer un **hash** par enregistrement et travailler sur les hashes.

```python
import hashlib
import json

def hash_record(record, fields):
    """Hash SHA-256 stable sur certains champs d’un enregistrement."""
    base = json.dumps([record.get(f, "") for f in fields],
                      ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(base.encode("utf-8")).hexdigest()
```

> **Crucial : ne hash que ce qui compte.** Si tu hashes le HTML brut, il change à chaque requête (timestamps, jetons CSRF, nonces, scripts d’analytics). Hash uniquement les **champs métier** qui te disent réellement « cet item est le même ».

|Pour quoi        |Hasher quoi                                                                          |
|-----------------|-------------------------------------------------------------------------------------|
|Article          |`titre` + `url` (ou `titre` + `auteur` + `date`)                                     |
|Prix d’un produit|`référence_produit` (`item_id`) — la valeur du prix change, mais l’item reste le même|
|Citation         |`texte` + `auteur`                                                                   |
|Annonce d’emploi |`titre` + `entreprise` + `localisation`                                              |

#### Définir ce qui « compte » comme changement

Une fois les items identifiés (par hash de leurs **clés** stables), tu peux comparer leurs **valeurs** changeantes :

```python
# Clés stables (identifient l’item)
KEY_FIELDS = ["titre", "url"]

# Valeurs surveillées (signalent un changement)
WATCHED_FIELDS = ["prix", "disponibilite", "resume"]


def index_by_key(items):
    """Indexe une liste d’items par leur hash de clé."""
    return {hash_record(it, KEY_FIELDS): it for it in items}


def diff(old, new):
    """Retourne (ajoutés, retirés, modifiés)."""
    old_idx = index_by_key(old)
    new_idx = index_by_key(new)

    ajoutes = [new_idx[k] for k in new_idx.keys() - old_idx.keys()]
    retires = [old_idx[k] for k in old_idx.keys() - new_idx.keys()]

    modifies = []
    for k in old_idx.keys() & new_idx.keys():
        old_v = old_idx[k]
        new_v = new_idx[k]
        changements = {
            f: {"avant": old_v.get(f), "apres": new_v.get(f)}
            for f in WATCHED_FIELDS
            if old_v.get(f) != new_v.get(f)
        }
        if changements:
            modifies.append({
                "key": k,
                "titre": new_v.get("titre"),
                "changements": changements,
            })

    return ajoutes, retires, modifies
```

Ce pattern (clés stables + valeurs surveillées) est extrêmement puissant. Tu sais exactement quels items sont apparus, quels items ont disparu, et quels champs ont changé sur les items qui restent.

> **À adapter à chaque cas d’usage :**
> 
> |Type de dataset   |Clés stables (`KEY_FIELDS`)          |Valeurs surveillées (`WATCHED_FIELDS`)|
> |------------------|-------------------------------------|--------------------------------------|
> |Articles d’un site|`url`                                |`titre`, `resume`                     |
> |Produit e-commerce|`product_id`                         |`prix`, `disponibilite`, `note`       |
> |Annonces d’emploi |`titre`, `entreprise`, `localisation`|`description`, `statut`               |
> |Bulletin officiel |`reference`, `date`                  |`texte_normalise`                     |
> 
> **Règle :** la clé identifie l’item de façon stable ; la valeur surveillée est ce dont le changement t’intéresse.

#### Stocker les snapshots dans le temps

Une organisation simple, robuste, lisible :

```
data/snapshots/
├── 20260517T080000Z/
│   ├── articles.json          (snapshot complet)
│   └── meta.json              (run_id, source, count, hash global)
├── 20260518T080000Z/
│   ├── articles.json
│   └── meta.json
└── 20260519T080000Z/
    ├── articles.json
    └── meta.json
```

Chaque exécution produit un dossier horodaté avec son `run_id`. Le dernier snapshot est facilement repérable par tri sur le nom.

```python
from pathlib import Path

def latest_snapshot(snap_dir="data/snapshots"):
    """Renvoie le chemin du snapshot le plus récent, ou None."""
    base = Path(snap_dir)
    if not base.exists():
        return None
    dossiers = sorted([d for d in base.iterdir() if d.is_dir()])
    return dossiers[-1] if dossiers else None
```

#### Le squelette d’un veilleur

```python
# src/watch.py
import json
import logging
from pathlib import Path
from datetime import datetime, timezone

logger = logging.getLogger(__name__)


def run_watch(collect_fn, snap_dir="data/snapshots", change_log="logs/changes.log"):
    """Lance une collecte et compare au snapshot précédent.

    collect_fn() -> list[dict] : fonction qui produit le nouveau dataset.
    """
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    # 1. Collecte
    new_items = collect_fn()

    # 2. Charger snapshot précédent
    prev = latest_snapshot(snap_dir)
    if prev:
        old_items = json.loads((prev / "articles.json").read_text(encoding="utf-8"))
        ajoutes, retires, modifies = diff(old_items, new_items)
        logger.info("Diff vs %s : +%d ajoutés, -%d retirés, ~%d modifiés",
                    prev.name, len(ajoutes), len(retires), len(modifies))
    else:
        ajoutes, retires, modifies = new_items, [], []
        logger.info("Premier snapshot, %d items collectés", len(new_items))

    # 3. Sauver le nouveau snapshot
    out = Path(snap_dir) / run_id
    out.mkdir(parents=True, exist_ok=True)
    (out / "articles.json").write_text(
        json.dumps(new_items, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "meta.json").write_text(json.dumps({
        "run_id": run_id,
        "count": len(new_items),
        "diff_vs_previous": {
            "previous": prev.name if prev else None,
            "added": len(ajoutes),
            "removed": len(retires),
            "modified": len(modifies),
        }
    }, indent=2), encoding="utf-8")

    # 4. Logguer les changements en clair
    if prev and (ajoutes or retires or modifies):
        with open(change_log, "a", encoding="utf-8") as f:
            f.write(f"\n=== {run_id} (vs {prev.name}) ===\n")
            for a in ajoutes:
                f.write(f"+ AJOUTÉ : {a.get('titre')} — {a.get('url')}\n")
            for r in retires:
                f.write(f"- RETIRÉ : {r.get('titre')} — {r.get('url')}\n")
            for m in modifies:
                f.write(f"~ MODIFIÉ : {m['titre']}\n")
                for ch_field, ch in m["changements"].items():
                    f.write(f"    {ch_field}: {ch['avant']!r} -> {ch['apres']!r}\n")

    return {"ajoutes": ajoutes, "retires": retires, "modifies": modifies}
```

#### Bonnes pratiques de cadence

|Cas                                            |Fréquence raisonnable              |
|-----------------------------------------------|-----------------------------------|
|Veille de blog/média                           |1× par jour                        |
|Suivi de bulletins officiels (CERT, ministères)|1× à 4× par jour                   |
|Page « emplois » d’une entreprise              |1× par jour                        |
|Page produit (prix, disponibilité)             |1× à 4× par jour                   |
|Quasi temps réel                               |Quelques fois par heure **au plus**|


> **À retenir :** la veille n’est pas une **course**. Tu veux détecter un changement dans la journée, rarement à la minute. Une cadence d’une fois par jour est presque toujours suffisante pour un cas OSINT défensif. Plus rapide → tu marteles le serveur sans gain réel.

#### Ce qu’on ne fait **pas** avec un veilleur

- **Imiter un service de monitoring payant** sans en avoir le droit (bypass d’un produit commercial).
- **Surveiller en permanence** une page qu’on n’a manifestement pas besoin de surveiller en temps réel.
- **Veiller sur des contenus accessibles uniquement en session connectée** : si tu dois te connecter, ce n’est pas du public.
- **Veiller sur des données personnelles** sans cadre légal explicite.

### Très utile en pratique

#### Comparer du texte avec `difflib`

Quand un même item a changé en interne (texte d’un article modifié, par exemple), tu veux savoir **où** :

```python
import difflib

def text_diff(old_text, new_text, context=2):
    """Retourne les lignes différentes au format unified diff."""
    old_lines = old_text.splitlines(keepends=True)
    new_lines = new_text.splitlines(keepends=True)
    return "".join(difflib.unified_diff(
        old_lines, new_lines,
        fromfile="avant", tofile="apres",
        n=context,
    ))
```

Pratique pour les bulletins, communiqués, mentions légales, conditions d’utilisation.

#### Comparaison rapide par hash global

Pour décider en deux lignes si quelque chose a changé sans rentrer dans le détail :

```python
import hashlib
import json

def dataset_hash(items, fields):
    """Hash d’un dataset entier sur les champs sélectionnés."""
    parts = sorted(hash_record(it, fields) for it in items)
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


if dataset_hash(new_items, KEY_FIELDS + WATCHED_FIELDS) \
        == dataset_hash(old_items, KEY_FIELDS + WATCHED_FIELDS):
    logger.info("Aucun changement.")
    return
```

Utile pour court-circuiter la suite quand rien n’a bougé.

#### Alertes : du plus simple au plus complet

|Niveau|Mécanisme                                                |Cas d’usage                                       |
|------|---------------------------------------------------------|--------------------------------------------------|
|0     |Rien, juste les logs                                     |Veille personnelle, on lit les logs à son rythme. |
|1     |Fichier `changes.log` (texte)                            |Veille structurée — on consulte en fin de journée.|
|2     |Notification système (`notify-send`, `terminal-notifier`)|Veille personnelle réactive.                      |
|3     |Email                                                    |Veille pour soi ou pour un petit groupe.          |
|4     |Webhook Slack/Discord                                    |Équipe collaborative.                             |


> **Précautions** sur les niveaux 3 et 4 : ne diffuse pas plus que ce que tu as collecté. Si la collecte respecte la minimisation, l’alerte aussi. Pas de fuite de données sensibles par un webhook mal configuré.

#### Le réflexe : un changelog humain

En plus du `changes.log` machine, tiens un **journal de veille** humain dans `reports/` :

```markdown
# Journal de veille — Section publications [domaine.fr/publications]

## 2026-05-18
- Nouveau document : "Note d’information n°2026-12" (publiée 2026-05-17).
- Modification : page "À propos" — mise à jour du conseil d’administration.

## 2026-05-17
- Aucun changement.

## 2026-05-16
- Nouveau document : "Bilan annuel 2025".
```

Trois lignes par jour suffisent. Ce journal a souvent **plus de valeur** que le dataset lui-même, parce qu’il raconte une histoire dans le temps.

### Bonus

#### Hash du HTML normalisé

Si tu n’as pas de dataset propre mais juste une page (cas d’une veille « brute »), tu peux hasher le HTML **normalisé** (parsé et reformaté) plutôt que brut :

```python
from bs4 import BeautifulSoup
import hashlib

def stable_html_hash(html_bytes):
    """Hash du texte visible, après nettoyage des scripts et styles."""
    soup = BeautifulSoup(html_bytes, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    texte = soup.get_text(" ", strip=True)
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()
```

C’est plus stable que `hashlib.sha256(html_bytes)` pour une veille naïve.

#### Webhook Discord/Slack (avec précautions)

Exemple minimal Discord :

```python
import requests

def notify_discord(webhook_url, message):
    requests.post(webhook_url, json={"content": message[:1900]}, timeout=10)
```

- **Webhook URL** = secret. Mets-la dans `.env`.
- **Ne pousse jamais** de données personnelles ou sensibles dans un webhook public.
- **Tronque** les messages — la plupart des services rejettent les longs payloads.

### ❌ Erreur classique

```python
# Hasher le HTML brut
hash1 = hashlib.sha256(html_today).hexdigest()
hash2 = hashlib.sha256(html_yesterday).hexdigest()
# ❌ Les hashes diffèrent à cause de timestamps, nonces, scripts dynamiques.
# La page semble changer tous les jours alors qu’elle est stable.
# ✅ Hash sur du texte visible normalisé OU sur des champs métier.

# Veille toutes les minutes
# ❌ Tu marteles le site sans gain, et tu finis par te faire bloquer.
# ✅ 1× à 4× par jour suffit dans 99 % des cas.

# changes.log qui grossit sans bornes
with open("changes.log", "a") as f:
    f.write("...")
# ❌ Au bout de 2 ans, fichier illisible et impossible à analyser.
# ✅ Roulement par mois : changes-2026-05.log, changes-2026-06.log

# Alerter sur tout changement, même cosmétique
# ❌ Si tu surveilles le HTML brut sans normalisation, tu reçois
# une alerte à chaque visite. Fatigue d’alerte → tu finis par les ignorer.
# ✅ N’alerte que sur changements de champs surveillés.

# Comparer le snapshot d’hier au snapshot d’aujourd’hui sans vérifier
# que les deux ont été collectés au même endroit
# ❌ Si tu changes la cible entretemps, tu détectes des "changements"
# qui n’en sont pas.
# ✅ Stocker la cible dans le meta.json et vérifier l’égalité avant diff.
```

### Exercices

**Guidé :**

1. À partir du mini-projet « Collecteur d’articles publics » de la Partie IV, écris `src/watch.py` qui :
- relance la collecte,
- compare avec le snapshot précédent,
- écrit le diff dans `logs/changes.log`.
1. Lance deux fois à 10 minutes d’intervalle.
1. Simule un changement en éditant le snapshot précédent (modifier un titre, en supprimer un, en ajouter un fictif) et relance — vérifie que les trois cas sont détectés.

**Autonome :**

1. Écris un script `src/section_watcher.py` qui surveille **un seul** sélecteur CSS sur une page publique (par exemple le contenu d’un `<main>` ou d’une section précise).
1. Stocke le texte normalisé dans des fichiers horodatés dans `data/snapshots/<run_id>/section.txt`.
1. À chaque exécution, si le texte diffère du snapshot précédent, génère un diff Markdown lisible dans `reports/<run_id>_section_diff.md`.
1. Pense à respecter la cadence (1×/jour suffit).

### 🧩 Mini-projet de Partie V (1/2) — *Veilleur de page publique*

**Objectif :** un outil complet de veille avec snapshots versionnés, détection structurée des changements, et notification minimale.

**Cible :** la page d’accueil ou une section d’un site **public et non sensible** (idéalement une page institutionnelle, un blog technique, un site bac à sable).

**Cahier des charges :**

1. **Configuration** (`config/watch.yaml`) :
- liste d’URLs à surveiller,
- sélecteurs CSS par URL pour cibler ce qui compte,
- cadence recommandée (commentaire informatif).
1. **Architecture** :
- `src/fetch.py` (réutilisé),
- `src/parse.py` : extraction par URL et sélecteur,
- `src/diff.py` : `index_by_key`, `diff`, `dataset_hash`,
- `src/watch.py` : orchestration, snapshots, journal,
- `src/main.py` : CLI, logs, `run_id`.
1. **Sorties** :
- `data/snapshots/<run_id>/<url_safe_name>.json` (snapshot par URL),
- `data/snapshots/<run_id>/meta.json`,
- `logs/changes.log` cumulatif,
- `reports/<run_id>_summary.md` (résumé humain de l’exécution).
1. **Exécution** :
- lancement manuel (puis, en bonus, via cron / Tâches planifiées),
- sortie 0 si exécution OK, indépendamment de la présence de changements,
- log clair de ce qui a été fait.
1. **Politesse** :
- User-Agent identifiable,
- délai de 2 secondes entre deux URLs,
- plafond global de 30 URLs.

### ✅ Tu sais maintenant…

- Concevoir une veille comme une **succession de snapshots** comparés
- Hasher des **champs métier** (et pas du HTML brut) pour comparer
- Distinguer clés stables et valeurs surveillées
- Calculer `ajoutés / retirés / modifiés` entre deux datasets
- Comparer du texte avec `difflib`
- Organiser tes snapshots par dossier horodaté
- Choisir une cadence raisonnable (pas de course inutile)
- Émettre des alertes proportionnées (du fichier au webhook)

-----


## Chapitre 14 — Du script au rapport d’enquête

Une enquête se termine **toujours** par un rapport lisible par un humain. Pas par un CSV brut, pas par un JSON imbriqué. Ce chapitre te fait passer de la donnée structurée au **livrable**.

### Le minimum à savoir

#### Donnée ≠ rapport

|Donnée                |Rapport                          |
|----------------------|---------------------------------|
|`CSV`, `JSON`, `JSONL`|Markdown, HTML, PDF              |
|Lit par un programme  |Lu par un humain                 |
|Brut, exhaustif       |Synthétique, hiérarchisé         |
|Pas de contexte       |Source, méthode, dates, auteur   |
|Pas d’interprétation  |Conclusion bornée par la collecte|

Tu ne **publies** jamais le CSV. Tu publies un rapport qui s’**appuie** sur le CSV.

> **Rappel minimisation :** le rapport ne contient que **ce qui sert la conclusion**. Le dataset complet reste dans `data/processed/` (ou en annexe), pas dans le corps du rapport. C’est cohérent avec la minimisation appliquée à la collecte (chapitre 2) : on collecte le minimum nécessaire, on rapporte le minimum nécessaire.

#### Anatomie d’un rapport OSINT

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

#### Le bloc de métadonnées (obligatoire)

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

#### Générer du Markdown depuis Python

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

#### Générer un tableau Markdown depuis une liste de dicts

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

#### Statistiques basiques utiles

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

### Très utile en pratique

#### Borner les conclusions à la collecte

C’est **la** règle d’or du rapport OSINT :

> Tout ce qu’on écrit doit être étayé par la collecte. Tout ce qui n’est pas étayé doit être explicitement formulé comme une hypothèse, une question, ou un angle mort.

|❌ Conclusion non bornée                     |✅ Conclusion bornée                                                                                          |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|
|« L’entreprise X a réorienté sa stratégie. »|« Au cours des 12 dernières semaines, 8 des 10 nouvelles offres d’emploi publiées portent sur le domaine Y. »|
|« Personne ne parle de ce sujet. »          |« Aucune des 250 publications collectées sur le site Z entre A et B ne mentionne ce sujet. »                 |

La nuance est constante : on parle de **ce qu’on a vu**, pas de **ce qui existe**. C’est ce qui fait la différence entre un rapport solide et une opinion habillée.

#### Conservation des preuves

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

#### Minimisation, jusque dans le rapport

Tu as collecté avec minimisation (chapitre 2). Tu **rapportes** avec minimisation aussi :

- Ne mets pas de données personnelles dans le rapport si elles ne sont pas indispensables à la conclusion.
- Ne reproduis pas des textes longs : résume, cite court, lie vers la source.
- Ne mets pas dans le rapport ce que tu as collecté « au cas où ».

#### Conversion Markdown → HTML / PDF (en bonus)

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

### Bonus

#### Génération depuis un template

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

#### Indicateurs visuels

Pour les rapports lus en ligne, des indicateurs simples améliorent la lecture :

```
✓ Collecte réussie sur 12/12 sources
⚠ 2 sources avec un avertissement (timeouts ponctuels)
✗ 0 source en échec total
```

À utiliser avec parcimonie — ne transforme pas un rapport en sapin de Noël.

### ❌ Erreur classique

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

### Exercices

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

### 🧩 Mini-projet de Partie V (2/2) — *Synthétiseur de veille hebdomadaire*

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

### ✅ Tu sais maintenant…

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
