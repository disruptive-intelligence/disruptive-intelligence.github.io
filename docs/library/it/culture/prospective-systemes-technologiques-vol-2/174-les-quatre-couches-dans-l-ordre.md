---
title: Les quatre couches, dans l'ordre
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

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


## Ce que l'architecture permet

**Déployer un système dont on ne peut pas démontrer le comportement**, en garantissant non pas ce qu'il fera mais ce qu'il ne pourra pas faire. **C'est le déplacement conceptuel décisif** du domaine : de la preuve du système à la preuve de son enveloppe.
