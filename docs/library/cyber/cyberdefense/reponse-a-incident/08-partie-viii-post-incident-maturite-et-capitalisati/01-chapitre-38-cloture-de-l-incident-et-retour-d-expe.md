---
title: Chapitre 38 — Clôture de l'incident et retour d'expérience (RETEX)
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VIII — Post-incident, maturité ET capitalisation
  - index.md
---

## 38.1 Quand considérer l'incident clos

Critères techniques : éradication validée (Ch.29), surveillance post-nettoyage terminée sans alerte, tous les systèmes en production. Critères métiers : activité revenue à la normale, backlog rattrapé. Critères administratifs : notifications effectuées (ANSSI, CNIL), plainte déposée, assureur informé, rapport final livré, actions résiduelles attribuées et suivies.

La clôture formelle est documentée : date, décideur, synthèse des résultats, et liste des actions résiduelles avec responsables et échéances.

## 38.2 Le RETEX structuré

Le RETEX est mené 2 à 4 semaines après la clôture (assez proche pour que les mémoires soient fraîches, assez éloigné pour avoir le recul). Il implique toutes les parties prenantes (cellule technique, cellule exécutive, IT, métiers, communication, juridique). Il suit une structure en 5 parties.

**Chronologie factuelle** : reconstitution des événements sans interprétation ni jugement. « Le serveur FS01-Lyon a été redémarré à 23h30 par l'admin d'astreinte sans collecte forensic préalable. » Pas : « L'admin d'astreinte a commis une erreur en redémarrant le serveur. »

**Ce qui a fonctionné** : détection EDR efficace (l'alerte a déclenché la réponse), escalade rapide du SOC N2, mobilisation du PRIS dans les délais contractuels, décision de ne pas payer (justifiée par les sauvegardes intactes), communication maîtrisée.

**Ce qui n'a pas fonctionné** : signaux faibles manqués (3 alertes classées faux positifs en 5 semaines), IRP jamais testé, sauvegardes quotidiennes non segmentées, absence de MFA sur le VPN prestataire, logs M365 limités (E3), comptes de service avec droits DA, redémarrage de serveurs sans collecte, absence de NDR.

**Causes racines** (Root Cause Analysis) : pourquoi le phishing a-t-il réussi ? (pas de MFA sur le VPN du sous-traitant + pas de sandbox email sur les pièces jointes). Pourquoi l'attaquant a-t-il pu progresser ? (compte de service `svc_deploy` avec droits Domain Admin et mot de passe faible). Pourquoi l'exfiltration n'a-t-elle pas été détectée ? (pas de NDR, exfiltration via services cloud légitimes, pas de DLP sur les partages).

**Recommandations priorisées** : chaque recommandation est classée par impact, faisabilité, urgence, et budget.

## 38.3 Culture du RETEX sans blâme

Le RETEX ne fonctionne que dans un environnement de sécurité psychologique. Les participants doivent pouvoir décrire leurs erreurs sans crainte de sanction. L'admin qui a redémarré les serveurs doit pouvoir dire « j'ai redémarré les serveurs parce que je pensais que c'était la bonne chose à faire et personne ne m'avait dit de ne pas le faire » — sans être blâmé. La culture du blâme tue le RETEX : les gens cachent leurs erreurs au lieu de les documenter, et les mêmes erreurs se reproduisent.

Le RETEX vise à améliorer le système, pas à punir les individus. La question n'est pas « qui a fait une erreur ? » mais « quel processus a permis que cette erreur soit possible, et comment le corriger ? »

## 38.4 Fil rouge — BLACKTIDE : le RETEX final

> **🔍 BLACKTIDE — Épisode 38 (conclusion du fil rouge)**
>
> Réunion RETEX le 11 avril 2026, 3 semaines après la clôture. Présents : Nadia (IR lead), Marc (RSSI), Thomas et Léa (PRIS CyberForce), Karim et Fatima (SOC), David (admin), le DPO, et un représentant de la direction générale.
>
> **15 recommandations validées :**
>
> | # | Recommandation | Priorité | Budget | Échéance |
> |---|---------------|----------|--------|----------|
> | 1 | Segmentation IT/OT physique (pare-feu dédié) | Critique | 150 K€ | J+30 |
> | 2 | Sauvegardes immuables (cloud WORM) | Critique | 80 K€/an | J+21 |
> | 3 | MFA sur tous les accès externes y compris prestataires | Critique | 30 K€ | J+14 |
> | 4 | Déploiement EDR 100 % du parc | Critique | 60 K€ | J+30 |
> | 5 | Exercice de crise annuel avec la direction | Haute | 25 K€/an | J+90 |
> | 6 | Upgrade M365 E5 (rétention logs étendue) | Haute | 200 K€/an | J+60 |
> | 7 | NDR déployé sur les segments critiques | Haute | 180 K€ | J+120 |
> | 8 | Tiering model AD (Tier 0/1/2 + PAW) | Haute | 250 K€ | J+180 |
> | 9 | Formation IR pour les admins d'astreinte | Haute | 15 K€ | J+45 |
> | 10 | Révision des comptes de service (suppression droits DA inutiles) | Haute | Interne | J+30 |
> | 11 | Sysmon déployé sur tout le parc | Moyenne | 40 K€ | J+90 |
> | 12 | Clause MFA obligatoire dans les contrats prestataires | Moyenne | Interne | J+60 |
> | 13 | DLP sur les partages de fichiers sensibles | Moyenne | 120 K€ | J+180 |
> | 14 | Playbooks IR mis à jour (AD compromis, OT, notification OIV) | Haute | Interne | J+30 |
> | 15 | Comptes break glass créés et sécurisés | Haute | 5 K€ | J+7 |
>
> Le conseil d'administration approuve un budget exceptionnel de 1,2 M€ pour le plan de durcissement, étalé sur 18 mois.

---
