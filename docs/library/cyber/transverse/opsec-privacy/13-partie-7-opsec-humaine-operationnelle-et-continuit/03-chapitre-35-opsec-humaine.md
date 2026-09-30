---
title: Chapitre 35 — OPSEC humaine
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 7 — OPSEC humaine, opérationnelle et continuité
  - index.md
---

entourage, photos, voix, stylométrie, traces comportementales

## 35.1 Entourage : maillon souvent ignoré

Ton meilleur OPSEC tombe si ton entourage publie ton anniversaire le jour, te tague sur une photo géolocalisée, ou répond à un appel de pretext en donnant ton emploi du temps.

**Mesures** :

- **Conversation explicite** avec les proches importants : pas de tag, pas de mention par nom, pas de photo en ligne sans accord, pas de réponse à des questions sur toi sans vérification.
- **Documents partagés** : ne pas mettre tes infos perso dans les listes Excel familiales partagées sur Google Sheets.
- **Réseaux familiaux** : ta mère a publié ton adresse sur Facebook ? Discussion privée, sans drame, avec aide à modifier les paramètres.
- **Enfants** : pas de prénom + école visible publiquement. Pas de photo géolocalisée.

## 35.2 Photos : géolocalisation visuelle

Au-delà de l’EXIF (Ch 31), une photo révèle par son contenu visuel :

- Vue par la fenêtre permettant de trianguler le quartier.
- Arrière-plan industriel ou architectural identifiable.
- Plaques d’immatriculation visibles.
- Marquages d’entreprise locale.
- Reflets sur surfaces brillantes (vitre, miroir, écran, œil).

**OSINT géo-visuel** est une discipline mature (Bellingcat, GeoGuessr). Un combinaison d’indices banaux permet une géolocalisation au quartier voire au bâtiment.

**Pour la publication** : examiner chaque photo en imaginant ce qu’un attaquant motivé peut déduire. Recadrer, flouter agressivement les éléments contextuels.

## 35.3 Voix : empreinte vocale et clonage

Cf. Ch 34. Implications spécifiques :

- Tes interviews publiques, conférences vidéo, podcasts sont des échantillons exploitables pour cloner ta voix.
- Stratégie : pour HVT, limiter la diffusion publique de longs échantillons vocaux. Pour usage public (journaliste qui doit témoigner), accepter et compenser par codes hors bande.

## 35.4 Stylométrie : signature d’écriture

Ton style d’écriture est une empreinte. Caractéristiques :

- Longueur moyenne des phrases.
- Distribution des virgules, points-virgules, deux-points.
- Vocabulaire spécifique (mots favoris, tics).
- Formulations récurrentes.
- Erreurs typographiques personnelles.
- Préférences orthographiques (français de Belgique vs France, anglicismes).

Cas Bitcoin et Satoshi Nakamoto : analyses stylométriques ont éliminé/proposé plusieurs candidats sur la base du seul style.

**Quand c’est important** : pour publication sous pseudonyme stable, si l’attaquant peut soupçonner qui tu es, comparer ton écriture pseudonyme à ton écriture connue est trivial. Le pseudonyme tombe.

**Mitigations** :

- **Réécriture par LLM** : faire passer ton texte par un LLM pour reformulation neutre. Atténue ta signature.
- **Discipline volontaire** : raccourcir ou allonger systématiquement les phrases par rapport à ton naturel, modifier ponctuation. Coût cognitif élevé, durabilité limitée.
- **Pseudonymes à publication courte** : moins d’échantillons = moins de signature stable détectable.

## 35.5 Traces comportementales : horaires, lieux, routines

Tu es prévisible. Tu te connectes à certaines heures. Tu visites certains sites. Tu écris à certaines personnes. Tu commandes la même chose. Tu prends le même chemin. Cette routine est une signature.

Pour une identité compartimentée : les routines doivent se compartimenter aussi. Le compte « anonyme » qui se connecte aux mêmes heures que ton compte nominal est trivialement corrélable.

**Pratique** :

- Pour compartiments sensibles, varier les fenêtres temporelles, les lieux de connexion, les rythmes.
- Pour rester crédible, ne pas adopter un comportement *trop* différent (qui devient un autre type de signature).

## 35.6 Métadonnées comportementales hors numérique

- **Achats** : régularité, lieux, types (cf. Ch 32).
- **Déplacements** : transports en commun avec carte nominative (Navigo, Métro), péages, parking surveillé.
- **Présence physique** : caméras (CCTV public et privé), reconnaissance faciale en croissance dans certains pays.
- **Smart home** : assistants vocaux qui enregistrent, thermostats connectés qui révèlent présence/absence.

## 35.7 Discipline du « jamais en ligne quand X »

Une discipline simple à grande efficacité : *ne jamais* utiliser le compte sensible quand tu es identifiable autrement. Si ton téléphone perso est allumé chez toi, ton compte sensible ne se connecte pas en même temps depuis ton FAI domestique — corrélation triviale.

Schéma :

- Compte sensible utilisé exclusivement depuis lieux/réseaux/appareils distincts.
- Téléphone perso physiquement absent de ces sessions (laissé chez soi, en faraday bag, etc.).
- Pas de cross-contamination horaire.

## 35.8 *Fil rouge* — Léa adopte une routine stricte

Sur l’enquête, Léa s’impose :

- Téléphone perso laissé chez elle (chargeur sur la table, comme si elle ne sortait pas) les jours d’enquête sensible.
- Travail enquête uniquement depuis le bureau séparé (loué via le consortium), ou Tails sur laptop dédié dans un lieu calme.
- Horaires d’enquête : afternoon et soir, jamais matin (qui est son créneau pro public).
- Communications avec Karim : créneaux convenus, jamais réponse impulsive.

-----
