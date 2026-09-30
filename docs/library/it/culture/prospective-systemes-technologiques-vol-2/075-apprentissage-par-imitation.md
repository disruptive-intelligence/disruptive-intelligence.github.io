---
title: ◆◆ Apprentissage par imitation
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - index.md
---

**Niveau** — capacité · **Couche** — apprendre et décider

**En une phrase.** Apprendre une tâche en reproduisant des démonstrations effectuées par un opérateur humain.

**Comment ça fonctionne.** Un opérateur exécute la tâche, souvent par téléopération, pendant que le système enregistre observations et actions. Le modèle apprend ensuite à produire l'action associée à chaque observation.

**Ce que ça permet.** Acquérir une compétence sans la spécifier · exploiter le savoir-faire d'un opérateur qui ne saurait pas l'expliciter · démarrer un apprentissage sans définir de fonction de récompense.

**Ce qui bloque.** **La dérive.** Le système apprend à agir dans les situations que l'humain a rencontrées ; dès qu'il s'en écarte un peu, il se retrouve dans des situations non démontrées, où il agit mal, ce qui l'en écarte davantage. **L'erreur s'auto-amplifie**, et c'est le problème structurel de la méthode.

S'y ajoutent le **coût de collecte** — une démonstration à la fois — et le fait que les démonstrations humaines contiennent des corrections implicites difficiles à reproduire.

**Ce que cela implique.** C'est **la source principale des données physiques** aujourd'hui, et donc le facteur limitant des architectures du chapitre. La téléopération n'est pas un pis-aller : c'est l'infrastructure de collecte.

**À ne pas confondre avec.** **L'apprentissage par renforcement**, qui apprend par essai et récompense sans démonstration.

> ⏱ **État au 23/08/2026** — 🏭 déployé en recherche et en pré-industrialisation, méthode dominante pour la manipulation.
> 🔄 **À revoir si** une méthode de collecte permet d'acquérir des démonstrations à un coût significativement inférieur à la téléopération individuelle.

**Renvois** — Convergence : robotique généraliste (36) · Voir aussi : téléopération (ch. 15).

---
