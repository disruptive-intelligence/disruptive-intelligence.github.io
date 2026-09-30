---
title: Partie VII — Gestion de crise, communication ET coordination
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - index.md
---

*Quand l'incident dépasse le cadre technique : piloter la crise, communiquer sous pression, coordonner les parties prenantes, et gérer les dimensions juridique et financière.*

---


## Chapitre 33 — Quand l'incident devient une crise

Ce chapitre approfondit les critères de bascule introduits au Ch.3 et détaille la dynamique de crise — ce qui change concrètement quand la gouvernance exécutive est activée. La crise se caractérise par la multiplicité des fronts (technique, communication, juridique, métier, RH, financier ouverts simultanément), l'incertitude amplifiée (la direction demande des réponses que personne ne peut encore donner), la pression temporelle démultipliée (le leak site a un compte à rebours, la CNIL attend la notification dans 72h, les clients appellent, le CA se réunit mardi), et les risques de décisions impulsives sous stress (couper tout le réseau par panique, communiquer prématurément, payer la rançon par peur).

Le passage en crise ne signifie pas que la cellule technique est dessaisie — elle continue de piloter la réponse technique. Cela signifie qu'une cellule exécutive se met en place en parallèle pour gérer les dimensions non techniques.

---


## Chapitre 34 — Cellule de crise cyber

### 34.1 Composition

DG ou représentant mandaté (décisions stratégiques), RSSI (charnière technique/exécutif), IR lead (situation technique, en visioconférence depuis la salle technique), DRH (impact employés, communication interne), directeur juridique (obligations réglementaires, dépôt de plainte, exposition), directeur de la communication (communication externe et interne, relation presse), DPO (RGPD, CNIL), directeur des opérations/métiers (impact production, priorisation de la reprise), DSI (ressources IT, infrastructure, budgets d'urgence).

### 34.2 Fonctionnement

Le rythme des points de situation est de toutes les 4 à 6 heures en phase aiguë (les premières 48h), puis 1 à 2 fois par jour en phase de stabilisation. Chaque point suit un format standardisé : situation technique (par l'IR lead ou le RSSI — 5 minutes, pas 30), situation communication (messages envoyés, retours reçus, demandes presse), situation juridique (notifications effectuées, plainte, assurance), décisions à prendre (options formulées, pas de discussions techniques), et prochaine échéance.

Le tableau de bord de crise résume en une page : périmètre technique (systèmes touchés / total), impact business (production arrêtée / en cours), notifications (ANSSI fait/à faire, CNIL fait/à faire, plainte fait/à faire), communication (interne fait/à faire, externe fait/à faire), et prochains jalons (prochaine décision, prochaine échéance réglementaire).

### 34.3 Erreurs classiques de la cellule de crise

Vouloir tout décider en plénière (paralysie — les discussions techniques de 45 minutes sur les Event IDs Windows n'ont pas leur place en cellule exécutive). Mélanger la cellule technique et la cellule exécutive (l'analyste forensic et le CEO n'ont rien à se dire directement — c'est le RSSI qui fait l'interface). Changer de stratégie à chaque point de situation (inconstance — les décisions prises doivent être maintenues sauf fait nouveau majeur). Sous-estimer la durée (« ce sera réglé lundi » → ce sera réglé dans 2 semaines minimum). Et négliger la fatigue des équipes (au bout de 72h sans dormir, les décisions sont mauvaises — la rotation est un enjeu de santé ET de qualité).

---


## Chapitre 35 — Communication de crise

### 35.1 Communication interne vers les employés

Le premier message aux employés doit être envoyé dès que les consignes de sécurité sont claires — pas avant (un message « on a un problème mais on ne sait pas quoi vous dire » est pire que le silence). Canal : si la messagerie est compromise, utiliser un canal alternatif (SMS masse, téléphone, réseau social d'entreprise s'il est hébergé hors SI, affichage physique dans les locaux).

Contenu type du premier message : « Un incident informatique majeur est en cours de traitement par nos équipes. Par précaution : ne connectez aucun appareil au réseau d'entreprise, ne cliquez sur aucun lien suspect, changez vos mots de passe dès que le service sera rétabli. Nous vous informerons régulièrement de l'évolution de la situation. »

Ce qu'il ne faut PAS dire dans le premier message : ne pas utiliser les mots « ransomware », « données volées », « piratage » tant que la communication n'est pas validée juridiquement. Ne pas minimiser (« un petit problème technique ») — les employés verront les serveurs éteints et les usines arrêtées, la minimisation détruit la crédibilité. Ne pas accuser (ni interne ni externe — les conclusions de l'investigation viendront plus tard).

### 35.2 Communication vers la direction et le conseil d'administration

La direction a besoin d'une note de synthèse sur 2 pages maximum, en langage non technique : impact financier estimé (perte de production + frais IR + frais juridiques + impact réputationnel), état de la couverture assurantielle, calendrier de reprise (réaliste, pas optimiste), exposition juridique (notifications, plainte, sanctions potentielles), et décisions en attente (payer ou ne pas payer, communiquer ou ne pas communiquer).

### 35.3 Communication externe : clients, partenaires, médias

La communication externe est déclenchée quand l'un des critères suivants est rempli : obligation contractuelle (certains contrats clients prévoient une notification en cas de compromission de leurs données), obligation réglementaire (RGPD si données personnelles de clients sont compromises), ou médiatisation (si l'attaquant a revendiqué publiquement, ou si un journaliste appelle, il est trop tard pour le silence — mieux vaut communiquer proactivement avec un message maîtrisé que de subir une couverture non contrôlée).

La communication médias suit des règles strictes : porte-parole unique, communiqué de presse validé juridiquement, message factuel (ce qu'on sait, ce qu'on fait, ce qu'on ne peut pas encore confirmer), et jamais de mensonge (si l'information s'avère fausse plus tard, la crédibilité est détruite et l'exposition juridique augmente).

### 35.4 Fil rouge — BLACKTIDE : la communication

> **🔍 BLACKTIDE — Épisode 35**
>
> Samedi 14h : SMS envoyé aux 12 000 employés via la plateforme de mass SMS (hors SI). Dimanche : note au conseil d'administration (réunion téléphonique extraordinaire). Lundi : communication aux 15 principaux clients industriels (les contrats prévoient une notification). Mardi : article dans la presse spécialisée (un journaliste de LeMagIT a vu la revendication PhantomCrypt). Réaction : communiqué de presse factuel publié le mardi 14h, après validation par le directeur juridique. J+10 : publication des données. Notification individuelle aux 8 000 employés concernés (email + courrier papier pour les données les plus sensibles).

---


## Chapitre 36 — Coordination avec les parties prenantes externes

### 36.1 ANSSI et CERT-FR

L'ANSSI est notifiée dès la confirmation de l'incident sur un OIV (obligation légale). Le CERT-FR peut fournir un appui technique (analyse de malware, partage d'IoC, déploiement d'équipes spécialisées — notamment en environnement OT). La relation est de coopération, pas de contrôle : l'ANSSI aide, elle n'inspecte pas (dans le cadre de la réponse à incident — les inspections sont un processus séparé).

### 36.2 Forces de l'ordre

Le dépôt de plainte est recommandé même s'il n'est pas juridiquement obligatoire (sauf pour l'activation de certaines polices d'assurance — la loi LOPMI de 2023 conditionne le remboursement du sinistre cyber au dépôt de plainte dans les 72h suivant la connaissance de l'incident). Le dossier de plainte comprend un rapport technique (chronologie, IoC, dommages), une estimation des préjudices, et les preuves collectées (avec chaîne de custody). L'enquête judiciaire peut apporter des éléments utiles à l'IR (identification de l'attaquant, saisie d'infrastructure, restitution de données), mais elle est longue (mois à années) et son calendrier n'est pas synchronisé avec celui de la réponse technique.

### 36.3 Prestataire PRIS et assureur

Le PRIS est intégré à la cellule technique, sous la coordination de l'IR lead interne. L'assureur est activé dans les conditions du contrat. L'assureur mandatera souvent ses propres experts (forensic, juridique, communication de crise) — il est important de clarifier l'articulation entre les experts de l'assureur et l'équipe IR de l'organisation pour éviter les redondances et les conflits d'intérêts.

---


## Chapitre 37 — Volet juridique, réglementaire et financier

### 37.1 Le dépôt de plainte en détail

Plainte simple (le parquet décide de poursuivre ou non) vs plainte avec constitution de partie civile (l'organisation se constitue partie civile et peut accéder au dossier d'instruction). Le dossier de plainte technique comprend la chronologie des faits, les indicateurs de compromission, les dommages constatés (chiffrement, exfiltration, arrêt de production), et l'estimation des préjudices (directs et indirects).

### 37.2 Le volet RGPD

La notification CNIL sous 72h comprend la nature de la violation (type de données, nombre de personnes, catégories de personnes concernées), les conséquences probables (risque d'usurpation d'identité, risque financier, risque de discrimination), et les mesures prises (confinement, éradication, notification aux personnes). La notification aux personnes concernées est obligatoire quand le risque est élevé (article 34 RGPD) — elle doit être claire, compréhensible, et inclure des recommandations concrètes (changer ses mots de passe, surveiller ses comptes bancaires, signaler toute activité suspecte).

### 37.3 Coût total de l'incident

L'estimation du coût total est un exercice nécessaire pour le retex, pour l'assureur, et pour le conseil d'administration. Les catégories de coûts incluent les coûts directs (prestataire PRIS, reconstruction IT, outils d'urgence, heures supplémentaires), la perte d'exploitation (production arrêtée × jours × marge), les coûts juridiques (avocat, procédure, notification CNIL, notification personnes), les coûts de communication (agence de communication de crise, communiqués, notifications individuelles), les coûts de durcissement (mesures post-incident, plan structurel), et les coûts indirects (perte de clients, atteinte à la réputation, impact sur le cours de bourse, attrition des talents).

### 37.4 Fil rouge — BLACKTIDE : le bilan financier

> **🔍 BLACKTIDE — Épisode 37**
>
> Coût total estimé : **8,5 M€**.
> - Prestataire PRIS CyberForce : 350 K€ (2 consultants × 15 jours + analyses complémentaires).
> - Reconstruction et remédiation IT : 1,2 M€ (reconstruction DC, serveurs de fichiers, sauvegardes immuables, déploiement EDR 100 %).
> - Perte de production (3 sites × 12 jours) : 3 M€.
> - Plan de durcissement structurel 18 mois : 1,5 M€ (NDR, PAW, tiering, M365 E5, Sysmon, exercices).
> - Frais juridiques et communication : 500 K€ (avocat, communication de crise, notifications CNIL + personnes).
> - Impact commercial et réputationnel estimé : 1,8 M€ (perte de contrats, dépréciation de marque).
> - Franchise assurance : 200 K€.
>
> Couverture assurance AXA XL : 3,2 M€ (frais IR + perte d'exploitation, dans la limite du plafond de 5 M€ après franchise).
> Reste à charge pour Arvantis : environ 5,3 M€.

---
