---
title: Chapitre 23 — Défense technique contre le social engineering
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie V — Défense ET contre-ingénierie sociale
  - index.md
---

## 23.1 Défense email

**DMARC en mode « reject ».** La configuration DMARC p=reject empêche l'usurpation directe du domaine de l'entreprise (un attaquant ne peut pas envoyer un email qui semble venir de @helios-aero.fr depuis un serveur non autorisé). C'est une mesure P0 — mais elle ne protège pas contre le typosquatting, les domaines lookalike ou la compromission d'email légitime.

**Bannières « email externe ».** L'ajout d'une bannière visible sur tous les emails provenant de l'extérieur de l'organisation (« ATTENTION : cet email provient d'un expéditeur externe ») est une mesure simple mais efficace qui réduit significativement le taux de réussite des phishings par display name spoofing.

**Passerelles anti-phishing.** Les solutions de sécurité email modernes (Proofpoint, Mimecast, Microsoft Defender for Office 365) analysent les URLs, les pièces jointes (sandboxing), le comportement de l'expéditeur et le contenu pour détecter les phishings. Leur efficacité est réelle mais non absolue — les emails de BEC (texte seul, pas de lien ni de pièce jointe) passent souvent les filtres.

**Simulation de phishing continue.** Les campagnes de phishing simulé régulières (mensuelles ou bimestrielles) avec retour individualisé constituent une couche de défense active qui maintient la vigilance.

## 23.2 Défense téléphonique

**Callback verification.** Pour toute demande sensible reçue par téléphone, rappeler l'interlocuteur sur un numéro de référence connu (annuaire interne, site web officiel) — jamais sur le numéro affiché (qui peut être spoofé) ni sur un numéro fourni par l'appelant.

**Procédures de helpdesk renforcées.** Les demandes de reset de credentials par téléphone doivent être soumises à une vérification d'identité robuste : callback sur le numéro enregistré, validation par le manager, code de vérification préétabli, ou vérification en personne pour les comptes à privilèges.

**STIR/SHAKEN.** Le protocole d'authentification de l'identité de l'appelant est en cours de déploiement mais reste incomplet en 2025. Il réduit le spoofing sur les réseaux conformes mais ne l'élimine pas.

## 23.3 Défense d'accès physique

**Contrôle d'accès multi-couches.** Badge seul pour les zones communes, badge + code pour les zones intermédiaires, badge + biométrie pour les zones sensibles (salle serveur, R&D, direction). La biométrie (empreintes, reconnaissance faciale) est résistante au clonage mais pose des questions RGPD (les données biométriques sont des données sensibles au sens du RGPD — leur traitement nécessite une base légale spécifique).

**Anti-tailgating.** Tourniquets unitaires, sas à passage unique, portiques à détection de double passage. Ces dispositifs sont efficaces mais nécessitent un investissement significatif et modifient les flux de circulation (impact sur l'ergonomie et l'acceptabilité par les employés).

**Politique visiteurs.** Accompagnement systématique des visiteurs par un employé de l'arrivée au départ, badge visiteur visuellement distinct (couleur, format), registre des visites, récupération du badge en fin de visite.

## 23.4 Gestion des identités et des accès

**MFA résistant au phishing.** Le déploiement de FIDO2/WebAuthn (clés de sécurité physiques ou passkeys) élimine les risques de phishing en temps réel (Evilginx) parce que l'authentification est liée au domaine — la clé ne s'active que sur le domaine légitime. C'est la mesure technique la plus efficace contre le credential harvesting par phishing. En 2025, le déploiement de FIDO2 est en forte accélération mais reste minoritaire dans les entreprises.

**Principe du moindre privilège.** Chaque utilisateur ne dispose que des accès nécessaires à ses fonctions. Cela limite l'impact d'une compromission : un identifiant d'employé standard compromis par phishing donne accès aux ressources de l'employé, pas aux ressources de l'ensemble de l'organisation.

**Surveillance des accès anormaux.** UEBA (User and Entity Behavior Analytics) et ITDR (Identity Threat Detection and Response) détectent les comportements anormaux après compromission : connexion depuis une géolocalisation inhabituelle, accès à des ressources hors du périmètre habituel, escalade de privilèges.

## 23.5 Les processus métier

**Validation multi-niveaux pour les virements.** Tout virement supérieur à un seuil défini nécessite la validation de deux personnes distinctes, dont au moins une vérification par callback. Les changements de coordonnées bancaires sont soumis à la même procédure.

**Séparation des tâches.** La personne qui initie un virement ne peut pas être la même personne qui le valide. La séparation des tâches élimine le scénario du BEC où un seul employé suffit pour déclencher un virement frauduleux.

---
