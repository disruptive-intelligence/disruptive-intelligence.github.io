---
title: Partie VII — Études de cas ET synthèse (ch.32-34)
source: Cyber/Red_Teaming.md
note: Red teaming
up:
- - Red teaming
  - index.md
---

*Trois cas complets qui intègrent l'ensemble des concepts du cours dans des livrables opérationnels. Chaque cas active une modalité différente (stress-test stratégique, wargame, tabletop hybride) pour montrer la complémentarité du triptyque.*

---


## Chapitre 32 — Cas complet

red teaming d'une stratégie de défense face à une campagne APT

### Synopsis

**Modalité activée :** principalement stress-test (Partie V), avec ancrage fort sur la modélisation adversaire (Partie II) et les TAS (Partie III).

**Contexte :** Hélio Group a défini sa stratégie de défense post-incident face au cluster APT. La stratégie repose sur 5 piliers. Diane conduit un red teaming complet.

**Déroulé :** Devil's Advocacy sur chaque pilier, pre-mortem de la stratégie globale, ACH sur les vecteurs d'attaque résiduels, Team A/Team B sur la priorisation des investissements, What-If sur l'évolution du contexte géopolitique.

**Livrable :** rapport de red teaming stratégique avec matrice de vulnérabilités, recommandations priorisées, indicateurs d'alerte précoce.

**Conclusion du fil rouge MIRRORGATE :** le rapport est présenté au COMEX. 3 vulnérabilités critiques identifiées, 7 recommandations, plan d'implémentation sur 6 mois. Le DG : « Pour la première fois, j'ai le sentiment qu'on sait ce qu'on ne sait pas. C'est inconfortable — mais c'est infiniment mieux que l'illusion de sécurité. »

---


## Chapitre 33 — Cas complet

wargame de crise ransomware avec cellule de crise exécutive

### Synopsis

**Modalité activée :** wargame (Partie IV Ch.17-18).

Format « prêt à jouer » : scénario complet, tous les injects, branches conditionnelles, fiches de rôle Red/Blue/White, guide de facilitation.

**Le scénario :** un opérateur RaaS (profil LockBit/BlackBasta) compromet Hélio via un infostealer acheté à un IAB sur Exploit.in. Accès initial à J-42. L'attaquant fait DCSync, exfiltre 800 Go, déclenche le chiffrement un vendredi 23h. Sauvegardes en ligne chiffrées. AD compromis. Note de rançon 8M€, compte à rebours 72h, leak site actif.

**12 injects sur 10 tours :** alerte initiale → dilemme de la rançon → notification ANSSI → notification CNIL (données de santé) → assureur → négociateur → panne du canal de communication → publication partielle → fuite presse.

**Guide de facilitation :** instructions par tour, critères d'observation, questions de relance, grille de RETEX.

---


## Chapitre 34 — Cas complet

tabletop hybride multi-acteurs — attaque hybride sur infrastructure critique

### Synopsis

**Modalité activée :** tabletop hybride multi-organisations (Partie IV Ch.21), avec dimension d'exercice de coordination inter-acteurs.

Le cas le plus complexe du cours. Participants : l'opérateur (Hélio), le régulateur (ANSSI simulée), le CERT sectoriel (EE-ISAC simulé), un partenaire industriel (co-victime simulée).

**Le scénario :** dans un contexte de tensions géopolitiques élevées, un acteur étatique mène une opération multi-couches sur 90 jours : (1) campagne de reconnaissance et spearphishing (J-90), (2) compromission d'un sous-traitant partagé avec un autre industriel (J-60), (3) pré-positionnement IT/OT de deux cibles (J-30), (4) campagne de désinformation ciblant le secteur énergétique (J-7), (5) sabotage OT conditionnel (J-0) synchronisé avec hack-and-leak.

**L'exercice teste :** coordination inter-organisationnelle, gestion de l'ambiguïté (incident technique ou opération étatique — ou les deux ?), réponse à une attaque hybride (cyber + information), décisions de communication dans un environnement informationnel hostile.

**Intègre :** cours CTI (profilage), APT (TTP étatiques), L2I (dimension informationnelle), IR (processus), IE (coordination IE/cyber), Dark Web (leak site), OSINT (vérification).

---
