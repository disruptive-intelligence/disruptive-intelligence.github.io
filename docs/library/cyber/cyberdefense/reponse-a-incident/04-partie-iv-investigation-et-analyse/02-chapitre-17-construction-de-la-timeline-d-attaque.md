---
title: Chapitre 17 — Construction de la timeline d'attaque
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie IV — Investigation ET analyse
  - index.md
---

## 17.1 Méthode de reconstruction

La timeline d'attaque est le livrable central de l'investigation IR. Elle reconstitue la séquence complète des actions de l'attaquant, de la compromission initiale au déploiement final, en passant par chaque étape intermédiaire. La méthode est rétrospective : partir de ce qu'on sait (l'alerte qui a déclenché l'IR) et remonter dans le temps, événement par événement, jusqu'au patient zéro.

Pour chaque événement identifié, rechercher l'événement précédent : « PsExec a été exécuté sur DC01 à 22h17 — d'où venait la session ? depuis quel poste ? avec quel compte ? ce compte était-il compromis avant ? comment ? » Remonter de machine en machine, de compte en compte, jusqu'au point d'entrée initial.

Puis reconstruire la séquence dans l'ordre chronologique, en identifiant les phases ATT&CK (voir 17.3).

## 17.2 Corrélation multi-sources

Les logs d'une seule source ne racontent qu'une partie de l'histoire. L'Event Log Windows montre que PsExec a été exécuté, mais pas d'où venait la connexion. Le log VPN montre qu'un compte s'est connecté depuis l'extérieur, mais pas ce que l'utilisateur a fait ensuite. Le log proxy montre un flux vers AWS S3, mais pas quel processus l'a généré. La corrélation entre sources reconstitue la séquence complète.

Outils pour la construction de timeline : le SIEM (Splunk, ELK, Sentinel) pour la corrélation des logs centralisés, Plaso/log2timeline pour la construction d'une « Super Timeline » à partir des artefacts forensic d'un endpoint (fusion de la MFT, du Prefetch, des Event Logs, du registre en une seule timeline chronologique), et Timesketch pour la visualisation collaborative de la timeline résultante.

## 17.3 Mapping ATT&CK

Chaque étape du chemin d'attaque est cartographiée sur la matrice MITRE ATT&CK. Ce mapping remplit trois fonctions : il structure le rapport final (les TTP sont décrites dans un vocabulaire normalisé que les autres équipes de sécurité comprennent), il oriente la remédiation (pour chaque technique utilisée par l'attaquant, quelle détection ou quelle mesure préventive aurait pu la contrer ?), et il facilite le partage avec la communauté (IoC + TTP ATT&CK = renseignement actionnable pour les pairs).

## 17.4 Fil rouge — BLACKTIDE : la timeline complète

> **🔍 BLACKTIDE — Épisode 17**
>
> Après 36 heures d'investigation, la timeline est reconstituée :
>
> | Date | Action | Technique ATT&CK |
> |------|--------|-------------------|
> | J-35 (7 fév.) | Phishing ciblé sur le DRH de GestPaie — email avec pièce jointe Excel contenant macro VBA | T1566.001 — Spearphishing Attachment |
> | J-35 | Macro exécutée → téléchargement et exécution de Lumma infostealer | T1204.002 — User Execution: Malicious File |
> | J-35 | Lumma collecte credentials navigateur, cookies, credentials VPN Arvantis | T1555 — Credentials from Password Stores |
> | J-28 (12 fév.) | Première connexion VPN au réseau Arvantis avec le compte compromis (`admin_rh_ext`), 20h47 | T1078 — Valid Accounts |
> | J-25 (15 fév.) | Exécution de BloodHound pour reconnaissance AD (détecté rétrospectivement via DNS) | T1087 — Account Discovery |
> | J-21 (19 fév.) | Kerberoasting — demande de TGS pour 12 comptes de service avec SPN | T1558.003 — Kerberoasting |
> | J-21 | Crackage offline du hash du compte `svc_deploy` (mot de passe : `Deploy2024!`, 12 car.) — 4h | T1110.002 — Password Cracking |
> | J-14 (26 fév.) | DCSync sur DC01 — dump de tous les hashes NTLM, y compris krbtgt | T1003.006 — DCSync |
> | J-12 (28 fév.) | Création d'un Golden Ticket avec le hash krbtgt | T1558.001 — Golden Ticket |
> | J-12 | Création de 3 comptes admin cachés dans des OU peu surveillées | T1136.001 — Create Account: Local Account |
> | J-7 (7 mars) | Installation de rclone sur 3 serveurs internes, exfiltration vers AWS S3 | T1567.002 — Exfiltration to Cloud Storage |
> | J-7 à J-0 | Exfiltration progressive : 380 Go de données R&D et RH | T1041 — Exfiltration Over C2 Channel |
> | J-0 (14 mars) | Création d'une GPO malveillante « Windows Update Configuration » | T1484.001 — Group Policy Modification |
> | J-0, 22h10 | Déploiement de PhantomCrypt via GPO sur les serveurs de fichiers | T1486 — Data Encrypted for Impact |
> | J-0, 22h17 | Détection EDR — PsExec + désactivation Defender | T1562.001 — Disable or Modify Tools |

---
