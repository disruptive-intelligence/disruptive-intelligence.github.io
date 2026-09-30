---
title: Couche h — VÉRIFIER
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

*Chapitres 28 à 30 — 15 entrées*

> ### La question
> **Comment savoir qu'une machine est bien celle qu'elle prétend être, qu'elle fait bien ce qu'elle prétend faire, et que ce qu'elle produit est authentique ?**
>
> ### Ce que la couche recouvre
> Racines de confiance matérielles · environnements d'exécution de confiance · attestation · cryptographie post-quantique · preuves à divulgation nulle · provenance et authenticité des contenus · identité machine · architecture de sûreté des systèmes autonomes · détection de sortie de domaine · dossiers de sûreté.
>
> ### La grande contrainte
> **La sécurité cryptographique ne repose pas sur une impossibilité physique mais sur des hypothèses de difficulté calculatoire.** Ces hypothèses sont solidement éprouvées et restent des hypothèses. Une hypothèse peut tomber — et la migration qui en découle est un problème d'infrastructure et de base installée, non de logiciel.
>
> ### La seconde contrainte, propre aux systèmes qui agissent
> **On ne peut pas énumérer les entrées d'un système ouvert sur le monde.** La vérification exhaustive est donc impossible, et il faut lui substituer autre chose : une garantie statistique, une surveillance en exploitation, ou une limitation du domaine d'emploi. C'est ce qui rend la certification d'un système apprenant structurellement différente.
>
> ### Dépend de
> Semi-conducteurs, calcul, normalisation, et d'un cadre institutionnel qui évolue plus lentement que la technologie.
>
> ### Permet
> Déploiement de systèmes autonomes dans des contextes à conséquence, échanges entre machines sans intervention humaine, assurabilité.
>
> ### ⏱ Ce qui a le plus bougé en cinq ans
> La normalisation d'algorithmes résistants au calcul quantique et le début des migrations. L'apparition d'identités propres aux agents logiciels. La montée en charge des dispositifs de provenance de contenus. Et l'entrée des architectures de sûreté pour systèmes apprenants dans les référentiels de certification.
>
> ### 🧱 Ce qui n'a pas bougé
> **Une signature atteste l'origine et l'intégrité, jamais la véracité.** Un capteur compromis qui signe correctement une mesure fausse produit une donnée authentique et fausse. N'ont pas bougé non plus : le fait qu'une certification porte sur une version, la difficulté de mettre à jour un système certifié, et la lenteur institutionnelle relativement au rythme technique.
>
> ### 🎯 Le piège de lecture dominant
> **Confondre authenticité et véracité, et confondre sûreté et sécurité.** La première confusion fait croire qu'une donnée signée est vraie. La seconde fait croire que des méthodes conçues contre des défaillances aléatoires protègent contre un adversaire — alors qu'un adversaire viole précisément l'hypothèse d'indépendance sur laquelle elles reposent.

🖼 **SCHÉMA — carte de la couche vérifier.** Deux colonnes en vis-à-vis : *sûreté* — défaillances aléatoires, indépendance supposée — et *sécurité* — adversaire, indépendance violée. Entre elles, une chaîne verticale : racine matérielle, attestation, signature, provenance, dossier de sûreté. Marquer d'un signe distinctif le point où la chaîne établit l'**authenticité** et non la **véracité**. Légende : *la chaîne prouve d'où vient la donnée, jamais qu'elle est vraie.*

---
