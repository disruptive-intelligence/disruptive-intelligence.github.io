---
title: Chapitre 6 — Personnes, alias et identités fragmentées
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie II — Les entités de L'écosystème
  - index.md
---

## 6.1 L'identité clandestine comme objet composite

Dans le monde clandestin, un acteur n'a pas « un nom » — il a un faisceau d'identifiants fragmentés, distribués sur plusieurs plateformes, parfois contradictoires, parfois intentionnellement trompeurs. L'identité clandestine est un objet composite qui comprend un ou plusieurs pseudonymes (le handle utilisé sur les forums et canaux), des adresses email (souvent multiples, certaines jetables, d'autres réutilisées par erreur), des clés PGP ou de chiffrement (utilisées pour la communication sécurisée et parfois comme identifiant stable), des avatars et photos de profil (parfois réutilisés d'une plateforme à l'autre), des numéros de téléphone (pour les comptes Telegram, souvent des numéros VoIP), des wallets crypto (qui peuvent servir d'identifiant stable si réutilisés), et un profil comportemental (horaires d'activité, style d'écriture, sujets d'intérêt, langues parlées).

La distinction fondamentale est celle entre l'individu réel (la personne physique derrière le clavier) et la persona (l'identité construite pour opérer dans l'espace clandestin). Un individu peut contrôler plusieurs personas distinctes pour compartimenter ses activités. Inversement, une persona peut être partagée entre plusieurs individus (un compte de forum peut changer de main, un pseudo peut être « vendu » avec son historique de réputation).

Pour l'analyste, l'objectif n'est pas d'identifier « qui est kr0n0s_ops dans la vraie vie » (c'est le travail des forces de l'ordre avec des moyens d'investigation judiciaire), mais de déterminer quels comptes, quelles activités, et quels rôles dans l'écosystème sont contrôlés par la même entité — qu'elle soit identifiée nominativement ou non.

## 6.2 Réutilisation d'identité et cloisonnement OPSEC

La sécurité opérationnelle (OPSEC) des acteurs clandestins varie considérablement, et c'est cette variation qui crée les opportunités d'investigation.

Les acteurs sophistiqués compartimentent rigoureusement : un pseudo par activité, des emails jetables créés pour chaque opération, des wallets à usage unique, des systèmes opérationnels différents pour chaque rôle, une discipline stricte sur les horaires de connexion (pour masquer le fuseau horaire réel), et l'utilisation systématique de VPN, Tor, et machines virtuelles. Face à un acteur parfaitement compartimenté, la cartographie identitaire est extrêmement difficile.

Les acteurs moins disciplinés — et c'est la majorité — réutilisent des identifiants d'une plateforme à l'autre. Le même pseudo sur un forum de carding et sur un profil GitHub personnel. Le même email ProtonMail pour enregistrer un domaine C2 et pour s'inscrire sur un site de jeu en ligne. Le même mot de passe (révélé dans une breach) sur un compte criminel et sur un compte personnel. C'est cette réutilisation qui crée les pivots permettant de relier les activités et, potentiellement, de remonter vers l'identité réelle.

L'erreur OPSEC la plus fréquente est temporelle : un acteur qui commence ses activités avec une mauvaise OPSEC (utilisant des identifiants personnels, se connectant sans VPN) puis améliore sa sécurité au fil du temps. Les traces anciennes restent dans les bases de données historiques (WHOIS historique, breaches anciennes, caches de moteurs de recherche, archives web) et constituent des « fossiles numériques » exploitables par l'analyste.

## 6.3 Analyse linguistique et comportementale

Au-delà des identifiants techniques, le profil linguistique et comportemental d'un acteur constitue un sélecteur d'identification souvent sous-exploité.

Le **style d'écriture** — vocabulaire, syntaxe, tics de langage, erreurs grammaticales récurrentes, utilisation de l'argot, mix de langues — peut servir à relier des comptes sur différentes plateformes. Un acteur qui utilise systématiquement « ngl » (not gonna lie), des doubles points de suspension, et un mélange d'anglais et de russe translittéré a une empreinte linguistique distinctive. L'analyse stylométrique (computational stylometry) est une discipline formalisée qui peut quantifier la similarité entre des textes attribués à différents auteurs, bien qu'elle ne soit pas une preuve à elle seule.

Le **fuseau horaire d'activité** est un indicateur géographique souvent fiable. En analysant les timestamps des messages sur un forum ou un canal Telegram (en supposant que l'acteur a un rythme de vie normal avec des heures de sommeil), on peut estimer le fuseau horaire probable. Un acteur qui publie régulièrement entre 09h et 02h UTC+3 vit probablement en Europe de l'Est ou au Moyen-Orient. Cette estimation est un indice, pas une preuve — un acteur peut intentionnellement décaler ses heures d'activité.

Les **habitudes comportementales** — types de sujets abordés, réactivité aux messages, fréquence de connexion, jours d'activité (la plupart des acteurs réduisent leur activité le week-end, ce qui confirme paradoxalement une routine « professionnelle ») — complètent le profil.

> **Piège fréquent :** L'analyse linguistique peut produire des faux positifs significatifs. Deux acteurs issus de la même communauté culturelle utiliseront un vocabulaire et un style similaires sans être la même personne. L'analyse linguistique est un indice convergent, jamais une preuve isolée. Voir Ch.12 sur la convergence d'indices.

## 6.4 Homonymie, usurpation et identité reconstruite

Les faux positifs identitaires sont parmi les pièges les plus dangereux de la cartographie d'écosystèmes.

L'**homonymie** est fréquente : un pseudo courant (« darkmaster », « h4ck3r », « admin ») peut être utilisé par des dizaines de personnes différentes sur des plateformes distinctes. Établir que le « darkmaster » du forum A est le même que le « darkmaster » du forum B exige des indices corroborants indépendants du pseudo lui-même (même email, même clé PGP, même style d'écriture, même fuseau horaire).

L'**usurpation** est un risque actif : un acteur peut délibérément utiliser le pseudo d'un autre pour le discréditer, lui attribuer des activités, ou créer de la confusion. Dans les conflits entre groupes cybercriminels, l'usurpation d'identité est une tactique courante (voir Ch.34 sur la déception).

L'**identité reconstruite** désigne un acteur qui abandonne un pseudo compromis et en crée un nouveau, parfois en achetant un compte ancien sur le marché noir (avec son historique de réputation intact). Cette pratique complique le suivi longitudinal des acteurs.

La règle fondamentale est que l'identification ne s'affirme jamais — elle se qualifie par convergence d'indices indépendants. Deux indices convergents (même pseudo + même email) suggèrent. Trois indices indépendants (même pseudo + même email + même clé PGP) commencent à démontrer. La convergence est détaillée au Ch.12.

## 6.5 Fil rouge — NEXUS : la piste identitaire

> **🔍 NEXUS — Épisode 6**
>
> L'email `kr0n0s-ops@proton.me` trouvé dans le WHOIS historique a été corrélé au pseudo `kr0n0s_ops` sur le forum XSS via une breach de 2023. Samira pousse l'investigation identitaire.
>
> **Sherlock (outil OSINT de recherche de pseudo) :** Le pseudo `kr0n0s_ops` apparaît sur GitHub (3 repositories publics contenant des scripts d'exploitation de vulnérabilités réseau, dernière activité il y a 5 mois), et sur un canal Telegram public lié à la revente d'accès réseau.
>
> **Analyse linguistique :** Sur le forum XSS, kr0n0s_ops écrit en anglais avec des fautes caractéristiques d'un locuteur russophone (confusion des articles, calques syntaxiques). Il utilise systématiquement l'expression « ez pz » et des emojis spécifiques. Le fuseau horaire d'activité (analyse des timestamps sur 6 mois) indique une plage UTC+3 à UTC+4 — compatible avec Moscou, mais aussi Istanbul ou Dubaï.
>
> **DeHashed (recherche étendue) :** L'email ProtonMail apparaît dans une seconde breach (base de données d'un service VPN en 2022). Le mot de passe hashé est différent de celui du forum, mais l'IP de création du compte VPN pointe vers un réseau résidentiel en Russie (ISP : Rostelecom). C'est un indice géographique, pas une preuve (l'IP peut être un proxy).
>
> **Bilan identitaire provisoire :** Les indices convergent vers un acteur unique (même email sur WHOIS et breaches, même pseudo sur forum/GitHub/Telegram, profil linguistique russophone cohérent, fuseau horaire cohérent, IP résidentielle russe sur une donnée ancienne). Niveau de confiance que les comptes sont liés : élevé (B2). Niveau de confiance sur la localisation géographique : modéré (C3). Identité réelle : inconnue.

---
