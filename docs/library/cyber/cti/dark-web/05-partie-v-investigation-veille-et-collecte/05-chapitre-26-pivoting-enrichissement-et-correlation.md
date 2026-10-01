---
title: Chapitre 26 — Pivoting, enrichissement et corrélation OSINT
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie V — Investigation, veille et collecte
  - index.md
---

Le **pivoting** est l'art de passer d'un indicateur à un autre pour enrichir l'investigation. Sur le dark web, c'est la différence entre une observation isolée et un renseignement exploitable.

## 26.1 Les types de pivots

**Pseudonyme → autres forums**. Un pseudonyme observé sur un forum peut exister sur d'autres. Recherche directe du pseudo sur XSS, Exploit, BreachForums, forums concurrents.

**Pseudonyme → Telegram / Jabber / TOX**. Les posts mentionnent souvent des handles de contact. Suivre ces handles sur les plateformes correspondantes.

**PGP key → autres utilisations**. Une clé PGP est un identifiant quasi-unique. Rechercher la clé (fingerprint) sur d'autres forums, dans des archives, sur des keyservers publics — peut révéler d'autres pseudos ou usages antérieurs.

**Adresse crypto → transactions, clustering**. Une adresse BTC observée permet de découvrir : historique on-chain, adresses liées (cluster), exchanges interagis, autres wallets probablement contrôlés par le même acteur (via heuristiques de change, co-dépense, etc.).

**Infrastructure (domaines, IPs) → autres services**. Un domaine enregistré pour un service criminel peut partager des infos avec d'autres (registrant email, serveurs de noms, mêmes IPs d'hébergement). Outils : DomainTools, SecurityTrails, ViewDNS, passivedns commerciaux.

**Email / fingerprint → OSINT classique**. Un email leaked sur un forum, un pseudonyme utilisé ailleurs (Discord, GitHub, Reddit, StackOverflow, jabber distinct) — permettent de construire un graphe d'identité.

**Style linguistique → attribution**. Tournures, fautes, patterns — peuvent corréler plusieurs pseudos.

**Timing → fuseau horaire**. Patterns d'activité horaire révèlent fuseau. Crosscheck avec autres pseudonymes actifs aux mêmes heures.

## 26.2 Méthodologie de pivoting

**Graph d'investigation**. Maintenir un graphe (Maltego, graphes maison) où chaque nœud est une entité (pseudo, email, wallet, IP, domaine) et chaque arête est une relation (« utilise », « contrôle », « a interagi avec », « mentionne »). Chaque nouveau pivot ajoute des nœuds et arêtes.

**Hypothèses explicites**. À chaque pivot, formuler une hypothèse (« Je pense que pseudo A et pseudo B sont la même personne parce que… »). Tester l'hypothèse avec nouveaux pivots. Renforcer ou rejeter.

**Niveaux de confiance**. Comme pour l'attribution APT (voir cours APT), utiliser vocabulaire calibré : certain / très probable / probable / possible / spéculatif.

**Limites documentées**. Certaines corrélations sont faibles (mêmes initiales pseudo, timing vague) ; d'autres fortes (même PGP key, même wallet). Le rapport final doit distinguer les deux.

## 26.3 Les ressources OSINT utiles

**Bases de données de breach**. Have I Been Pwned, DeHashed, LeakCheck, Snusbase — vérifier si un email ou identifiant a été exposé dans des breaches publics, reconnaître un pseudo qui apparaît dans d'autres contextes.

**Archives forums**. Certains forums disparus ont des archives partielles disponibles — BreachForums archives, Tor's Everything mirror, Internet Archive pour le clearnet.

**GitHub / GitLab**. Parfois, un acteur utilise le même pseudo professionnellement (développement, open source) et dans les forums cybercriminels. Historique public GitHub peut révéler nom réel, email, localisation, compétences.

**LinkedIn / Xing**. Pour les pivots partiels vers identité civile. Un email pro leaked peut correspondre à un profil LinkedIn.

**Keyservers PGP**. Ubuntu keyserver, SKS pools (legacy), Keys.openpgp.org. Recherche par fingerprint peut révéler identités alternatives.

**Blockchain explorers**. Blockstream.info, Mempool.space (Bitcoin), Etherscan (Ethereum), Tronscan (TRON), BlockChair (multi-chain). Traçage des transactions à partir d'adresses observées.

**WHOIS et passive DNS**. Pour le pivoting d'infrastructure.

**Reverse image search**. Google Images, TinEye, Yandex. Un profile picture d'un forum peut correspondre à un profil ailleurs.

**Services spécialisés dark web**. IntelX (archives .onion et leaks), Flare, Recorded Future, DarkOwl, Cybersixgill — agrègent et indexent.

## 26.4 Les erreurs courantes

**Sur-corrélation**. Conclure qu'un pattern faible (initiales communes, style superficiel) prouve que deux pseudos sont la même personne. Le dark web compte des millions d'utilisateurs, beaucoup de coïncidences.

**Biais de confirmation**. Une fois qu'on a un chouchou (« c'est forcément X »), on trouve partout des « preuves ». Discipline : chercher activement ce qui **infirmerait** l'hypothèse.

**Timing trompeur**. Les fuseaux horaires se simulent facilement — un acteur peut activer son compte à des heures calibrées.

**Pseudos communs**. « admin », « king », « boss », « ghost » sont utilisés par des milliers d'acteurs indépendants. Pas un pivot fiable seul.

**Infrastructure partagée**. Plusieurs acteurs utilisent le même hébergeur, registrar, service de certificat. Pas un pivot fiable à lui seul.

**PGP reprise**. Rare, mais une clé PGP peut être volée ou rachetée. Changement soudain du style après une longue présence d'un pseudo avec la même clé = alerte sur une possible rachat.

## 26.5 Fil rouge — DARKSTREAM : pivoting sur aero_source

> **🌐 DARKSTREAM — Épisode 15 : élargissement**
>
> Lucas pivote sur aero_source au-delà d'IndustrialLeaks.
>
> **Pivot 1 — XSS Forum** : recherche du pseudo « aero_source » sur XSS (accès Athéna via partenariat vouching). **Pas de compte direct**, mais un compte « aerosrc » créé il y a 13 mois, style similaire, utilise le même serveur XMPP. Probable sock puppet ou compte antérieur. Activité modeste (4 posts).
>
> **Pivot 2 — Exploit.in** : recherche. Pseudo « aero_src » existe, compte créé il y a 7 mois, style compatible. 3 posts, un sur une vente de specs turbines (non-Vectris, différente cible). **Cohérent avec pattern** d'un même acteur opérant sur 3 forums russophones.
>
> **Pivot 3 — PGP** : la clé PGP affichée par aero_source sur IndustrialLeaks est **identique** à celle sur aerosrc (XSS) et aero_src (Exploit.in). **Très forte corrélation** — probabilité qu'il s'agisse du même acteur : 95%+.
>
> **Pivot 4 — Wallet BTC** : l'adresse BTC mentionnée dans le post aero_source sur IndustrialLeaks. Chainalysis révèle un cluster de ~40 adresses liées. Transactions totales : ~180 000 USDT sur 14 mois. Quelques flux vers exchange non-KYC (Garantex historique, avant sanctions 2022). Interactions avec adresses labellisées « BlackSprut » (marché russophone) — indique acheteur de drogues ou fournisseur dans cet écosystème.
>
> **Pivot 5 — Analyse linguistique** : les posts des 3 comptes (aero_source, aerosrc, aero_src) présentent les mêmes tics — « dear colleagues » comme ouverture, « best regards » comme signature, fautes consistantes (confusion article « the », prépositions). Russophone, niveau anglais intermédiaire. **Corrélation linguistique cohérente avec PGP**.
>
> **Pivot 6 — Telegram** : le handle mentionné par aero_source (non utilisé ici pour OPSEC) pointe vers un compte Telegram. Observation light, pas de contact. Ancienneté compte : 2 ans. Membre de plusieurs canaux cybercriminels russophones.
>
> **Synthèse** : aero_source est (très probablement) un acteur russophone individuel, présent sur l'écosystème depuis 2+ ans, profil IAB/courtier de données intermédiaire, pas un acteur majeur. Son réel intérêt pour les données Vectris n'est pas idéologique ni étatique — motivation financière classique.
>
> Ce profiling oriente l'attribution et le conseil : la menace est réelle mais contenue dans un profil cybercriminel, pas le signe d'une opération étatique majeure. Conséquences pour Vectris : le dump ne servira probablement pas un concurrent direct ou un service de renseignement étranger à court terme — il sera vendu au plus offrant, potentiellement n'importe qui.

---
