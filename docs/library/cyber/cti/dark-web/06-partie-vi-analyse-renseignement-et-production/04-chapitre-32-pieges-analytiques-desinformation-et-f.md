---
title: Chapitre 32 — Pièges analytiques, désinformation et faux signaux
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VI — ANALYSE, renseignement et production
  - index.md
---

L'investigation dark web opère dans un environnement **hostile** où les acteurs cherchent activement à tromper, désinformer, piéger. Ce chapitre cartographie les pièges et les contre-mesures.

## 32.1 Les biais analytiques

**Biais de confirmation**. Une fois une hypothèse formée, on cherche les preuves qui la confirment et on minimise les preuves qui la contredisent. Classique et puissant.

**Mitigation** : formuler explicitement l'hypothèse, puis lister activement ce qui l'infirmerait. ACH (Analysis of Competing Hypotheses) formalise cette discipline.

**Biais d'ancrage**. La première information reçue colore l'interprétation de toute la suite. Si le premier poster du cas a dit « c'est Lazarus », on cherche inconsciemment ce qui va dans ce sens.

**Mitigation** : réévaluer périodiquement depuis zéro. Faire re-présenter le cas par un collègue qui n'a pas été exposé à l'hypothèse initiale.

**Biais de disponibilité**. Ce qui est visible et récent semble plus important. Un groupe ransomware médiatisé la semaine dernière paraît plus menaçant qu'un groupe discret mais plus dangereux.

**Mitigation** : données quantitatives plutôt qu'impressions. Statistiques de ransomfeed, rapports sectoriels.

**Biais d'autorité**. On fait plus confiance à ce que dit un vendor CTI réputé qu'à ce que dit un chercheur indépendant. Parfois justifié, parfois pas.

**Mitigation** : évaluer les sources sur leur mérite, pas leur réputation. Un vendor réputé peut se tromper ; un chercheur indépendant peut voir juste.

**Biais de cohérence narrative**. On préfère les histoires qui font sens (« cet acteur est un agent russe qui cible la défense européenne ») aux histoires messy (« cet acteur est un opportuniste qui a acheté un accès revendu, peut-être revendra lui-même, motivation incertaine »). La réalité est souvent messy.

**Mitigation** : accepter l'ambiguïté. Ne pas sur-narrativiser.

**Biais géopolitique**. Face à un acteur russe, on tend à sur-attribuer à un État. Face à un acteur chinois, idem. Ces biais ne sont pas infondés (beaucoup d'acteurs sont liés à des États), mais ne doivent pas devenir automatiques.

**Mitigation** : évaluer chaque cas sur ses mérites, avec multiples hypothèses explicites.

## 32.2 La désinformation active

Les acteurs malveillants produisent intentionnellement de la désinformation pour tromper analystes et autorités.

**Faux drapeaux (false flags)**. Un acteur se fait passer pour un autre — imite un TTP, utilise un pseudonyme inspiré d'un acteur connu, plante des indices pointant vers un tiers innocent.

Cas emblématique : **Olympic Destroyer (2018)**. Sandworm (GRU russe) inclut des fragments de code Lazarus + artefacts chinois dans son malware déployé pendant les JO de PyeongChang. Analyse minutieuse (Kaspersky) a identifié les faux indices et consolidé l'attribution russe — mais des vendeurs moins attentifs ont initialement pointé vers DPRK.

**Recyclage et fabrication**. Publication de données « fraîchement volées » qui sont en fait anciennes (recyclage) ou fabriquées (composition de différents breaches anciens + données inventées). Donne l'impression d'un breach récent sans réalité sous-jacente.

**Scam ciblé**. Un vendeur qui prétend offrir un accès à une organisation cible — en réalité, il n'a rien, mais veut vendre du vent à un acheteur crédule (qui pourrait être un investigateur lui-même).

**Amplification artificielle**. Un scam mineur présenté comme breach majeur pour attirer l'attention médiatique. Certains « leak massifs » sont en fait de petites compromissions + inflation.

**Honey traps contre analystes**. Un vendeur qui répond rapidement à l'investigateur, fournit des échantillons crédibles, tente de le conduire dans une direction qui bénéficie à l'acteur (faire porter le chapeau à un concurrent, mettre en avant une cible qui n'est pas réellement ciblée).

## 32.3 Les pièges techniques

**Fichiers piégés**. Échantillons fournis par un vendeur qui contiennent malware ciblant l'environnement d'analyse. Exploits navigateur pour identifier l'IP. Macros Office malveillantes. PDF avec JS.

**Mitigation** : ouverture uniquement en VM isolée, mode Safest, sandbox, extraction de métadonnées avant exécution.

**Web beacons dans documents**. Documents PDF ou DOCX contenant des ressources externes (images chargées à l'ouverture, iframes). Signal l'ouverture du document à l'acteur, révèle fuseau horaire, potentiellement IP (si ressource chargée hors VPN/Tor).

**Mitigation** : ouverture offline, airplane mode avant ouverture, analyse des ressources liées avant d'ouvrir.

**URLs piégées**. Liens pointant vers pages avec exploits navigateur. Toujours investiguer en mode Safest.

**Telegram / XMPP avec read receipts**. Certaines messageries confirment lecture/livraison. L'adversaire sait quand son message a été lu — informe sur fuseau horaire, disponibilité. **Mitigation** : désactiver read receipts si possible, lire en offline puis se connecter (pour certains protocoles).

**Watermarks individualisés**. Un échantillon fourni à un « acheteur » peut contenir un marker unique qui l'identifie. Si l'analyste le rediffuse (à la victime, à la DGSI), l'acteur peut tracer via qui a diffusé. **Mitigation** : re-création des documents analysés, suppression d'éléments potentiellement markers.

## 32.4 Les patterns de désinformation

**Narratifs coordonnés**. Plusieurs comptes (sock puppets) diffusent le même narratif sur différentes plateformes pour créer une impression de consensus communautaire. Classique dans hacktivisme et influence.

**Pseudo-leaks**. Fausses fuites conçues pour influencer. Données fabriquées qui contiennent des éléments plausibles + éléments orientés (accusant un tiers, poussant un agenda).

**Attribution fausse**. Certains acteurs s'attribuent délibérément des opérations qu'ils n'ont pas conduites (pour se faire de la pub) ou attribuent à d'autres leurs propres opérations (pour se protéger).

**Timing manipulé**. Publication d'un leak juste avant un événement politique, financier, médiatique — pour maximiser l'impact et suggérer un lien narratif.

## 32.5 Contre-mesures analytiques

**Multi-source**. Ne jamais conclure sur une source unique. Crosscheck avec 2-3 sources indépendantes avant de considérer un fait établi.

**Validation indépendante**. Si un vendeur dit « j'ai X », demander échantillon. Si un vendor dit « APT tel a fait ci », voir si d'autres vendors concordent.

**ACH systématique**. Pour chaque attribution non-triviale, poser les hypothèses alternatives et les tester.

**Vocabulaire calibré**. WEP (Words of Estimative Probability) utilisé systématiquement.

**Documentation du doute**. Rapport analytique inclut section « limites et incertitudes » — honnête sur ce qui n'est pas certain.

**Review par pairs**. Un collègue qui lit un rapport avec œil neuf détecte souvent biais et sauts logiques.

**Red teaming analytique**. Demander à un collègue de jouer l'avocat du diable, tester les conclusions.

**Revisite temporelle**. Relire le rapport 48h après rédaction. Beaucoup de biais apparaissent avec recul.

## 32.6 Les alertes classiques

Signaux qu'une observation est peut-être manipulée.

**« Trop beau pour être vrai »**. Un vendeur trop coopérant, un échantillon trop complet, une identification trop facile. Si l'investigation avance vite et loin, suspicion.

**Convergence trop parfaite**. Tous les indicateurs pointent dans la même direction, sans bruit. Le monde réel est messy ; une convergence parfaite est suspecte.

**Narratif qui « sert » quelqu'un**. Si l'attribution pointe commodément vers un acteur déjà stigmatisé, suspicion d'un false flag.

**Timing opportun**. Un leak qui arrive juste avant une échéance sensible, dans un contexte politiquement chargé.

**Source unique**. Un fait entier repose sur une seule source, même si réputée.

**Pression temporelle artificielle**. « Il faut conclure vite, avant la reunion board demain ». Les conclusions sous pression temporelle sont plus susceptibles à des biais — ralentir autant que possible.

## 32.7 Fil rouge — DARKSTREAM : écarter les faux drapeaux

> **🌐 DARKSTREAM — Épisode 18 : vérification de l'absence de false flag**
>
> Avant de finaliser, Lucas vérifie que DARKSTREAM n'est pas un false flag.
>
> **Hypothèse alternative 1 — aero_source est un APT étatique déguisé**. Vérification : le style linguistique, les patterns d'activité, le profil financier (cluster modeste, flux vers BlackSprut marché de drogues), l'absence de TTP sophistiquée, l'infrastructure grand public (XMPP standard), le prix de vente (65k, dans la norme cybercriminelle) — tous pointent vers profil cybercriminel. **Hypothèse rejetée** (probabilité < 10%).
>
> **Hypothèse alternative 2 — aero_source essaie de piéger Athéna**. Vérification : les échantillons fournis ne contiennent pas de watermarks détectés. Pas d'exploits identifiés. Communications cohérentes (pas d'over-cooperation suspecte). **Possible mais improbable** (les markers intentionnels sont rares chez acteurs de ce niveau).
>
> **Hypothèse alternative 3 — le dump n'est pas réellement Vectris**. Vérification : marker interne Vectris confirmé. Cohérence avec forensics Mandiant côté victime. **Rejetée** avec très haute confiance.
>
> **Hypothèse alternative 4 — aero_source est un proxy d'un acteur plus grand**. Vérification : style cohérent d'un acteur individuel (vs patterns de grande équipe), historique transactionnel personnel, comportement opportuniste (pas stratégique). **Possible (~25%)** mais sans support fort.
>
> Lucas documente ces vérifications dans le rapport, section « limites et incertitudes ». Le rapport final conclut avec un profil cybercriminel individuel à haute confiance, mais note explicitement que la revente ultérieure à un acteur étatique est une hypothèse qui reste ouverte. La DGSI appréciera cette calibration.

---
