---
title: Chapitre 14 — Sélecteurs OSINT et logique de pivot
source: Cyber/02 OSINT/Méthode & enquête/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE III — Méthodologie d'enquête et gestion du dossier
  - index.md
---

## 14.1 Définition du sélecteur

Un **sélecteur** est un élément d'information qui sert de **point d'entrée** ou de **point de pivot** dans une enquête. Le sélecteur permet d'interroger des sources, d'obtenir des résultats, et de découvrir d'autres sélecteurs.

L'enquête OSINT progresse par **pivots successifs** : on part d'un sélecteur initial, on l'interroge dans une source, on obtient un résultat qui contient un nouveau sélecteur, on pivote sur ce nouveau sélecteur dans une autre source, etc. La trajectoire forme un graphe d'exploration.

## 14.2 Les 14 sélecteurs canoniques

Quatorze sélecteurs sont opérationnels en OSINT moderne. Les six premiers sont les sélecteurs primaires que tout analyste maîtrise. Les huit suivants sont des sélecteurs avancés selon les contextes.

**Sélecteurs primaires.**

1. **Nom complet.** Sélecteur évident, mais imprécis en raison des homonymies. À enrichir systématiquement (date de naissance, lieu, profession).
2. **Email.** Sélecteur puissant : utilisé partout, peu réutilisé, traçable à travers leaks, registres WHOIS, plateformes.
3. **Username (pseudonyme).** Très puissant car les utilisateurs réutilisent souvent le même username sur plusieurs plateformes.
4. **Téléphone.** Sélecteur d'identification fort (lié à SIM, opérateur). Utilisé sur Telegram, WhatsApp, Signal pour le découvrir.
5. **Photo (visage, image).** Recherche inversée (Yandex, Google Lens, TinEye), reconnaissance faciale (PimEyes, FaceCheck).
6. **Adresse postale.** Cadastre, annuaires, registres fonciers, sociétés domiciliées.

**Sélecteurs avancés.**

7. **Domaine et sous-domaine.** WHOIS, DNS, certificats, hébergement.
8. **Adresse IP.** Géolocalisation, ASN, services exposés, historique.
9. **Wallet crypto (adresse blockchain).** Explorateurs, clustering, attributions partielles *(renvoi → OSINT Crypto vFULL)*.
10. **Document (PDF, image avec métadonnées).** EXIF, propriétés Office, traces de création.
11. **Organisation (raison sociale, numéro d'enregistrement).** Registres corporate.
12. **Événement (date, lieu, type).** Sources presse, archives, médias sociaux.
13. **Véhicule (immatriculation, VIN).** Limité légalement, certains pays autorisent ; aérien et maritime (registres ADS-B, AIS) sont plus accessibles.
14. **Lieu (coordonnées GPS, point d'intérêt).** Cartographie, imagerie, données géolocalisées.

## 14.3 Sélecteurs forts versus sélecteurs faibles

Tous les sélecteurs n'ont pas la même puissance discriminante.

**Sélecteurs forts.** Identification quasi-unique. Email (sauf en cas de partage rare), téléphone, IP avec timestamp précis, wallet crypto.

**Sélecteurs faibles.** Polysémie possible. Nom commun (Jean Dupont), photo de visage standard (jumeau), prénom seul.

**Implication.** Un pivot sur sélecteur fort = grande confiance. Un pivot sur sélecteur faible = à corroborer immédiatement.

## 14.4 Logique de pivot : la mécanique

Le pivot est l'opération centrale de l'OSINT.

**Schéma.**

1. Sélecteur initial S1 (ex : email `m.delaunay@technovert.fr`).
2. Interrogation source X1 (ex : WHOIS lookups).
3. Résultat contenant nouveau sélecteur S2 (ex : domaine `delta-consulting.eu` enregistré avec cet email).
4. Interrogation source X2 sur S2 (ex : registre maltais).
5. Résultat → S3 (ex : nom de société Delta Consulting Ltd, numéro d'enregistrement, administrateur).
6. Interrogation source X3 sur S3 (ex : OpenCorporates pour réseau d'administrations connexes).
7. Etc.

Chaque pivot est **documenté** dans le journal d'enquête (Ch.15). La traçabilité du pivot est ce qui rend l'enquête défendable.

## 14.5 Pivots fréquents

Quelques pivots emblématiques.

- **Email → WHOIS** : un domaine peut être enregistré avec un email personnel.
- **Email → leaks (HIBP, DeHashed)** : exposition dans des fuites.
- **Email → Hunter / Epieos** : confirmation d'existence, plateformes liées.
- **Username → Sherlock / WhatsMyName / Maigret** : présence cross-plateforme.
- **Photo → Yandex Images / PimEyes** : autres apparitions en ligne.
- **Photo → métadonnées EXIF** : géolocalisation GPS, appareil utilisé.
- **Domaine → DNS / passive DNS / sous-domaines** : infrastructure complète.
- **Domaine → certificats (crt.sh)** : autres domaines liés via certificat.
- **Société → bénéficiaires (OpenCorporates, Pappers, RBE)** : structure d'UBO.
- **Société → adresse de domiciliation → autres sociétés domiciliées** : cluster d'entités.

## 14.6 Discipline du pivot

L'erreur classique du débutant : pivoter au hasard, explorer toutes les directions, dériver sans direction.

**Réflexes.**

- Avant chaque pivot, se demander : **ceci m'apporte-t-il un nouveau sélecteur pertinent pour mes IR ?**
- Hiérarchiser les pivots par valeur attendue.
- Documenter chaque pivot dans le journal.
- Ne pas s'enfoncer dans des branches stériles plus de 30-60 minutes sans bilan.
- Faire un point de bilan tous les 2-3 heures pour évaluer la trajectoire.

> **MIRAGE — Épisode 2 : Sélecteurs initiaux**
>
> L'analyste recense les sélecteurs disponibles au démarrage : nom Marc Delaunay (sélecteur faible — au moins 23 homonymes identifiables en France), date de naissance approximative (1976-1977), poste (DAF TechnoVert SAS), email professionnel (`m.delaunay@technovert.fr`, sélecteur fort). C'est mince.
>
> Premier pivot : recherche Google sur `"Marc Delaunay" "TechnoVert"`. Résultat : trois communiqués de presse mentionnant le poste, un profil LinkedIn ouvert (Sales Navigator inutile, profil partiel), une interview vidéo sur YouTube datée de 2023. Pivot vers LinkedIn : confirmation du parcours (X-Ponts 1999, parcours en cabinet d'audit puis ETI), photo de profil, 4 abonnements à des comptes professionnels.
>
> Pivot sur l'email : Hunter.io confirme existence et déliverabilité. Pivot Holehe : présence détectée sur LinkedIn, WordPress, Adobe, Spotify, Apple. Pas de présence Telegram/Signal détectable depuis l'email pro (qui ne signifie pas absence — usage probable d'email perso pour ces plateformes).
>
> Recherche WHOIS large : l'email pro n'apparaît dans aucun WHOIS public en lookup direct (les registrars masquent par défaut). Bascule vers l'hypothèse : Delaunay utilise un email personnel pour ses opérations offshore, non encore identifié. Première recherche : username dérivé du nom (`mdelaunay`, `m.delaunay`, `marcdelaunay`, `delaunaymarc`) testé sur Sherlock. Hit sur Twitter sous `@mdelaunay76` (compte verrouillé), Instagram `mdelaunay76` (compte privé), GitHub `mdelaunay` (compte sans activité 2017-2019).
>
> Le 76 dans le username (peut-être lié à 1976, année de naissance) devient un sélecteur secondaire. Hypothèse : Delaunay utilise un username personnel récurrent. L'arbre de pivots commence à prendre forme. Trois pistes à explorer en parallèle dans les jours suivants : approfondissement username, recherche email personnel, exploration corporate à partir du parcours.

-----
