---
title: PARTIE V — ÉTUDES DE CAS ET OPÉRATIONS DOCUMENTÉES
source: Cyber/01_CTI/20260405_L2I_Contre-Ingerence.md
note: Contre-ingérence (L2I)
chapter: 5
chapters: 7
---

---

## Chapitre 23 — IRA/GRU 2016 : l'opération fondatrice

### 23.1 Chronologie

L'Internet Research Agency (IRA) est créée à Saint-Pétersbourg en 2013, financée par Evgueni Prigozhin via la société Concord. L'opération américaine commence dès 2014-2015 avec la phase de reconnaissance (envoi d'employés aux États-Unis pour étudier le paysage politique et social), puis s'intensifie en 2015-2016 avec le déploiement de centaines de comptes sur Facebook, Instagram, Twitter et YouTube. Parallèlement, le GRU (via APT28/Fancy Bear et APT29/Cozy Bear) compromet les systèmes du DNC et de John Podesta à partir de mars 2016, et organise la publication des emails exfiltrés via DCLeaks (juin 2016), Guccifer 2.0 (juin 2016) et WikiLeaks (juillet et octobre 2016).

### 23.2 Le volet IRA

Le volet IRA est remarquable par sa compréhension granulaire des fractures sociales américaines. Les opérateurs ont créé des personnages et des groupes ciblant spécifiquement les communautés afro-américaines (page « Blacktivist » sur Facebook avec 11 millions de portée), les communautés latino-américaines, les chrétiens évangéliques, les groupes pro-armes, les mouvements pro-LGBTQ+ (pour polariser), et les vétérans militaires. L'IRA a même organisé des manifestations réelles aux États-Unis via des personnages fictifs — des citoyens américains ont participé à des rassemblements physiques organisés depuis Saint-Pétersbourg.

Les publicités ciblées sur Facebook (plus de 3 500 publicités identifiées par le Comité sénatorial) exploitaient le micro-targeting par intérêts, localisation et données démographiques. Le budget total de l'opération — environ 1,25 million de dollars par mois — était dérisoire au regard de l'impact.

### 23.3 Le volet GRU

Le volet GRU illustre la coordination espionnage/influence. L'unité 26165 du GRU (APT28) a compromis les réseaux du DNC et l'email de John Podesta par phishing. L'unité 74455 a géré la publication via DCLeaks et Guccifer 2.0. La coordination avec WikiLeaks (dont le rôle exact fait l'objet de débats) a assuré la couverture médiatique mondiale des fuites.

### 23.4 Leçons opérationnelles

L'opération 2016 a révélé : la vulnérabilité des plateformes au CIB à grande échelle, l'efficacité du ciblage émotionnel et identitaire, la puissance du hack-and-leak en période électorale, la difficulté d'attribution en temps réel, et les limites de la réponse institutionnelle (l'administration Obama a hésité à attribuer publiquement avant l'élection par crainte de paraître partisan). Les réponses apportées — sanctions, indictments du DOJ, renforcement de la cybersécurité électorale — n'ont pas empêché la continuation des opérations sous d'autres formes.

---

## Chapitre 24 — Doppelgänger/RRN, Storm-1516 et les opérations post-2022

### 24.1 L'opération Doppelgänger/RRN

L'opération Doppelgänger est un mode opératoire qui consiste à créer des clones quasi identiques de sites médiatiques réputés (Le Monde, Der Spiegel, The Guardian, Bild) avec des articles modifiés pour injecter des narratifs pro-russes. Les faux articles sont ensuite amplifiés via des publicités ciblées sur les réseaux sociaux, dirigeant les utilisateurs vers les clones. Le réseau RRN (*Recent Reliable News*) constitue l'infrastructure de sites de « réinformation » associée à cette opération.

L'industrialisation du modèle est remarquable : des centaines de domaines enregistrés, des dizaines de faux sites, une production de contenu multilingue à grande échelle, et une amplification coordonnée via des publicités payantes. L'opération a fait l'objet de multiples expositions et démantèlements, mais la reconstitution est systématique — les opérateurs remplacent les domaines supprimés en quelques jours.

### 24.2 Storm-1516 : le MOI russe le plus sophistiqué

Storm-1516 (aussi connu sous le nom Neva Flood depuis mars 2025) est l'un des modes opératoires informationnels les plus complets et les plus sophistiqués documentés à ce jour. Le rapport technique VIGINUM de mai 2025 documente 77 opérations informationnelles entre août 2023 et mars 2025. Le MOI se caractérise par une chaîne de diffusion en quatre phases (planification → primo-diffusion → blanchiment → amplification), l'utilisation de deepfakes vidéo et audio, un réseau de faux sites (CopyCop) opéré par John Mark Dougan, et l'imbrication avec d'autres MOI (Lakhta, Portal Kombat, Mriya).

L'implication d'acteurs liés au gouvernement russe est documentée : John Mark Dougan (ancien policier américain exilé en Russie, sanctionné par l'UE), le Centre d'expertise géopolitique (CEG, think tank moscovite), Youry Khorochenky (potentiel officier de l'unité 29155 du GRU), et des organisations de la galaxie Prigozhin (FCI, BJA).

### 24.3 African Initiative et les opérations en Afrique

Le rapport technique conjoint VIGINUM/FCDO/EEAS de juin 2025 documente African Initiative, une agence de presse russe créée en septembre 2023, devenue le principal vecteur de la stratégie d'influence informationnelle russe en Afrique post-Prigozhin. La structure est « bicéphale » : une agence de presse basée à Moscou qui diffuse de la propagande pro-russe et anti-occidentale en plusieurs langues, et un réseau associatif sur le continent africain qui recrute des influenceurs, journalistes et militants locaux pour relayer les narratifs.

African Initiative illustre la professionnalisation de l'influence : diplomatie publique de façade, production documentaire, jeux vidéo de propagande, partenariat avec les Maisons russes (Rossotroudnitchestvo), et articulation avec le Corps africain. Ses dirigeants sont suspectés d'être liés aux services de renseignement russes.

### 24.4 Leçons pour la détection 2025-2026

L'évolution des MOI russes montre une adaptation constante des TTPs : utilisation croissante de services d'anonymisation, amélioration de la sécurité opérationnelle, recours à l'IA pour la production de contenu, diversification des plateformes et des langues, imbrication entre MOI pour fragmenter l'attribution. La détection doit suivre cette évolution — les indicateurs qui fonctionnaient en 2020 ne sont plus suffisants en 2026.

---

## Chapitre 25 — Campagnes chinoises, iraniennes et autres

### 25.1 Opérations chinoises

Les opérations chinoises documentées se caractérisent par un volume massif mais une sophistication souvent limitée. **Spamouflage/Dragonbridge** est le MOI chinois le plus documenté — des milliers de comptes coordonnés diffusant des narratifs pro-Chine et anti-occidentaux avec un faible engagement organique. Le Canada a documenté une campagne Spamouflage ciblant des parlementaires canadiens avec des deepfakes vidéo.

La stratégie chinoise se distingue par l'articulation entre influence ouverte (CGTN, Xinhua, partenariats médiatiques) et opérations clandestines. L'opération PAPERWALL, documentée par EU DisinfoLab, illustre un modèle de création de faux médias locaux imitant des portails d'information régionaux. Le 4e rapport EEAS note une montée en compétences et un recours croissant à l'IA, avec 6 % des incidents FIMI attribués à la Chine.

### 25.2 Opérations iraniennes

Les opérations iraniennes ciblent principalement les audiences régionales et les diasporas. Les MOI iraniens documentés incluent des réseaux de faux comptes sur les réseaux sociaux, la création de faux médias en anglais, et des opérations de hack-and-leak ciblées. L'Iran a également été impliqué dans des tentatives d'ingérence dans l'élection américaine de 2024, avec des opérations de hack-and-leak ciblant la campagne Trump.

### 25.3 Opérations privées et commerciales

L'affaire Team Jorge a révélé l'existence d'un marché structuré de l'influence électorale. Le système « AIMS » (Advanced Impact Media Solutions) de Tal Hanan proposait des services complets : gestion de faux comptes, manipulation de sondages en ligne, piratage ciblé, production de contenus. L'entreprise affirmait avoir ciblé des processus électoraux dans plus de 30 pays.

### 25.4 Analyse comparative

Chaque acteur a un « style » opérationnel identifiable qui facilite l'attribution comparative. La Russie privilégie la sophistication opérationnelle, le hack-and-leak, les deepfakes, et la coordination entre MOI. La Chine privilégie le volume, la présence médiatique ouverte, et le ciblage des diasporas. L'Iran combine des opérations limitées mais ciblées avec des capacités cyber significatives. Les acteurs privés offrent des services sur mesure avec une capacité d'adaptation rapide.

---

## Chapitre 26 — Opérations d'influence en France : cas documentés

### 26.1 Macron Leaks 2017

Chronologie : compromission des systèmes de la campagne En Marche (attribuée au GRU/APT28), publication de 20 000 emails et documents le 5 mai 2017 (48h avant le second tour), mélange de documents authentiques et de documents suspects de falsification. La réponse a été rapide : communiqué de la campagne alertant sur le caractère potentiellement frauduleux du corpus, période de réserve limitant la couverture médiatique, mobilisation des autorités. Les leçons : la préparation (la campagne avait anticipé le risque de hack-and-leak), le timing (la période de réserve a été un facteur de protection, involontairement), et la communication rapide.

### 26.2 Opérations documentées par VIGINUM

VIGINUM publie régulièrement des rapports techniques documentant des opérations spécifiques. Les publications 2024-2026 incluent les rapports sur Storm-1516, sur les opérations informationnelles russes ciblant les JOP 2024 (menaces terroristes fabriquées), sur les manœuvres informationnelles liées à la Nouvelle-Calédonie (Baku Initiative Group), et le rapport conjoint sur African Initiative.

### 26.3 Ingérence dans les outre-mer

La Nouvelle-Calédonie a fait l'objet d'opérations d'influence documentées en 2024, avec l'implication du Baku Initiative Group (Azerbaïdjan) dans l'amplification de narratifs anti-français. Mayotte a également été ciblée. Ces territoires présentent des vulnérabilités informationnelles spécifiques : éloignement géographique, fragilités sociales, paysage médiatique limité.

> **🔵 BROUILLARD — Épisode 8**
> L'analyse forensique du deepfake audio est achevée. L'expert externe confirme une synthèse : des artefacts spectraux caractéristiques sont identifiés aux transitions entre segments de l'enregistrement, compatibles avec un assemblage de segments synthétiques. Cependant, le résultat du détecteur automatique reste « incertain » — il est documenté comme tel. Le rapport final d'Élise identifie l'opération comme cohérente avec les TTPs d'un acteur documenté (le MOI identifié partage des caractéristiques d'infrastructure, de timing et de narrative avec un acteur suivi par l'EEAS et des partenaires européens). L'attribution technique est posée en confiance modérée. L'attribution stratégique — qui a commandité ? — reste en confiance faible : les éléments convergent vers un acteur étatique mais le lien de commandement n'est pas démontré. La distinction fait/hypothèse/piste est rigoureusement documentée dans le rapport.

---
