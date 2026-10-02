---
title: Chapitre 49 — Éthique, légalité et sécurité de l’enquêteur
source: Cyber/02 OSINT/Finance & cryptoactifs/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie IX — Production, cadre et professionnalisation
  - index.md
---

L’enquête crypto opère dans un **cadre éthique et juridique** qui doit être maîtrisé. Ce chapitre couvre les principaux enjeux.

## 49.1 Légalité

**Cadre français** :

**OSINT** : généralement légal. Données publiques accessibles légalement. Mais :

- **Pas de hacking** : pas d’accès non-autorisé à systèmes.
- **Pas d’usurpation d’identité** : pas de faux comptes (sauf cadre HUMINT autorisé).
- **Pas de manipulation** : pas d’interaction trompeuse avec cibles.
- **Respect RGPD** : traitement de données personnelles encadré.
- **Pas d’enquête sous couverture privée** : réservé aux autorités.

**Enquêteur privé** : peut être encadré par CNAPS (Conseil national des activités privées de sécurité) selon nature de l’activité.

**Crypto spécifique** :

- Lecture de blockchain publique : libre.
- Achat de crypto pour transaction de test : possible mais peu pratiqué OSINT pur (plus IR/red team).
- Interaction avec sanctioned addresses : interdit (sanctions OFAC, UE).

## 49.2 Cadre éthique

**Principes** :

**Honnêteté** : ne pas mentir au mandant ni aux interlocuteurs. Calibration honnête.

**Discrétion** : confidentialité du mandat. Pas de bavardage. Respect TLP.

**Minimisation** : collecter seulement ce qui est nécessaire.

**Non-prolifération** : ne pas diffuser hors cercle justifié.

**Respect des victimes** : dignité, sensibilité.

**Pas d’aide aux acteurs criminels** : refus de mandat suspect.

**Pas de production de rapports orientés** : résister à pressions pour conclusions politiques.

## 49.3 Conflits d’intérêt

**Détection** : évaluation systématique avant acceptation de mandat.

- Le mandant a-t-il intérêt à orienter l’enquête ?
- L’analyste a-t-il un intérêt personnel dans le résultat ?
- Y a-t-il des liens préexistants avec les cibles de l’enquête ?

**Gestion** : refus de mandat, recusation, transparence avec autres acteurs.

## 49.4 Pression et menaces

L’enquête crypto peut générer **pressions et menaces**.

**Sources** :

- **Acteurs criminels** : acteur enquêté découvre l’enquête (si OPSEC analyste fait défaut), tentative d’intimidation.
- **Mandants insatisfaits** : pression pour conclusions différentes.
- **Médias / journalistes** : pression pour révélations prématurées.

**Protection** :

- **OPSEC stricte** : pas d’identification publique d’analyste sur dossiers sensibles.
- **Confidentialité** : pas de divulgation hors cercle justifié.
- **Cadre légal** : respect strict pour ne pas s’exposer.
- **Soutien institutionnel** : cabinet / employeur protège ses analystes.
- **Coopération autorités** : si menaces graves, signalement et protection.

## 49.5 Sécurité physique et numérique

**Numérique** :

- Machine d’investigation isolée.
- VPN / Tor pour navigation sensible (selon contexte).
- Comptes dédiés.
- Crypto-wallets séparés (pas d’argent personnel).
- Sauvegardes chiffrées.
- MFA universel.

**Physique** :

- Pour cas à très haut risque (acteurs étatiques, terrorisme), consignes opérationnelles spécifiques.
- Protection de l’identité (en particulier pour analystes individuels publiant publiquement).

**Bureaux** :

- Sécurité périmétrique.
- Contrôle d’accès.
- Caméras (selon contexte).
- Politique de visiteurs.

## 49.6 Bien-être psychologique

**Risques** :

- Exposition à contenus difficiles (cas victimes, contenus sensibles si Dark Web).
- Stress et pression (deadlines, enjeux).
- Isolement (travail solitaire en deep work).
- Burnout sur enquêtes longues / complexes.

**Mesures** :

- **Rotations** sur dossiers difficiles.
- **Soutien psychologique** disponible.
- **Pauses** structurées.
- **Limites horaires**.
- **Communauté de pairs** pour partage.
- **Activités hors travail** préservées.

Pour cabinets : politique formalisée de bien-être.

## 49.7 Fin de mission et clôture

**Archivage** : preuves conservées immutablement, accessibles si re-questions ultérieures.

**Suppression** : selon politique RGPD, certaines données supprimées après période de conservation.

**Communication finale** : mandant remercie, debriefe.

**Retour d’expérience** : interne au cabinet.

**Post-mortem** : ce qui a fonctionné, ce qui peut s’améliorer.

## 49.8 Limites éthiques absolues

Quelques cas où **refus est obligatoire** :

**Faciliter une activité illicite**. Mandat qui demanderait, sous prétexte d’enquête, à fournir éléments à acteur criminel.

**Cibler un innocent**. Mandat qui demanderait à « salir » un tiers sans base.

**Violer secret professionnel**. Mandat qui demanderait à divulguer informations privilégiées.

**Espionnage économique illégitime**. Mandat qui demanderait à enquêter sur concurrent sans cadre légal.

**Travail pour acteur sanctionné**. Évident.

L’analyste a la responsabilité de **détecter et refuser** ces cas. Si pression interne du cabinet, escalade.

-----
