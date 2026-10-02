---
title: Chapitre 27 — IA, traduction, OCR et PDF en ligne
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie V — Choisir ses outils numériques de confiance
  - index.md
---

pratique ou fuite invisible ?

*Beaucoup d'incidents du quotidien ne viennent pas d'une attaque sophistiquée, mais d'un mauvais choix d'outil : par confort, par urgence, ou par manque d'alternative connue. C'est probablement le chapitre le plus important de la Partie V — la catégorie de risque qui a le plus augmenté en 2024-2026 est l'externalisation involontaire de données vers des outils en ligne grand public.*

## 27.1 Le problème : l'externalisation invisible des données

Quand on dépose un fichier sur un convertisseur PDF gratuit, qu'on colle un mail dans un assistant IA pour le résumer, ou qu'on transfère un document professionnel vers son Gmail personnel pour « travailler ce weekend », on ne fait pas une erreur de sécurité au sens classique. On fait une **délégation invisible** : le fichier sort de son périmètre maîtrisé, et entre dans un périmètre sur lequel on n'a aucun contrôle réel.

Les questions qu'on ne se pose pas :

- Où le fichier est-il stocké, et pour combien de temps ?
- Qui peut y accéder ?
- Le service le réutilise-t-il pour entraîner un modèle, alimenter une base de données, le revendre, ou simplement le conserver « par défaut » ?
- Si le service est piraté demain, mon fichier sera-t-il exposé ?
- Si je veux supprimer le fichier, est-ce que je peux ? Et la suppression est-elle effective ?

Pour la majorité des outils gratuits en ligne, la réponse à toutes ces questions est : **on ne sait pas vraiment**. Et même si les conditions d'utilisation sont rassurantes, elles peuvent changer, l'éditeur peut être racheté, ou l'éditeur peut être piraté.

## 27.2 Les cas concrets

**Convertir, compresser, fusionner un PDF** sur un site gratuit (iLovePDF, Smallpdf, et des dizaines d'autres) : l'usage est massif et la majorité des utilisations sont sans gravité. Mais déposer un **contrat client**, un **bulletin de salaire**, un **avis d'imposition**, une **CNI numérisée**, ou un **document interne** sur un service tiers gratuit pose un vrai problème — le document quitte votre environnement, sa durée de conservation est floue, et vous n'avez pas signé de DPA (Data Processing Agreement) avec ce prestataire. Pour ces cas, préférer un outil local (Aperçu sur macOS, des outils desktop gratuits sur Windows, LibreOffice, Adobe Acrobat licencié).

**Coller un texte dans une IA conversationnelle publique** (ChatGPT, Claude, Gemini grand public) pour le résumer, le traduire, le reformuler : l'usage est devenu quotidien. Le risque : selon le service et le mode (gratuit, payant, entreprise), les données saisies peuvent être utilisées pour entraîner les modèles, conservées pour audit, ou exposées en cas d'incident de sécurité. Les éléments à NE JAMAIS coller dans une IA publique grand public sans politique d'entreprise dédiée :

- Documents internes confidentiels (rapports, comptes rendus, présentations stratégiques)
- Données clients (noms, emails, adresses, identifiants)
- Données RH (bulletins de salaire, évaluations, contrats)
- Code source propriétaire avec secrets, tokens, ou clés API
- Données de santé (résultats médicaux, ordonnances, dossiers patients)
- Informations financières non publiques
- Documents juridiques (contrats avec clauses de confidentialité)
- Logs ou exports techniques contenant des identifiants utilisateurs réels

La **règle simple** : *« Si je n'aurais pas le droit d'envoyer ce document à une personne extérieure, je ne dois pas le déposer dans un outil externe non validé. »* Cette règle s'applique aussi à l'usage personnel — un avis d'imposition collé dans une IA pour le « comprendre » est en train d'être transmis à un service tiers dont la politique de conservation n'est pas claire.

**Si l'usage IA est nécessaire**, plusieurs alternatives existent selon le contexte :

- **Compte IA entreprise avec engagement contractuel** : mode « workspace » ou « business » avec non-rétention pour entraînement, DPA signé, conformité RGPD. C'est le bon réflexe pour les usages professionnels.
- **Anonymisation forte avant collage** : remplacer les noms réels par des placeholders, masquer les chiffres précis, retirer les identifiants. Acceptable pour des cas ponctuels mais fragile par construction (les patterns peuvent rester reconnaissables).
- **IA locale qui tourne sur sa propre machine** : modèles open source comme **Mistral**, **Llama**, **Gemma**, accessibles via **Ollama**, **LM Studio** ou **GPT4All**. Pour un particulier, les performances sont plus modestes que les grands modèles cloud, mais la confidentialité est totale — rien ne sort de la machine.
- **Alternatives orientées confidentialité côté grand public** : **Lumo** (assistant IA de Proton, hébergé en Europe) annonce une approche « no logs », un chiffrement à divulgation nulle pour les conversations sauvegardées, et l'absence d'utilisation des conversations pour entraîner les modèles. C'est un positionnement explicitement orienté confidentialité, intéressant pour qui veut une IA cloud sans le compromis des grands acteurs grand public. **Nuance importante** : une IA cloud reste une IA cloud — le contenu doit nécessairement être traité côté serveur pour produire la réponse. Les garanties annoncées par l'éditeur sont sérieuses mais ne valent pas une exécution locale. À considérer comme « plus respectueux de la vie privée selon les garanties annoncées par l'éditeur », pas comme une confidentialité absolue.
- **Côté agents publics et administration** : la DINUM développe **Albert** (assistant IA d'État, Etalab) et **La Suite numérique** intègre progressivement des outils IA destinés à l'usage interne de l'administration. Ces solutions, hébergées en France, sont à privilégier pour les usages institutionnels quand elles sont disponibles.

Comme pour les autres outils, **aucune solution n'est « parfaite » dans l'absolu** : une IA locale a des limites de capacités, une IA cloud souveraine évolue dans le temps, une IA entreprise dépend du contrat signé. Le bon choix dépend du niveau de sensibilité du contenu et des obligations de l'organisation.

**Traduire un document confidentiel** dans un traducteur web gratuit : même logique que l'IA. Préférer un outil intégré au système (traduction Apple, traduction Microsoft Office en version entreprise) ou un outil local.

**Outils OCR en ligne** pour scanner un document : un scan d'identité, de bulletin médical, ou de contrat envoyé à un OCR en ligne quitte votre environnement. Préférer les fonctions OCR intégrées au téléphone (Apple Notes, Google Lens local), à un scanner dédié, ou à des logiciels installés.

**Outils de signature électronique gratuits** non agréés : pour un document important, la valeur juridique de la signature dépend du niveau du service. Préférer les services agréés (DocuSign, YouSign, Adobe Sign en version pro) plutôt que des outils gratuits inconnus, surtout pour les contrats avec valeur juridique forte.

## 27.3 Le mélange perso/pro : la fuite par déplacement

C'est le mauvais réflexe le plus banal et le plus fréquent :

- Transférer un document pro vers son Gmail personnel pour le lire ce weekend
- Déposer un fichier d'entreprise sur son Google Drive personnel pour « gagner du temps »
- Utiliser WhatsApp perso pour envoyer des documents internes sensibles à un collègue
- Photographier l'écran du PC pro avec son téléphone perso pour avoir l'info sous la main
- Travailler sur un ordinateur familial non maîtrisé (ordinateur de l'autre conjoint, ordinateur partagé en famille)
- Imprimer un document confidentiel chez soi sans nettoyer la corbeille à papier ni effacer la mémoire de l'imprimante

Le problème n'est pas que ces gestes soient « hackés » — c'est qu'ils créent une **perte de maîtrise** : on ne sait plus où est le document, qui peut y accéder, combien de temps il reste disponible, et comment le supprimer. Si l'entreprise subit un incident, ces fichiers personnels sont hors du périmètre de réponse. Si le particulier subit un incident (compte perso piraté, téléphone volé), les données pro sont compromises.

Le **réflexe** : utiliser exclusivement les outils validés par l'organisation pour les données pro. Si l'organisation n'a pas l'outil adapté, le signaler — c'est un manque qui doit être traité par l'IT, pas contourné par chaque salarié.

## 27.4 Les 4 questions à se poser avant de déposer un fichier

> **Avant d'envoyer ou de déposer un fichier, se poser 4 questions :**
>
> 1. Le document contient-il des données personnelles, professionnelles, médicales, bancaires ou confidentielles ?
> 2. Est-ce que je sais où le fichier est envoyé, et qui peut y accéder ?
> 3. Est-ce que je sais combien de temps il sera conservé, et si je peux le supprimer ?
> 4. Si je suis salarié(e) : mon organisation autorise-t-elle cet outil pour ce type de données ?
>
> Si la réponse à l'une de ces questions est floue, **ne pas déposer le fichier**. Trouver une alternative locale, une alternative validée, ou demander à l'IT.

> **🔵 Lina — Épisode 7 :** Lina doit préparer un document de synthèse pour un client à partir d'un long rapport interne de 80 pages. Elle pense le coller dans une IA grand public pour gagner du temps sur le résumé. Elle s'arrête : le rapport contient des données financières clients, des noms de personnes, des éléments stratégiques. Coller ce contenu dans un service grand public serait une fuite — le rapport est sous accord de confidentialité avec le client. Elle utilise l'outil IA d'entreprise (qui a une politique de non-rétention contractuelle), ou à défaut, elle anonymise fortement le contenu avant collage : noms remplacés, chiffres modifiés, projets renommés. C'est plus long mais c'est conforme.

---

<a id="chapitre-28"></a>
