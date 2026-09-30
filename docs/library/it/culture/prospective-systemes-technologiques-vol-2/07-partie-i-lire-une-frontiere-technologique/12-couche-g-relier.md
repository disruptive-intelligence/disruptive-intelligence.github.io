---
title: Couche g — Relier
source: IT/Culture/Prospective_SYSTEMES-TECHNOLOGIQUES-Volume-2.md
note: Prospective — systèmes technologiques (vol. 2)
up:
- - Prospective — systèmes technologiques (vol. 2)
  - ../index.md
- - Partie I — Lire une frontière technologique
  - index.md
---

*Chapitres 24 à 25 — 8 entrées*

> ### La question
> **Comment transporter de l'information entre des points distants, de façon fiable, à un débit suffisant, et où placer le traitement ?**
>
> ### Ce que la couche recouvre
> Réseaux mobiles avancés · réseaux non terrestres · communications optiques · réseaux déterministes · communications en environnement dégradé · edge, exécution locale et embarquée · continuum entre le centre et la périphérie.
>
> ### La grande contrainte
> **La latence due à la distance ne s'achète pas.** Le débit se négocie en ajoutant de la capacité ; le temps de propagation est borné par la vitesse de la lumière — environ deux cents kilomètres par milliseconde dans une fibre. Toute architecture distribuée se conçoit contre cette borne, et c'est elle qui justifie l'essentiel de cette couche.
>
> ### La seconde contrainte, souvent oubliée
> **La simultanéité n'existe pas gratuitement.** Deux systèmes distants ne peuvent pas savoir instantanément ce que fait l'autre. Toute coordination suppose des échanges, donc du délai, donc une incertitude sur l'état de l'autre pendant ce délai. Ce n'est pas un défaut d'ingénierie logicielle : c'est une contrainte physique.
>
> ### Dépend de
> Semi-conducteurs, photonique, énergie, spectre radioélectrique — ressource attribuée et non achetée — et d'infrastructures spatiales pour la couverture et le temps.
>
> ### Permet
> Coordination, supervision, mise à jour, mutualisation du calcul, autonomie distribuée.
>
> ### ⏱ Ce qui a le plus bougé en cinq ans
> La liaison directe entre un satellite en orbite basse et un terminal ordinaire. Les liaisons optiques entre satellites, devenues opérationnelles. L'exécution de modèles sur des appareils que chacun possède déjà. Et la reconnaissance du fait que le placement du calcul est un problème d'architecture au moins autant que de performance.
>
> ### 🧱 Ce qui n'a pas bougé
> La borne de propagation. Le fait que le spectre est fini et attribué. La relation entre bande passante disponible, rapport signal sur bruit et débit maximal, dont les systèmes modernes sont proches. Et la longévité des protocoles largement déployés, qui résistent à leurs successeurs même supérieurs.
>
> ### 🎯 Le piège de lecture dominant
> **Confondre débit et latence, et croire qu'on achète la seconde comme le premier.** Une part de la latence tient à l'équipement et se réduit ; une part tient à la distance et ne se réduira jamais. Devant toute promesse de réduction de latence, demandez quelle fraction est due à la distance.

🖼 **SCHÉMA — carte de la couche relier.** Deux axes croisés : en abscisse la distance, en ordonnée la latence, avec la borne de propagation tracée comme une droite infranchissable. Positionner les architectures de la couche par rapport à cette droite, en distinguant la part de latence due à l'équipement — compressible — et celle due à la distance. En marge, une bande étroite figurant le spectre, saturée et attribuée. Légende : *une part de la latence s'achète, l'autre non.*

---
