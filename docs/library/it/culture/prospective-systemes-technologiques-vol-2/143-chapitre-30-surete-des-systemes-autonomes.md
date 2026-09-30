---
title: Chapitre 30 — Sûreté des systèmes autonomes
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

> **Ce que ce chapitre ajoute.** Les chapitres 28 et 29 traitaient de la confiance dans **ce qu'un système est**. Celui-ci traite de la confiance dans **ce qu'un système fait** — et particulièrement lorsqu'il décide.
>
> **La première entrée absorbe six termes du marché.** Runtime monitoring, runtime verification, runtime assurance, architecture Simplex, safety envelope, shield layer : ce ne sont pas six technologies mais **les couches d'une même architecture**. Les traiter séparément les rendrait incompréhensibles.
>
> **Cinq entrées.**

---


## ◆◆◆ Architecture de sûreté d'un système autonome — *entrée comparative*

**Niveau** — système · **Couche** — vérifier

**En une phrase.** L'ensemble des dispositifs qui permettent de faire confiance à un système qui décide — organisés en quatre couches complémentaires.

**Pourquoi cette entrée est comparative.** Parce que les termes du domaine circulent comme s'ils désignaient des technologies concurrentes, alors qu'ils désignent **des étages d'une même construction**. Comprendre l'ordre est plus utile que connaître les définitions.

**Le problème à résoudre.** Un système classique se vérifie avant déploiement : on démontre qu'il se comporte correctement sur toutes les entrées possibles. Un système apprenant ne le permet pas — **on ne peut pas énumérer les entrées d'un système ouvert sur le monde**. La vérification exhaustive étant impossible, il faut lui substituer autre chose.


### Les quatre couches, dans l'ordre

**① OBSERVER — la surveillance en exploitation.**
Un dispositif indépendant observe le système pendant qu'il fonctionne et enregistre son état, ses entrées, ses sorties. Il ne juge pas : il constate. C'est la base de tout le reste, et c'est aussi ce qui permet le retour d'expérience.
*Terme du domaine : runtime monitoring.*

**② VÉRIFIER — le contrôle de propriétés en temps réel.**
On exprime des propriétés qui doivent rester vraies — « la distance à l'obstacle ne descend jamais sous ce seuil », « la commande reste dans cette plage » — et un dispositif vérifie en continu qu'elles le sont. **Il détecte une violation, il ne l'empêche pas.**
*Terme du domaine : runtime verification.*

**③ CONTRAINDRE — l'intervention qui garantit.**
Un dispositif simple, vérifiable par les méthodes classiques, s'interpose entre le système apprenant et les actionneurs. Il laisse passer les commandes qui préservent la sûreté et **substitue une commande sûre à celles qui ne le font pas**. Le système apprenant propose ; le dispositif de contrainte dispose.

C'est le principe le plus important de cette entrée : **on ne cherche pas à prouver que le système apprenant est sûr, on l'entoure d'un dispositif dont on peut prouver qu'il l'est.** La garantie ne porte pas sur l'intelligence mais sur son enveloppe.

*Termes du domaine : shield layer, architecture Simplex, safety envelope, runtime assurance.*

**④ DÉMONTRER — l'argumentation opposable.**
Un dossier structuré qui expose la revendication de sûreté, les arguments qui la soutiennent et les preuves qui étayent chaque argument. C'est ce qu'on présente à un régulateur, à un assureur, à un tribunal.
*Termes du domaine : safety case, assurance case.*


### Ce que l'architecture permet

**Déployer un système dont on ne peut pas démontrer le comportement**, en garantissant non pas ce qu'il fera mais ce qu'il ne pourra pas faire. **C'est le déplacement conceptuel décisif** du domaine : de la preuve du système à la preuve de son enveloppe.


### Ce qui bloque

**La définition des propriétés à garantir.** Écrire ce qui ne doit jamais arriver est plus difficile qu'il n'y paraît, et une propriété mal formulée produit soit des interventions incessantes qui rendent le système inutilisable, soit une garantie vide.

**Le conservatisme du dispositif de contrainte.** Plus il est prudent, plus il intervient, plus le système perd de sa capacité. **L'arbitrage entre sûreté et performance se joue entièrement ici**, et il est explicite — ce qui est préférable à un arbitrage implicite.

**La détection de sortie de domaine**, qui conditionne le déclenchement et fait l'objet de l'entrée suivante.

**Et le cadre.** Ces architectures sont reconnues dans certains référentiels sectoriels et pas dans d'autres. **Leur acceptation par les autorités est le facteur limitant du déploiement**, non leur disponibilité technique.

**Ce que cela implique.** La question à poser devant tout système autonome n'est pas « son modèle est-il fiable ? » mais **« quelle est son architecture de sûreté, et sur quelles propriétés porte la garantie ? »**

**À ne pas confondre avec.** La **sécurité informatique**, qui protège contre un adversaire — la carte de couche a établi que les hypothèses des deux disciplines sont opposées. Et les **essais**, qui vérifient avant déploiement ce que ces dispositifs vérifient pendant.

> ⏱ **État au 23/08/2026** — 🔬 émergent. Architectures établies dans l'aéronautique et l'industrie ; extension aux systèmes apprenants en cours d'intégration dans les référentiels.
> 🔄 **À revoir si** un référentiel de certification accepte explicitement une architecture de ce type comme démonstration de sûreté pour un système apprenant.

**Renvois** — Couche : vérifier · Convergence : autonomie mobile (39) · Voir aussi : domaine de conception opérationnelle (ch. 17), volume 1 chapitre 16.

---
