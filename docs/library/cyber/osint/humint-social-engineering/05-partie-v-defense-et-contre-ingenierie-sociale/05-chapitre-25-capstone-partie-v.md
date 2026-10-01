---
title: Chapitre 25 — Capstone Partie V
source: Cyber/02 OSINT/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie V — Défense et contre-ingénierie sociale
  - index.md
---

incident de social engineering — de la détection au retex

**Scénario.** Un employé du service comptabilité signale un appel téléphonique suspect au SOC : un interlocuteur se présentant comme le prestataire comptable a demandé l'envoi d'un fichier de paie « pour vérification ». L'employé a d'abord envoyé le fichier, puis a eu un doute et a signalé.

**Livrables attendus :**

1. Fiche de qualification de l'incident (type, gravité, impact potentiel)
2. Plan de containment immédiat
3. Protocole d'investigation (forensique email, analyse de l'appel, évaluation de l'impact)
4. Rapport d'incident (chronologie, analyse, impact, recommandations P0/P1/P2)
5. Plan de retex (format no-blame, actions correctives, responsables, échéances)

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 6**
>
> **Convergence.** L'enquête sur « David Chen » confirme le diagnostic de Nathan. La vérification du profil LinkedIn révèle : photo générée par IA (confirmé par analyse des artefacts — pas de résultat en recherche d'image inversée, symétrie anormale des oreilles), entreprise « Meridian Consulting Asia » sans enregistrement commercial vérifiable dans les registres consultés, numéro WhatsApp enregistré dans un pays tiers, et parcours professionnel avec des incohérences (dates, entreprises non vérifiables).
>
> L'analyse des échanges WhatsApp montre un schéma d'élicitation structuré : 3 premières semaines de conversation générale (flattery, intérêt professionnel, réciprocité), semaine 4-6 escalade vers des questions techniques spécifiques, semaine 7-8 proposition de consulting rémunéré et de rencontre physique. Alexandre Petit a divulgué, sans s'en rendre compte, des informations sur les orientations technologiques de son programme, les noms de ses collègues et les partenaires du consortium.
>
> La DGSI est alertée et prend le relais de l'investigation (ingérence économique étrangère). Alexandre est débriefé sans sanction — il est informé des mécanismes exploités et reçoit une formation de contre-élicitation. Nathan intègre ce cas réel dans son rapport de red team comme illustration de la menace de niveau étatique qui pèse sur Helios.


---
