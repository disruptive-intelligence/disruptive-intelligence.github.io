---
title: Chapitre 7 — Entités organisationnelles
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie II — Les entités de L'écosystème
  - index.md
---

## 7.1 Groupes cybercriminels et marques

L'un des pièges conceptuels les plus fréquents est de confondre le « groupe » avec la « marque ». Dans l'écosystème ransomware, la marque (LockBit, BlackCat, Conti, PhantomCrypt dans notre fil rouge) est un nom commercial — l'équivalent d'une franchise. Derrière la marque, il faut distinguer quatre niveaux d'acteurs.

L'**opérateur** (ou core team) est le noyau qui contrôle le code source du ransomware, maintient l'infrastructure (builder, panel, leak site, serveurs de négociation), fixe les règles du programme d'affiliation, et capte une commission sur chaque rançon payée (typiquement 20 à 30 %). L'opérateur est souvent un petit groupe de 5 à 15 personnes — développeurs, administrateurs système, et gestionnaires. C'est l'entité la plus critique de l'écosystème : si l'opérateur est compromis, tout le réseau d'affiliés est impacté.

Les **affiliés** sont les utilisateurs du service. Ils reçoivent le builder (l'outil qui génère des variants personnalisées du ransomware), accèdent au panel (l'interface de contrôle des victimes), et mènent les opérations d'attaque de manière autonome. Un opérateur RaaS peut avoir des dizaines d'affiliés actifs simultanément. Chaque affilié gère ses propres cibles, ses propres méthodes de compromission, et ses propres négociations. Cette autonomie signifie que deux attaques sous la même marque peuvent avoir des profils très différents.

Les **prestataires** sont les acteurs externes qui fournissent des services à l'écosystème sans en être formellement membres : les IAB qui vendent les accès initiaux, les fournisseurs de crypters qui rendent le malware indétectable, les hébergeurs bulletproof, les services de mixing, et les négociateurs spécialisés. Ces prestataires servent souvent plusieurs marques simultanément.

Les **anciens affiliés et successeurs** constituent la mémoire et la continuité. Quand une marque est disrupted (comme Conti après les leaks de 2022, ou ALPHV/BlackCat après l'action du FBI en décembre 2023), les affiliés ne disparaissent pas — ils migrent vers d'autres plateformes. Les développeurs et opérateurs peuvent rebrandir sous un nouveau nom. La communauté CTI suit ces migrations en analysant les TTP, le code, et les infrastructure partagées.

## 7.2 Sociétés écrans et structures de façade

De nombreux écosystèmes cybercriminels utilisent des structures juridiques légales comme couverture. Ces sociétés écrans peuvent servir à enregistrer des domaines et louer de l'hébergement sans attirer l'attention, à ouvrir des comptes bancaires pour le blanchiment, à fournir une couverture d'emploi pour les participants (le développeur d'un ransomware peut être officiellement « consultant IT » dans une société écran), et à faciliter les transactions financières internationales.

L'identification des sociétés écrans passe par la consultation des registres d'entreprises (en France : Infogreffe, Societe.com, Pappers ; à l'international : OpenCorporates, CompanyHouse UK, registres locaux), le cross-référencement des dirigeants (un même individu qui apparaît comme directeur de 15 sociétés dans 5 juridictions est suspect), l'analyse des flux financiers (des sociétés sans activité économique visible mais avec des flux bancaires importants), et la vérification de la substance (la société a-t-elle des employés, des locaux, une activité réelle ?).

Les juridictions privilégiées pour les sociétés écrans liées au cybercrime incluent les Émirats Arabes Unis (Dubaï en particulier, avec des sociétés en free zone), les îles Vierges Britanniques, les Seychelles, la Géorgie, et certains pays baltes. Le choix de la juridiction dépend du service recherché : Dubaï pour le cash-out crypto et l'immobilier, les BVI pour l'opacité juridique, les pays baltes pour les licences de services financiers.

## 7.3 Communautés et collectifs

Tous les regroupements d'acteurs ne sont pas des organisations formelles. De nombreux écosystèmes gravitent autour de communautés informelles — forums spécialisés, canaux Telegram, serveurs Discord — qui fonctionnent comme des écosystèmes sociaux sans hiérarchie formelle.

Ces communautés se caractérisent par une hiérarchie informelle (les membres les plus anciens, les plus actifs, ou les plus compétents ont plus d'influence sans titre officiel), des codes d'entrée (certains canaux Telegram exigent un vouching, un paiement, ou une preuve de compétence technique), des normes comportementales (les forums russophones ont des règles non écrites strictes : ne pas cibler la Russie, ne pas arnaquer les autres membres, ne pas coopérer avec les forces de l'ordre), et des mécanismes de sanction informels (bannissement, exposition publique, blacklisting).

L'analyste doit éviter de traiter une communauté comme une organisation. Tous les membres d'un forum ne coopèrent pas entre eux. Deux personnes actives sur le même canal Telegram ne sont pas nécessairement complices. La communauté est un espace social dans lequel des transactions et des coopérations se forment, mais le fait d'y participer ne constitue pas en soi un lien opérationnel.

## 7.4 Franchises et affiliations — le modèle RaaS comme archétype

Le Ransomware-as-a-Service est le modèle organisationnel le plus important de la cybercriminalité contemporaine, et il se réplique dans d'autres domaines.

Le mécanisme est le suivant : un opérateur central développe le ransomware, fournit le builder (outil de génération de variants), met en place un panel de contrôle (interface web sécurisée pour gérer les victimes, suivre les paiements, accéder aux outils de négociation), opère un leak site (pour la double extorsion), et recrute des affiliés. Les affiliés paient un dépôt initial (typiquement quelques centaines de dollars pour les plateformes entrantes, plus pour les plateformes premium — LockBit 5.0 demande environ 500$ en Bitcoin) et s'engagent à verser un pourcentage de chaque rançon payée (typiquement 20 à 30 % pour l'opérateur). L'affilié gère autonomement la compromission, le déploiement, et la négociation.

Ce modèle se réplique dans le Phishing-as-a-Service (kits de phishing pré-construits avec panels de récupération de credentials, vendus par abonnement mensuel), le Malware-as-a-Service (infostealers comme Lumma, vendus entre 250 et 20 000$ selon le tier — voir Ch.16), le DDoS-for-hire (plateformes de stress testing/booter qui sont en réalité des services de DDoS à la demande), et les botnets en location.

## 7.5 Fil rouge — NEXUS : l'écosystème organisationnel se dessine

> **🔍 NEXUS — Épisode 7**
>
> Sur le canal Telegram identifié, kr0n0s_ops interagit avec deux autres pseudos de manière régulière.
>
> Le premier, `ghost_access`, publie des annonces de vente d'accès réseau : « FR energy company, domain admin, $12,000 ». Le format est standardisé : pays, secteur, niveau d'accès, prix. C'est un IAB (Initial Access Broker).
>
> Le second, `nego_phantom`, gère les négociations avec les victimes pour le compte de la plateforme PhantomCrypt. Il partage des captures d'écran de « chats clients » montrant des échanges avec des victimes paniquées. C'est un service de négociation externalisé.
>
> Samira met à jour le graphe : trois entités organisationnelles distinctes apparaissent — l'affilié (kr0n0s_ops), l'IAB (ghost_access), et le service de négociation (nego_phantom), tous gravitant autour de la plateforme PhantomCrypt (l'opérateur RaaS). Le modèle franchisé se confirme.

---
