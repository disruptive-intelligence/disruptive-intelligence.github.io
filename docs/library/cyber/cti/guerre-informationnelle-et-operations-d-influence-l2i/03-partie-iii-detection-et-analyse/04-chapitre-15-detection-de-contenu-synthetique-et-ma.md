---
title: Chapitre 15 — Détection de contenu synthétique et manipulé
source: Cyber/01 CTI & renseignement/Influence & intelligence économique/Guerre informationnelle et opérations d'influence (L2I).md
note: Guerre informationnelle et opérations d'influence (L2I)
up:
- - Guerre informationnelle et opérations d'influence (L2I)
  - ../index.md
- - Partie III — Détection et analyse
  - index.md
---

## 15.1 Images et vidéos

La détection de manipulation d'images repose sur un arsenal de techniques complémentaires. Le **reverse image search** (Google Images, TinEye, Yandex Images) permet d'identifier si une image a été publiée auparavant dans un autre contexte — c'est souvent le moyen le plus efficace de détecter un contenu détourné (image réelle dans un contexte faux). L'**analyse de métadonnées EXIF** (données embarquées dans le fichier image — appareil, date, coordonnées GPS, logiciel d'édition) peut révéler des modifications, mais les métadonnées sont facilement supprimées ou modifiées. L'**Error Level Analysis** (ELA) détecte les différences de compression JPEG qui peuvent indiquer une retouche, mais cette technique produit de nombreux faux positifs et nécessite une interprétation experte. La **détection d'artefacts IA** — artefacts caractéristiques des modèles génératifs (mains mal formées, textes incohérents, reflets asymétriques, textures répétitives) — est de moins en moins fiable à mesure que les modèles s'améliorent.

## 15.2 Audio

L'analyse forensique audio est un domaine spécialisé. L'**analyse spectrale** permet d'identifier des artefacts de synthèse vocale (discontinuités spectrales, patterns de fréquence anormaux, transitions non naturelles). La **comparaison avec des échantillons authentiques** permet d'évaluer si une voix synthétique correspond à une voix réelle connue. Les détecteurs automatiques de synthèse vocale ont des performances variables et ne constituent pas un verdict — le rapport VIGINUM sur Storm-1516 documente explicitement un cas où le détecteur automatique donnait un résultat « incertain » alors que l'expert humain identifiait des artefacts spectraux.

## 15.3 Texte

Les détecteurs de texte généré par IA (GPTZero, Originality.ai, Copyleaks, et al.) méritent une attention particulière en raison de leur utilisation croissante — et des risques d'interprétation abusive de leurs résultats. Les performances de ces outils sont médiocres sur les textes courts (moins de 200 mots), fortement sensibles aux paraphrases et au post-editing humain, et présentent des taux de faux positifs significatifs (des textes humains classés comme « IA »). Un détecteur de texte IA ne doit jamais être utilisé comme preuve autonome — il produit un signal qui doit être corroboré par d'autres éléments.

## 15.4 La course aux armements détection/génération

La dynamique fondamentale est celle d'une course aux armements : chaque amélioration de la détection est contournée par la génération suivante. Les watermarks sont supprimés, les artefacts corrigés, les patterns de détection contournés. Cette dynamique a une implication opérationnelle directe : les outils de détection ont une durée de vie limitée et doivent être constamment mis à jour. L'investissement dans les capacités de détection est un coût récurrent, pas un investissement ponctuel.

## 15.5 Principe fondamental

la détection comme signal, jamais comme preuve

Ce principe est si important qu'il mérite d'être explicitement posé : **la détection automatique de contenu synthétique est un signal exploratoire, jamais une preuve**. La corroboration multi-méthode est obligatoire. Un contenu ne peut être qualifié de « synthétique » ou de « manipulé » que sur la base d'une convergence de signaux : résultat de détecteurs automatiques + analyse humaine experte + vérification contextuelle + analyse de la chaîne de diffusion + cohérence avec les TTPs connus. Tout rapport présentant un résultat de détecteur comme un verdict est méthodologiquement défaillant.

---
