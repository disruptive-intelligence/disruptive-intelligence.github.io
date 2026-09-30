---
title: Exercice final de la Partie IX — Mini-investigation défensive légitime
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IX — Navigation pratique et collecte défensive encadrée
  - index.md
---

**Objectif**. Réaliser une collecte complète, légitime et documentée sur une ressource .onion officielle. Mobilise les compétences des Ch.45-48 en une démarche cohérente.

**Scénario**. Vous êtes analyste CTI junior. Votre responsable vous demande de documenter l'existence d'un miroir .onion officiel d'un média ou d'une institution, de vérifier son authenticité, puis de produire une note courte expliquant votre méthode.

**Étapes attendues** :

1. **Choisir une ressource légitime** : BBC, ProPublica, Tor Project, Deutsche Welle, ou autre média/institution mentionné en Ch.45.6.
2. **Trouver l'adresse .onion** depuis le site clearnet officiel.
3. **Vérifier si un header Onion-Location** est présent quand vous visitez le site clearnet via Tor Browser.
4. **Comparer l'adresse complète** avec la source officielle (caractère par caractère).
5. **Visiter le miroir .onion** avec Tor Browser en mode Safest.
6. **Capturer la page** avec Hunchly ou, à défaut, capture manuelle + sauvegarde HTML.
7. **Calculer le hash SHA-256** des fichiers collectés.
8. **Rédiger une note courte** (template ci-dessous).

**Livrable attendu** :

```markdown
# Note courte — Authentification d'un miroir .onion légitime

## Ressource étudiée
[Nom de l'organisation]

## Adresse clearnet officielle
[URL]

## Adresse .onion vérifiée
[Adresse complète, 56 caractères + .onion]

## Méthode de vérification
- Source officielle consultée :
- Header Onion-Location observé : oui/non
- Recoupement secondaire :
- Date et heure de vérification :

## Collecte
- Outil utilisé :
- Captures réalisées :
- Hash SHA-256 :

## Conclusion
[Adresse authentifiée / non authentifiée / incertaine]

## Limites
[Éléments non vérifiés, incertitudes, date de validité de la vérification]
```


**Critères d'évaluation** :

- Méthode reproductible par un autre analyste sans contact avec vous.
- Adresse vérifiée sur **au moins deux sources d'autorité indépendantes**.
- Captures horodatées et hashées.
- Note synthétique, factuelle, calibrée.
- Limites explicitement documentées.

Cet exercice transforme les chapitres 45-48 en **compétence mesurable**. Il sert aussi de référence interne — l'analyste qui le réussit produit son premier livrable structuré, réutilisable comme template pour ses missions futures.
