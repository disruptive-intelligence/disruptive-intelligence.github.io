---
title: PARTIE VII — TYPOLOGIES DE CRIMINALITÉ FINANCIÈRE
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
chapter: 8
chapters: 11
---

*Neuf chapitres pour comprendre, sous l’angle défensif et investigatoire, les principaux schémas de criminalité financière modernes. L’objectif est la détection, l’analyse et la coopération, jamais le mode d’emploi pour commettre.*

-----

## Chapitre 40 — Blanchiment : placement, empilement, intégration

### Objectif du chapitre

Maîtriser le **cadre conceptuel** du blanchiment de capitaux : trois phases (placement, empilement, intégration), typologies courantes, signaux de détection. C’est la matrice de référence pour la majorité des dossiers FININT.

### Le concept

Le **blanchiment de capitaux** est l’opération par laquelle une personne dissimule l’origine illicite de fonds pour les introduire dans l’économie légale.

Le modèle classique en **trois phases** (popularisé par le GAFI dans les années 1990, encore utile pédagogiquement même s’il simplifie la réalité) :

**1. Placement.** Introduire les fonds illicites dans le système financier. Mécanismes : dépôts en espèces (souvent fractionnés sous les seuils — *structuration* ou *smurfing*), achats en cash de biens revendables, conversions en cryptos, infiltration dans des activités à forte composante cash (restauration, hôtellerie, salons de coiffure, lavages auto, bars-tabacs). C’est la phase la plus risquée pour le blanchisseur car la plus visible.

**2. Empilement (layering).** Multiplier les opérations et les juridictions pour brouiller la traçabilité. Mécanismes : virements multiples entre sociétés écrans, conversions de devises, allers-retours bancaires, fragmentation par plusieurs PSP, layering crypto via mixers ou bridges, transit par des juridictions à secret bancaire. Le but : créer une distance entre l’origine et la destination.

**3. Intégration.** Réinjecter les fonds blanchis dans l’économie légale sous une forme apparemment légitime : achat immobilier, acquisition d’entreprises, investissements dans des actifs financiers, achats de luxe.

### Évolution moderne du modèle

Le modèle trois phases simplifie la réalité 2020+. Les schémas modernes :

- **Combinent rapidement** placement et layering (BEC + fintechs + crypto en quelques heures).
- **Intègrent la crypto** comme rail de placement et de layering (renvoi OSINT Crypto).
- **S’appuient sur des structures juridiques** (sociétés écrans, trusts) plus que sur les espèces.
- **Exploitent les jeux d’argent en ligne** comme couche.
- **Utilisent les marchés de l’art, des NFT, des cartes de collection** comme moyens d’intégration.

### L’utilité opérationnelle

L’analyste cherche à :

- **Identifier la phase** dans laquelle se situe une opération observée.
- **Reconstituer la chaîne** : retrouver le placement initial à partir des indices de layering ou d’intégration.
- **Qualifier l’infraction prédécesseur** (qu’est-ce qui a généré les fonds : trafic, fraude, corruption ?).

### Méthode — signaux par phase

**Placement** : dépôts d’espèces fréquents et fractionnés, activité incohérente avec le compte, achats en cash de biens revendables, onboarding rapide sur PSP/EME avec activité immédiate inhabituelle.

**Layering** : cascades de virements en cycle court, multiplication des juridictions sans rationale, conversions multiples de devises, transferts en cascade entre fintechs, sorties crypto avec mixers ou bridges.

**Intégration** : acquisitions immobilières disproportionnées, investissements dans des sociétés sans expérience préalable, acquisitions d’œuvres d’art à prix élevés, importations de biens de luxe, donations à des organismes avec retours indirects.

### Mini-walkthrough — schéma observable

Un trafiquant accumule 1 M€ en espèces. **Placement** : dépôts par 10-50 mules de 5-9 K€ chacun en plusieurs agences. **Layering** : virements vers une SAS écran, puis société émirate, conversion USDT, transferts entre exchanges, reconversion en EUR sur fintech. **Intégration** : achat d’un appartement à Paris via SCI.

L’analyste qui intervient à un point quelconque doit reconstituer en amont et en aval pour identifier infraction prédécesseur et bénéficiaire final.

### Erreurs fréquentes

- **Considérer toute opération inhabituelle comme blanchiment.** Beaucoup ont des explications légitimes.
- **Ignorer la phase d’intégration** : c’est souvent la plus visible et la plus exploitable judiciairement.
- **Sous-estimer le rôle des assujettis non bancaires** : notaires, avocats, marchands d’art, agents immobiliers, casinos.

### Limites

La qualification *« blanchiment »* est une qualification juridique qui exige une **infraction prédécesseur** établie. En FININT, on parle de **schéma compatible avec un blanchiment** et l’on transmet à l’autorité compétente.

### Lien avec le fil rouge

> **CLEARFLOW — Phases observables**
> 
> Dans le dossier Haddad, les phases sont mélangées. Le **placement** apparaît marginal (peu de cash visible). Le **layering** est central (transit multi-juridictionnel via sociétés écrans). L’**intégration** apparaît dans les acquisitions immobilières françaises et présumées étrangères. L’infraction prédécesseur n’est pas clairement établie ; les hypothèses retenues : corruption autour des marchés ouest-africains (probable), évasion fiscale et fraudes diverses (possible).

### Points clés à retenir

- Modèle GAFI : placement → layering → intégration.
- Évolution moderne : phases mélangées, accélérées, intégrant crypto.
- L’analyste identifie la phase et reconstitue en amont/aval.
- Qualification juridique de blanchiment exige l’infraction prédécesseur.

-----

## Chapitre 41 — Trade-Based Money Laundering (TBML)

### Objectif du chapitre

Comprendre le **blanchiment par le commerce international (TBML)** — l’une des typologies les plus utilisées et les plus difficiles à détecter, car elle s’appuie sur des flux commerciaux qui paraissent légitimes.

### Le concept

Le **TBML** est le blanchiment via des opérations commerciales internationales : import-export, achats-ventes de marchandises, prestations de service. La dissimulation passe par le **décalage entre valeur déclarée et valeur réelle** de la marchandise, ou par la **fictivité totale** de l’opération.

### Mécanismes courants

**Sur-facturation** : la marchandise est vendue à un prix supérieur à sa valeur réelle. Le payeur transfère ainsi un montant supérieur, l’excédent étant un canal de valeur déguisé.

**Sous-facturation** : la marchandise est vendue à un prix inférieur. Permet de minimiser les droits de douane à l’import, ou de transférer de la valeur via revente à valeur réelle.

**Facturation multiple** : la même marchandise est facturée plusieurs fois à des entités liées.

**Marchandise fictive** : facture sans contrepartie physique.

**Documents falsifiés** : certificats d’origine, bills of lading, CMR, certificats douaniers — donnent une apparence légitime à des flux fictifs.

**Transit par juridictions complaisantes** : la marchandise passe (ou semble passer) par des free zones (Dubai, Singapour) pour brouiller la traçabilité.

**Triangulation** : achat dans un pays A, vente dans un pays C, transit par un pays B intermédiaire — opportunité de surcouches.

### L’utilité opérationnelle

Le TBML est particulièrement difficile à détecter parce qu’il imite des opérations commerciales légitimes. La détection repose sur l’analyse fine de la cohérence économique (chapitre 38).

### Méthode — signaux de TBML

- Marges sur-prix marché significatives.
- Décalages valeur facture / valeur de marché (Eurostat Comext, UN Comtrade, indices sectoriels).
- Contreparties commerciales sans activité réelle vérifiable.
- Pays de transit sans rationale économique.
- Documents douaniers incohérents (ports d’embarquement, dates).
- Paiements en avance disproportionnée par rapport aux pratiques sectorielles.
- Flux financiers déconnectés des flux physiques observables.

### Mini-walkthrough — schéma TBML simplifié

Une société A en France importe « 200 tonnes d’huile de palme » depuis une société B au Bénin, payée 850 K€. La société B est facturée par une société C en Côte d’Ivoire pour 350 K€.

- Si la marchandise existe : marge B = 500 K€ — atypique pour le marché.
- Vérification douanière française : aucune trace d’import enregistré pour A à ces volumes.
- Vérification logistique : aucun transport identifié.

Hypothèse forte : opération **fictive ou sur-facturée**, le flux de 850 K€ ayant une finalité de transfert de valeur déguisée. Probable TBML.

### Erreurs fréquentes

- **Confondre marge atypique et TBML.** Certains secteurs (luxe, technologies de pointe) ont des marges très élevées légitimement.
- **Conclure sans vérification physique** : la vérification douanière (existence du transport) est souvent la clé.
- **Sous-estimer le rôle des free zones** : la traçabilité y est moindre.

### Limites

La détection fine du TBML exige souvent une coopération douanière internationale (OMD, douanes nationales). En CRF, cette coopération est mobilisable mais lente.

### Lien avec le fil rouge

> **CLEARFLOW — TBML hypothèse centrale**
> 
> Dans le dossier Haddad, plusieurs éléments convergent vers une hypothèse TBML *probable* : sur-facturation apparente sur le marché ivoirien (×2), incohérences entre flux financiers et flux physiques pour les imports déclarés français depuis le Bénin, transit Bénin → France sans rationale logistique. La qualification précise exigerait coopération douanière française et ivoirienne, prévue dans les recommandations.

### Points clés à retenir

- TBML = blanchiment via flux commerciaux internationaux.
- Mécanismes : sur/sous-facturation, facturation multiple, marchandise fictive, documents falsifiés.
- Détection : cohérence valeur, contreparties, logistique.
- Coopération douanière internationale souvent nécessaire.

-----

## Chapitre 42 — Corruption, commissions occultes et PEP

### Objectif du chapitre

Comprendre les **schémas de corruption** transnationale : commissions occultes, pots-de-vin, rétrocommissions, et le concept de **PEP** (Personne Politiquement Exposée).

### Le concept

La **corruption** est l’obtention d’un avantage en échange d’un acte illicite par une personne en position de pouvoir. Variantes :

- **Corruption active** (celui qui offre) et **passive** (celui qui reçoit).
- **Corruption nationale** vs **transnationale** (régie par les conventions OCDE 1997, ONU Mérida 2003, loi Sapin II 2016 en France).
- **Trafic d’influence** : intermédiaire facilitant l’obtention d’un avantage.
- **Concussion** : exigence d’une rémunération non due par un agent public.
- **Prise illégale d’intérêts** : cumul d’intérêts privés et de fonctions publiques.
- **Favoritisme** : avantage indu dans la commande publique.

**PEP — Personne Politiquement Exposée.** Catégorie LCB-FT définie par la 4e/5e directive AML. Recouvre :

- Chefs d’État et de gouvernement, ministres, parlementaires.
- Membres de cours suprêmes et cours constitutionnelles.
- Membres de la haute hiérarchie militaire.
- Dirigeants de partis politiques significatifs.
- Dirigeants d’entreprises publiques significatives.
- Dirigeants d’organisations internationales.
- **Membres de la famille proche** (conjoint, parents, enfants, beaux-parents).
- **Collaborateurs étroits connus** (associés, prête-noms).

Le statut PEP ne fait pas du PEP un criminel ; il **déclenche une vigilance renforcée** (KYC renforcé, monitoring spécifique).

### Schémas typiques

- **Rétrocommissions sur marché public** : marché remporté à prix surévalué, partie reversée au décideur ou à un proche, via structure offshore.
- **Cadeaux et invitations** : voyages, séjours, biens — formes plus subtiles.
- **Pacte de corruption** : facture de « conseil » à une société écran contrôlée par le décideur ou un proche.
- **Société de couverture** : le décideur crée une société (par prête-nom) qui « facture » des prestations fictives au fournisseur bénéficiaire.
- **Trust avec bénéficiaires politiquement exposés** : fonds parqués dans un trust dont le PEP ou ses proches sont bénéficiaires.

### L’utilité opérationnelle

L’analyste cherche à :

- **Identifier le PEP** ou son entourage (PEP famille, PEP collaborateur).
- **Repérer les flux atypiques** (entrées depuis fournisseurs publics vers comptes personnels ou de proches).
- **Documenter les liens** entre décideurs et entreprises bénéficiaires.
- **Croiser avec marchés publics** (chapitre 15) et HATVP en France.

### Méthode — signaux de corruption

- Flux entrants depuis fournisseurs de la commande publique vers comptes personnels ou de proches.
- Sociétés de « conseil » dont l’activité réelle est inidentifiable, facturant des entités publiques ou semi-publiques.
- Acquisitions patrimoniales disproportionnées par des proches.
- Train de vie incohérent avec les revenus déclarés.
- Présence du décideur dans HATVP avec déclarations partielles ou contradictoires.

### Mini-walkthrough

Un haut fonctionnaire signe régulièrement des marchés publics avec une PME. Cette PME, par convention, verse 5 % de chaque marché à une « société de conseil » domiciliée à Chypre, dont l’UBO est l’oncle du fonctionnaire.

Lecture FININT : pattern de rétrocommissions probable. Vérification : marchés publics gagnés (BOAMP, DECP), flux PME → société de conseil (réquisition), UBO de la société (registre, leaks), lien familial fonctionnaire-oncle (état civil, presse, SOCMINT). Si tous les éléments se confirment, schéma *quasi-certain*.

### Erreurs fréquentes

- **Considérer toute relation PEP / entreprise comme corruption.** Beaucoup sont parfaitement légales.
- **Surinterpréter une déclaration HATVP partielle.** Peut être omission, pas nécessairement fraude.
- **Diaboliser le statut PEP** : ce n’est pas un soupçon, c’est une exigence de vigilance.

### Limites

La corruption transnationale est notoirement difficile à prouver : témoignages réticents, juridictions étrangères, secret bancaire résiduel. Les dossiers FININT débouchent souvent sur des recommandations à des autorités spécialisées (PNF, OCDE Working Group on Bribery, Interpol).

### Lien avec le fil rouge

> **CLEARFLOW — Volet corruption ivoirien**
> 
> Sur le volet du marché public ivoirien, l’hypothèse de **favoritisme avec corruption** est *possible* à *probable*. Sans coopération ivoirienne, l’établissement précis est *indéterminable*. La note finale recommande au PNF d’engager les coopérations nécessaires.

### Points clés à retenir

- Corruption : variantes nombreuses (active, passive, trafic d’influence, favoritisme).
- PEP : statut déclencheur de vigilance, pas d’accusation.
- Schémas typiques : rétrocommissions, sociétés de couverture, trusts avec bénéficiaires PEP.
- Coopération internationale souvent indispensable.

-----

## Chapitre 43 — Fraude fiscale, carrousel TVA et abus de biens sociaux

### Objectif du chapitre

Comprendre les **principales typologies de fraude fiscale** : fraude TVA (notamment carrousel), évasion fiscale internationale, et l’**abus de biens sociaux** (ABS).

### Le concept

**Fraude fiscale** : ensemble des comportements visant à éluder l’impôt par dissimulation, fausses déclarations, montages fictifs.

**Carrousel TVA** (intracommunautaire). Exploite l’exonération de TVA sur les livraisons intracommunautaires pour générer des crédits de TVA fictifs ou pour ne pas reverser la TVA collectée. Acteurs typiques :

- **Société de défaut** (« missing trader » ou « buffer ») : collecte la TVA des clients mais disparaît avant de la reverser.
- **Société écran intermédiaire** : crée la chaîne d’opérations.
- **Société de récupération** : récupère la TVA déductible.
- **Société de revente** : termine la chaîne.

Le carrousel fait tourner les opérations entre les mêmes acteurs sur de multiples cycles.

**Évasion fiscale internationale** : planification fiscale agressive franchissant la ligne du légal :

- Treaty shopping (utilisation de conventions fiscales hors objet initial).
- Transfert de bénéfices vers juridictions à faible imposition via prix de transfert non conformes.
- Domiciliation fictive dans une juridiction à faible imposition.
- Structures hybrides (mismatch entre qualifications fiscales nationales).
- Trusts et fondations utilisés à des fins de dissimulation fiscale.

**Abus de biens sociaux (ABS)**. Délit français consistant pour le dirigeant à utiliser les biens de la société à des fins personnelles ou pour favoriser une autre société. Mécanismes : prélèvements personnels masqués, factures personnelles payées par la société, voyages perso facturés, biens immobiliers à usage privé.

### L’utilité opérationnelle

L’analyste cherche à :

- **Détecter le pattern** dans les flux (cycles, fragmentation, contreparties croisées).
- **Identifier les rôles** dans le schéma (buffer, intermédiaire, récupérateur).
- **Documenter les flux** entre la société et le dirigeant ou ses proches (ABS).
- **Quantifier le préjudice** (fiscal pour la fraude TVA, social pour l’ABS).

### Méthode — signaux carrousel TVA

- Cycles d’opérations entre les mêmes acteurs.
- Sociétés sans substance économique faisant transit de marchandise.
- Crédits de TVA disproportionnés avec activité réelle.
- Sociétés disparaissant brutalement (radiation, dissolution rapide).
- Secteurs à risque historiquement : téléphonie, électronique grand public, métaux, parfums et cosmétiques, droits d’émission CO₂, énergie renouvelable, services digitaux.

### Méthode — signaux d’évasion fiscale

- Charges de « conseil », « royalties », « management fees » à des entités liées en juridictions à faible imposition, disproportionnées.
- Prêts intragroupe sans intérêts ou à conditions anormales.
- Holding intermédiaire sans substance économique.
- Acquisitions de PI (marques, brevets) cédées à une entité offshore et reconcédées sous redevances.

### Méthode — signaux d’ABS

- Virements de la société vers comptes personnels du dirigeant sans contrepartie évidente.
- Factures de fournisseurs personnels acquittées par la société.
- Biens (véhicules, immobilier) de la société à usage manifestement privé.
- Comptes courants associés gonflés (le dirigeant a « prêté » à la société mais la société est dépendante).

### Mini-walkthrough — schéma fraude TVA simplifié

Trois sociétés A, B, C en cycle. A vend en intracommunautaire à B (exonéré TVA). B vend à C en national (TVA 20 % collectée). B disparaît avec la TVA. C revend à un client A (l’opération revient dans le pays d’origine). Crédit TVA de C illégitime ; perte fiscale = TVA non reversée par B.

Lecture FININT : pattern carrousel TVA classique. Vérification : registres (durée de vie des sociétés), comptes (TVA déclarée vs collectée), flux (cycles), liens entre A/B/C (mêmes UBO ou dirigeants partagés).

### Erreurs fréquentes

- **Confondre optimisation fiscale légale et fraude fiscale.** La frontière est juridique et factuelle.
- **Sous-estimer l’ampleur du carrousel TVA** : c’est l’une des fraudes fiscales les plus massives en UE.
- **Confondre ABS et choix de gestion contestable** : tous les choix discutables d’un dirigeant ne sont pas ABS.

### Limites

La qualification juridique de fraude fiscale et d’ABS appartient au judiciaire et à l’administration fiscale. Le FININT alimente. La coopération avec les services fiscaux nationaux (DGFiP en France) est centrale.

### Lien avec le fil rouge

> **CLEARFLOW — Évasion fiscale et ABS**
> 
> Dans le réseau Haddad, l’évasion fiscale via charges de conseil intragroupe à Chypre est *probable*. L’ABS via prélèvements personnels disproportionnés depuis les comptes des SAS françaises est *probable* à *quasi-certain* (signal récurrent dans les relevés). Pas de signal clair de carrousel TVA. La note finale recommande coopération avec la DGFiP pour qualifier les volets fiscaux.

### Points clés à retenir

- Trois familles : fraude TVA (carrousel), évasion fiscale internationale, ABS.
- Détection : flux, cycles, contreparties, substance économique.
- Coopération DGFiP / autorités fiscales étrangères centrale.
- Qualification juridique : pas du ressort du FININT seul.

-----

## Chapitre 44 — BEC, fraude au fournisseur et réseaux de mules

### Objectif du chapitre

Comprendre les **fraudes au virement** modernes : Business Email Compromise (BEC), fraude au changement d’IBAN, fraude au président, et le rôle des **réseaux de mules** dans le cashout.

### Le concept

**BEC (Business Email Compromise)** : famille d’attaques où un attaquant prend le contrôle (réel ou simulé) d’une adresse email professionnelle pour détourner un paiement. Variantes principales :

- **Fraude au président (CEO fraud)** : un faux email d’un dirigeant demande un virement urgent et confidentiel à un collaborateur des finances.
- **Fraude au changement d’IBAN** : un fournisseur légitime semble écrire à son client pour signaler un changement d’IBAN. Le client paie sur le nouveau RIB — au fraudeur.
- **Fraude au faux client** : un faux client semble passer commande, demande livraison, puis disparaît sans payer (à la marge du BEC, mais souvent traité ensemble).
- **Fraude à l’avocat** : un faux avocat ou notaire demande un virement urgent dans le cadre d’une fausse transaction.
- **Vendor email compromise** : compromission réelle de la boîte email d’un fournisseur, exploitée pour rediriger les paiements.

**Réseau de mules.** Les fonds détournés transitent par des comptes de personnes physiques (mules) avant cashout. Les mules sont :

- **Recrutées** via fausses offres d’emploi (« assistant financier », « agent de transfert »), réseaux sociaux, applications de rencontre, sites de petites annonces.
- **Volontaires** (rémunérées) ou **involontaires** (manipulées par phishing ou romance scam).
- **Utilisées** pour recevoir un virement frauduleux, retirer en cash ou retransférer vers le réseau, en quelques heures.

### L’utilité opérationnelle

Le BEC est un volet majeur de la fraude moderne. Pour la victime (PME, ETI, grand groupe), les pertes sont fréquemment de 50 K€ à plusieurs millions. La récupération dépend de la rapidité du gel — typiquement quelques heures.

### Méthode — détection et réponse

**En prévention** (au-delà du périmètre FININT pur) : double signature obligatoire pour les virements significatifs, validation par téléphone d’un changement d’IBAN, formation des équipes finances, vérifications techniques (SPF, DKIM, DMARC sur les emails).

**En détection** :

- Virement vers IBAN nouveau, montant inhabituel, libellé urgent.
- Demandes en dehors des heures ouvrées.
- Discrépance entre nom du bénéficiaire affiché et titulaire réel du compte (la **Verification of Payee** — VOP — devient progressivement obligatoire dans l’UE avec le règlement sur les paiements instantanés ; pour les PSP de la zone euro, l’échéance opérationnelle majeure est **octobre 2025** ; pour les PSP hors zone euro, **juillet 2027**. Au moment où l’analyste travaille, le déploiement effectif varie selon les PSP).
- Activité immédiate de fractionnement et de cashout sur le compte bénéficiaire.

**En réaction** (essentielle, urgente) :

- **Contact immédiat** avec la banque émettrice pour gel (fenêtre quasi-nulle en SCT Inst).
- **Plainte** auprès des autorités (en France : Plate-forme PHAROS, plainte en ligne, ou commissariat).
- **Coopération internationale** via CRF (signalement urgent à TRACFIN qui peut activer FIU.NET pour les comptes destinataires européens).
- **Volet crypto** si conversion crypto : renvoi vers OSINT Crypto pour le traçage on-chain.

### Mini-walkthrough

Une PME française reçoit, le mardi 14h32, un email semblant venir de son fournisseur habituel, demandant le paiement d’une facture sur un nouvel IBAN espagnol. Le directeur financier paie 215 K€ via SCT Inst.

À 14h35-14h41 : le compte espagnol fractionne en 5 virements vers PT et LT.
À 16h12 : conversion USDT sur exchange.
À 18h45 : sortie vers wallet auto-géré.

La PME découvre la fraude le mercredi matin (le vrai fournisseur appelle pour réclamer le paiement). Délai : 18+ heures. Fenêtre de gel : pratiquement fermée pour la portion crypto. Pour les comptes PT et LT, gel possible si rapidité d’action de la CRF.

Bilan typique : récupération de 20 à 40 % du montant si action rapide ; recouvrement total très rare.

### Erreurs fréquentes

- **Sous-estimer la vitesse.** Les fraudeurs exploitent la non-réversibilité de SCT Inst.
- **Croire que la victime est forcément négligente.** Beaucoup de BEC sont sophistiqués (compromission réelle d’email, manipulation contextuelle).
- **Ignorer le réseau de mules** : sans elles, le cashout est plus difficile. Identifier la mule peut conduire au recruteur.

### Limites

Le BEC est rapide ; la coopération internationale est plus lente. La récupération totale est rare. Le travail FININT vise souvent à **identifier le réseau** (mules, recruteurs, organisateurs) pour démanteler, plus qu’à récupérer les fonds.

### Lien avec le fil rouge

> **CLEARFLOW — Branche BEC limitée**
> 
> Une des entrées du dossier Haddad inclut un BEC : 215 K€ détournés d’une PME française vers le compte d’une SAS du réseau Haddad. La piste mule semble présente — la SAS pouvait être utilisée comme étape de layering pour des fonds frauduleux d’origine externe au réseau lui-même. Cette branche est secondaire dans le dossier mais documente que le réseau a pu fonctionner comme **infrastructure de service** pour des fraudes externes.

### Points clés à retenir

- BEC = famille de fraudes au virement par compromission ou simulation d’email.
- SCT Inst rend le gel quasi impossible.
- Réseaux de mules : volontaires ou involontaires, recrutées en ligne.
- Réaction : rapidité critique, coopération CRF, renvoi crypto si pertinent.

-----

## Chapitre 45 — Contournement de sanctions et biens dual-use

### Objectif du chapitre

Comprendre les **mécanismes de contournement de sanctions économiques** — sujet devenu central depuis 2022 — et les enjeux liés aux **biens à double usage** (dual-use).

### Le concept

Les **sanctions économiques** sont des mesures restrictives imposées par des États ou organisations internationales contre des personnes, entités ou pays. Trois sources principales :

- **ONU** : sanctions de l’ONU, contraignantes pour tous les États membres.
- **UE** : sanctions UE consolidées, contraignantes pour tous les opérateurs UE et leurs filiales.
- **US** : sanctions OFAC, avec portée extraterritoriale forte (sanctions secondaires impactant les opérateurs non-US qui font affaire avec les personnes sanctionnées).
- **UK** : sanctions OFSI.
- **Sanctions nationales** spécifiques (France via la DGT).

**Catégories** :

- **Sanctions ciblées** (PEP, dirigeants, entités spécifiques) : gel d’avoirs, interdiction de transactions.
- **Sanctions sectorielles** (banques, énergie, défense, etc.).
- **Embargos** : interdictions générales de commerce avec un pays.
- **Restrictions à l’exportation** de biens (dual-use, militaires, technologiques).

**Contournement** : techniques utilisées pour échapper aux sanctions.

### Mécanismes de contournement courants

- **Front companies** : société tierce non sanctionnée agit pour le compte d’une entité sanctionnée.
- **Sociétés écrans dans pays tiers** : Émirats, Turquie, Asie centrale, Caucase — par où transitent des flux et marchandises vers et depuis les juridictions sanctionnées.
- **Triangulation commerciale** : achat dans pays A, vente apparente vers pays B (non sanctionné), revente effective vers pays C (sanctionné).
- **Re-pavillonnement** : navires (notamment pétroliers), aéronefs sous pavillon de complaisance pour masquer l’identité réelle.
- **Falsification de documents** : certificats d’origine, bills of lading, documents douaniers.
- **Crypto** : utilisation de stablecoins pour les paiements (renvoi OSINT Crypto pour le détail on-chain).
- **Mixers et bridges** crypto pour brouiller la traçabilité.
- **AIS spoofing** ou éteignage : navires éteignent leur transpondeur AIS pour masquer leur trajectoire.

### Biens dual-use

Biens à **double usage** civil et militaire (semi-conducteurs avancés, capteurs, lasers, équipements de cryptographie, certains logiciels, drones, équipements industriels lourds). Régulation UE par le règlement 2021/821. Listes mises à jour régulièrement.

Détection FININT : flux financiers vers fournisseurs de biens dual-use, contreparties dans des juridictions à risque, schémas de triangulation, sous-traitance suspecte.

### L’utilité opérationnelle

Depuis 2022 (sanctions Russie), le contournement est un domaine en croissance forte. Les CRF dédient des ressources spécifiques. Les banques renforcent leur screening (filtres OFAC et UE).

### Méthode — signaux de contournement

- Flux soudains et significatifs vers une juridiction tierce (Émirats, Turquie, Géorgie, Arménie, Asie centrale).
- Sociétés intermédiaires récemment créées en juridictions tierces.
- Bénéficiaires effectifs liés à des entités sanctionnées (recherche dans OFAC SDN, UE consolidated list).
- Activités d’import-export de biens dual-use ou de technologies sensibles.
- Schémas de triangulation incohérents économiquement.
- AIS spoofing repérable via plateformes de tracking maritime.

### Mini-walkthrough — schéma simplifié

Une société turque récemment créée commence à recevoir des virements significatifs d’Europe pour « consulting services » et à envoyer des marchandises (semi-conducteurs) vers la Russie. L’UBO de la société turque est lié à une personne précédemment associée à une entreprise russe sanctionnée.

Lecture FININT : *probable* contournement de sanctions UE/US. Signalement et coopération sont prioritaires (CRF turque, sanctions UE et US, services nationaux dédiés).

### Erreurs fréquentes

- **Considérer toute opération avec un pays tiers comme contournement.** La grande majorité du commerce avec Émirats, Turquie, Géorgie est légitime.
- **Sous-estimer la portée extraterritoriale des sanctions OFAC.** Un opérateur européen peut être impacté.
- **Confondre dual-use et militaire.** Le dual-use est civil mais soumis à autorisation.

### Limites

Le contournement de sanctions est un domaine **politiquement sensible** et techniquement complexe. Les CRF travaillent en étroite collaboration avec services dédiés (DG Trésor — pôle sanctions financières, OFAC, OFSI, services douaniers).

### Lien avec le fil rouge

> **CLEARFLOW — Volet sanctions exploratoire**
> 
> Le dossier Haddad contient des flux passant par Émirats, Turquie. À ce stade, aucun lien direct avec une entité sanctionnée n’est démontré. La possibilité que certains flux relèvent d’un contournement *opportuniste* (vente vers juridictions sous embargo via réseau commercial) reste *possible*. La note finale signale ce volet exploratoire au PNF et recommande coopération avec la DG Trésor — pôle sanctions financières.

### Points clés à retenir

- Sanctions ONU, UE, OFAC, OFSI, nationales.
- Mécanismes de contournement : fronts, triangulation, crypto, re-pavillonnement.
- Dual-use = sujet sensible avec régulation propre.
- Coopération services dédiés (DG Trésor pôle sanctions, OFAC) essentielle.

-----

## Chapitre 46 — Ponzi, pyramides et fraudes à l’investissement

### Objectif du chapitre

Comprendre les **schémas de fraude à l’investissement** : Ponzi, pyramides, fausses ICO/IDO, fraudes au trading, scams crypto.

### Le concept

**Ponzi (schema)**. Le promoteur attire des investisseurs en promettant des rendements supérieurs au marché. Les « rendements » versés aux premiers investisseurs sont prélevés sur les apports des nouveaux investisseurs (et non sur une activité économique réelle). Le système s’effondre lorsque les retraits dépassent les nouveaux apports.

**Pyramide (MLM frauduleux)**. Variante : les investisseurs sont incités à recruter de nouveaux participants. Le revenu provient principalement du recrutement, pas d’un produit ou service réel.

**Fausses ICO / IDO / TGE** : émissions de tokens crypto sans projet réel, avec promesses irréalistes, abandon après collecte (« rug pull »).

**Scam pig butchering** : combinaison fraude sentimentale + fraude à l’investissement. La victime est manipulée pendant des mois par une fausse relation, puis incitée à « investir » dans une plateforme crypto qui semble fonctionner — jusqu’au retrait final impossible.

**Faux trading** : plateformes simulant un trading rentable, où la victime voit des « gains » virtuels mais ne peut pas retirer.

### L’utilité opérationnelle

Les fraudes à l’investissement représentent des pertes massives pour les victimes (souvent l’épargne d’une vie). En CRF, les signalements convergents permettent de détecter et de signaler tôt.

### Méthode — signaux

- Rendements promis très supérieurs au marché.
- Pression à recruter d’autres investisseurs (pyramide).
- Plateforme inconnue, juridiction obscure.
- Garanties auto-désignées, faux régulateurs.
- Présence de figures publiques (vraies ou usurpées) en endorsement.
- Difficulté ou refus de retrait dès qu’on dépasse certains seuils.
- Cashout difficile sur stablecoins, voire impossible.

### Mini-walkthrough — pig butchering simplifié

Une victime française rencontre sur application de rencontre un faux ami sentimental basé prétendument à Hong Kong. Après plusieurs mois, le contact recommande une « opportunité d’investissement » sur une plateforme crypto. La victime investit 50 K€ qui sont convertis en USDT, transitent par plusieurs adresses, et atteignent rapidement un exchange asiatique non-KYC. Tentative de retrait : refus pour « frais bloquants ».

Lecture FININT : pig butchering quasi-certain. Volet on-chain renvoyé à OSINT Crypto (Athéna ou équivalent). Signalement à la PHAROS et au PNF JUNALCO (cybercriminalité). Le réseau organisé derrière ces opérations est souvent identifié à terme avec coopération internationale (notamment SE Asie).

### Erreurs fréquentes

- **Sous-estimer la sophistication** des fraudes pig butchering modernes — équipes professionnelles, scripts éprouvés.
- **Blâmer la victime** : la manipulation est efficace même sur des personnes éduquées.

### Limites

Les schémas se passent souvent partiellement à l’étranger ; la coopération internationale est lente. Le volet crypto est renvoyé à OSINT Crypto pour le traitement détaillé.

### Lien avec le fil rouge

> **CLEARFLOW — Hors périmètre principal**
> 
> Le dossier Haddad ne comporte pas de volet Ponzi ou pig butchering identifié. Ce chapitre reste utile à la compréhension du contexte général des typologies modernes.

### Points clés à retenir

- Ponzi, pyramides, fausses ICO, pig butchering : schémas distincts mais structure commune.
- Rendements promis disproportionnés = signal majeur.
- Coopération internationale (notamment SE Asie) lente mais nécessaire.
- Volet crypto traité par OSINT Crypto.

-----

## Chapitre 47 — Criminalité organisée et économie légale

### Objectif du chapitre

Comprendre comment la **criminalité organisée** infiltre et instrumentalise l’**économie légale** : secteurs vulnérables, schémas de prise de contrôle, signaux d’enquête.

### Le concept

La criminalité organisée moderne ne se limite pas à des activités strictement illicites (trafics, vols, extorsions). Elle réinvestit massivement dans l’économie légale via :

- **Restauration et hôtellerie** (forte composante cash, présentation légitime).
- **Bâtiment et travaux publics** (volumes financiers importants, sous-traitance opaque).
- **Transport routier et logistique** (couverture du déplacement de marchandises diverses).
- **Commerce de détail** (lavages auto, bars-tabacs, taxis, distributeurs).
- **Immobilier** (acquisition, location, montages SCI).
- **Trading commodities** (matières premières, métaux, agroalimentaire — TBML).
- **Jeux et paris en ligne** (couches de blanchiment).
- **Crypto et fintech** (rails de placement et layering).
- **Sport professionnel** (paris, transferts, agents).
- **Art et objets de collection** (intégration à valeur élevée).

### L’utilité opérationnelle

L’analyste FININT travaillant sur la criminalité organisée cherche à :

- **Identifier la prise de contrôle** sur des sociétés légales.
- **Cartographier le réseau** : entreprises, personnes, flux.
- **Détecter le rôle de prête-noms** (chapitre 25).
- **Suivre l’argent** dans l’économie légale jusqu’à ses bénéficiaires réels.

### Méthode — signaux

- Acquisition d’entreprises en difficulté à prix bas par des intermédiaires opaques.
- Dirigeants avec antécédents (presse, fichiers).
- Croissance soudaine et inexpliquée d’une petite société.
- Recrutement massif et anormal dans certains secteurs (sociétés de gardiennage, par exemple).
- Présence d’entités dans plusieurs juridictions sans rationale économique.

### Mini-walkthrough

Un réseau acquiert plusieurs PME du BTP en région française, via plusieurs SARL intermédiaires. Les dirigeants des SARL sont des personnes ayant des liens familiaux mais sans expérience BTP. Les marchés gagnés progressent rapidement (BOAMP). Les flux montrent des paiements à des sous-traitants offshore dont l’activité réelle est douteuse.

Lecture FININT : *probable* infiltration de la criminalité organisée dans le BTP régional. Schémas combinés : faux salariat, sous-traitance fictive, fraude TVA. Coopération avec services spécialisés (JIRS, OCLCIFF en France).

### Erreurs fréquentes

- **Stigmatiser un secteur entier.** La grande majorité des entreprises de chaque secteur sont parfaitement légales.
- **Confondre opacité et criminalité organisée.** Beaucoup d’opacités sont sans lien avec le crime organisé.

### Limites

L’identification précise et la qualification exigent des moyens d’enquête judiciaire (écoutes, observations, perquisitions). Le FININT alimente, ne tranche pas.

### Lien avec le fil rouge

> **CLEARFLOW — Hors périmètre**
> 
> Le dossier Haddad ne présente pas de signaux clairs de criminalité organisée au sens strict (mafia, narco, etc.). C’est un dossier de criminalité économique avec des éléments transnationaux. Mais la frontière est poreuse — un dossier qui commence en fraude fiscale peut révéler des connexions à terme.

### Points clés à retenir

- La criminalité organisée infiltre l’économie légale (BTP, restauration, immobilier, etc.).
- Signaux : acquisitions opaques, croissance inexpliquée, dirigeants à profil suspect.
- Coopération avec services spécialisés (JIRS, OCLCIFF) centrale.
- FININT alimente, ne tranche pas.

-----

## Chapitre 48 — Cybercriminalité, cashout et renvoi vers OSINT Crypto

### Objectif du chapitre

Comprendre l’**interaction cybercriminalité / criminalité financière** : ransomware, vol de cryptos, BEC, infostealers — et savoir quand renvoyer à OSINT Crypto pour le traitement on-chain.

### Le concept

Toute cybercriminalité monétisée passe par un **cashout** : conversion des fonds illicites en valeur utilisable. Modalités :

- **Ransom en crypto** (BTC, Monero, USDT) — le plus courant.
- **Vol de fonds DeFi / exchanges** — flash loans, exploits, phishing wallet.
- **BEC** (chapitre 44) — virement fiat puis souvent conversion crypto.
- **Vente de données volées** sur darknet — paiement crypto.
- **Carding** : utilisation frauduleuse de cartes bancaires, cashout en cash, gift cards, biens.

Le cashout final passe souvent par :

- **Exchanges KYC dans juridictions à faible application** des règles.
- **P2P** (LocalBitcoins historiquement, Paxful, ou alternatives modernes).
- **Bureaux de change crypto** dans certaines villes.
- **Stablecoins** comme valeur intermédiaire avant cashout fiat.

### Articulation FININT / OSINT Crypto

C’est le sujet typique où **FININT et OSINT Crypto coopèrent** :

- **FININT** : cadre le contexte (qui est la victime, qui est probablement derrière l’attaque, quel réseau de mules, quelles coopérations avec banques et autorités, quel suivi judiciaire).
- **OSINT Crypto** : trace les fonds on-chain depuis le wallet d’attaquant jusqu’aux off-ramps (exchanges, P2P), identifie les clusters, qualifie les services traversés (mixers, bridges).

Le rapport FININT **renvoie** à OSINT Crypto pour le détail on-chain. Il ne le refait pas.

### L’utilité opérationnelle

Pour les dossiers ransomware, vol crypto, BEC majeur, fraude DeFi :

- FININT identifie victimes, impact, contexte, attribution probable (avec CTI).
- OSINT Crypto trace, identifie services, attribue.
- Coopération internationale est centrale (Europol EC3, FBI, services nationaux).

### Méthode — workflow type

1. **Signalement / DS / incident** détecté.
1. **FININT** cadre : périmètre, victime, contexte.
1. **OSINT Crypto** (Sarah Marin / Athéna Group dans le fil rouge) prend le volet on-chain.
1. **Coopération** avec exchanges pour KYC sur off-ramps via réquisition.
1. **Synthèse** intégrée dans la note FININT.

### Mini-walkthrough — ransomware sur PME

Une PME française est victime d’un ransomware. Rançon de 80 K€ demandée en USDT vers une adresse Tron. La PME paie (déconseillé, mais souvent fait).

FININT : identification de l’incident, signalement ANSSI/PHAROS, plainte, coopération avec CRF.
OSINT Crypto : traçage de l’adresse de paiement, identification du cluster (TRM Labs / Chainalysis / outils Athéna), suivi jusqu’aux off-ramps, possiblement attribution à un groupe ransomware connu.

Synthèse FININT : note de transmission au PNF JUNALCO et à Europol EC3, avec annexe technique d’OSINT Crypto, et recommandations (poursuite internationale, monitoring continu).

### Erreurs fréquentes

- **Refaire OSINT Crypto dans le FININT** : duplication, perte de temps, risque d’erreur.
- **Ignorer le lien CTI** : l’attribution à un groupe ransomware (Akira, ALPHV, LockBit, etc.) éclaire le dossier.
- **Sous-estimer l’importance du cashout** : c’est le maillon faible des cybercriminels.

### Limites

L’attribution finale d’une cybercriminalité est rarement *quasi-certaine* en pur on-chain. Elle exige souvent l’ajout d’éléments hors-chaîne (CTI, témoignages, arrestations).

### Lien avec le fil rouge

> **CLEARFLOW — Volet crypto secondaire**
> 
> Dans le dossier Haddad, les conversions USDT identifiées ne relèvent pas de ransomware mais de cashout / layering crypto opportuniste. Le volet est confié à Sarah Marin (Athéna). Son rapport on-chain est annexé à la note finale, avec renvoi explicite au cours OSINT Crypto pour les méthodes utilisées.

### Points clés à retenir

- Cybercriminalité = cashout obligatoire, souvent crypto.
- FININT cadre, OSINT Crypto trace on-chain.
- Coopération avec exchanges via réquisitions.
- Le rapport FININT renvoie à OSINT Crypto, ne refait pas.

-----
