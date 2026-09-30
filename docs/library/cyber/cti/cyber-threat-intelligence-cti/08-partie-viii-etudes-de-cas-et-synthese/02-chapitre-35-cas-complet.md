---
title: Chapitre 35 — Cas complet
source: Cyber/01_CTI/CTI.md
note: Cyber Threat Intelligence (CTI)
up:
- - Cyber Threat Intelligence (CTI)
  - ../index.md
- - Partie VIII — Études de cas ET synthèse
  - index.md
---

réponse CTI à une campagne de ransomware active

**Contexte :** Un mardi à 14h, le SOC de Sentinelle Cyber détecte un ransomware en cours de déploiement chez un client (ETI industrielle, 1 800 employés, secteur agroalimentaire). L'IR est activé (cours IR). L'analyste CTI, **Nathan Roux** (junior, 18 mois d'expérience), est mobilisé pour contextualiser la menace.

**Identification du groupe (15 min) :** La note de rançon mentionne « BlackBasta ». Nathan vérifie : le format de la note, l'extension des fichiers chiffrés (.basta), et le portail de négociation (.onion) correspondent au groupe BlackBasta connu. Confirmation : le leak site de BlackBasta (monitoring via Ransomwatch) ne liste pas encore le client — le compte à rebours n'a pas commencé.

**Contextualisation (2h) :** Nathan produit une fiche de contexte pour l'IR lead. Profil de BlackBasta : RaaS actif depuis avril 2022, soupçonné d'être composé d'anciens membres de Conti, double extorsion systématique, cible préférentiellement les entreprises industrielles européennes et nord-américaines avec un CA > 50M€. TTP typiques : accès initial via Qakbot (historiquement) ou via phishing direct (post-disruption Qakbot), mouvement latéral via Cobalt Strike, escalade via exploitation Zerologon ou PrintNightmare, exfiltration via rclone avant chiffrement. Cette contextualisation oriente l'IR : chercher les traces de Cobalt Strike, vérifier Zerologon/PrintNightmare, quantifier l'exfiltration.

**Flash alert (1h après détection) :** Nathan émet un flash alert interne (TLP:AMBER) : « Campagne BlackBasta active — client [nom] impacté — IoC joints — tous les clients du secteur agroalimentaire avec profil similaire doivent renforcer le monitoring sur les IoC suivants et vérifier l'exposition aux CVE exploitées par BlackBasta. »

**Alimentation de la cellule de crise (J+1 à J+7) :** Nathan fournit le contexte au RSSI du client pour la communication de crise (« BlackBasta est un groupe criminel connu, pas un acteur étatique — le risque est financier et réputationnel, pas géopolitique »), l'évaluation du risque de publication (« BlackBasta publie systématiquement les données des victimes qui ne paient pas — délai typique : 10-14 jours »), et le monitoring du leak site (surveillance quotidienne — le client apparaît à J+3 avec un compte à rebours de 10 jours).

**Rapport post-incident (J+30) :** Nathan produit le rapport CTI post-incident. TTP observées mappées sur ATT&CK. Corrélation avec les campagnes BlackBasta documentées : les TTP correspondent (Cobalt Strike, rclone, Zerologon). Recommandations : patching Zerologon/PrintNightmare, détection de Cobalt Strike beaconing, et monitoring dark web renforcé. Le rapport est partagé avec l'ISAC du secteur agroalimentaire.

---
