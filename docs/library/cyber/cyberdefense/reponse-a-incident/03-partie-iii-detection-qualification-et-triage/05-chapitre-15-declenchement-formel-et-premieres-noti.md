---
title: Chapitre 15 — Déclenchement formel et premières notifications
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie III — Détection, qualification ET triage
  - index.md
---

## 15.1 Ouverture formelle de l'incident

L'ouverture formelle marque le passage du mode « investigation exploratoire » au mode « réponse structurée ». Elle comprend la désignation du pilote (IR lead), la constitution de la cellule technique, l'ouverture du journal d'incident (chronologique, chaque action horodatée et signée — le document le plus important de l'incident, car il reconstitue la séquence des décisions et protège les décideurs), l'activation du canal de communication sécurisé (hors SI — Signal, WhatsApp groupe, téléphone — le SI interne est potentiellement compromis et ne peut plus être utilisé pour des communications sensibles), et l'attribution d'un nom de code (pour la communication interne et la traçabilité des documents).

## 15.2 Première SitRep

Le premier SitRep est produit dans les 2 à 4 premières heures, à destination du RSSI et de la direction. Il suit une structure standardisée : ce qu'on sait (faits confirmés, cotés), ce qu'on ne sait pas (inconnues explicites), ce qu'on fait (actions en cours), ce qu'on envisage (prochaines étapes, options de confinement), et ce dont on a besoin (ressources, décisions, autorisations). Format : une page maximum, factuel, sans jargon technique excessif.

## 15.3 Notifications urgentes

Les notifications qui ne peuvent pas attendre : ANSSI/CERT-FR si OIV ou OSE (dans les délais réglementaires), prestataire PRIS (si non encore mobilisé), assureur cyber (dans les conditions du contrat — souvent 24 à 48h), et direction générale (information de la bascule en crise si applicable). Les notifications complètes (CNIL 72h, dépôt de plainte) viendront dans les jours suivants mais doivent être préparées dès maintenant.

## 15.4 Fil rouge — BLACKTIDE : le déclenchement

> **🔍 BLACKTIDE — Épisode 15**
>
> 01h00 — Opération BLACKTIDE est officiellement ouverte. Nadia est IR lead. Canal Signal « IR-BLACKTIDE » activé avec 8 participants (Nadia, Karim, Marc/RSSI, David/admin astreinte, Fatima/SOC N2 relève, et 3 autres analystes mobilisables). Journal d'incident ouvert sur un tableur Excel hébergé sur le laptop personnel de Nadia (non joint au domaine Arvantis — bonne pratique improvisée).
>
> ANSSI notifiée à 08h00 le samedi (obligation OIV — site de Fos-sur-Mer impacté). Le CERT-FR accuse réception et propose un appui spécialisé OT pour le lundi. Prestataire PRIS CyberForce arrivé à 08h15 (Thomas Hartmann, consultant senior forensic, et Léa Chen, spécialiste AD). Assureur cyber AXA XL notifié à 10h00 le samedi (dans le délai contractuel de 48h).

---
