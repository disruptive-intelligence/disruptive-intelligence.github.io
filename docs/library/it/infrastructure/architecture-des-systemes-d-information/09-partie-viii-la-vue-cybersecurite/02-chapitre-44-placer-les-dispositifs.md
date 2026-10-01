---
title: Chapitre 44 — Placer les dispositifs
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VIII — La vue cybersécurité
  - index.md
---

## 44.1 Le principe

> **Le bon emplacement d'un dispositif dépend de l'architecture, pas du produit.**

Un même produit placé à deux endroits différents ne voit pas la même chose, ne protège pas les mêmes actifs, et ne produit pas les mêmes traces.

## 44.2 Les emplacements, par dispositif

| Dispositif | Emplacement pertinent | Ce qu'il voit | Ce qu'il **ne voit pas** |
|---|---|---|---|
| **Pare-feu** | Entre deux zones | Ce qui traverse la frontière | **Ce qui reste dans une zone** |
| **Détection sur poste** | Sur chaque poste et serveur | L'activité locale, les processus | Ce qui se passe sur ce qui n'en porte pas |
| **Sonde réseau** | Sur un point de passage, en dérivation | Les flux qui y transitent | **Les flux chiffrés · ceux qui ne passent pas là** |
| **Scanner de vulnérabilités** | Au plus près des cibles | Ce qu'il peut joindre | **Ce qui est derrière un filtre, ou éteint** |
| **Collecte de journaux** | Centralisée, alimentée par tous | Ce que les sources envoient | **Ce qui n'est pas configuré pour émettre** |
| **Point d'authentification** | Mandataire, applicatif, ou les deux | Les accès qui y passent | **Les accès internes directs** — §29.3 |

⚠️ **La colonne de droite définit la couverture réelle.** Un dispositif ne protège que ce qu'il voit, et un schéma dit exactement ce qu'il voit.

## 44.3 Le même dispositif, trois emplacements — l'exemple de la sonde

**C'est l'exercice qui installe le principe.**

```
  A — SONDE AU PÉRIMÈTRE
      Internet ──►[SONDE]──► [ FW ] ──► DMZ ──► interne
      VOIT     : ce qui entre et sort
      NE VOIT PAS : tout le trafic interne — postes vers serveurs
      COUVERTURE RÉELLE : faible en volume, forte en visibilité externe

  B — SONDE ENTRE POSTES ET SERVEURS
      [ postes ] ──►[SONDE]──► [ serveurs ]
      VOIT     : le mouvement latéral, la reconnaissance, la collecte
      NE VOIT PAS : ce qui reste entre postes
      COUVERTURE RÉELLE : la phase la plus longue d'une compromission

  C — SONDE DEVANT LA BASE
      [ applicatif ] ──►[SONDE]──► [ base ]
      VOIT     : les requêtes vers les données
      NE VOIT PAS : qui les a demandées — §34.2
      COUVERTURE RÉELLE : étroite, mais sur l'actif le plus sensible
```


| Emplacement | Volume de trafic observé | Phase d'attaque couverte |
|---|---|---|
| **A — périmètre** | Faible | Accès initial |
| **B — postes/serveurs** | **Élevé** | **Reconnaissance, mouvement latéral, collecte** |
| **C — devant la base** | Faible | Exfiltration |

⚠️ **Le placement A est un réflexe courant, et c'est celui qui observe le plus petit volume de trafic.** Le placement B couvre la phase la plus longue d'une compromission — celle qui dure des jours ou des semaines. **Et il exige un point de passage, donc une segmentation** : c'est le §45.3.

## 44.4 Les quatre emplacements impossibles, et ce qu'on fait alors

| Situation | Pourquoi c'est impossible | Ce qu'on fait |
|---|---|---|
| **Un agent sur un automate industriel** | Constructeur ne le supporte pas, ressources insuffisantes, garantie perdue | Observation passive du réseau · segmentation stricte · §28.6 |
| **Un scanner authentifié sur un système hérité** | Pas de compte disponible, risque d'indisponibilité | Inventaire déclaratif · scan passif · **périmètre déclaré non couvert** |
| **Une sonde sur un flux chiffré de bout en bout** | Rien à voir sans le terminer | Journalisation aux extrémités · métadonnées uniquement |
| **Un contrôle sur un service en ligne** | Ce n'est pas chez vous | Configuration du service · **journaux du fournisseur, s'il en donne** |

**Le point commun des quatre réponses** : quand une action est impossible à un endroit, **on la déplace, on la remplace, ou on déclare la zone non couverte**. On ne fait jamais semblant.

⚠️ **C'est exactement la doctrine des périmètres déclarés non couverts du volume Maintien en condition de sécurité.** Une zone où l'on ne peut pas agir est acceptable **si elle est déclarée** ; elle est dangereuse quand elle est ignorée.

## 44.5 L'erreur de placement la plus coûteuse

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous placez une sonde réseau sur le lien Internet pour détecter les intrusions. Quelle proportion de l'activité de votre organisation voyez-vous ?*
**Une fraction — et pas celle que vous croyez.** Vous voyez ce qui entre et sort. Vous ne voyez **rien** de ce qui se passe entre les six cents postes et les serveurs internes, c'est-à-dire là où se déroule l'essentiel d'une compromission après l'accès initial. La mauvaise décision évitée : **placer les moyens au périmètre en croyant couvrir l'organisation**, et découvrir en incident que les onze jours d'activité interne n'ont laissé aucune trace exploitable.

🔥 **SCÉNARIO — le scanner ne voit pas ce qu'il devrait voir**

| Question | Réponse |
|---|---|
| Symptôme | Un scan hebdomadaire remonte 40 machines. L'inventaire en compte 214 |
| Hypothèse naïve | « Le scanner est mal configuré » |
| Dépendance réelle | **Il est placé dans un segment, et le filtrage inter-segments le bloque** |
| Ce que le schéma aurait dû montrer | Depuis où le scanner opère, et ce qu'il peut joindre |
| Concevoir différemment | Un point de scan par zone · ou des règles dédiées, **et alors le scanner devient un chemin privilégié à protéger** |

⚠️ **La dernière ligne est un compromis qu'on oublie** : donner au scanner le droit de joindre tout le parc en fait **une cible de choix**. Un scanner compromis dispose d'un accès réseau que personne d'autre n'a. **Principe du coût.**

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « On est couverts à 95 % » | Un agent est déployé sur 95 % des machines | **Et les 5 % restants ? Ce sont souvent les plus anciennes** |
| « La sonde ne voit rien » | Peu d'alertes | **Est-elle bien placée ?** Peu d'alertes peut vouloir dire peu de trafic observé |
| « Le scan est passé » | Un balayage a eu lieu | **Combien de machines a-t-il vues, sur combien d'attendues ?** |
| « On mettra un agent plus tard » | Un périmètre non couvert | **Est-ce déclaré quelque part, ou oublié ?** |

---
