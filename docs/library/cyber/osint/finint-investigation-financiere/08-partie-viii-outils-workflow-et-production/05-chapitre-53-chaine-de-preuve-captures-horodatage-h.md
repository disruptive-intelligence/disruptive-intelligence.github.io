---
title: Chapitre 53 — Chaîne de preuve, captures, horodatage, hash
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VIII — Outils, workflow et production
  - index.md
---

## Objectif du chapitre

Maîtriser la **discipline de chaîne de preuve** : capture des sources, horodatage, hashing, archivage — pour que les éléments collectés restent exploitables et défendables.

## Le concept

La **chaîne de preuve** (chain of custody) est la traçabilité des éléments d’enquête : qui a collecté, quand, où, comment, avec quelle modification, qui les a transmis, à qui. Une chaîne de preuve solide est nécessaire pour :

- Garantir l’**intégrité** des éléments.
- Permettre la **reproduction** par un tiers (juge, magistrat, expert).
- Éviter les contestations d’authenticité.

## Bonnes pratiques

**Capture** : pour chaque élément OSINT collecté :

- Capture d’écran (PNG, PDF) ou enregistrement HTML brut.
- URL exacte de la source.
- Date et heure de capture (avec fuseau horaire).
- Identifiant de l’analyste.

**Horodatage** : utilisation de services d’horodatage tiers pour les éléments critiques (Tiers de confiance, service notarisation horaire). Pour la grande majorité des cas, l’horodatage interne (système de fichiers + journal de l’analyste) suffit.

**Hash** : pour les fichiers téléchargés (rapports, documents PDF, archives), calculer un hash SHA-256 (ou SHA-512) au moment du téléchargement. Le hash garantit l’intégrité.

**Archivage** : stockage dans un système de gestion de dossiers (DMS) avec contrôle d’accès, journalisation, sauvegarde. En CRF : système agréé. En cabinet : à minima répertoire sécurisé avec contrôle d’accès.

**Annotation** : chaque élément annoté de son contexte (pourquoi collecté, qu’apporte-t-il).

**Transmission** : transmission par canaux sécurisés (chiffrement bout en bout, courriers chiffrés, plateformes professionnelles).

## Méthode — workflow type

À chaque collecte :

```
[date/heure] [analyste] capture [URL]
- Capture : nom_fichier.png (hash SHA-256)
- Archive HTML : nom_fichier.html
- PDF source : nom_fichier.pdf (hash)
- Note : pourquoi collecté, qu'apporte-t-il
- Tags : entité concernée, type de source
```


Outils utiles : extensions navigateur de capture (Singlefile pour HTML complet, Hunchly pour OSINT), gestionnaires de notes (Obsidian, Notion, Joplin), DMS internes.

## Erreurs fréquentes

- **Pas de capture** : on s’appuie sur une URL qui change ou disparaît.
- **Pas d’horodatage** : on perd la séquence des collectes.
- **Pas de hash** : on ne peut pas prouver l’intégrité.
- **Stockage non sécurisé** : risque de fuite ou de perte.

## Limites

La chaîne de preuve OSINT n’a pas la même valeur judiciaire qu’une saisie sous procédure. Mais une chaîne propre rend le livrable beaucoup plus crédible.

## Lien avec le fil rouge

> **CLEARFLOW — Chain of custody Nassim**
> 
> Sur 8 semaines de travail, Nassim accumule environ 1 200 captures (HTML, PNG, PDF). Toutes archivées dans le DMS interne de la CRF, hashées, horodatées, tagées par entité. Cette discipline rend la note finale **reproductible** : un tiers peut suivre chaque chaîne.

## Points clés à retenir

- Chaîne de preuve = intégrité + reproductibilité + non-contestation.
- Pratiques : capture, horodatage, hash, archivage, annotation, transmission sécurisée.
- Outils : Singlefile, Hunchly, Obsidian, DMS interne.

-----
