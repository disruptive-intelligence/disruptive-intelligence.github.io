---
title: Chapitre 15 — Manipulation psychologique avancée
source: Cyber/02 OSINT/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie III — Social engineering physique
  - index.md
---

de la théorie à l'opérationnel

Ce chapitre est le pendant opérationnel du Ch.2. Là où le Ch.2 explique *pourquoi* les leviers psychologiques fonctionnent (cognition, biais, mécanismes), le présent chapitre explique *comment* le praticien les met en œuvre concrètement en situation.

## 15.1 Le pied dans la porte et la porte au nez

**Le pied dans la porte.** Commencer par une petite demande à laquelle la cible accède facilement, puis escalader vers la demande réelle. La première compliance crée un engagement psychologique qui rend le refus de la demande suivante plus coûteux. En red team : « Est-ce que vous pouvez me montrer où sont les toilettes ? » (petite demande, accès au couloir) → « Au fait, vous savez où est la salle serveur ? Mon collègue m'attend là-bas pour l'intervention » (demande réelle).

**La porte au nez.** Commencer par une demande excessive que la cible refusera, puis proposer une demande modérée (la vraie demande) qui sera perçue comme un compromis raisonnable. « Je dois vérifier tous les postes de travail de l'étage — ça va prendre la journée. » Refus. « Bon, au minimum je dois vérifier le poste du responsable, ça prendra 5 minutes. » Acceptation. La concession de l'éliciteur crée une obligation de concession réciproque.

## 15.2 La création de rapport rapide

Le rapport — cette connexion interpersonnelle qui crée un sentiment de confiance et de sympathie — peut être construit en quelques minutes avec des techniques documentées.

**Le mirroring.** Reproduire subtilement les gestes, la posture, le rythme de parole et le vocabulaire de l'interlocuteur. Le mirroring active les neurones miroirs et crée un sentiment de similarité inconscient. Il doit être subtil — un mirroring trop évident est perçu comme moquerie et détruit le rapport.

**Le pacing-leading.** S'aligner d'abord sur l'état émotionnel et le rythme de la cible (pacing), puis progressivement l'amener vers l'état souhaité (leading). Si la cible est stressée, commencer par un tempo rapide et une énergie élevée (pacing), puis ralentir progressivement (leading) pour créer un état de calme et d'ouverture.

**Les limites éthiques.** Le rapport est un outil, pas une fin en soi. Le red teamer ne crée pas de relation affective réelle — il simule une connexion pour atteindre un objectif opérationnel. La distinction est fondamentale : le rapport de red team est une technique temporaire et bornée. Un red teamer qui développe une relation personnelle authentique avec une cible franchit une ligne éthique.

## 15.3 Le pretexting avancé et la résistance au questionnement

Un pretexte avancé n'est pas une simple identité fictive — c'est un personnage complet avec une histoire, des mannerisms, des réponses aux questions imprévues, et une cohérence interne suffisante pour résister à un interrogatoire léger.

La construction d'un pretexte robuste inclut : une identité complète (nom, entreprise, poste, ancienneté, parcours), une backstory cohérente (comment et pourquoi cette personne est là aujourd'hui), des détails sensoriels (vêtements, accessoires, matériel — cohérents avec le rôle), une préparation aux questions (« qui vous a envoyé ? », « quel est votre numéro de ticket ? », « comment s'appelle votre responsable ? »), et un plan de sortie si le pretexte est mis en doute.

La durée d'un pretexte varie de quelques minutes (interaction avec un gardien) à plusieurs semaines (opération d'élicitation prolongée, faux profil LinkedIn maintenu sur des mois). Plus la durée augmente, plus le risque de démasquage est élevé et plus la maintenance du pretexte consomme de ressources.

## 15.4 Gestion de la résistance et de la confrontation

Quand la cible dit non, hésite ou exprime de la suspicion, le praticien dispose de plusieurs options.

**Le pivoting.** Changer d'angle d'approche sans changer de pretexte. Si la demande directe échoue, reformuler indirectement. « Je ne peux pas vous donner accès au réseau » → « Pas de problème, je comprends — je peux juste utiliser le WiFi visiteur pour envoyer un email à mon responsable ? » (le WiFi visiteur peut révéler des informations sur l'infrastructure réseau).

**Le recadrage.** Réinterpréter le refus dans un cadre favorable. « Non, je ne suis pas autorisé à donner cette information » → « Bien sûr, je comprends parfaitement — votre politique de sécurité est impressionnante. Justement, c'est ce que je veux documenter dans mon rapport d'audit. »

**L'abandon gracieux.** Quand la résistance est trop forte ou la suspicion trop élevée, se retirer proprement sans éveiller davantage de soupçons. « Pas de souci, je vais rappeler mon responsable pour clarifier. Merci de votre temps. » Un abandon gracieux préserve la possibilité d'une seconde tentative par un autre vecteur.

**La lecture des signaux de gêne.** Reconnaître quand la cible passe de la coopération à l'inconfort : changement de posture (bras croisés, recul), regard fuyant, réponses plus courtes, changement de sujet, vérification du badge. Ces signaux indiquent que la vigilance de la cible est activée et que l'escalade risque la confrontation.

## 15.5 Les limites absolues du red team

Certaines techniques sont absolument proscrites en red team, même si un attaquant réel les utiliserait. L'exploitation de vulnérabilités personnelles (addiction, maladie, problèmes financiers, détresse émotionnelle), les menaces, le chantage, l'intimidation réelle, l'établissement d'une relation intime ou sentimentale avec une cible, et toute action susceptible de causer une détresse psychologique durable sont des lignes rouges non négociables. Un red teamer qui franchit ces lignes cause un préjudice réel à des individus réels — ce qui est contraire à l'objectif même du test, qui est d'améliorer la sécurité, pas de traumatiser des employés.

---
