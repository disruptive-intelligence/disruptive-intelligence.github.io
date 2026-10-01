---
title: Partie 3 — Portables, mini-PC et stations de travail
source: IT/06 Infrastructure & architecture/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

---

## 12. PC portables et mini-PC

Un portable est un PC contraint par la **place** et la **chaleur**.

- **CPU basse consommation** : suffixes qui changent tout. Chez Intel, U (économe) < P < H < HX (proche d'un fixe) ; chez AMD, U < HS < H < HX. À nom proche, un portable est toujours plus lent qu'un fixe à cause des limites thermiques.
- **Batterie** : capacité en **Wh** (wattheures), la vraie mesure d'énergie.
- **Écran intégré** : non remplaçable, donc à bien choisir à l'achat (Partie 5).
- **Réparabilité** — les deux lignes décisives :
  - **RAM soudée** ou non : si soudée, jamais extensible.
  - **SSD** remplaçable (M.2) ou soudé.

### Mini-PC, NUC, thin client

- **Mini-PC / NUC** : un PC complet miniature, idéal media-center, bureautique, ou petit serveur domestique discret (quelques watts).
- **Thin client** : machine légère conçue pour se connecter à un bureau distant (VDI) ; le calcul se fait sur le serveur. Courant en entreprise.

> **🎯 À retenir**
> Avant d'acheter un portable à garder longtemps : RAM soudée ? SSD remplaçable ? Ces deux réponses décident de sa durée de vie utile bien plus que la marque. Et un mini-PC d'occasion (ex-parc d'entreprise) à 10-15 W est souvent le meilleur *premier* serveur perso.

> **🔧 Cas concret (support)**
> « Mon portable de travail rame. » Si RAM soudée à 8 Go saturée : on optimise l'OS, on ne peut pas étendre. Si le « disque » est un vieux HDD et que le M.2 est libre/remplaçable : passage en SSD NVMe → machine transformée pour un coût modique. Connaître la réparabilité oriente tout le diagnostic.

---

## 13. Stations de travail

Machines pro taillées pour la **fiabilité** et le calcul lourd, pas le jeu.

- **CPU workstation** : beaucoup de cœurs (Xeon, Threadripper/EPYC).
- **GPU pro** (RTX/Quadro, Radeon Pro) : pilotes certifiés métier (CAO, 3D), fiabilité de calcul privilégiée.
- **RAM ECC** : pour ne pas corrompre un rendu de 12 h ou un calcul scientifique.
- **Certification** : les éditeurs (CAO, simulation) valident des configs précises.
- **Usages** : rendu 3D, CAO, calcul, montage haut de gamme, entraînement de modèles d'IA.

> **⚠️ Erreur fréquente**
> Croire qu'une station est « un PC gamer en mieux ». Priorités différentes : la station vise la **stabilité sur calculs longs** et la **certification logicielle**, pas le maximum d'images par seconde. Un PC gamer peut être plus rapide en jeu et moins fiable sur un rendu de 10 h.

---
