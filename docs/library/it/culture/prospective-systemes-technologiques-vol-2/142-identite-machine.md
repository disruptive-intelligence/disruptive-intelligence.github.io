---
title: ◆◆◆ Identité machine
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — vérifier

**En une phrase.** Attribuer à une machine, un service ou un agent logiciel une identité vérifiable, avec des droits, une durée de vie et un mécanisme de révocation.

**Pourquoi cette entrée est majeure.** Parce que **le nombre d'identités non humaines a dépassé de loin celui des identités humaines** dans les systèmes d'information — et parce que l'arrivée d'agents logiciels agissant de façon autonome en fait un objet en constitution rapide.

**Comment ça fonctionne.** Une identité machine repose sur un secret cryptographique et sur une attestation de son porteur. Elle se distingue d'une identité humaine par trois propriétés : elle est **créée et détruite en grand nombre et rapidement** ; elle n'a **pas de facteur d'authentification humain** — pas de mot de passe mémorisé, pas de second facteur ; et **elle agit sans intention**, ce qui rend la notion de responsabilité différente.

**Ce que ça permet.** Contrôler ce qu'un service peut faire · tracer une action jusqu'à son auteur non humain · révoquer un accès sans interrompre les autres · établir une confiance entre systèmes appartenant à des organisations différentes.

**Ce qui bloque.** **La prolifération.** Le nombre d'identités croît plus vite que la capacité à les gouverner : secrets oubliés dans du code, certificats expirés, comptes de service surprivilégiés et jamais révoqués. **C'est l'une des causes documentées de compromission les plus fréquentes**, et elle est organisationnelle autant que technique.

**La durée de vie** : un secret à longue durée de vie est un risque, un secret à courte durée exige une infrastructure de renouvellement automatique.

**Et l'identité des agents.** Un agent logiciel qui agit pour le compte d'un utilisateur pose des questions nouvelles : **agit-il avec ses droits propres ou avec ceux de l'utilisateur ?** Comment tracer une chaîne d'actions passant par plusieurs agents ? Comment révoquer une délégation ? Ces questions sont ouvertes et se posent avec urgence.

**Ce que cela implique.** L'identité machine était un sujet d'exploitation ; elle devient un sujet d'architecture. **Un système où des agents agissent doit répondre, avant tout déploiement, à la question : qui a fait cela, avec quels droits, et qui en répond ?**

**À ne pas confondre avec.** L'**identité numérique** des personnes, dont les enjeux — vie privée, souveraineté, inclusion — sont d'une autre nature.

> ⏱ **État au 23/08/2026** — 🔬 émergent en structuration rapide. Pratiques établies pour les services et les charges de travail ; cadre pour les identités d'agents en construction.
> 🔄 **À revoir si** un standard d'identité et de délégation propre aux agents logiciels est adopté largement.

**Renvois** — Couche : vérifier · Courants : Trust Technologies (ch. 35), Agentic AI (ch. 32) · Voir aussi : agents IA (ch. 12).

---
