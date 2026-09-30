---
title: G.3 — Exemple d'entrée de journal MIRAGE
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - Annexes
  - index.md
---

```markdown
# Entrée 2026-05-17-1430 — Investigation Delta Consulting (Malte)

## Contexte
Investigation MIRAGE/IR1 (structures offshore Delaunay). Approfondissement
de la fiche entité Delta Consulting Ltd identifiée en MIRAGE 8.

## Action conduite
1. Consultation Companies Registry Malta directement.
2. Recherche cross-juridictions via OpenCorporates.
3. Vérification adresse domiciliation (Athinon Street, Valletta).

## Sources consultées
- https://registry.mfsa.com.mt/ (capture Hunchly 2026-05-17 14:32)
  Hash : 7a3f2b8c...
- https://opencorporates.com/companies/mt/[id] (capture Hunchly 2026-05-17 14:38)
  Hash : 9e1d4f5a...
- Cross-search adresse : 47 sociétés à la même adresse de domiciliation
  identifiées (typique registered agent).

## Résultats
- Delta Consulting Ltd, immatriculée 03/2020.
- Capital 1200 €.
- Director unique : Marc Delaunay.
- Activité déclarée : "consulting services".
- Adresse : 24 Athinon Street, Valletta (registered agent commun).
- UBO déclaré : Marc Delaunay 100 %.

## Cotation préliminaire
- Source (Companies Registry Malta) : A1 — registre officiel
- Information : 1 — confirmée par capture officielle

## Pivots possibles identifiés
- Cross-recherche adresse domiciliation : 47 autres sociétés.
- 12 d'entre elles ont directors avec prénoms français — cluster
  potentiel à explorer.
- Investigation Cyprus Confidential pour mention Delta.

## Limites / questions ouvertes
- Capital social symbolique (1200 €) : cohérent avec usage offshore mais
  pas démonstration de fonction.
- Comptes Delta non publiés sur Malta (pas obligation pour micro-entité).
- Activité réelle non observable directement.

## Liens dossier
- Fiches mises à jour : [[Fiche E-002 Delta Consulting]]
- Pièces archivées : pieces/mirage-014-companies-registry-malta.pdf, ...

## Notes méthodologiques
- Bonne intuition de cross-rechercher l'adresse de domiciliation : ouvre
  un cluster non anticipé.
- Cotation prudente : présence administrateur ≠ démonstration bénéfice
  économique direct.

---
Hash de cette entrée : 4b8c3e2a91d5f6c7...
```



### G.4 — Bonnes pratiques

**Rédiger en temps réel.** Pas le soir, pas le lendemain. L'erreur de mémoire est aussi grave que l'erreur d'analyse.

**Niveau de détail.** Suffisant pour qu'un confrère puisse reproduire la démarche, sans tomber dans la verbosité.

**Citation des sources.** URL + capture archive + hash systématique pour chaque source significative.

**Cotation préliminaire.** Pas attendre la synthèse. Coter au fil de l'eau, ajustable.

**Pivots identifiés.** Lister explicitement, même si on n'a pas le temps de tous les explorer. Évite l'oubli.

**Notes méthodologiques.** Ce qui marche, ce qui ne marche pas. Capitalisation.


### G.5 — Versioning et intégrité

**Vault Obsidian + Git local.**

```
mirage-investigation/
├── .git/
├── 0-mandat.md
├── 1-methodologie.md
├── 2-fiches/
│   ├── P-001-marc-delaunay.md
│   ├── E-001-technovert.md
│   └── ...
├── 3-journal/
│   ├── 2026-05-16-cadrage.md
│   ├── 2026-05-17-delta-consulting.md
│   └── ...
├── 4-pieces/
│   ├── pieces.json (catalogue avec hashes)
│   └── archived/
└── 6-livrables/
    ├── rapport-v0.1.md
    └── rapport-v1.0-final.pdf
```


**Commits Git réguliers.** À chaque session d'enquête.

**Backups chiffrés.** Quotidiens. 3-2-1.


### G.6 — Confidentialité

**Chiffrement.** Disque VeraCrypt (recommandé container 50-200 Go selon enquête).

**Mot de passe.** Phrase de passe robuste, gestionnaire de mots de passe local (KeePassXC).

**Accès.** Strictement limité à l'analyste / cabinet.

**Pas de cloud sync.** Disable Dropbox, OneDrive, iCloud sur ce répertoire.


### G.7 — Catalogue des pièces

Un fichier dédié `pieces.json` (ou table dans Obsidian) catalogue **chaque pièce** :

```json
{
  "ref": "mirage-014",
  "title": "Companies Registry Malta - Delta Consulting Ltd",
  "type": "capture_hunchly",
  "date_collected": "2026-05-17T14:32:00+02:00",
  "source_url": "https://registry.mfsa.com.mt/[...]",
  "hash_sha256": "7a3f2b8c...",
  "filepath": "4-pieces/archived/mirage-014.html",
  "captured_by": "AnalysteX",
  "tool": "Hunchly v3.2",
  "cotation_source": "A",
  "cotation_information": "1",
  "tags": ["delta-consulting", "malte", "registre-officiel"],
  "notes": "Capture intégrale page registre. Pages 1-3 utiles."
}
```



### G.8 — Synthèse — discipline de journal

Le journal d'investigation est ce qui distingue **l'analyste mature** de l'amateur. Il transforme une recherche éparpillée en dossier défendable. C'est aussi ce qui rend le travail **reproductible**, **auditable**, **capitalisable**.

Sans journal, l'enquête meurt avec son auteur. Avec journal, elle survit, se transmet, s'améliore.

-----


## ANNEXE H — Templates de fiches

Templates standards pour les principaux types de fiches mobilisés dans une enquête OSINT mature. À adapter selon contexte.
