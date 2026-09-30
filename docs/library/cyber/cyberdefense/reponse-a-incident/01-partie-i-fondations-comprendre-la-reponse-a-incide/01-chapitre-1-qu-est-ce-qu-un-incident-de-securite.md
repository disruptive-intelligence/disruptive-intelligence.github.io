---
title: Chapitre 1 — Qu'est-ce qu'un incident de sécurité
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - 'Partie I — Fondations : comprendre la réponse à incident'
  - index.md
---

## 1.1 Définition opérationnelle : événement, alerte, incident, crise

La chaîne conceptuelle qui va du bruit ambiant du système d'information jusqu'à la crise majeure comprend quatre niveaux distincts, et la confusion entre ces niveaux est une source récurrente de dysfonctionnement dans les organisations.

Un **événement** est un fait observable dans le système d'information : une connexion réseau, une authentification, une modification de fichier, un scan de port, un redémarrage de service. Les systèmes d'information modernes génèrent des milliards d'événements par jour. La quasi-totalité sont normaux et attendus.

Une **alerte** est un événement signalé par un système de détection (EDR, SIEM, IDS, antivirus, règle de corrélation) comme potentiellement anormal ou malveillant. Le taux de faux positifs des systèmes de détection varie considérablement (de 10 % dans les environnements bien calibrés à plus de 90 % dans les environnements mal configurés), ce qui signifie que la majorité des alertes ne correspondent pas à des incidents réels. Le travail du SOC est précisément de trier ces alertes pour identifier celles qui nécessitent une investigation.

Un **incident** est une alerte confirmée qui compromet effectivement la confidentialité, l'intégrité, ou la disponibilité d'un actif du système d'information. La confirmation transforme la suspicion en certitude : un comportement malveillant est effectivement en cours ou a eu lieu. L'incident déclenche des processus spécifiques (investigation, confinement, notification) et mobilise des acteurs qui ne sont pas impliqués dans le traitement des alertes courantes.

Une **crise cyber** est un incident dont l'impact dépasse la capacité de réponse normale de l'organisation et nécessite l'activation d'une gouvernance exécutive. La crise se caractérise par l'ampleur de l'impact (technique, business, réputationnel, réglementaire), l'incertitude sur l'évolution, la pression temporelle intense, et la nécessité de décisions stratégiques qui dépassent le périmètre de l'équipe technique. La distinction entre incident et crise est traitée en profondeur au Ch.3.

Ces distinctions ne sont pas sémantiques. Elles déterminent le niveau de mobilisation (qui est réveillé à 2h du matin), les processus activés (IRP, cellule de crise, communication), les obligations réglementaires (notification ANSSI, CNIL), et les interlocuteurs impliqués (la direction générale n'est pas mobilisée pour chaque alerte — elle l'est pour une crise).

> **Piège fréquent :** Confondre la gravité technique et la gravité business. Un malware sur un poste isolé sans données sensibles est un incident technique mineur même si le malware est sophistiqué. Un phishing qui compromet le compte email du directeur financier est un incident business potentiellement majeur même si la technique est triviale. La classification doit intégrer les deux dimensions.

## 1.2 Taxonomie des incidents

Une taxonomie partagée est indispensable pour trois raisons : elle accélère le triage (chaque catégorie active un playbook spécifique — voir Ch.7), elle normalise la communication (tous les acteurs parlent le même langage), et elle structure le reporting (les métriques et les tendances ne sont comparables que si les incidents sont classés de manière cohérente).

La classification par **vecteur d'attaque** identifie comment l'attaquant a pénétré le système : phishing (email, SMS, voix), exploitation de vulnérabilité (0-day, N-day non patchée), compromission supply chain (mise à jour logicielle piégée, prestataire compromis), credential stuffing ou brute force, insider (employé ou ex-employé malveillant), accès physique, ou compromission de tiers de confiance (VPN prestataire, accès partenaire).

La classification par **objectif** identifie ce que l'attaquant cherche à accomplir : ransomware et extorsion (chiffrement + menace de publication), espionnage et exfiltration (vol de propriété intellectuelle, renseignement), sabotage et destruction (wiper, manipulation de systèmes OT), fraude financière (BEC, détournement de virements), hacktivisme (défacement, DDoS idéologique), ou cryptomining (utilisation des ressources de calcul).

La classification par **impact** identifie les conséquences : atteinte à la confidentialité (données exposées), atteinte à la disponibilité (systèmes hors service), atteinte à l'intégrité (données modifiées), impact réputationnel (perte de confiance des clients, médiatisation), impact réglementaire (notification obligatoire, sanctions), et impact financier (perte d'exploitation, rançon, frais de remédiation).

La classification par **gravité** va de P4 (incident mineur — malware isolé, phishing sans compromission) à P1 (incident critique — compromission de l'AD, ransomware à grande échelle, exfiltration massive) avec des critères objectifs pour chaque niveau. Le détail de la grille de gravité est en Annexe G.

## 1.3 L'incident comme révélateur systémique

Un incident de sécurité n'est jamais un événement isolé. Il est le symptôme visible d'une ou plusieurs défaillances systémiques dans les couches de défense de l'organisation. L'investigation IR ne vise pas seulement à résoudre l'incident présent — elle vise à comprendre pourquoi les défenses ont échoué et à corriger les causes racines.

Pourquoi le phishing a-t-il fonctionné ? Parce que le sous-traitant n'avait pas de MFA, parce que l'utilisateur n'était pas formé, parce que le filtre anti-phishing n'a pas détecté la pièce jointe. Pourquoi l'attaquant a-t-il pu progresser pendant 5 semaines ? Parce que l'infostealer a échappé à l'antivirus, parce que les alertes de l'EDR ont été classées en faux positifs, parce que la surveillance des comptes de service était insuffisante. Pourquoi le ransomware a-t-il pu chiffrer les sauvegardes ? Parce qu'elles étaient sur le même réseau, accessibles avec les mêmes credentials.

Chaque « pourquoi » révèle une faille corrigeable. C'est cette logique de Root Cause Analysis qui transforme un incident douloureux en opportunité d'amélioration structurelle. L'IR n'est pas du « pompierisme » — c'est de l'investigation structurée avec un double objectif : résoudre l'incident actuel ET empêcher le suivant.

## 1.4 Fil rouge — BLACKTIDE : l'alerte initiale

> **🔍 BLACKTIDE — Épisode 1**
>
> Vendredi 14 mars 2026, 22h17. L'EDR CrowdStrike Falcon déployé sur le contrôleur de domaine DC01 d'Arvantis déclenche une alerte de sévérité « haute » : détection de l'exécution de `PsExec.exe` depuis le répertoire `C:\Users\svc_deploy\AppData\Local\Temp\`, couplée à une modification de GPO visant à désactiver Windows Defender (commande PowerShell `Set-MpPreference -DisableRealtimeMonitoring $true` exécutée via GPO).
>
> Karim Belkacem, analyste SOC N2 en astreinte, reçoit l'alerte sur son téléphone. Il se connecte à la console EDR depuis son domicile et vérifie : aucune opération de maintenance planifiée ce soir, le compte `svc_deploy` est un compte de service rarement utilisé, et l'exécution de PsExec depuis un répertoire temporaire est anormale. Il contacte l'administrateur d'astreinte : « Tu as lancé quelque chose sur DC01 ce soir ? » Réponse : « Non, rien du tout. »
>
> Karim qualifie : **incident confirmé**. L'activité n'est pas légitime, elle cible un contrôleur de domaine, et elle implique un outil de mouvement latéral et une tentative de désactivation des défenses. Classification initiale : P2 (incident significatif — compromission de serveur critique), en attente de réévaluation.
>
> Il applique la procédure d'escalade : appel à l'IR lead, Nadia Moreau. Il est 22h45.
>
> Première question que personne ne pose encore : depuis combien de temps l'attaquant est-il dans le réseau ?

---
