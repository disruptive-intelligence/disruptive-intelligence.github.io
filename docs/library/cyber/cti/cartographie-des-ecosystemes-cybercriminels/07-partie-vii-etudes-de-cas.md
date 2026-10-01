---
title: Partie VII — Études de cas
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - index.md
---

*Les mêmes outils analytiques (cartographie + analyse économique + niveaux de confiance) permettent d'étudier des écosystèmes de natures très différentes — ransomware industriel, fraude financière, opérations para-étatiques, manipulation informationnelle, et marchés clandestins. C'est la polyvalence de la méthode qui en fait la force. Chaque étude de cas suit le même processus : point d'entrée → cartographie → analyse économique → conclusions.*

---


## Chapitre 29 — Écosystème ransomware

**Point d'entrée :** Un rapport CTI mentionne une nouvelle plateforme RaaS, « NovaCrypt », qui revendique 40 victimes en 3 mois avec un focus sur le secteur santé européen.

**Cartographie.** L'analyse du leak site révèle les victimes (pays, secteur, taille). Le reverse engineering du sample disponible sur VirusTotal identifie le builder et les configurations C2. L'infrastructure C2 est tracée via DNS/WHOIS/Certificate Transparency. Les annonces de recrutement sur les forums russophones (RAMP, XSS) révèlent les conditions de l'affiliation (80/20 en faveur de l'affilié, dépôt de 300 $). Les wallets de paiement des rançons sont tracés via OXT.me et Chainalysis.

**Analyse économique.** NovaCrypt suit le modèle RaaS classique. Le focus santé est stratégique : les hôpitaux européens paient rapidement (l'urgence vitale presse la décision), les montants sont modérés (100 000-500 000 €) mais le volume est élevé. Le revenu estimé de l'opérateur : 2 à 5 M€ sur 3 mois. Les coûts sont faibles (infrastructure, développement, support). Le ROI est exceptionnel.

**Conclusions.** NovaCrypt est un écosystème fédéré de taille moyenne, avec un opérateur compétent et une dizaine d'affiliés actifs. Les points de fragilité sont l'hébergeur (un seul prestataire pour toute l'infrastructure) et le canal de recrutement (RAMP — si le forum est compromis, la filière d'affiliation est coupée).

---


## Chapitre 30 — Fraude et scam crypto

**Point d'entrée :** Une plainte de plusieurs investisseurs français concernant une plateforme d'investissement crypto « YieldMax Pro » qui a disparu avec les fonds.

**Cartographie.** Le site web est analysé (WHOIS, hébergement, date de création, contenu). Les canaux Telegram et groupes Facebook utilisés pour le recrutement des victimes sont identifiés. Les wallets de dépôt sont tracés. Les influenceurs ayant promu la plateforme sont identifiés (certains payés, d'autres victimes eux-mêmes). Les sociétés écrans enregistrées (une société au Panama, une licence fictive mentionnant un régulateur inexistant) sont vérifiées dans les registres.

**Analyse économique.** YieldMax Pro est un schéma de Ponzi crypto classique : les premiers investisseurs sont payés avec les dépôts des suivants, créant l'illusion de rendements. Le funnel de captation utilise des publicités sur les réseaux sociaux, des témoignages fabriqués, des vidéos deepfake de « CEO » fictif, et une interface web professionnelle mimant les plateformes légitimes. Le cash-out utilise des bridges cross-chain (Ethereum → Polygon → Binance Smart Chain) pour compliquer le traçage, puis des OTC desks en Asie du Sud-Est.

**Conclusions.** L'écosystème est centralisé (un noyau de 3-5 personnes contrôle l'ensemble), sa résilience est faible (la disparition du site met fin à l'opération), mais les acteurs se reconstitueront probablement sous une autre marque. Les points de fragilité sont les wallets de consolidation (traçables) et les sociétés écrans (identifiables dans les registres).

---


## Chapitre 31 — Acteur hybride ou para-étatique

**Point d'entrée :** Un rapport de threat intelligence d'un éditeur CTI décrit un groupe, « SteelViper », qui mène simultanément des opérations de cyber-espionnage contre des ministères européens et des attaques ransomware contre des entreprises de défense.

**Cartographie.** L'analyse des TTP révèle deux profils distincts : les opérations d'espionnage utilisent des implants sophistiqués custom avec des C2 bien dissimulés ; les opérations ransomware utilisent un builder RaaS connu avec des C2 plus classiques. Mais les deux types d'opérations partagent certains éléments d'infrastructure (un serveur de staging commun, un domaine d'exfiltration réutilisé) et des patterns comportementaux similaires (mêmes horaires d'activité, mêmes techniques de mouvement latéral).

**Analyse.** Le partage d'infrastructure entre espionnage et ransomware est l'indice le plus discriminant. Trois hypothèses : (H1) deux groupes distincts qui partagent un prestataire d'hébergement (faux lien par mutualisation), (H2) un seul groupe qui mène les deux types d'opérations (acteur hybride), (H3) un groupe étatique qui utilise le ransomware comme couverture ou comme source de financement. L'analyse des cibles (les victimes d'espionnage sont toutes des entités liées à la politique de défense européenne) et du timing (les opérations d'espionnage s'intensifient avant des sommets diplomatiques) soutient H3, mais l'absence de preuve de commandement étatique direct maintient la prudence.

**Conclusions.** L'attribution para-étatique est probable (confiance modérée) mais non confirmée. Le rapport recommande de traiter le groupe comme une menace de niveau étatique pour la posture défensive, tout en documentant l'incertitude analytique.

---


## Chapitre 32 — Opération d'influence coordonnée

**Point d'entrée :** Un réseau de comptes sur X/Twitter et Facebook amplifie simultanément des narratifs anti-européens en ciblant spécifiquement les débats sur l'énergie et le climat, avec des contenus en français, allemand et polonais.

**Cartographie.** L'analyse des comptes révèle des patterns d'inauthenticité : création en masse (dates de création regroupées), noms générés (prénom + nom + chiffres aléatoires), photos de profil générées par IA (détectables par analyse d'artefacts), et patterns de publication synchronisés (les mêmes contenus partagés à quelques minutes d'intervalle par des dizaines de comptes). L'infrastructure technique est tracée : les liens partagés redirigent vers un réseau de sites web hébergés sur un même serveur, enregistrés par la même société écran. Les flux financiers remontent à un prestataire de « services de communication » basé en Russie, identifié dans des rapports précédents comme un acteur de l'écosystème de désinformation.

**Analyse économique.** L'opération fonctionne comme une prestation de service : le commanditaire (présumé étatique) passe commande, le prestataire crée les contenus, déploie les comptes, et gère l'amplification. Le coût est relativement faible (quelques dizaines de milliers d'euros par mois pour une opération de cette envergure). Les plateformes de réseaux sociaux détectent et suppriment régulièrement ces réseaux, mais la reconstitution est rapide et peu coûteuse.

**Conclusions.** L'opération d'influence est un écosystème clandestin à part entière, avec ses prestataires, ses infrastructures, ses flux financiers, et ses mécanismes de résilience. Les mêmes outils de cartographie (Maltego, analyse de réseau, analyse financière) sont applicables.

---


## Chapitre 33 — Marché clandestin / forum

**Point d'entrée :** Analyse du forum russophone « BlackMarket », actif depuis 2021, spécialisé dans la vente d'accès, de données, et de services de hacking.

**Cartographie.** Le forum est analysé comme une institution économique. La hiérarchie est cartographiée (2 admins, 5 modérateurs, 30+ vendeurs vérifiés, 2 000+ membres). Le système de réputation est analysé (rating par transaction, ancienneté, statut « trusted vendor »). Les catégories de services sont inventoriées (accès RDP, accès VPN, credentials bancaires, services de carding, crypter FUD, DDoS-for-hire). Le mécanisme d'escrow est documenté (le forum retient 5 % de chaque transaction comme commission et fournit un service d'arbitrage).

**Analyse économique.** Le forum génère des revenus via les commissions d'escrow (5 % sur chaque transaction), les fees d'adhésion (certaines sections premium nécessitent un paiement), les fees de vouching (un nouveau vendeur paie pour être vérifié), et les publicités internes (bannières pour des services premium). Le volume de transactions estimé (basé sur les ratings publics) suggère un chiffre d'affaires annuel de plusieurs centaines de milliers de dollars pour les admins.

**Conclusions.** Le forum fonctionne comme un marché structuré avec des mécanismes de gouvernance sophistiqués. Sa vulnérabilité principale est la concentration de pouvoir dans les admins : une compromission ou un exit scam détruirait instantanément la confiance accumulée. Sa résilience repose sur le capital réputationnel et les relations de confiance qui ne migreraient que partiellement vers un successeur.

---
