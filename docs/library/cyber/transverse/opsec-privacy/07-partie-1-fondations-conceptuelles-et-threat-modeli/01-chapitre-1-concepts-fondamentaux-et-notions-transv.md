---
title: Chapitre 1 — Concepts fondamentaux et notions transverses
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 1 — Fondations conceptuelles et threat modeling
  - index.md
---

## 1.1 Privacy, sécurité, anonymat, pseudonymat, secret

les confusions qui tuent

Cinq mots qui désignent cinq choses différentes, constamment mélangés dans la conversation publique. Cette confusion n’est pas anecdotique : elle conduit à choisir le mauvais outil pour le mauvais problème.

**Privacy** (vie privée) est le contrôle qu’on exerce sur l’information qui circule à son sujet. Tu fermes la porte des toilettes non pas parce que tu caches un secret, mais parce que tu veux décider qui sait quoi de ton intimité. La privacy est un droit ; elle n’implique aucune dissimulation d’activité.

**Sécurité** est la capacité à protéger l’intégrité, la confidentialité et la disponibilité de ses actifs (données, comptes, appareils) contre des menaces. Tu peux être *sécurisé* sans être *anonyme* : ton compte bancaire est à ton nom, mais protégé par MFA. Tu peux être *anonyme* sans être *sécurisé* : un pseudonyme sur un forum dont la base de données fuit ne te protège plus.

**Anonymat** est l’impossibilité, pour un observateur, d’attribuer une action à une identité — y compris une identité pseudonyme. C’est le degré le plus exigeant et le plus rare. L’anonymat *absolu* n’existe pas ; on parle d’anonymat *contre un modèle d’adversaire donné*.

**Pseudonymat** est l’usage d’un nom de substitution stable. @GamerGuy12 est un pseudonyme : ce n’est pas anonyme, parce que le pseudo est persistant et peut être corrélé avec le temps à un comportement, des habitudes, des contacts, voire à une identité civile. La plupart des « anonymes » sur internet sont en réalité des pseudonymes.

**Secret** désigne une information qu’on cache activement. Tout secret est privé, mais toute information privée n’est pas secrète. Tu ne caches pas que tu prends une douche ; tu protèges l’image de toi nu sous la douche. La privacy est une question de *contexte* (qui voit quoi dans quel cadre), le secret est une question de *contenu* (cette information ne doit être vue par personne d’autre).

**OPSEC** (Operational Security) est la discipline qui consiste à identifier, contrôler et protéger les *indicateurs* qui, agrégés, permettraient à un adversaire de déduire des informations sensibles. C’est une métadiscipline : elle s’applique à tout ce qui précède.

> 🟨 **Pourquoi ces distinctions sont opérationnelles**
> Un journaliste qui veut protéger une **source** a besoin que personne ne puisse établir un *lien* entre lui et cette personne. C’est de l’anonymat (de la relation), pas du secret du contenu : peu importe ce qui est dit, ce qui compte, c’est que personne ne sache que la conversation a eu lieu. Or beaucoup de journalistes confondent les deux et chiffrent fortement le *contenu* sur des canaux qui révèlent massivement les *métadonnées de relation*. C’est une erreur de cadrage qui annule la protection.

## 1.2 OPSEC

héritage militaire, cycle en 5 étapes, transposition civile

L’OPSEC est née dans l’armée américaine pendant la guerre du Vietnam (opération Purple Dragon, 1966) après le constat que les Nord-Vietnamiens anticipaient les opérations sans avoir besoin de casser les codes : ils observaient des indicateurs (mouvements logistiques, communications radio routinières, rotations de personnel) qui, agrégés, révélaient les intentions. La parade fut de cesser de raisonner en *secrets* et de commencer à raisonner en *indicateurs*.

Le cycle OPSEC formalisé comporte cinq étapes :

1. **Identification des informations critiques** — qu’est-ce qui, si appris par l’adversaire, lui donnerait un avantage décisif ? Pour un individu : son adresse, ses contacts sensibles, sa localisation en temps réel, ses identifiants, sa relation à une source.
1. **Analyse des menaces** — qui est l’adversaire, quelles sont ses capacités, sa motivation, ses méthodes ?
1. **Analyse des vulnérabilités** — quels indicateurs, dans mes routines, mes communications, mon comportement, révèlent ces informations critiques ?
1. **Évaluation des risques** — probabilité × impact, hiérarchisation.
1. **Application de contre-mesures** — réduire les indicateurs, masquer les corrélations, compartimenter, etc.

La transposition civile ne change pas le cycle, elle change l’échelle : un individu n’a pas les ressources d’une armée. Cela impose des arbitrages de soutenabilité : une posture OPSEC qui détruit la vie sociale ou professionnelle finit par s’effondrer. **La meilleure OPSEC est celle qu’on tient dans la durée**, pas celle qu’on tient brillamment trois semaines avant de craquer.

## 1.3 Confidentialité du contenu vs confidentialité des métadonnées

Distinction fondamentale, et probablement la plus sous-estimée du domaine.

Le **contenu** d’une communication, c’est ce qui est dit. Les **métadonnées** sont tout le reste : qui parle à qui, quand, depuis où, combien de temps, à quelle fréquence, avec quel volume de données, depuis quel appareil. Le chiffrement de bout en bout (E2EE) protège typiquement le contenu. Il ne protège presque jamais les métadonnées.

Or l’attaquant sérieux préfère les métadonnées. Le général Michael Hayden, ancien directeur de la NSA, l’a résumé brutalement : *« We kill people based on metadata. »* Les drones américains ne lisent pas les conversations, ils lient des numéros à des positions à des contacts à des routines, et tirent.

À l’échelle d’un individu non militaire, la même mécanique tient : un harceleur qui sait avec qui tu communiques tous les soirs à 23h connaît probablement ta liaison ; un employeur qui voit que tu écris à un journaliste sait probablement que tu es la source ; un service de renseignement qui voit deux téléphones se géolocaliser quotidiennement au même endroit la nuit a établi une relation, indépendamment du contenu des messages.

**Conséquence pratique** : protéger le contenu sans protéger les métadonnées, c’est mettre un coffre-fort blindé dans une vitrine. Une partie significative de ce cours est consacrée à la réduction des métadonnées : choix de messageries qui les minimisent (Ch 25-26), routage anonymisé du trafic (Ch 21), compartimentation des canaux (Ch 9), et hygiène du comportement répétitif (Ch 9 et 35).

## 1.4 Surface d’attaque, surface d’exposition, surface de corrélation

Trois notions cousines qu’il faut tenir distinctes.

La **surface d’attaque** est l’ensemble des points par lesquels un adversaire peut tenter de t’atteindre techniquement : ports réseau ouverts, applications installées, services en écoute, comptes existants. Plus elle est large, plus il y a de vulnérabilités potentielles. La réduire, c’est minimiser ce qu’on installe, ce qu’on ouvre, ce qu’on expose.

La **surface d’exposition** est l’ensemble des informations qu’un adversaire peut collecter sur toi *sans avoir à t’attaquer* : ce que tu publies, ce que les data brokers compilent, ce que les fuites de données ont déjà révélé, ce que ton entourage rend public. La réduire, c’est réfléchir avant de publier et nettoyer rétroactivement (Ch 5 à 8).

La **surface de corrélation** est l’ensemble des points par lesquels deux identités, deux activités ou deux comptes peuvent être *reliés*. Un même numéro de téléphone sur deux comptes les corrèle. Un même style d’écriture sur deux pseudos les corrèle. Une même IP, un même fingerprint navigateur, une même heure de connexion les corrèlent. La compartimentation (Ch 9) vise précisément à réduire cette surface.

Ces trois surfaces interagissent. Réduire la surface d’attaque sans réduire la surface d’exposition ne sert qu’à demi : un attaquant motivé n’a plus besoin de hacker quand l’information est déjà publique.

## 1.5 Défense en profondeur, moindre privilège, need-to-know

Trois principes importés de la sécurité d’entreprise, parfaitement applicables à un individu.

**Défense en profondeur** : ne jamais miser sur une seule barrière. Si ton mot de passe est ta seule défense, sa compromission est totale. Si tu as un mot de passe fort + MFA matériel + alertes de connexion + sessions audités + procédure de récupération hors-ligne, la compromission de l’un ne renverse pas tout. Cela vaut pour les communications (E2EE + appareil durci + vérification d’identité), pour les données (chiffrement disque + chiffrement fichier + sauvegarde chiffrée hors-site), et pour la posture globale (compartimentation + minimisation + détection).

**Moindre privilège** : ne donner à chaque application, chaque compte, chaque service que les droits strictement nécessaires. L’application météo n’a pas besoin de tes contacts. Le compte que tu utilises pour une newsletter n’a pas besoin d’être le compte qui contient ta vie. Le téléphone que tu emportes en manifestation n’a pas besoin d’avoir accès à ton coffre-fort de mots de passe principal.

**Need-to-know** : ne partager une information sensible qu’avec ceux qui en ont strictement besoin pour leur rôle. Ton avocat a besoin de savoir, ton voisin non. Ta source a besoin de savoir comment te joindre, pas comment tu vis. Cette discipline, banale dans le renseignement, est rare dans la vie civile — mais elle est l’une des plus efficaces.

## 1.6 Identification, corrélation, attribution : la chaîne adversaire

Comprendre comment un adversaire passe d’une information à l’identité d’une personne est essentiel pour savoir où couper la chaîne.

1. **Identification** : associer un élément observable (pseudonyme, adresse email, appareil, numéro de téléphone, photo) à une autre information.
1. **Corrélation** : relier plusieurs identifications. Le pseudo @LunaB37 utilise le même téléphone que l’email luna.b@protonmail.com qui se connecte depuis la même IP qu’un compte Twitter sous nom civil.
1. **Attribution** : conclure, avec un niveau de confiance donné, que telle action est l’œuvre de telle personne réelle.

La défense ne consiste pas à empêcher l’identification (souvent impossible) mais à **casser les corrélations** : faire en sorte que les éléments identifiés n’appartiennent pas tous à la même chaîne. C’est l’objet de la compartimentation.

## 1.7 Le mythe de l’outil magique et le mythe de l’anonymat absolu

Deux croyances symétriques, toutes deux fausses, toutes deux dangereuses.

Le **mythe de l’outil magique** : « j’utilise X (Signal, Tor, VPN, GrapheneOS, Qubes), donc je suis protégé ». Un outil est une fonction, pas une posture. Signal protège le contenu d’un message, pas le fait que tu communiques avec cette personne ; Tor anonymise la couche réseau, pas tes habitudes ; un VPN déplace la confiance, il ne crée pas d’anonymat ; GrapheneOS durcit un téléphone, il ne t’empêche pas de te connecter à Facebook depuis ce téléphone.

Le **mythe de l’anonymat absolu** : « il est possible de disparaître totalement ». Non. Tout est question d’adversaire et de ressources. Contre un voisin curieux : trivial. Contre un employeur intrusif : faisable. Contre un harceleur déterminé : exigeant mais possible. Contre un État motivé avec budget et patience : extraordinairement difficile, et plus on essaie d’effacer ses traces de façon visible, plus on attire l’attention. La meilleure stratégie est de **rendre l’attaque coûteuse**, pas de viser l’invisibilité.

Ce cours postule en permanence que la protection est *probabiliste* et *contextuelle*. Aucune affirmation absolue n’y est faite sur ce qu’un outil garantit.

## 1.8 L’argument « rien à cacher »

démontage opérationnel et philosophique

L’argument « si tu n’as rien à cacher, tu n’as rien à craindre » se réfute sur trois niveaux.

**Niveau philosophique** : tu fermes la porte des toilettes, tu ne lis pas tes mails de famille devant inconnus, tu ne dictes pas ton mot de passe à voix haute en réunion. Personne ne vit comme s’il n’avait rien à cacher. La privacy n’est pas l’aveu d’un secret, c’est la condition d’une vie digne et d’une autonomie individuelle.

**Niveau juridique** : la vie privée est un *droit*, pas une faveur conditionnée à la conformité. L’inverser, c’est inverser la charge de la preuve : ce n’est pas à toi de prouver que tu mérites la vie privée, c’est aux États et aux entreprises de prouver qu’ils ont un motif légitime d’y porter atteinte.

**Niveau opérationnel** : ce qui est anodin aujourd’hui peut devenir compromettant demain. Une opinion politique légale dans un pays démocratique peut être criminalisée après bascule autoritaire. Une orientation sexuelle banale ici peut être létale ailleurs. Une opinion religieuse, une grossesse, une consultation médicale, une lecture, une association : tout cela est légal aujourd’hui, dans ton pays, dans ton contexte. Réduire ses traces, ce n’est pas cacher des fautes, c’est protéger des futurs qu’on ne contrôle pas.

> 🟩 **À retenir du chapitre 1**
> 
> - Cinq mots, cinq concepts : privacy, sécurité, anonymat, pseudonymat, secret. OPSEC est le métaconcept.
> - Métadonnées > contenu dans la plupart des modèles d’adversaire sérieux.
> - Trois surfaces : attaque, exposition, corrélation. Toutes trois à réduire.
> - Trois principes : défense en profondeur, moindre privilège, need-to-know.
> - La défense efficace coupe la **corrélation**, pas l’identification.
> - Pas d’outil magique, pas d’anonymat absolu. La protection est probabiliste et contextuelle.

-----
