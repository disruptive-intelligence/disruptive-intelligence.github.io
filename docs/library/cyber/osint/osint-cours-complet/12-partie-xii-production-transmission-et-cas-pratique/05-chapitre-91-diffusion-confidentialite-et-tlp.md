---
title: Chapitre 91 — Diffusion, confidentialité et TLP
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 91.1 Diffusion comme acte professionnel

Produire un rapport n'épuise pas l'enquête. **Diffuser** intelligemment, **protéger** les informations, **respecter** les engagements de confidentialité sont des actes professionnels distincts.

## 91.2 TLP : Traffic Light Protocol

Le **TLP** (Traffic Light Protocol) est le standard international de classification d'informations sensibles. Géré par FIRST (Forum of Incident Response and Security Teams). Version 2.0 depuis 2022.

**Quatre niveaux.**

- **TLP:RED.** Information personnelle, individuelle. Pas de diffusion au-delà du destinataire direct.
- **TLP:AMBER.** Information limitée. Diffusion restreinte à organisation du destinataire et à ses partenaires directs nécessaires.
- **TLP:AMBER+STRICT.** Limité à l'organisation du destinataire, pas de partage avec partenaires.
- **TLP:GREEN.** Information communautaire. Partage avec partenaires et homologues, mais pas publication ouverte.
- **TLP:CLEAR** (anciennement WHITE). Publication libre.

## 91.3 Application TLP en OSINT

**Mandat type.**

- Rapport d'enquête sensible : **TLP:AMBER+STRICT** ou **TLP:RED**.
- IOCs CTI pour communauté : **TLP:GREEN** ou **AMBER**.
- Étude publique pour client : **TLP:CLEAR**.

**Marquage.** Chaque page du rapport porte la mention TLP. Email d'envoi mentionne TLP. Le destinataire est responsable du respect.

## 91.4 RGPD et diffusion

Si le rapport contient **données personnelles**, le RGPD s'applique :

- Base légale documentée.
- Minimisation (que ce qui est nécessaire).
- Sécurité (chiffrement transmission).
- Droits des personnes (notamment droit d'accès, opposition).
- Durée de conservation.

**Pratique.** Anonymisation / pseudonymisation quand pertinent. Diffusion ciblée. Tracabilité.

## 91.5 Confidentialité contractuelle

Le mandat impose typiquement **engagement de confidentialité** :

- Sur le rapport.
- Sur la méthodologie spécifique.
- Sur les sources particulières.
- Sur l'identité du commanditaire.

L'analyste **respecte** ces engagements même après la fin du mandat.

## 91.6 Chiffrement de la transmission

**Pour transmission au commanditaire.**

- Email : **PGP/GPG** (mature mais peu utilisé), **S/MIME** (plus enterprise).
- Plateforme dédiée : **SecureDrop**, **OnionShare**, **Tresorit Send**, **ProtonMail Drive**.
- Remise physique avec support chiffré (très sensible).

**Pour transmission au magistrat.**

- Canal officiel (greffe, e-Barreau).
- Chiffrement complémentaire si pertinent.

## 91.7 Marquage et watermarking

**Watermarking destinataire.** Un rapport peut porter un watermark visible (ou invisible) identifiant le destinataire. Si fuite, source identifiable.

**Pratique.** Watermark discret en pied de page (nom destinataire, date, hash). Watermark invisible (méthodes spécialisées).

## 91.8 Archivage post-diffusion

Après diffusion :

- **Archivage** local chiffré (3-2-1).
- **Index** dans système de gestion des rapports (pour retrouver ultérieurement).
- **Durée de conservation** documentée.
- **Purge** programmée à fin de période.

**RGPD.** La durée doit être justifiée et limitée. Conservation indéfinie problématique.

## 91.9 Sortie du périmètre du mandat

**Question.** Que faire si l'analyste découvre, en cours de mandat, des éléments **hors périmètre** qui semblent pertinents pour d'autres enquêtes (autres clients, autorités) ?

**Principe général.** Pas de diffusion hors mandat sans autorisation explicite.

**Exceptions.**

- **Obligation légale** (signalement d'infractions graves : terrorisme, CSAM, etc.).
- **Consentement** explicite du commanditaire.

**Pratique.** Documentation rigoureuse. Si signalement légal nécessaire, mention dans le rapport au commanditaire.

## 91.10 Conférences, publications académiques, presse

Si l'analyste souhaite publier (article, conférence, presse), méthodologie :

- **Autorisation** explicite du commanditaire si données sensibles.
- **Anonymisation** du cas si nécessaire.
- **Cas générique** plutôt que cas réel.
- **Accord écrit** mentionné dans la publication.

## 91.11 Synthèse — discipline de diffusion

| Phase | Action |
|---|---|
| Préparation | Définir TLP, chiffrement transmission |
| Diffusion | Canal sécurisé, watermark si pertinent |
| Réception | Confirmation par destinataire |
| Archivage | Chiffrement, durée documentée |
| Post-mandat | Purge programmée, anonymisation si publication |

> **Principe.** La diffusion est un acte professionnel. Elle protège le commanditaire, l'analyste, les personnes mentionnées. Une diffusion mal maîtrisée détruit la confiance bâtie pendant l'enquête.

-----
