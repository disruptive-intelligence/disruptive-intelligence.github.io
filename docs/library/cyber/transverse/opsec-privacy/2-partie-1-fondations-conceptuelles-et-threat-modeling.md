---
title: Partie 1 — Fondations conceptuelles et threat modeling
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
chapter: 2
chapters: 8
---

> **Objectif** : poser le vocabulaire, démonter les confusions courantes, installer le réflexe « threat model d’abord, outil ensuite ». Cette partie ne contient presque aucun nom d’outil. C’est volontaire : avant de choisir, il faut savoir contre quoi on se défend.

-----

## Chapitre 1 — Concepts fondamentaux et notions transverses

### 1.1 Privacy, sécurité, anonymat, pseudonymat, secret : les confusions qui tuent

Cinq mots qui désignent cinq choses différentes, constamment mélangés dans la conversation publique. Cette confusion n’est pas anecdotique : elle conduit à choisir le mauvais outil pour le mauvais problème.

**Privacy** (vie privée) est le contrôle qu’on exerce sur l’information qui circule à son sujet. Tu fermes la porte des toilettes non pas parce que tu caches un secret, mais parce que tu veux décider qui sait quoi de ton intimité. La privacy est un droit ; elle n’implique aucune dissimulation d’activité.

**Sécurité** est la capacité à protéger l’intégrité, la confidentialité et la disponibilité de ses actifs (données, comptes, appareils) contre des menaces. Tu peux être *sécurisé* sans être *anonyme* : ton compte bancaire est à ton nom, mais protégé par MFA. Tu peux être *anonyme* sans être *sécurisé* : un pseudonyme sur un forum dont la base de données fuit ne te protège plus.

**Anonymat** est l’impossibilité, pour un observateur, d’attribuer une action à une identité — y compris une identité pseudonyme. C’est le degré le plus exigeant et le plus rare. L’anonymat *absolu* n’existe pas ; on parle d’anonymat *contre un modèle d’adversaire donné*.

**Pseudonymat** est l’usage d’un nom de substitution stable. @GamerGuy12 est un pseudonyme : ce n’est pas anonyme, parce que le pseudo est persistant et peut être corrélé avec le temps à un comportement, des habitudes, des contacts, voire à une identité civile. La plupart des « anonymes » sur internet sont en réalité des pseudonymes.

**Secret** désigne une information qu’on cache activement. Tout secret est privé, mais toute information privée n’est pas secrète. Tu ne caches pas que tu prends une douche ; tu protèges l’image de toi nu sous la douche. La privacy est une question de *contexte* (qui voit quoi dans quel cadre), le secret est une question de *contenu* (cette information ne doit être vue par personne d’autre).

**OPSEC** (Operational Security) est la discipline qui consiste à identifier, contrôler et protéger les *indicateurs* qui, agrégés, permettraient à un adversaire de déduire des informations sensibles. C’est une métadiscipline : elle s’applique à tout ce qui précède.

> 🟨 **Pourquoi ces distinctions sont opérationnelles**
> Un journaliste qui veut protéger une **source** a besoin que personne ne puisse établir un *lien* entre lui et cette personne. C’est de l’anonymat (de la relation), pas du secret du contenu : peu importe ce qui est dit, ce qui compte, c’est que personne ne sache que la conversation a eu lieu. Or beaucoup de journalistes confondent les deux et chiffrent fortement le *contenu* sur des canaux qui révèlent massivement les *métadonnées de relation*. C’est une erreur de cadrage qui annule la protection.

### 1.2 OPSEC : héritage militaire, cycle en 5 étapes, transposition civile

L’OPSEC est née dans l’armée américaine pendant la guerre du Vietnam (opération Purple Dragon, 1966) après le constat que les Nord-Vietnamiens anticipaient les opérations sans avoir besoin de casser les codes : ils observaient des indicateurs (mouvements logistiques, communications radio routinières, rotations de personnel) qui, agrégés, révélaient les intentions. La parade fut de cesser de raisonner en *secrets* et de commencer à raisonner en *indicateurs*.

Le cycle OPSEC formalisé comporte cinq étapes :

1. **Identification des informations critiques** — qu’est-ce qui, si appris par l’adversaire, lui donnerait un avantage décisif ? Pour un individu : son adresse, ses contacts sensibles, sa localisation en temps réel, ses identifiants, sa relation à une source.
1. **Analyse des menaces** — qui est l’adversaire, quelles sont ses capacités, sa motivation, ses méthodes ?
1. **Analyse des vulnérabilités** — quels indicateurs, dans mes routines, mes communications, mon comportement, révèlent ces informations critiques ?
1. **Évaluation des risques** — probabilité × impact, hiérarchisation.
1. **Application de contre-mesures** — réduire les indicateurs, masquer les corrélations, compartimenter, etc.

La transposition civile ne change pas le cycle, elle change l’échelle : un individu n’a pas les ressources d’une armée. Cela impose des arbitrages de soutenabilité : une posture OPSEC qui détruit la vie sociale ou professionnelle finit par s’effondrer. **La meilleure OPSEC est celle qu’on tient dans la durée**, pas celle qu’on tient brillamment trois semaines avant de craquer.

### 1.3 Confidentialité du contenu vs confidentialité des métadonnées

Distinction fondamentale, et probablement la plus sous-estimée du domaine.

Le **contenu** d’une communication, c’est ce qui est dit. Les **métadonnées** sont tout le reste : qui parle à qui, quand, depuis où, combien de temps, à quelle fréquence, avec quel volume de données, depuis quel appareil. Le chiffrement de bout en bout (E2EE) protège typiquement le contenu. Il ne protège presque jamais les métadonnées.

Or l’attaquant sérieux préfère les métadonnées. Le général Michael Hayden, ancien directeur de la NSA, l’a résumé brutalement : *« We kill people based on metadata. »* Les drones américains ne lisent pas les conversations, ils lient des numéros à des positions à des contacts à des routines, et tirent.

À l’échelle d’un individu non militaire, la même mécanique tient : un harceleur qui sait avec qui tu communiques tous les soirs à 23h connaît probablement ta liaison ; un employeur qui voit que tu écris à un journaliste sait probablement que tu es la source ; un service de renseignement qui voit deux téléphones se géolocaliser quotidiennement au même endroit la nuit a établi une relation, indépendamment du contenu des messages.

**Conséquence pratique** : protéger le contenu sans protéger les métadonnées, c’est mettre un coffre-fort blindé dans une vitrine. Une partie significative de ce cours est consacrée à la réduction des métadonnées : choix de messageries qui les minimisent (Ch 25-26), routage anonymisé du trafic (Ch 21), compartimentation des canaux (Ch 9), et hygiène du comportement répétitif (Ch 9 et 35).

### 1.4 Surface d’attaque, surface d’exposition, surface de corrélation

Trois notions cousines qu’il faut tenir distinctes.

La **surface d’attaque** est l’ensemble des points par lesquels un adversaire peut tenter de t’atteindre techniquement : ports réseau ouverts, applications installées, services en écoute, comptes existants. Plus elle est large, plus il y a de vulnérabilités potentielles. La réduire, c’est minimiser ce qu’on installe, ce qu’on ouvre, ce qu’on expose.

La **surface d’exposition** est l’ensemble des informations qu’un adversaire peut collecter sur toi *sans avoir à t’attaquer* : ce que tu publies, ce que les data brokers compilent, ce que les fuites de données ont déjà révélé, ce que ton entourage rend public. La réduire, c’est réfléchir avant de publier et nettoyer rétroactivement (Ch 5 à 8).

La **surface de corrélation** est l’ensemble des points par lesquels deux identités, deux activités ou deux comptes peuvent être *reliés*. Un même numéro de téléphone sur deux comptes les corrèle. Un même style d’écriture sur deux pseudos les corrèle. Une même IP, un même fingerprint navigateur, une même heure de connexion les corrèlent. La compartimentation (Ch 9) vise précisément à réduire cette surface.

Ces trois surfaces interagissent. Réduire la surface d’attaque sans réduire la surface d’exposition ne sert qu’à demi : un attaquant motivé n’a plus besoin de hacker quand l’information est déjà publique.

### 1.5 Défense en profondeur, moindre privilège, need-to-know

Trois principes importés de la sécurité d’entreprise, parfaitement applicables à un individu.

**Défense en profondeur** : ne jamais miser sur une seule barrière. Si ton mot de passe est ta seule défense, sa compromission est totale. Si tu as un mot de passe fort + MFA matériel + alertes de connexion + sessions audités + procédure de récupération hors-ligne, la compromission de l’un ne renverse pas tout. Cela vaut pour les communications (E2EE + appareil durci + vérification d’identité), pour les données (chiffrement disque + chiffrement fichier + sauvegarde chiffrée hors-site), et pour la posture globale (compartimentation + minimisation + détection).

**Moindre privilège** : ne donner à chaque application, chaque compte, chaque service que les droits strictement nécessaires. L’application météo n’a pas besoin de tes contacts. Le compte que tu utilises pour une newsletter n’a pas besoin d’être le compte qui contient ta vie. Le téléphone que tu emportes en manifestation n’a pas besoin d’avoir accès à ton coffre-fort de mots de passe principal.

**Need-to-know** : ne partager une information sensible qu’avec ceux qui en ont strictement besoin pour leur rôle. Ton avocat a besoin de savoir, ton voisin non. Ta source a besoin de savoir comment te joindre, pas comment tu vis. Cette discipline, banale dans le renseignement, est rare dans la vie civile — mais elle est l’une des plus efficaces.

### 1.6 Identification, corrélation, attribution : la chaîne adversaire

Comprendre comment un adversaire passe d’une information à l’identité d’une personne est essentiel pour savoir où couper la chaîne.

1. **Identification** : associer un élément observable (pseudonyme, adresse email, appareil, numéro de téléphone, photo) à une autre information.
1. **Corrélation** : relier plusieurs identifications. Le pseudo @LunaB37 utilise le même téléphone que l’email luna.b@protonmail.com qui se connecte depuis la même IP qu’un compte Twitter sous nom civil.
1. **Attribution** : conclure, avec un niveau de confiance donné, que telle action est l’œuvre de telle personne réelle.

La défense ne consiste pas à empêcher l’identification (souvent impossible) mais à **casser les corrélations** : faire en sorte que les éléments identifiés n’appartiennent pas tous à la même chaîne. C’est l’objet de la compartimentation.

### 1.7 Le mythe de l’outil magique et le mythe de l’anonymat absolu

Deux croyances symétriques, toutes deux fausses, toutes deux dangereuses.

Le **mythe de l’outil magique** : « j’utilise X (Signal, Tor, VPN, GrapheneOS, Qubes), donc je suis protégé ». Un outil est une fonction, pas une posture. Signal protège le contenu d’un message, pas le fait que tu communiques avec cette personne ; Tor anonymise la couche réseau, pas tes habitudes ; un VPN déplace la confiance, il ne crée pas d’anonymat ; GrapheneOS durcit un téléphone, il ne t’empêche pas de te connecter à Facebook depuis ce téléphone.

Le **mythe de l’anonymat absolu** : « il est possible de disparaître totalement ». Non. Tout est question d’adversaire et de ressources. Contre un voisin curieux : trivial. Contre un employeur intrusif : faisable. Contre un harceleur déterminé : exigeant mais possible. Contre un État motivé avec budget et patience : extraordinairement difficile, et plus on essaie d’effacer ses traces de façon visible, plus on attire l’attention. La meilleure stratégie est de **rendre l’attaque coûteuse**, pas de viser l’invisibilité.

Ce cours postule en permanence que la protection est *probabiliste* et *contextuelle*. Aucune affirmation absolue n’y est faite sur ce qu’un outil garantit.

### 1.8 L’argument « rien à cacher » : démontage opérationnel et philosophique

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

## Chapitre 2 — Threat modeling personnel

### 2.1 Les cinq questions fondatrices

L’Electronic Frontier Foundation a formalisé un cadre minimal de threat modeling personnel en cinq questions. Elles sont simples, mais leur mise en œuvre rigoureuse change tout.

1. **Que veux-je protéger ?** (mes actifs)
1. **Contre qui ?** (mes adversaires)
1. **Quelle est la probabilité que je doive le protéger ?** (le risque)
1. **Quelles sont les conséquences si j’échoue ?** (l’impact)
1. **Combien de difficultés suis-je prêt(e) à accepter pour empêcher cela ?** (le coût acceptable)

La cinquième est la plus importante et la plus souvent oubliée. Elle ancre la réflexion dans le réel : sans elle, on dérive vers des architectures théoriquement parfaites mais inapplicables dans la vraie vie.

### 2.2 Inventaire des actifs

Un actif est une chose à laquelle tu tiens et que tu veux protéger. Pour un individu, ce sont généralement :

- **Identité** : nom, photo, voix, adresse, état civil, nationalités.
- **Comptes** : email principal (centre de gravité, cf. Ch 29), réseaux sociaux, comptes bancaires, comptes professionnels, comptes cloud, comptes administratifs (impôts, sécurité sociale).
- **Données** : fichiers personnels, photos, documents professionnels, dossiers médicaux, contrats, journaux, correspondance.
- **Appareils** : téléphone(s), ordinateur(s), tablettes, IoT, clés de sécurité, cartes SIM.
- **Relations** : carnet d’adresses, liens familiaux, sources journalistiques, contacts professionnels, réseaux d’engagement (associatif, politique, religieux).
- **Localisation** : domicile, lieux de travail, déplacements habituels, voyages.
- **Réputation** : image publique, dossiers passés, opinions exprimées, contenus produits.
- **Présence physique** : sécurité personnelle, intégrité corporelle, accès au domicile.

Liste tes actifs *avant* de penser aux outils. Pour chacun, note : où est-il stocké, qui y a accès, qu’est-ce qui empêche aujourd’hui un tiers d’y accéder. La plupart des gens découvrent à ce stade que l’« email principal » concentre les clés de tout le reste (récupération de mot de passe, MFA SMS, factures).

### 2.3 Identifier ses adversaires sans inflation ni déni

Deux travers symétriques empoisonnent l’exercice.

L’**inflation** consiste à se croire la cible de la NSA quand on est un militant climatique local. C’est flatteur, c’est anxiogène, c’est inefficace : on construit des architectures sur-dimensionnées qui détournent l’attention des vraies menaces (un employeur qui surveille les emails, un ex qui a gardé un mot de passe, un harceleur qui scrute les réseaux sociaux). On se prépare à Pegasus alors qu’on est vulnérable à un simple phishing.

Le **déni** est l’inverse : « je ne suis personne, qui voudrait m’attaquer ? ». Or beaucoup d’attaques sont *opportunistes* (phishing de masse, vol de crédentials, ransomware). Tu n’as pas besoin d’intéresser quelqu’un personnellement pour être ciblé statistiquement. Et certaines menaces sont *de proximité* (ex-partenaire, employeur intrusif) : il suffit d’une relation à problèmes pour avoir un adversaire réel.

Le bon réflexe : lister les adversaires *plausibles* compte tenu de qui tu es et de ce que tu fais. Un journaliste d’investigation a comme adversaires réalistes : États visés par ses enquêtes, sociétés visées, criminalité organisée si pertinent, harceleurs en ligne (notamment femmes journalistes), employeurs (sécurité industrielle des médias). Une activiste a : forces de l’ordre nationales, infiltrés, contre-mouvements organisés, harceleurs. Un dirigeant : concurrents (espionnage économique), fraudeurs ciblés, criminalité organisée si secteur exposé. Un particulier durci typique : criminalité de masse, employeur, ex-partenaire, plateformes elles-mêmes (capitalisme de surveillance).

### 2.4 Capacité × motivation × probabilité

Chaque adversaire doit être caractérisé par trois paramètres :

- **Capacité** : quelles ressources techniques, juridiques, humaines, financières ? Un service de renseignement étatique a accès à des zero-days, à de la coopération inter-services, à des contraintes judiciaires sur les opérateurs. Un harceleur isolé a accès à Google, des forums, peut-être un peu d’OSINT manuel. La capacité borne le *plafond* de la menace.
- **Motivation** : quel intérêt l’adversaire a-t-il à m’attaquer, *moi spécifiquement* ? Forte (une enquête qui le compromet) ou faible (statistique, sans personnalisation) ?
- **Probabilité** : sachant capacité et motivation, quelle est la probabilité d’occurrence ?

Une matrice utile :

|                      |Faible capacité   |Capacité moyenne|Forte capacité              |
|----------------------|------------------|----------------|----------------------------|
|**Faible motivation** |Risque négligeable|Risque faible   |Risque modéré (opportuniste)|
|**Motivation moyenne**|Risque faible     |Risque modéré   |Risque élevé                |
|**Forte motivation**  |Risque modéré     |Risque élevé    |Risque critique             |

Les défenses doivent être calibrées sur les cases à *risque modéré et plus*. Les cases à risque négligeable n’imposent rien de spécifique.

### 2.5 Coût acceptable de la défense

C’est l’arbitrage permanent. Trois dimensions :

- **Coût financier** : prix des appareils, abonnements (VPN, gestionnaire de mots de passe), clés matérielles.
- **Coût cognitif** : apprendre, mémoriser, configurer, maintenir.
- **Coût social et ergonomique** : friction au quotidien, perte de fonctionnalités, isolement par rapport aux usages dominants.

Une mesure trop coûteuse sur l’une des trois dimensions finit abandonnée. La vraie question n’est pas « quelle est la meilleure configuration ? » mais « quelle est la meilleure configuration que je suis capable de maintenir 18 mois sans relâcher ? ».

Un exemple : Qubes OS offre une compartimentation excellente, mais demande un matériel adapté, deux heures d’installation, une discipline opérationnelle, et une acceptation de friction quotidienne. Si la personne, après deux semaines, repasse à Windows par fatigue, le bénéfice net est négatif (elle a perdu du temps et n’a pas amélioré sa posture). Pour cette personne, un Linux durci + gestionnaire de mots de passe + clé FIDO2 est *meilleur* que Qubes, parce que c’est ce qu’elle tiendra.

### 2.6 Trois niveaux de posture : N1 / N2 / N3

Pour éviter le sur-dimensionnement (et le sous-dimensionnement) qui sont les deux travers symétriques du threat modeling individuel, ce cours propose trois niveaux de posture explicites. Chaque chapitre indiquera, quand pertinent, à quel niveau telle mesure se rapporte.

**Niveau 1 — Hygiène essentielle**

- *Pour qui* : tout adulte connecté, sans contexte de menace personnalisée. La grande majorité des lecteurs.
- *Objectif* : réduire significativement la surface d’exposition au capitalisme de surveillance, à la criminalité opportuniste, aux fuites de credentials, aux harcèlements de bas niveau.
- *Stack type* : gestionnaire de mots de passe (Bitwarden) + MFA matériel (YubiKey) ou TOTP pour comptes critiques + Signal pour communications + chiffrement disque (BitLocker / FileVault / LUKS) + mises à jour disciplinées + sauvegardes 3-2-1 + uBlock Origin + DNS chiffré + ADP iCloud si Apple.
- *Coût* : 50-200 € de matériel (YubiKey, abonnement gestionnaire éventuel), 2-3 h de configuration initiale, 15-30 min par mois de maintenance.
- *Ce que ce niveau fait* : élimine 90 % du risque statistique.

**Niveau 2 — Profil exposé**

- *Pour qui* : journaliste, militant identifié, dirigeant d’entreprise sensible, personnalité publique modérée, professionnel du droit ou de la santé manipulant des dossiers sensibles, personne ayant un adversaire de proximité connu et motivé.
- *Objectif* : ajouter une compartimentation forte et une résistance aux attaques ciblées de niveau intermédiaire.
- *Stack type* : N1 + GrapheneOS sur Pixel dédié *ou* iPhone avec Lockdown Mode + SimpleX pour canaux les plus sensibles + Tails sur USB pour sessions ponctuelles + Mullvad VPN permanent + Mullvad Browser quotidien + email Proton avec alias + procédures BEC si pro + reboot quotidien des appareils sensibles.
- *Coût* : 500-1500 € (Pixel, USB Tails, abonnements), 1-2 jours de configuration initiale + apprentissage continu, 1-2 h par mois de maintenance disciplinée.

**Niveau 3 — HVT / source / journaliste sensible / cible documentée**

- *Pour qui* : journaliste avec enquête en cours sur acteurs ressourcés, lanceur d’alerte avant divulgation, opposant politique en exil, dissident, avocat de la défense sur dossier sensible, personne ayant reçu une *Threat Notification* d’Apple/Google/Meta.
- *Objectif* : résister aux attaques par spyware mercenaire, à l’analyse forensique avancée, à la coercition juridique transfrontière.
- *Stack type* : N2 + Qubes OS sur laptop principal + Whonix dans Qubes + GrapheneOS avec profils multiples + air-gap pour secrets long terme + MVT mensuel + iVerify + audit forensique périodique + plan d’incident documenté + équipe juridique mobilisable + relation établie avec Access Now / Citizen Lab.
- *Coût* : 2000-5000 € (matériel adapté Qubes, multiples appareils), 2-4 semaines d’apprentissage initial, 4-8 h par mois de maintenance, discipline opérationnelle continue.

**Note critique** : un niveau plus élevé ne se substitue pas à un niveau plus bas. Le Niveau 3 *contient* le Niveau 1. Une posture Niveau 3 mal entretenue sur les fondamentaux N1 (mot de passe réutilisé sur un compte de récupération) est moins solide qu’une posture N1 disciplinée. **Aucun lecteur ne devrait viser directement le N3 sans avoir maîtrisé le N1.**

**Anti-pattern à éviter** : se dimensionner en N3 par fascination technique alors que le threat model réel est N1. La friction qui en résulte épuise et conduit à abandonner *en bloc*, sortant alors en N0 (rien). Mieux vaut un N1 tenu dix ans qu’un N3 abandonné en deux mois.

### 2.7 Matrice STRIDE/LINDDUN adaptée au particulier

Pour un audit plus structuré, deux taxonomies de menaces sont utiles.

**STRIDE** (Microsoft, focalisée sécurité) :

- **S**poofing — usurpation d’identité (compte piraté, SIM swap, faux mail au nom de…)
- **T**ampering — altération de données (modification de fichiers, faux documents)
- **R**epudiation — possibilité de nier une action (qui a fait quoi sur un appareil partagé ?)
- **I**nformation disclosure — fuite d’informations
- **D**enial of service — déni de service (compte bloqué, appareil rendu inutilisable)
- **E**levation of privilege — élévation de privilèges (admin sur ton appareil)

**LINDDUN** (focalisée privacy) :

- **L**inkability — possibilité de relier deux activités
- **I**dentifiability — possibilité d’identifier une personne derrière une activité
- **N**on-repudiation — impossibilité de nier une action (problème côté privacy)
- **D**etectability — possibilité de détecter qu’une activité a eu lieu
- **D**isclosure of information — divulgation d’information
- **U**nawareness — l’utilisateur ignore ce qui se passe avec ses données
- **N**oncompliance — non-conformité aux règles applicables

LINDDUN est particulièrement utile pour penser privacy plutôt que sécurité pure. *Linkability* notamment recoupe la surface de corrélation discutée au Ch 1.

### 2.8 L’erreur « threat model trop complexe »

Privacy Guides a identifié un anti-pattern récurrent : la personne qui construit un threat model d’opposant politique alors qu’elle fait du tricot. Trois symptômes :

- Empilement d’outils dont la combinaison crée de nouvelles surfaces d’attaque (un VPN qui fuit, branché derrière un Tor mal configuré, sur un OS compromis).
- Procédures qui exigent une discipline permanente impossible à tenir (rotation manuelle de comptes hebdomadaire).
- Adversaires fantasmés qui justifient des mesures, en ignorant les adversaires réels.

Le bon test : *« Si l’adversaire que je redoute me ciblait demain, que ferait-il en premier ? »* La réponse, dans 90 % des cas, n’est pas un zero-day Pegasus. C’est un phishing, une réutilisation de mot de passe, une question de récupération de compte mal protégée, une publication imprudente d’un proche. Commence par ça.

### 2.9 Définir ce qui est hors périmètre

Un threat model honnête liste explicitement ce qu’il *ne couvre pas* :

- « Je ne cherche pas à résister à une perquisition judiciaire en France. »
- « Je ne cherche pas à empêcher que ma banque sache combien j’ai sur mon compte. »
- « Je ne cherche pas l’anonymat sur LinkedIn, qui est mon outil professionnel. »
- « Je ne cherche pas à protéger contre un voleur qui aurait mon téléphone allumé et déverrouillé en main. »

Cette explicitation a deux vertus. D’abord, elle décharge la conscience : tu n’as pas à porter le poids de défenses contre tout. Ensuite, elle clarifie où placer les efforts.

### 2.10 *Fil rouge* — Léa construit son premier threat model en 90 minutes

Léa Martens, journaliste freelance à Bruxelles, démarre son enquête en consortium. Elle s’assied avec un carnet et trois colonnes : actifs, adversaires, mesures.

**Actifs critiques** :

- Identité de ses sources (priorité absolue — la révéler les met en danger physique).
- Documents reçus (priorité haute — base de l’enquête).
- Carnet d’adresses (priorité haute — révèle ses relations).
- Communications avec ses sources (contenu *et* métadonnées).
- Son matériel et son domicile (sécurité personnelle).

**Adversaires plausibles** :

- Le commissaire visé (capacité moyenne via cabinet, motivation forte si l’enquête sort).
- La société de surveillance privée (capacité technique élevée — c’est leur métier — motivation modérée à élevée selon avancement).
- L’oligarque (capacité élevée via services achetés, motivation élevée).
- Services russes (capacité très élevée, motivation modérée à élevée si l’enquête touche).
- Trolls et harceleurs en ligne (capacité faible, motivation possible si l’enquête sort).

**Hors périmètre explicite** :

- Résistance à une saisie judiciaire belge ou française légale (Léa s’engage à respecter la loi locale et fera appel à son avocat si besoin).
- Anonymat sur LinkedIn et auprès de sa rédaction.
- Protection contre criminalité opportuniste classique (couverte par hygiène standard, pas spécifique à l’enquête).

**Mesures prioritaires identifiées** (à creuser dans les chapitres suivants) :

- Compartimentation stricte : un appareil enquête séparé du quotidien.
- Canal source ne passant pas par Gmail/WhatsApp.
- Réduction d’empreinte publique sur les réseaux sociaux *pendant* l’enquête.
- Audit de son entourage proche pour ne pas créer de fuite indirecte.
- Préparation à un possible voyage en pays sensible.

Le document tient sur deux pages. Léa le date, le chiffre dans son gestionnaire de mots de passe (qu’elle vient de mettre en place — cf. Ch 29), et se promet de le réviser tous les trimestres.

> 🟦 **Exercice du chapitre**
> Produis ton propre threat model en une page : 3 actifs prioritaires, 3 adversaires plausibles, 3 mesures réalistes, 3 éléments explicitement hors périmètre. Date-le, range-le, prévois sa relecture à 3 mois.

-----

## Chapitre 3 — Taxonomie des adversaires

Un adversaire n’est pas un autre. Confondre les catégories conduit à mal calibrer la défense. Voici les grandes familles, du moins ciblé au plus ciblé, avec leurs capacités, motivations et méthodes typiques.

### 3.1 Surveillance de masse étatique

**Acteurs** : agences de renseignement (NSA, GCHQ, DGSE, BND, FSB, etc.), services de signalisation (SIGINT), partenariats inter-services (Five Eyes, Nine Eyes, Fourteen Eyes).

**Capacités** : collecte passive massive (interception de câbles sous-marins, points d’échange internet), rétention de métadonnées sur des durées variables selon les juridictions, accès légal aux opérateurs (réquisitions, lettres de sécurité nationale), capacité de déchiffrement limitée (la crypto moderne tient — c’est l’OPSEC et les endpoints qui tombent), et exploitation de zero-days lorsque ciblage justifié.

**Modèle** : surveillance *non ciblée par défaut*, ciblage *à la demande* lorsqu’une personne devient pertinente. Tu n’es pas écouté *spécifiquement* aujourd’hui, mais tes métadonnées circulent dans des bases dont la rétention varie.

**Méthodes pertinentes pour toi** : collecte de métadonnées (qui parle à qui, quand), géolocalisation cellulaire, analyse de graphes sociaux, exploitation des relations entre individus.

**Ce contre quoi protéger** : minimisation des métadonnées (messageries adaptées, Tor), compartimentation des identités, prudence sur les graphes de relation.

**Limite réaliste** : si tu es activement ciblé par un service étatique majeur, tu ne pourras pas gagner seul cette guerre. Ton objectif est de *rendre coûteux* le suivi et de minimiser ce qu’ils ont déjà.

### 3.2 Capitalisme de surveillance

**Acteurs** : data brokers (Acxiom, LexisNexis, Spokeo, Intelius, Whitepages), ad-tech (Google, Meta, The Trade Desk, Criteo), courtiers de localisation (X-Mode, Cuebiq, Veraset — souvent revendus à des agences gouvernementales).

Une évolution préoccupante de ce modèle est l’ADINT (Advertising Intelligence) : l’exploitation des données et mécanismes publicitaires à des fins de renseignement. Des données initialement collectées pour le ciblage marketing — identifiants publicitaires, localisation, applications utilisées, signaux comportementaux — peuvent être revendues, agrégées ou exploitées pour suivre des individus, cartographier des groupes ou préparer des actions ciblées. L’ADINT illustre la porosité entre publicité, courtage de données, surveillance privée et renseignement étatique.

**Capacités** : agrégation massive de données issues d’applications mobiles, de cookies, de programmes de fidélité, de fuites, de registres publics, de réseaux sociaux. Construction de profils détaillés vendus à des fins publicitaires, mais aussi à des fins de scoring (crédit, assurance), de vérification (background check), voire à des forces de l’ordre via achat plutôt que mandat.

**Modèle** : profit par accumulation. Tu n’es pas la cible, tu es la marchandise.

**Méthodes** : SDK publicitaires dans les apps, cookies tiers (en déclin), fingerprinting (en croissance, cf. Ch 23), achat de bases de données fuitées, agrégation cross-device.

**Ce contre quoi protéger** : navigateurs anti-fingerprint (Ch 24), désinscription data brokers (Ch 6), minimisation des permissions mobiles (Ch 15), email aliasing (Ch 27), paiements compartimentés (Ch 32).

**Spécificité** : c’est l’adversaire le plus probable de tout lecteur. Et pourtant le moins fantasmé. La discipline anti-tracking quotidienne est le bénéfice immédiat de ce cours pour la grande majorité des gens.

### 3.3 Plateformes elles-mêmes : Google, Meta, Apple, Microsoft, TikTok

**Acteurs** : les géants du numérique. Statut hybride entre fournisseurs et adversaires : tu leur confies des données pour utiliser leurs services, et eux les exploitent.

**Capacités** : accès intégral à ce que tu leur confies (emails Gmail, photos Google Photos, contacts iCloud, messages WhatsApp côté métadonnées, etc.). Capacité de réquisition judiciaire à laquelle ils répondent selon les juridictions et les procédures. Capacité d’analyse comportementale fine (Apple Intelligence, Gemini sur Android, etc.).

**Modèle** : variable selon la plateforme. Apple revendique un modèle moins intrusif (et Advanced Data Protection chiffre certaines données de bout en bout, cf. Ch 14 et 30). Google et Meta vivent du ciblage publicitaire. Microsoft est entre les deux. TikTok pose des questions spécifiques liées à sa juridiction.

**Méthodes pertinentes** : ce que tu leur donnes volontairement (essentiellement tout, si tu utilises leurs services sans précaution), enrichi par l’IA générative côté Microsoft Copilot et Apple Intelligence (Ch 34).

**Ce contre quoi protéger** : chiffrement côté client par-dessus le cloud (Ch 30), email auto-hébergé ou chez fournisseur E2EE (Ch 27), ADP iCloud activée si Apple, minimisation des comptes Google rattachés au principal.

### 3.4 Censure et restriction d’accès

**Acteurs** : États autoritaires (Chine, Iran, Russie, Émirats, Vietnam, etc.) mais aussi démocratiques sur certains contenus (filtrage DNS au RU et en France pour terrorisme et pédocriminalité, etc.), FAI qui appliquent les ordres, plateformes qui appliquent les politiques.

**Capacités** : blocage DNS, blocage IP, deep packet inspection (DPI), perturbation de protocoles (Tor, VPN), obligation d’enregistrement, sanctions pénales pour les contournements.

**Ce contre quoi protéger** : VPN (Ch 20), Tor avec bridges (Ch 21), DNS chiffré (Ch 19), résolveurs alternatifs.

**Cadre légal** : varie radicalement selon les juridictions. En Iran, l’usage de VPN est techniquement illégal mais massif. En Chine, le contournement du Great Firewall expose à des sanctions. En France, le RGPD protège l’usage privé d’outils légitimes.

### 3.5 Attaques ciblées : APT étatiques, mercenaires

**Acteurs étatiques** : APT chinois (APT10, APT41), russes (APT28, APT29, Turla), nord-coréens (Lazarus), iraniens (APT34, Charming Kitten), occidentaux aussi mais moins publiquement documentés. Les APT visent typiquement entreprises, gouvernements, ONG sensibles, dissidents.

**Acteurs mercenaires** : NSO Group (Pegasus), Intellexa (Predator), Paragon Solutions (Graphite), QuaDream, Candiru, Hacking Team (historique). Ces sociétés vendent à des États (parfois autoritaires) du spyware mobile de pointe.

**Capacités** : zero-days iOS/Android (zero-click parfois), exploits chaînés, infrastructure C2 résiliente, capacité de pivot et d’exfiltration.

**Cibles documentées par Citizen Lab et Amnesty Security Lab** : journalistes d’investigation, activistes des droits humains, avocats de la défense, leaders d’opposition, proches de cibles. Cas confirmés dans des dizaines de pays.

**Méthodes** : zero-click iMessage/WhatsApp (cas Pegasus FORCEDENTRY, cas Paragon Graphite 2024-2025), liens piégés ciblés, installation physique en transit, infection via Wi-Fi infrastructure compromise.

**Ce contre quoi protéger** : Lockdown Mode iOS (Ch 15), GrapheneOS, redémarrage régulier (zero-clicks souvent non persistants), MVT et iVerify (Ch 33), notifications Apple/WhatsApp/Google.

**Coût** : déploiement d’un spyware mercenaire coûte entre 10k$ et plusieurs millions selon la cible. *Tu n’es pas ciblé par défaut.* Si tu l’es, tu le sauras probablement par les notifications des plateformes.

### 3.6 Criminalité opportuniste

**Acteurs** : groupes de cybercriminalité organisée, opérateurs ransomware, vendeurs de credentials, brokers d’accès, phishers de masse.

**Capacités** : kits de phishing prêts à l’emploi, base de credentials achetée sur forums, malware as a service, infrastructure botnet.

**Modèle** : volume. Tu n’es pas ciblé, tu es statistique. Si tu cliques sur le bon lien le bon jour, tu paies.

**Ce contre quoi protéger** : MFA fort, gestionnaire de mots de passe (Ch 29), méfiance des liens, mises à jour à jour, sauvegardes 3-2-1 (Ch 30).

### 3.7 Adversaires de proximité

**Acteurs** : ex-partenaire (cas particulièrement fréquent et dangereux, notamment dans les contextes de violences conjugales), harceleur (stalker), famille intrusive ou hostile, employeur intrusif, journaliste hostile, voisin curieux.

**Capacités** : faibles techniquement, mais **élevées en connaissance préalable** — ils savent ton anniversaire, le nom de ton chien (souvent ton mot de passe), tes habitudes, tes lieux de passage. Ils ont parfois eu accès physique à tes appareils (voir spyware *stalkerware* commercial : mSpy, FlexiSpy, etc.).

**Modèle** : motivation très forte, capacité technique faible mais compensée par la proximité.

**Méthodes** : devinette de mot de passe, accès physique, stalkerware installé pendant la relation, observation OSINT classique, exploitation des proches.

**Ce contre quoi protéger** : changement complet de credentials après rupture, audit des appareils (cf. annexe 8 ressources Coalition Against Stalkerware), MFA matériel, séparation des comptes Apple/Google, sortie des comptes partagés, prudence Find My et localisation.

> 🟧 **À noter** : ce threat model est sous-traité dans la plupart des cours de cybersécurité, qui se focalisent sur l’étatique. Or pour une fraction significative de la population, l’adversaire principal est dans son entourage. Le **Cas D** en fin de cours traite spécifiquement ce scénario.

### 3.8 Adversaires accidentels : l’entourage qui dénonce sans le savoir

Catégorie particulière. Ton frère qui te tague sur une photo Instagram à un anniversaire de famille révèle ta localisation à un harceleur. Ton collègue qui répond à un appel de prétexte donne ton emploi du temps à un ingénieur social. Tes parents qui rendent publique ta date de naissance et le nom de jeune fille de ta mère mettent la sécurité de tes questions de récupération en danger.

L’entourage n’est pas hostile mais constitue un vecteur d’exposition que tu ne contrôles pas. Une partie de la défense consiste à *éduquer* discrètement les personnes proches (Ch 35).

### 3.9 HVT (High Value Targets) : qui est vraiment ciblé, qui se croit ciblé

**HVT réels** : journalistes d’investigation publiant sur des dossiers critiques, leaders d’opposition dans des régimes autoritaires, lanceurs d’alerte avant publication, avocats de la défense sur des dossiers sensibles, militants sur des sujets visés (climat radical, droits humains dans certains pays). Catégories documentées par Citizen Lab et Amnesty Security Lab comme cibles répétées de spyware mercenaire.

**HVT autoperçus mais peu probables** : la plupart des « privacy enthusiasts », des professionnels cyber non exposés professionnellement, des particuliers durcis. Ils auraient *tout intérêt* à concentrer leurs efforts sur les menaces réelles (capitalisme de surveillance, criminalité opportuniste, doxxing), plus probables et plus traitables.

**Test honnête de HVT-ness** : as-tu publiquement, et dans le dernier exercice de ton activité, produit une information qui mette en danger un acteur capable et motivé ? Si non, tu n’es probablement pas HVT. Si oui, tu l’es peut-être — et il est temps de durcir sérieusement.

> 🟩 **À retenir du chapitre 3**
> 
> - Le capitalisme de surveillance est l’adversaire le plus probable de tout le monde.
> - Les adversaires de proximité sont sous-évalués et particulièrement dangereux car ils ont de la connaissance préalable.
> - Les attaques mercenaires (Pegasus & co) sont réelles mais ciblent un nombre restreint de profils ; ne pas dimensionner sa défense sur ce seul axe.
> - Définir honnêtement son profil de HVT-ness conditionne tout le reste.

-----

## Chapitre 4 — Cartographie de l’empreinte et grands modèles d’exposition

L’objectif de ce chapitre est de produire une cartographie systématique de ce qui, depuis toi, s’échappe vers le monde extérieur. Sans cette cartographie, toute mesure défensive est aveugle.

### 4.1 Empreinte volontaire, involontaire et héritée

L’**empreinte volontaire** est ce que tu publies consciemment : posts, photos, opinions, profil professionnel, contributions GitHub, articles. Elle est, en théorie, sous ton contrôle. En pratique, sa permanence (Wayback Machine, archives, captures) la rend irréversible.

L’**empreinte involontaire** est ce qui fuit sans intention : métadonnées de fichiers, géolocalisation de photos, fingerprints navigateur, requêtes DNS, données vendues par des applications.

L’**empreinte héritée** est ce que d’autres exposent sur toi : photos taguées par des amis, mentions dans des publications, témoignages, registres publics, données vendues par des courtiers qui t’ont profilé sans ton accord.

Les trois s’accumulent. Et seule la première est en théorie sous ton contrôle.

### 4.2 Exposition par les comptes

L’email principal est le **centre de gravité** de l’identité numérique. Il est utilisé pour récupérer les mots de passe de la plupart des autres comptes. Sa compromission donne accès à la quasi-totalité de la vie numérique. Inversement, sa perte (faille, oubli, suspension par le fournisseur) cascade en perte massive.

L’audit des comptes consiste à dresser la liste de tous les services où tu as un compte. La plupart des gens, à cet exercice, en découvrent entre 100 et 500. Outils utiles : recherche dans les emails reçus (« welcome », « confirm your email »), historique de gestionnaire de mots de passe, vérification HaveIBeenPwned avec ton email principal.

Pour chaque compte critique, note : email associé, MFA activé ou non, type de MFA, dernière connexion, mot de passe unique ou non, données stockées.

### 4.3 Exposition par les appareils

Chaque appareil collecte et transmet :

- Identifiants matériels : adresse MAC (Wi-Fi, Bluetooth), IMEI pour les téléphones, numéros de série, identifiants TPM, identifiants publicitaires (Advertising ID Android, IDFA iOS — désactivables).
- Capteurs : GPS, accéléromètre (qui révèle des modes de transport, des activités physiques), microphone, caméra.
- Connectivité : Wi-Fi probing (le téléphone qui hurle les noms des réseaux passés), Bluetooth/BLE beacons.
- Logiciels installés : chaque application installe son SDK, qui collecte typiquement plus que ce que l’application semble faire.

### 4.4 Exposition par les applications

Les applications mobiles sont des vecteurs sous-estimés. Une appli météo typique demande accès à la localisation précise (raisonnable), au stockage (douteux), aux contacts (suspect), à l’identifiant publicitaire (mauvais signe). Beaucoup d’applis intègrent 5 à 30 SDK tiers, chacun avec ses propres flux de données.

**Test pratique** : sur ton téléphone, ouvre les paramètres → confidentialité → audit des permissions. Combien d’applis ont accès à ta localisation en arrière-plan ? À tes contacts ? À ton micro ? Réponse moyenne : beaucoup trop.

### 4.5 Exposition par le réseau

Chaque connexion réseau révèle :

- **IP source** : identifie ton FAI et ta localisation grossière (souvent ville).
- **Requête DNS** : révèle les noms de domaine que tu consultes (sauf DoH/DoT — Ch 19).
- **SNI** (Server Name Indication) : révèle l’hôte que tu joins, même en HTTPS (sauf ECH — Ch 19).
- **Métadonnées TLS** : horodatages, suites cryptographiques, taille des échanges.
- **Wi-Fi et Bluetooth** : émissions radio en clair de probes et de beacons.

Le FAI voit *tout* ce qui passe par sa box (sauf si VPN). Les opérateurs cellulaires aussi. Les exploitants de Wi-Fi public également.

### 4.6 Exposition par le cloud

La synchronisation automatique est la fuite cloud la plus massive. Les photos iCloud/Google Photos s’uploadent automatiquement avec leurs métadonnées EXIF (Ch 31). Les contacts iCloud/Google synchronisent ton carnet d’adresses chez Apple/Google. Les sauvegardes WhatsApp dans iCloud/Google Drive ne sont pas chiffrées de bout en bout par défaut (et le sont seulement si activées explicitement).

Quand Apple Advanced Data Protection (ADP) est activée, une partie significative des données iCloud devient chiffrée de bout en bout (photos, sauvegardes iCloud, notes, rappels, signets Safari, etc.). Mais : les contacts, le calendrier, et les mails iCloud restent accessibles à Apple pour des raisons d’interopérabilité (Ch 14 et 30).

### 4.7 Exposition par les métadonnées

Les métadonnées sont le gisement le plus sous-estimé. À traiter en profondeur au Ch 31, mais à mentionner ici :

- **EXIF photo** : coordonnées GPS, modèle d’appareil, numéro de série, horodatage, profil ICC personnalisé qui peut identifier l’écran de prise de vue ou de retouche.
- **PDF** : auteur, logiciel de création, historique de révisions, objets cachés, signatures invisibles.
- **Office (DOCX/XLSX/PPTX)** : auteur, commentaires, suivi des modifications activé sans en avoir conscience.
- **Audio/vidéo** : tags, codecs, traces de montage, voire artefacts d’enregistrement (gyroscope révélant le modèle exact d’iPhone).

### 4.8 Exposition par l’entourage

Le graphe social est un identifiant en soi. Deux personnes ayant 15 contacts en commun sont probablement reliées d’une façon ou d’une autre. Les plateformes (Facebook, LinkedIn, Instagram, Snapchat) construisent ces graphes en permanence. Le « people you may know » est l’application directe de cette analyse.

Tes proches publient à ton sujet sans en mesurer l’impact : photo de famille géolocalisée, mention de ton lieu de travail dans un post de félicitations professionnelles, lien social public sur Facebook.

### 4.9 Exposition par les habitudes

L’analyse comportementale identifie des motifs : tu te connectes à Tor tous les jeudis à 22h ; tu écris en moyenne 60 mots par minute avec un certain rythme ; tu utilises certaines tournures (cf. stylométrie, Ch 35) ; tu consultes certains sites à certaines heures. Pris isolément, chaque indicateur est insignifiant. Agrégés, ils forment une signature.

**Conséquence opérationnelle** : si tu ouvres un nouveau pseudonyme et que tu le pratiques avec les mêmes habitudes que ton identité connue, le pseudonyme se corrélera à terme.

### 4.10 Exposition par les fuites

HaveIBeenPwned recense, en 2025-2026, plus de 13 milliards de credentials exposées issues de fuites passées. Si tu utilises internet depuis plus de cinq ans, ton email principal a presque certainement été inclus dans au moins une fuite. Le contenu varie : email + mot de passe (le plus courant), email + numéro de téléphone, profil complet (LinkedIn 2021), informations bancaires (rares mais existantes).

Ces fuites alimentent :

- Le *credential stuffing* : tentative automatisée de réutilisation des mots de passe fuités sur d’autres services. Première cause de compromission de comptes pour la majorité des utilisateurs.
- L’OSINT : un attaquant peut croiser ton email avec une fuite pour obtenir d’autres infos (numéro de téléphone, anciens mots de passe pouvant révéler des motifs).
- Le *doxxing* : agrégation pour produire un dossier ciblé.

### 4.11 Méthode d’audit personnel en 10 étapes

À faire une première fois sérieusement, puis à répéter tous les six mois.

1. **Lister ses comptes** : recherche dans email principal des termes “welcome”, “verify your email”, “confirm”. Compléter avec le gestionnaire de mots de passe.
1. **Tester son email principal sur HaveIBeenPwned** : noter les fuites confirmées.
1. **Audit des permissions mobiles** : sur iOS Réglages → Confidentialité ; sur Android Paramètres → Confidentialité → Gestionnaire d’autorisations.
1. **Recherche de son nom et email** sur les moteurs (Google, Bing, DuckDuckGo) — sans être connecté, sur navigateur privé.
1. **Reverse image search** sur ses photos publiques (Yandex Images, PimEyes, Google Lens).
1. **Audit des réseaux sociaux** : qui peut voir quoi, qui sont mes amis, qu’ai-je publié au cours de la dernière année, mes photos sont-elles taguées ?
1. **Audit des sessions actives** sur Google, Apple, Microsoft, Facebook : appareils connectés, dernière activité, sessions à révoquer.
1. **Audit du gestionnaire de mots de passe** : mots de passe réutilisés, mots de passe faibles, comptes sans MFA.
1. **Audit cloud** : que synchronise mon téléphone ? Mon ordinateur ? Ai-je activé ADP (Apple) ou équivalent ?
1. **Recherche de soi sur data brokers** : Spokeo, BeenVerified, Whitepages, Pages Jaunes (FR), Société.com.

À l’issue de cet audit, tu auras une carte. Le reste du cours t’apprendra à la réduire.

### 4.12 *Fil rouge* — Audit complet de Léa

Léa fait l’exercice. Ses résultats, en synthèse :

**Top 20 des fuites identifiées** :

1. Email professionnel dans 7 fuites HaveIBeenPwned (dont LinkedIn 2021 et Adobe 2013).
1. Numéro de téléphone trouvable sur LinkedIn (paramètre par défaut).
1. Adresse postale visible via une ancienne souscription à une association (avant RGPD).
1. Date d’anniversaire publique sur Facebook (paramètre par défaut).
1. Nom de jeune fille de sa mère trouvable via un faire-part de mariage scanné en ligne.
1. Photos d’enfance avec géolocalisation EXIF intacte sur Flickr (compte oublié de 2010).
1. Adresse email principale utilisée pour 200+ services (centre de gravité absolu).
1. Aucun MFA sur Gmail (récupération par SMS uniquement).
1. iCloud sans ADP activée.
1. WhatsApp synchronisé dans iCloud, sauvegardes non chiffrées par défaut.
1. Carnet d’adresses iCloud → contient les numéros de plusieurs sources potentielles.
1. Compte Twitter/X avec géotag occasionnel activé.
1. Account-pivoted via PimEyes : photos professionnelles publiques permettent reverse image vers comptes personnels.
1. Identifiants publicitaires actifs sur téléphone (IDFA + Android ID secondaire).
1. Réutilisation d’un même pseudo « LeaM » sur trois forums professionnels, dont un lié à son identité civile.
1. Présence Strava active avec parcours de course incluant son domicile et son bureau.
1. GitHub avec son nom civil et email pro, contributions horodatées révélant son rythme de travail.
1. Mailing-list professionnelle archivée publiquement avec ses anciennes adresses.
1. Photos taguées par son frère sur Instagram révèlent vacances, famille, lieux fréquentés.
1. Adresse postale et téléphone fixe dans le registre du commerce belge (entreprise individuelle).

**Décision** : avant tout outil de chiffrement, Léa décide de consacrer deux week-ends à réduire cette empreinte. Le reste du cours l’accompagne dans cette démarche.

> 🟩 **À retenir du chapitre 4**
> 
> - L’empreinte numérique a trois dimensions : volontaire, involontaire, héritée.
> - Neuf vecteurs d’exposition à auditer systématiquement.
> - L’audit personnel en 10 étapes est le préalable à toute action de durcissement.
> - L’email principal est le centre de gravité : sa protection prime sur tout.
> - Beaucoup de gens découvrent à l’audit que leurs « gros risques perçus » sont moins critiques que des fuites banales déjà acquises.

-----
