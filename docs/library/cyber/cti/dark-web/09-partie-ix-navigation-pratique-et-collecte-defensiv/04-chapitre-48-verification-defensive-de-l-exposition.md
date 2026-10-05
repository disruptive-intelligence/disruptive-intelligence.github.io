---
title: Chapitre 48 — Vérification défensive de l'exposition dans les bases de leaks publiques
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie IX — Navigation pratique et collecte défensive encadrée
  - index.md
---

Au-delà du dark web .onion, la **veille des data leaks publiques** est un aspect essentiel de la pratique défensive. Plusieurs services indexent les breaches publics et permettent à une organisation de vérifier son exposition. Ce chapitre couvre les outils, méthodes, et limites — strictement défensifs.

## 48.1 Comprendre les bases de leaks publiques

**Have I Been Pwned (HIBP)** — haveibeenpwned.com. Maintenu par Troy Hunt depuis 2013. La référence absolue. Indexe les breaches publiquement connus, déduplique, expose via interface web et API. Gratuit pour usage standard, API payante pour usage volumétrique.

Caractéristiques :

- ~13 milliards de comptes indexés (cumul historique).
- ~700+ breaches répertoriés.
- Recherche email simple : entre l'email, voit les breaches où il apparaît.
- Recherche password (« Pwned Passwords ») : vérifier si un mot de passe spécifique apparaît dans un breach.
- **Domain search** : pour propriétaires de domaines vérifiés, voir tous les emails du domaine compromis.

**DeHashed** — dehashed.com. Plateforme commerciale qui va plus loin que HIBP — indexe données complètes (pas seulement emails), permet recherches par username, IP, téléphone, nom, etc. Inclut breaches qu'HIBP ne couvre pas. Coût : ~5-15 USD/mois individuel, plus pour entreprises.

**LeakCheck.io** — leakcheck.io. Concurrent DeHashed, accès commercial.

**Snusbase** — snusbase.com. Autre alternative payante.

**IntelX** — intelx.io. Plateforme plus large : leaks, .onion archives, pastebin, deep web. Tier gratuit limité.

**Limite importante** : ces services ne donnent pas une vision **exhaustive** de l'exposition réelle. Ils donnent une vision partielle, utile pour prioriser des actions défensives, mais ils ne remplacent ni une investigation complète ni un programme CTI structuré. Faux négatifs possibles : votre exposition réelle peut être plus large que ce qui apparaît.

## 48.2 Limites juridiques et RGPD

Avant les walkthroughs avancés, cadrer le périmètre.

**Principes** :

- **Base légale** : recherche sur sa propre identité ou sur le périmètre de son organisation = base légale solide (intérêt légitime, sécurité). Recherche sur tiers = nécessite mandat client, autorité légale, ou autre base précise.
- **Minimisation** : ne télécharger que ce qui est nécessaire à l'investigation.
- **Durée de conservation** : limitée, suppression après usage.
- **Habilitation** : seul personnel autorisé accède aux données collectées.
- **Journalisation des recherches** : tracer qui cherche quoi pour audit.
- **Non-prolifération** : ne pas rediffuser les données récupérées.
- **Suppression** : politique formalisée post-investigation.

**Cadre juridique français/européen** :

- **RGPD** : traitement de données personnelles encadré, même si données déjà publiquement exposées.
- **Code pénal article 226-18** : traitement de données à caractère personnel par moyens frauduleux.
- **Articles 226-1 et suivants** : atteinte à la vie privée.

Un analyste qui dériverait dans des usages offensifs (recherche sur tiers sans mandat, préparation cred stuffing, doxing) s'expose à sanctions disciplinaires, civiles, et pénales. Le cadre **professionnel défensif** est strict.

## 48.3 Vérification individuelle

**Vérifier votre propre adresse email** :

1. Aller sur haveibeenpwned.com.
2. Entrer votre email pro et perso.
3. Voir la liste des breaches où l'email apparaît.

**Interprétation** :

- Plusieurs breaches : statistique pour utilisateur internet actif (LinkedIn 2012, Adobe 2013, Collection #1 2019).
- Breaches récents : préoccupant — réinitialiser mot de passe sur services concernés, activer MFA.
- Breach mentionnant « passwords cracked » : votre mot de passe a été exposé en clair → ne plus le réutiliser, MFA prioritaire.

L'objectif n'est pas de paniquer à chaque apparition d'un email dans un breach ancien. L'objectif est de **vérifier les réutilisations de mots de passe**, **activer le MFA** et **comprendre quels comptes restent exposés**.

**Vérifier vos mots de passe**. HIBP « Pwned Passwords » permet de tester un mot de passe (sans l'envoyer en clair grâce à k-anonymity — vous envoyez seulement les 5 premiers caractères du hash SHA-1, le service renvoie tous les hashes commençant par ces 5 caractères, vous comparez localement).

**Activer le monitoring**. HIBP propose des alertes — entrer son email, recevoir un email à chaque nouveau breach contenant cet email. Gratuit. Bonne pratique pour tout utilisateur.

## 48.4 Vérification organisationnelle avec HIBP Domain Search

Pour les propriétaires de domaines vérifiés, HIBP expose tous les emails compromis du domaine.

**Vérification de propriété** :

1. Aller sur haveibeenpwned.com/DomainSearch.
2. Entrer le domaine (ex : `vectris-aerospace.eu`).
3. HIBP demande de prouver la propriété — plusieurs méthodes :
    - Email à un compte privilégié du domaine (postmaster@, security@, etc.).
    - DNS TXT record.
    - Meta tag sur le site web.
    - Upload d'un fichier sur le site web.
4. Une fois vérifié, accès aux résultats.

**Résultats** : liste de tous les emails du domaine apparaissant dans des breaches, breaches concernés, dates, statistiques.

**Distinction de criticité** :

- **Email exposé dans un breach ancien grand public** : criticité faible à moyenne.
- **Mot de passe en clair ou hash faible associé à email professionnel** : criticité élevée.
- **Log infostealer récent avec cookie ou accès VPN** : criticité critique.
- **Accès corporate vendu par IAB** : urgence sécurité.

**Action défensive** :

- **Reset mots de passe** des emails concernés (en supposant le mot de passe utilisé sur le service breach a été ou pourrait être réutilisé en interne).
- **Vérifier réutilisation** : si l'email pro a été compromis dans LinkedIn 2012 avec un mot de passe, ce mot de passe est-il toujours utilisé en interne ?
- **MFA partout** : breach + réutilisation = compromission ; MFA résistant phishing protège.
- **Sensibilisation** : informer les employés concernés, les inviter à vérifier leurs propres comptes personnels.

## 48.5 Recherche granulaire avec DeHashed / LeakCheck

Pour aller au-delà de HIBP (qui ne donne que les breaches concernés, pas les données), les plateformes commerciales permettent recherches granulaires.

**DeHashed walkthrough** :

1. Compte créé sur dehashed.com (vérification email).
2. Souscription mensuel ($5-15 selon tier).
3. Interface de recherche : champs email, username, IP, téléphone, nom, hash, password (pour reverse lookup d'un mot de passe vers comptes l'ayant utilisé).

**Recherches utiles pour défense** :

- **Email professionnel** : voir non seulement les breaches mais le contenu (mot de passe en clair, hash, infos additionnelles).
- **Username** : vérifier si un username utilisé en pro apparaît ailleurs (réutilisation = pivot pour attaquants).
- **IP de l'organisation** : breaches de fournisseurs SaaS contenant log entries depuis IPs Vectris peuvent indiquer compromission de partenaire.

Une recherche granulaire sur des personnes identifiables doit être limitée au **périmètre autorisé**. Même si l'outil permet techniquement de chercher n'importe qui, l'analyste ne doit rechercher que les identités, domaines ou actifs couverts par sa mission.

## 48.6 Veille active vs ponctuelle

**Vérification ponctuelle** : à l'embauche d'un nouveau RSSI, lors d'un audit, après un incident.

**Veille active** : monitoring continu, alerting en temps réel.

**Outils de veille active** :

- **HIBP** alerts automatiques (gratuit, par email).
- **DeHashed** monitoring (commercial).
- **Plateformes CTI** intégrées (SOCRadar, Flare, Recorded Future) — incluent monitoring data leak avec attribution sectorielle.

**Pour une organisation** : combinaison recommandée :

- HIBP Domain Monitoring pour exposition large.
- Une plateforme commerciale (Flare, SOCRadar) pour monitoring multi-source.
- Procédure de réaction documentée à chaque alerte (qui investigue, qui notifie, qui escalade).

## 48.7 Workflow d'alerte data leak — matrice opérationnelle

Cas pratique : votre plateforme CTI alerte qu'un email cadre Vectris apparaît dans un nouveau breach.

**Étape 1 — qualification (15 min)** :

- Quel est le breach concerné ?
- Date de la compromission, type de données exposées.
- Source du leak (publication publique, vente sur dark web, leak interne).
- Email du cadre concerné, position, criticité du compte.

**Étape 2 — investigation profonde (1-2h)** :

- Recherche complète sur DeHashed/HIBP : autres comptes du cadre exposés ?
- Vérifier sur Russian Market / autres marchés logs : credentials récents disponibles ?
- Vérifier le poste du cadre : signe de compromission via stealer ?
- Vérifier les services associés au compte breach : mot de passe réutilisé en interne ?

**Matrice de criticité et action** :

| Signal détecté | Criticité | Action |
|---|---|---|
| Email pro dans breach ancien sans mot de passe clair | Faible | Information utilisateur, vérification MFA |
| Email pro + mot de passe en clair | Élevée | Reset, révocation sessions, contrôle réutilisation |
| Log infostealer récent | **Critique** | Isolation poste, reset global, révocation tokens, hunting |
| Accès VPN/RDP vendu par IAB | **Critique** | IR immédiat, vérification logs, notification RSSI/autorités |
| Dump entreprise annoncé | **Critique** | Cellule de crise, authentification, juridique, communication |

**Étapes complémentaires** (selon criticité) :

- **Communication** : si impact business significatif → remontée RSSI puis direction. Si données personnelles compromises → évaluation notification CNIL (RGPD art. 33-34). Si OIV → remontée ANSSI selon procédure.
- **Audit** : poste du cadre, autres cadres du même périmètre (effet de cluster).
- **Documentation** : CRM CTI, IoC SIEM si pertinents.

## 48.8 Valeur des données et priorisation

Pour calibrer la valeur d'un leak observé sur dark web, ordres de grandeur indicatifs (cf Ch.14 pour grille complète).

| Type | Source primaire | Prix dark web (indicatif) | Valeur défensive |
|---|---|---|---|
| Combo lists générales | Breaches mass-cumulés | 5-50 USD pour millions | Vérifier reuse via HIBP |
| Logs infostealer corporate | Russian Market | 50-500 USD/log | **Critique** — accès direct possible |
| Fullz US | BriansClub | 10-70 USD/identité | Prévention fraude |
| Dossier médical US | Marchés santé | 50-250 USD | Compliance HIPAA, fraude assurance |
| Base données enterprise | Forums/IndustrialLeaks | 500-100 000 USD+ | Selon sensibilité |
| Données R&D / IP | Niche | 1 000-100 000 USD+ | Compliance export, IP protection |

Le prix dark web ne mesure pas seulement la gravité pour la victime. Il mesure surtout la **valeur marchande perçue par les criminels**. Une donnée peu chère peut néanmoins être critique pour une organisation donnée — un employé exposé dans un combo list à 5 USD peut être le maillon faible d'une compromission majeure.

## 48.9 Manipuler des données de fuite sans devenir un facteur de risque

Un analyste qui manipule des leak data — même publiquement disponibles — opère dans un cadre éthique strict.

**Principes opérationnels** :

- **Minimisation** : ne télécharger que ce qui est nécessaire à l'investigation.
- **Sécurisation** : stocker chiffré, accès limité.
- **Limitation temporelle** : suppression après usage.
- **Non-prolifération** : ne pas rediffuser.
- **Respect des victimes** : les données représentent des personnes réelles.
- **Non-exploitation curieuse** : ne pas explorer un dump par curiosité, seulement pour mission.
- **Coopération autorités** : si découverte d'infractions graves, signalement.

**Cas litigieux** :

- Découverte d'un breach non publiquement annoncé : qu'en faire ? Notification responsible disclosure à la victime, signalement éventuel CNIL/ANSSI, pas de publication unilatérale.
- Données contenant CSAM : **arrêt immédiat**, non-conservation, signalement Pharos / autorités compétentes.
- Données politiquement sensibles : neutralité analytique, pas d'exploitation idéologique.

Le cadre professionnel impose une discipline éthique que l'analyste maintient au-delà des règles strictes — c'est ce qui le distingue des acteurs malveillants partageant les mêmes accès techniques.

## 48.10 Synthèse pour l'analyste

**Outils essentiels gratuits** :

- HIBP : exposition individuelle et organisationnelle.
- HIBP Pwned Passwords : hygiène mots de passe.

**Outils complémentaires commerciaux (selon budget)** :

- DeHashed / LeakCheck : recherches granulaires.
- IntelX : leaks plus larges incluant .onion archives.
- Plateforme CTI complète (Recorded Future, Flare, SOCRadar) : monitoring continu sectoriel.

**Procédures à formaliser** :

- Vérification périodique de l'exposition organisationnelle.
- Réaction structurée aux alertes data leak.
- Communication avec employés concernés.
- Coordination IR + CTI + communication + juridique.

Pour beaucoup d'organisations, **la surveillance des leaks publics et des logs d'infostealers est le premier niveau réaliste de CTI défensive** : peu coûteux, rapidement déployable, et directement relié à des actions de sécurité concrètes. Pour une organisation moyenne, c'est souvent le **premier programme** de veille à mettre en place — bénéfice/coût excellent.

---
