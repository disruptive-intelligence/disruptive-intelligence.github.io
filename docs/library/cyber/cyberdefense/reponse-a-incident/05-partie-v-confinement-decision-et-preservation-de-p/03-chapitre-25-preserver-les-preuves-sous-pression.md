---
title: Chapitre 25 — Préserver les preuves sous pression
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie V — Confinement, décision ET préservation de preuve
  - index.md
---

## 25.1 L'ordre de volatilité

La collecte de preuves doit suivre l'ordre de volatilité — du plus éphémère au plus durable. La **mémoire vive** s'efface à l'extinction (collecte en 10-20 minutes avec DumpIt). L'**état des processus et connexions réseau** est dynamique (capture via EDR ou ligne de commande). Les **fichiers temporaires et artefacts système** persistent jusqu'à écrasement. Les **logs** persistent jusqu'à rotation (jours à mois). Les **disques** persistent indéfiniment (sauf chiffrement par le ransomware).

Le principe fondamental : collecter AVANT ou PENDANT le confinement, pas après. Le confinement peut impliquer l'extinction de machines (perte de RAM), la modification de configurations réseau (perte de l'état réseau), ou la restauration de systèmes (écrasement des artefacts).

## 25.2 Chaîne de custody

Chaque acquisition est documentée avec un formulaire de chaîne de custody (template en Annexe C) : identifiant unique de la preuve, description (machine, type d'acquisition), analyste responsable, date et heure de l'acquisition, outil et version utilisés, hash SHA256 de l'image ou du fichier, lieu de stockage, et journal des accès ultérieurs.

## 25.3 Les erreurs qui détruisent les preuves

Redémarrer un serveur compromis sans collecte mémoire préalable (RAM perdue — irréversible). Lancer un scan antivirus qui supprime ou met en quarantaine le malware (sample perdu — le hash est peut-être préservé dans les logs, mais le binaire est détruit). Restaurer un système depuis une sauvegarde avant acquisition forensic (tous les artefacts écrasés). Modifier des configurations réseau avant capture de l'état (connexions actives perdues). Ne pas documenter les actions prises (impossible de reconstituer la séquence pour le retex ou la procédure judiciaire).

Chacune de ces erreurs est commise régulièrement par des administrateurs IT qui agissent de bonne foi mais sans formation IR. La formation des IT à « ne pas toucher avant le forensic » est un investissement de préparation critique (Ch.5).

## 25.4 Fil rouge — BLACKTIDE : la preuve perdue

> **🔍 BLACKTIDE — Épisode 25**
>
> Deux serveurs de fichiers (FS01-Lyon et FS01-Fos) ont été redémarrés par David (admin astreinte) à 23h30, avant l'arrivée du PRIS. Nadia documente factuellement : « Serveurs redémarrés sans collecte préalable — cause : absence de procédure. Conséquence : perte de la RAM et des artefacts de session. » Elle note dans ses recommandations RETEX : « Former les admins d'astreinte au premier réflexe IR : NE PAS redémarrer, APPELER l'IR lead. »

---
