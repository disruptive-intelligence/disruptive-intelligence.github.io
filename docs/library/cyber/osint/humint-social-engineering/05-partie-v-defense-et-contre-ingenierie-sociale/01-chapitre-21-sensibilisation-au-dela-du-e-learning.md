---
title: 'Chapitre 21 — Sensibilisation : au-delà du e-learning annuel'
source: Cyber/02 OSINT/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie V — Défense et contre-ingénierie sociale
  - index.md
---

## 21.1 Pourquoi la sensibilisation classique ne fonctionne pas

Les formations de sensibilisation e-learning annuelles — un module en ligne de 30 minutes suivi d'un quiz à choix multiples — ont un impact démontrablement limité sur le comportement réel des employés. Les études montrent que le taux de clic sur les campagnes de phishing diminue faiblement (5-10 %) après une formation e-learning et que cet effet s'estompe en quelques semaines.

Les raisons de cet échec sont identifiées. Le biais d'optimisme (« je sais maintenant, donc je ne me ferai pas piéger ») est renforcé par la réussite au quiz — l'employé a la preuve qu'il « connaît le phishing ». Le transfert d'apprentissage est faible : reconnaître un phishing dans un contexte d'examen (où on s'attend à un phishing) est radicalement différent de reconnaître un phishing dans le flux quotidien de 200 emails alors qu'on est pressé par un deadline. Et la formation traite le phishing comme un problème de connaissance (« si vous savez, vous ne cliquerez pas ») alors que c'est un problème de comportement en situation de charge cognitive (« même en sachant, vous cliquerez si les conditions sont réunies »).

## 21.2 Les formations qui fonctionnent

**Les simulations réalistes.** Les campagnes de phishing simulé (envoyées sans avertissement préalable, avec des leurres crédibles personnalisés) sont significativement plus efficaces que les formations théoriques. Le retour individualisé après le clic (« vous avez cliqué parce que l'email exploitait le mécanisme X — voici comment le détecter ») est l'élément pédagogique clé. Important : le retour doit être explicatif et bienveillant, jamais punitif.

**Les exercices de vishing.** Les simulations d'appels téléphoniques de social engineering (par le red team interne ou un prestataire) testent la résistance des employés au pretexting vocal — une compétence que les formations e-learning ne développent pas du tout.

**Les micro-formations ciblées.** Sessions courtes (15-20 min) sur un sujet spécifique, adaptées au profil de risque : BEC pour les DAF et la comptabilité, pretexting helpdesk pour l'IT support, tailgating pour la réception et la sécurité, élicitation pour les ingénieurs R&D et les dirigeants. La pertinence thématique augmente l'engagement et le transfert.

**Les exercices tabletop.** Scénarios d'incident de social engineering discutés en groupe (comité de direction, équipe de sécurité, service concerné) : « un employé reçoit cet appel — que fait-il ? que fait son manager ? que fait le SOC ? ». Les exercices tabletop développent les réflexes collectifs et identifient les failles de processus.

## 21.3 La formation par profil de risque

Tout le monde n'a pas besoin de la même formation. Les profils à risque doivent recevoir une formation spécifique adaptée aux menaces qui les ciblent.

| Profil | Menace principale | Formation prioritaire |
|---|---|---|
| DAF / Comptabilité | BEC, fraude au fournisseur | Processus de vérification, callback, double validation |
| Assistants de direction | Fraude au président, impersonation du dirigeant | Vérification des demandes urgentes, procédure de validation |
| Helpdesk / IT Support | Pretexting, reset de credentials, MFA manipulation | Procédures de vérification d'identité renforcées |
| Ingénieurs R&D | Élicitation, faux recruteurs, ingérence étrangère | Contre-élicitation, signaux d'alerte HUMINT, protection en conférence |
| Réception / Sécurité | Tailgating, impersonation, intrusion physique | Procédures de vérification des visiteurs, refus poli |
| Dirigeants | Ciblage personnel, deepfake, spear-phishing VIP | Surface d'exposition personnelle, sécurité des communications |

## 21.4 Mesurer l'efficacité

Les métriques classiques (taux de clic sur le phishing simulé) sont nécessaires mais insuffisantes. Un programme de mesure complet inclut : le taux de clic (en baisse au fil des campagnes ?), le taux de signalement (en hausse ? — plus important que le taux de clic, car il mesure la culture de sécurité), le temps de signalement (les employés signalent-ils dans les minutes ou les heures ?), le taux de récidive (les employés qui ont cliqué une fois cliquent-ils encore ?), et les résultats qualitatifs des exercices de vishing et d'intrusion physique.

**Limite importante** : les métriques de phishing ne mesurent pas la résistance au vishing, à l'élicitation ou à l'intrusion physique. Un employé qui ne clique jamais sur les phishings simulés peut se faire piéger par un appel téléphonique convaincant ou une élicitation de face-à-face. La mesure doit être multi-vecteurs.

## 21.5 La culture de sécurité

La culture de sécurité est l'objectif final — au-delà de la formation et des processus, c'est l'environnement humain qui détermine la résilience d'une organisation face au social engineering.

Une culture de sécurité efficace se caractérise par : le signalement encouragé (signaler un email, un appel ou un comportement suspect est perçu comme un acte positif, jamais comme une perte de temps ou une preuve de paranoïa), la vérification normalisée (vérifier l'identité d'un interlocuteur, même s'il se présente comme un supérieur hiérarchique, est un acte professionnel, pas un acte de défiance), la transparence (les résultats des tests de social engineering sont partagés avec les employés — sans nommer les individus — pour démontrer la réalité de la menace), et le renforcement positif (les employés qui signalent sont remerciés publiquement, pas les employés qui « ne se font jamais piéger » — car ceux qui ne signalent jamais ne sont pas nécessairement plus vigilants, ils sont peut-être simplement moins exposés).

---
