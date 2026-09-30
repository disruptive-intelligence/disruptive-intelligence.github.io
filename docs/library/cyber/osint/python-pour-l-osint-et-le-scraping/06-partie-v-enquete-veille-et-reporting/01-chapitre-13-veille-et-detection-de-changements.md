---
title: Chapitre 13 — Veille et détection de changements
source: Cyber/02_OSINT/Python_Scraping.md
note: Python pour l'OSINT et le scraping
up:
- - Python pour l'OSINT et le scraping
  - ../index.md
- - Partie V — Enquête, veille et reporting
  - index.md
---

Une collecte unique te donne un instantané. Une veille te donne un **mouvement**. C’est souvent ce qui compte vraiment : qu’est-ce qui a changé, depuis quand, et dans quel sens ?

## Le minimum à savoir

### Le principe : snapshots et comparaison

```
T0 : collecte n°1 → snapshot_T0
T1 : collecte n°2 → snapshot_T1
                       ↓
          comparer(snapshot_T0, snapshot_T1)
                       ↓
        ajouts / retraits / modifications
```


Chaque exécution de ton veilleur produit un **snapshot** complet (dataset propre), horodaté et conservé. La veille consiste à comparer deux snapshots successifs et à isoler les différences.

### Hasher pour comparer rapidement

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

### Définir ce qui « compte » comme changement

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

### Stocker les snapshots dans le temps

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


### Le squelette d’un veilleur

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


### Bonnes pratiques de cadence

|Cas                                            |Fréquence raisonnable              |
|-----------------------------------------------|-----------------------------------|
|Veille de blog/média                           |1× par jour                        |
|Suivi de bulletins officiels (CERT, ministères)|1× à 4× par jour                   |
|Page « emplois » d’une entreprise              |1× par jour                        |
|Page produit (prix, disponibilité)             |1× à 4× par jour                   |
|Quasi temps réel                               |Quelques fois par heure **au plus**|


> **À retenir :** la veille n’est pas une **course**. Tu veux détecter un changement dans la journée, rarement à la minute. Une cadence d’une fois par jour est presque toujours suffisante pour un cas OSINT défensif. Plus rapide → tu marteles le serveur sans gain réel.

### Ce qu’on ne fait **pas** avec un veilleur

- **Imiter un service de monitoring payant** sans en avoir le droit (bypass d’un produit commercial).
- **Surveiller en permanence** une page qu’on n’a manifestement pas besoin de surveiller en temps réel.
- **Veiller sur des contenus accessibles uniquement en session connectée** : si tu dois te connecter, ce n’est pas du public.
- **Veiller sur des données personnelles** sans cadre légal explicite.

## Très utile en pratique

### Comparer du texte avec `difflib`

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

### Comparaison rapide par hash global

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

### Alertes : du plus simple au plus complet

|Niveau|Mécanisme                                                |Cas d’usage                                       |
|------|---------------------------------------------------------|--------------------------------------------------|
|0     |Rien, juste les logs                                     |Veille personnelle, on lit les logs à son rythme. |
|1     |Fichier `changes.log` (texte)                            |Veille structurée — on consulte en fin de journée.|
|2     |Notification système (`notify-send`, `terminal-notifier`)|Veille personnelle réactive.                      |
|3     |Email                                                    |Veille pour soi ou pour un petit groupe.          |
|4     |Webhook Slack/Discord                                    |Équipe collaborative.                             |


> **Précautions** sur les niveaux 3 et 4 : ne diffuse pas plus que ce que tu as collecté. Si la collecte respecte la minimisation, l’alerte aussi. Pas de fuite de données sensibles par un webhook mal configuré.

### Le réflexe : un changelog humain

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

## Bonus

### Hash du HTML normalisé

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

### Webhook Discord/Slack (avec précautions)

Exemple minimal Discord :

```python
import requests

def notify_discord(webhook_url, message):
    requests.post(webhook_url, json={"content": message[:1900]}, timeout=10)
```


- **Webhook URL** = secret. Mets-la dans `.env`.
- **Ne pousse jamais** de données personnelles ou sensibles dans un webhook public.
- **Tronque** les messages — la plupart des services rejettent les longs payloads.

## ❌ Erreur classique

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


## Exercices

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

## 🧩 Mini-projet de Partie V (1/2) — *Veilleur de page publique*

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

## ✅ Tu sais maintenant…

- Concevoir une veille comme une **succession de snapshots** comparés
- Hasher des **champs métier** (et pas du HTML brut) pour comparer
- Distinguer clés stables et valeurs surveillées
- Calculer `ajoutés / retirés / modifiés` entre deux datasets
- Comparer du texte avec `difflib`
- Organiser tes snapshots par dossier horodaté
- Choisir une cadence raisonnable (pas de course inutile)
- Émettre des alertes proportionnées (du fichier au webhook)

-----
