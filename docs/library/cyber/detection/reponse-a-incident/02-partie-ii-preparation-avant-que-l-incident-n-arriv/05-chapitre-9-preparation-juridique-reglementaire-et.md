---
title: Chapitre 9 — Préparation juridique, réglementaire et contractuelle
source: Cyber/06 Détection & réponse/Réponse à incident/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie II — Préparation : avant que l''incident n''arrive'
  - index.md
---

## 9.1 Obligations de notification

Le paysage réglementaire français impose plusieurs obligations de notification en cas d'incident cyber, avec des délais et des destinataires différents.

**ANSSI — OIV :** les Opérateurs d'Importance Vitale doivent notifier l'ANSSI dans les délais prescrits par les arrêtés sectoriels (variable selon le secteur, mais typiquement « sans délai » pour les incidents majeurs). La notification est obligatoire, et le non-respect peut entraîner des sanctions. L'ANSSI peut déployer des équipes du CERT-FR en appui.

**NIS 2 — Entités essentielles et importantes :** la directive NIS 2, en cours de transposition en France via la « Loi Résilience » (adoptée en commission spéciale à l'Assemblée nationale en septembre 2025, adoption finale attendue début 2026), imposera une notification initiale sous 24 heures (alerte préliminaire indiquant qu'un incident significatif a été détecté) et une notification complète sous 72 heures (analyse de l'incident, impact, mesures prises). Les entités concernées sont considérablement plus nombreuses qu'avec NIS 1 : environ 15 000 entités en France, réparties en « entités essentielles » et « entités importantes » selon leur secteur et leur taille. Les sanctions prévues sont significatives (amendes administratives pouvant atteindre 10 M€ ou 2 % du CA mondial pour les entités essentielles).

**CNIL — Violations de données personnelles :** notification sous 72 heures après la « prise de connaissance » de la violation (article 33 du RGPD). La « prise de connaissance » n'est pas le moment de la détection de l'incident, mais le moment où l'organisation acquiert une certitude raisonnable que des données personnelles sont compromises. La notification doit décrire la nature de la violation, les catégories de données concernées, le nombre de personnes touchées, les conséquences probables, et les mesures prises. Si la violation présente un risque élevé pour les personnes (données de santé, données bancaires, données permettant l'usurpation d'identité), la notification aux personnes concernées est également obligatoire (article 34 du RGPD).

**Forces de l'ordre :** le dépôt de plainte n'est pas une obligation réglementaire mais une recommandation forte, et il est souvent nécessaire pour activer l'assurance cyber. La plainte se fait auprès du procureur de la République (parquet de Paris, section J3 cybercriminalité pour les affaires complexes). Le dépôt de plainte ne nécessite pas d'avoir terminé l'investigation — il peut être fait dès que l'incident est confirmé, avec les éléments disponibles à ce stade.

La préparation de ces notifications en amont (templates pré-rédigés en Annexe C, contacts identifiés, processus documenté) accélère considérablement la réponse le jour J.

## 9.2 Cadre contractuel des prestataires et assurance cyber

Le contrat avec le prestataire PRIS doit prévoir les SLA d'intervention (délai maximum entre l'appel et l'arrivée sur site ou la connexion à distance), le périmètre (quelles activités PRIS sont couvertes — toutes les 5 activités du référentiel ANSSI ?), les conditions de remontée d'information (que communique le PRIS au commanditaire, quand, sous quelle forme), les clauses de confidentialité (le PRIS a accès aux données les plus sensibles de l'organisation), et la responsabilité en cas de perte de preuve.

L'assurance cyber est un élément de plus en plus important de la préparation IR. Les points clés à connaître avant l'incident : les conditions d'activation (notification dans les délais — souvent 24 à 48h, préservation des preuves, non-aggravation), la couverture (frais de réponse à incident, perte d'exploitation, frais juridiques, frais de notification, communication de crise — et éventuellement la rançon, sujet controversé et variable selon les polices), les exclusions (actes de guerre, faute intentionnelle, certaines exclusions spécifiques), les plafonds et franchises, et la liste de prestataires agréés par l'assureur (vérifier la compatibilité avec le PRIS sous contrat).

## 9.3 Conservation de preuve et recevabilité judiciaire

Les preuves collectées pendant l'IR peuvent être utilisées dans une procédure pénale (plainte pour accès frauduleux aux systèmes — art. 323-1 du Code pénal, extorsion — art. 312-1, destruction de données — art. 323-2) ou civile (action contre un prestataire défaillant, contentieux assurance). Pour être recevables, elles doivent respecter la chaîne de custody : documentation de chaque acquisition, calcul et vérification des hash SHA256, stockage sécurisé et intégrité vérifiable. Le détail de la chaîne de custody est traité au Ch.25.

## 9.4 Fil rouge — BLACKTIDE : les obligations d'Arvantis

> **🔍 BLACKTIDE — Épisode 9**
>
> Arvantis est OIV sur 2 sites (Fos-sur-Mer et Lyon) → notification ANSSI obligatoire, effectuée le samedi 15 mars à 08h00. Données RH de 8 000 employés potentiellement exfiltrées (noms, adresses, RIB, numéros de sécurité sociale) → notification CNIL sous 72h, préparée par le DPO dès le samedi, envoyée le lundi 17 mars. Contrat PRIS en place avec CyberForce (SLA : 12h le week-end, couverture des 5 activités PRIS). Assurance cyber souscrite auprès d'AXA XL (plafond 5 M€, franchise 200 K€, exclusion rançon dans cette police, liste de prestataires agréés incluant CyberForce).

---
