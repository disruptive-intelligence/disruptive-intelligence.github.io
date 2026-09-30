---
title: Partie 3 — Sécurité matérielle, racine de confiance et isolation
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
chapter: 4
chapters: 8
---

> **Objectif** : descendre dans la pile, du silicium au bureau, pour comprendre ce qu’on défend réellement. La sécurité applicative ne tient que si la base tient. Ce qui se passe avant le système d’exploitation conditionne ce qui se passe après.

-----

## Chapitre 10 — Sécurité matérielle : choix, supply chain, intégrité physique

### 10.1 Modèle d’attaque physique

L’attaquant physique est radicalement plus dangereux que l’attaquant distant. S’il a accès à ton appareil, même brièvement, la plupart des défenses logicielles s’effondrent. Quatre scénarios :

- **Vol opportuniste** : sac arraché, ordinateur oublié au café. Adversaire faible, mais accès total à l’appareil éteint puis allumé.
- **Evil maid** : accès temporaire pendant ton absence (chambre d’hôtel, bureau, frontière). Adversaire compétent : modification de firmware, ajout de keylogger matériel, clonage de disque, implantation de backdoor.
- **Saisie** : douane, perquisition, arrestation. Adversaire étatique avec accès quasi illimité à l’appareil.
- **Coercition** : tu es présent et contraint de fournir codes et accès. Aucune défense technique pure n’y résiste totalement.

Le chiffrement complet (Ch 12) protège contre vol et saisie *si l’appareil est en BFU (Before First Unlock)*. Il protège peu contre evil maid (qui agit sur l’appareil éteint mais peut pré-installer des éléments qui s’activeront après ton déverrouillage). Il ne protège pas contre coercition.

### 10.2 Choix de matériel : coprocesseurs de sécurité

Les laptops modernes intègrent souvent un coprocesseur dédié à la sécurité, qui isole les opérations cryptographiques sensibles du processeur principal :

- **Apple Silicon (M1/M2/M3/M4)** : Secure Enclave intégré au SoC, gère les clés de chiffrement FileVault, Touch ID, déverrouillage. Architecture mature et auditée.
- **Microsoft Pluton** : disponible sur certains processeurs AMD Ryzen et Intel récents (à partir de 2022, généralisé en 2024-2025). Coprocesseur sécurisé directement dans le CPU.
- **Google Titan M2** sur Pixel : équivalent Secure Enclave côté Android, gère le déverrouillage, l’attestation, le stockage de clés.
- **TPM 2.0 discret** : sur la majorité des laptops Windows depuis 2021. Moins intégré qu’un coprocesseur dédié mais offre des garanties cryptographiques sérieuses (Ch 11).

**Conséquence pratique** : un Pixel récent + GrapheneOS, un MacBook Apple Silicon, ou un laptop Windows avec Pluton offrent aujourd’hui de bien meilleures garanties matérielles qu’un laptop générique sans TPM.

### 10.3 ThinkPad, Framework et le choix Linux

Pour ceux qui veulent du Linux durci, deux choix s’imposent en 2025-2026 :

- **ThinkPad** récents (T14, X1 Carbon, P-series) : bon support Linux, TPM 2.0, qualité industrielle, certaines références supportent Coreboot ou Heads (cf. Ch 11).
- **Framework Laptop** : modulaire, support Linux excellent, choix éthique sur la réparabilité.

Risque commun : les **mises à jour firmware** dépendent du constructeur. Sur ThinkPad, fwupd/LVFS gère bien. Sur d’autres marques, les firmwares restent obscurs et rarement mis à jour côté Linux.

### 10.4 Supply chain

L’attaquant peut intercepter ton matériel entre la commande et la livraison. Cas documentés : NSA TAO interceptait des routeurs Cisco avant livraison pour y implanter des backdoors (révélations Snowden). Pour un individu :

- Acheter directement en magasin physique limite l’interception postale.
- L’achat d’occasion expose à un matériel déjà compromis ou modifié.
- Le refurbishing professionnel certifié réduit ce risque sans l’éliminer.
- Pour les cibles à haut risque : achat en personne, dans un magasin choisi au dernier moment, paiement cash.

### 10.5 Détection d’intrusion physique

Tu ne peux pas empêcher l’evil maid si l’attaquant est compétent. Tu peux le *détecter*, ce qui change la stratégie défensive : un appareil suspecté de compromission n’est plus utilisé pour le sensible.

Techniques élémentaires :

- **Vis non standard** sur les panneaux d’accès (Torx Security, etc.).
- **Vernis à ongles glittery** sur les vis et joints du boîtier : motif unique, photographié pour comparaison ultérieure.
- **Photo macro** de la disposition des composants internes lors de l’achat, pour comparaison.
- **Scellés** sur les ports USB inutilisés.
- **Câble Kensington** ou solution équivalente quand l’appareil est en lieu non sûr.

Aucune de ces techniques n’arrête un attaquant gouvernemental sérieux, mais elles arrêtent l’attaquant moyen et imposent un coût supérieur au reste.

### 10.6 Disposal sécurisé

Quand un appareil sort de ton circuit (revente, recyclage, défaillance), il emporte tes données. Trois niveaux :

- **Disque mécanique (HDD)** : effacement multipasses (DBAN, NIST 800-88 Clear) reste valide.
- **SSD** : l’effacement logique est moins fiable (wear leveling). La commande `cryptographic erase` via le firmware SSD (souvent `hdparm --security-erase`) est plus efficace. En dernier recours : broyage physique. ANSSI recommande la destruction physique pour les SSD contenant des secrets sensibles.
- **Téléphones** : reset usine + chiffrement actif est généralement suffisant. Sur GrapheneOS, la procédure inclut un effacement complet du stockage chiffré.

### 10.7 Périphériques non fiables

USB et ports d’extension sont les vecteurs sous-estimés. BadUSB (Hak5 Rubber Ducky et clones) émule un clavier et tape des commandes à grande vitesse dès le branchement. Les câbles peuvent être piégés (O.MG cables).

Règles : ne jamais brancher un USB inconnu ; pour le chargement public, préférer un câble *data-only-off* (ou un USB condom comme PortaPow) ; sur Linux, paquet `usbguard` qui bloque les périphériques USB non whitelistés ; sur Windows, Device Guard et Credential Guard.

### 10.8 Webcam, micro, capteurs

Couverture caméra physique : trivial, efficace. Apple le déconseille sur MacBook (risque d’écraser le mécanisme), mais une fine pellicule autocollante reste sans risque. Pour le micro : sur certains laptops, un interrupteur matériel (Framework, certains ThinkPad). Sinon, désactivation logicielle (qui peut être contournée par malware) ou retrait physique du module si nécessaire.

Sur smartphone, les modes « micro/caméra coupés au niveau OS » de iOS (indicateurs verts) et GrapheneOS (toggle système) offrent des garanties matérielles. Sur Android stock, ces indicateurs existent mais l’OS reste contournable par exploits.

> 🟩 **À retenir du chapitre 10**
> 
> - Attaquant physique > attaquant distant. Le matériel est la racine.
> - Coprocesseurs de sécurité (Secure Enclave, Pluton, Titan M2) changent la donne.
> - Tu ne peux pas empêcher l’evil maid compétent, tu peux le détecter.
> - Disposal sécurisé : SSD = effacement crypto ou broyage.
> - Le minimum réaliste pour la plupart : laptop récent avec TPM 2.0, BitLocker/FileVault/LUKS, vis vernies, vigilance sur les USB.

-----

## Chapitre 11 — Firmware, UEFI, Secure Boot, TPM et chaîne de démarrage

### 11.1 Qu’est-ce que le firmware et pourquoi c’est critique

Le **firmware** est le code qui s’exécute avant ton système d’exploitation, et qui le charge. Il vit dans une puce de la carte mère, accessible avant tout antivirus, tout chiffrement, tout système de détection. Un firmware compromis = persistance totale, invisible, irrémédiable par réinstallation du système.

UEFI a remplacé le BIOS historique en apportant : démarrage plus rapide, prise en charge de disques > 2 To, et surtout *Secure Boot*, qui vérifie cryptographiquement chaque étape de la chaîne de démarrage.

### 11.2 Secure Boot : principe et limites

Secure Boot vérifie que chaque composant chargé (bootloader, noyau, drivers) est signé par une autorité de confiance. Ce qui n’est pas signé ne s’exécute pas. Cela bloque les rootkits qui s’injectaient au démarrage.

Mais Secure Boot a été attaqué :

- **BlackLotus** (2022-2023) : bootkit UEFI capable de bypass Secure Boot via une signature légitime mais vulnérable de bootloader Windows.
- **LogoFAIL** (2023) : exploit dans le parsing d’images BMP/PNG affichées au démarrage permettant l’exécution de code avant Secure Boot.

Conséquence : Secure Boot est *nécessaire* mais pas *suffisant*. Sa désactivation laisse une fenêtre d’attaque ouverte ; son activation, sans mise à jour firmware, laisse aussi des fenêtres connues.

### 11.3 TPM 2.0

Le **Trusted Platform Module** est une puce dédiée au stockage de clés cryptographiques et à la mesure de l’état du système. Il est utilisé typiquement pour :

- Stocker la clé de déchiffrement disque (FileVault, BitLocker, LUKS+systemd-cryptenroll).
- Mesurer la chaîne de démarrage (Measured Boot) et libérer ces clés *seulement* si l’état correspond à un état attendu.
- Attester à un service distant que l’appareil n’a pas été modifié.

**Effet pratique** : avec TPM 2.0 et déverrouillage automatique du disque, ton ordinateur déverrouille tout seul s’il démarre dans un état attendu, mais si quelqu’un a modifié le firmware, le bootloader ou les paramètres TPM, le déverrouillage échoue et tu es prévenu d’une intrusion. C’est puissant — mais cela suppose que tu surveilles les échecs (souvent un échec TPM est interprété par l’utilisateur comme un bug à contourner, ce qui annule la protection).

### 11.4 Coreboot, Heads, Pureboot

Pour qui veut sortir du firmware constructeur (souvent opaque) :

- **Coreboot** : firmware open source minimaliste, supporté sur certains ThinkPad et autres modèles.
- **Heads** : firmware sécurisé basé sur Coreboot, conçu pour la sécurité physique (vérification cryptographique de tout le boot + clé GPG matérielle).
- **PureBoot** : commercial (Purism), basé sur Coreboot + Heads.

Ces options sont réservées à un public technique et acceptant une perte de fonctionnalités (suspend parfois cassé, certaines fonctions matérielles indisponibles).

### 11.5 Mises à jour firmware

Sur Linux, **fwupd** + le LVFS (Linux Vendor Firmware Service) permettent des mises à jour automatiques de firmware pour les marques compatibles (Dell, Lenovo récents, HP, Framework, certains autres). C’est l’un des chantiers les plus aboutis de Linux desktop ces dernières années.

Sur Windows, les mises à jour firmware passent par Windows Update pour les marques OEM intégrées.

Sur macOS, les mises à jour firmware sont incluses dans les mises à jour système.

Sur Android, dépend du constructeur. Pixel et iPhone reçoivent les mises à jour rapidement. Marques moyennes : variable. Marques basses : souvent rien après deux ans.

### 11.6 Limites : Intel ME, AMD PSP

Tous les CPU Intel récents intègrent un **Management Engine** (ME), tous les AMD un **Platform Security Processor** (PSP). Ce sont des sous-systèmes propriétaires fonctionnant à un niveau supérieur au système d’exploitation, avec accès complet à la mémoire, au réseau, à tous les périphériques.

Ils sont *nécessaires* au fonctionnement (gestion d’énergie, boot, etc.) et *non désactivables* complètement par l’utilisateur. Certains laptops permettent de neutraliser partiellement Intel ME (`me_cleaner`), au prix de fonctionnalités. Pour la plupart des usages : on vit avec, en sachant que le matériel n’est pas totalement transparent.

### 11.7 *Fil rouge* — Olivier soupçonne une modification UEFI

Olivier M., dirigeant d’une PME de chiffrement, rentre d’un séjour à Pékin où son laptop a passé deux heures hors de sa vue à l’hôtel. À son retour, il constate que l’écran de démarrage met deux secondes de plus à afficher. Possible coïncidence, possible LogoFAIL. Il :

1. N’utilise pas l’appareil pour quoi que ce soit de sensible.
1. Compare la photo macro qu’il avait prise du boîtier interne avant départ avec une nouvelle photo.
1. Sort le disque et le déchiffre depuis un autre poste sain pour récupérer ses documents.
1. Retire le SSD, le détruit physiquement, considère le laptop comme grillé.

Le coût (un MacBook) est inférieur à l’incertitude.

-----

## Chapitre 12 — Chiffrement complet du disque

### 12.1 Pourquoi le chiffrement de session ne suffit pas

Un mot de passe utilisateur sans chiffrement disque est un théâtre. Quiconque démonte le disque accède aux fichiers via un autre système. Le chiffrement complet du disque (Full Disk Encryption, FDE) rend les données illisibles sans la clé de déchiffrement.

### 12.2 LUKS / dm-crypt sous Linux

**LUKS** (Linux Unified Key Setup) est la norme Linux. AES-XTS 256 bits par défaut, multiples slots de clés, possibilité d’utiliser TPM via `systemd-cryptenroll` pour déverrouillage automatique. Configuration typique : volume chiffré contenant un volume LVM, avec partition racine et home.

LUKS2 (2018+) apporte Argon2id pour la dérivation de clé — résistance aux attaques par force brute matérielle.

**Déni plausible** : LUKS ne le propose pas nativement. VeraCrypt (hérité de TrueCrypt) propose des volumes cachés, mais leur efficacité dépend du modèle d’adversaire. Si l’adversaire sait que VeraCrypt est installé, l’existence d’un volume caché est probable, ce qui peut tourner contre toi.

### 12.3 BitLocker

BitLocker chiffre les volumes Windows. AES-XTS 128 ou 256 bits, intégré au TPM 2.0. Trois modes :

- **TPM only** (par défaut sur Windows 11 Home) : déverrouillage automatique. Vulnérable à attaque physique BFU si attaquant compétent (extraction de clé via debug du TPM ou contournement contextuel).
- **TPM + PIN** : ajout d’un code court tapé au démarrage. Bien plus solide.
- **Startup key** sur USB : variation rare.

**Récupération** : par défaut, la clé de récupération est sauvegardée dans ton compte Microsoft cloud. C’est un compromis : tu n’es pas verrouillé hors de tes données si oubli du mot de passe, mais Microsoft (et qui le force) peut accéder à ta clé. Pour profil sensible : désactiver la sauvegarde cloud de la clé et la stocker hors ligne.

### 12.4 FileVault

FileVault chiffre les volumes macOS. AES-XTS 128 bits, intégré au Secure Enclave sur Apple Silicon. La clé est protégée par le Secure Enclave : impossible à extraire même avec accès physique total (à l’état de l’art public).

**Récupération** : par défaut, optionnel via iCloud ou clé de récupération imprimable. Choix : iCloud = confort, clé = autonomie.

### 12.5 Pre-Boot Authentication vs auto-déverrouillage TPM

**Pre-Boot Authentication (PBA)** : tu tapes le mot de passe au démarrage, avant que l’OS charge. Plus sécurisé, moins ergonomique.

**Auto-déverrouillage TPM** : le TPM libère la clé si l’état du système est conforme. Plus ergonomique. Le compromis : un attaquant qui maintient la cohérence d’état (par exemple en clonant l’appareil) peut potentiellement déverrouiller hors de ta présence.

Profil journaliste/HVT : PBA. Profil quotidien : TPM + PIN.

### 12.6 Conteneurs chiffrés

Au-dessus du chiffrement disque, des outils pour conteneurs individuels :

- **VeraCrypt** : conteneurs portables, support multi-OS, volumes cachés.
- **Cryptomator** : focalisé cloud (chiffre des dossiers destinés à Dropbox, Google Drive, etc.).
- **gocryptfs / EncFS** : montage chiffré transparent sous Linux.
- **Zed!** (Prim’X) : usage spécifique francophone (justice, AAI, secteur public) ; conteneurs auto-extractibles chiffrés ; reconnu CC EAL3+ et qualifié ANSSI ; pratique pour transmettre un dossier sensible à un correspondant non technique.

### 12.7 Attaques connues contre FDE

- **Cold boot attack** : la RAM conserve les données quelques secondes après extinction. Avec spray refroidisseur (azote ou simplement air comprimé inversé), ce délai s’étend à plusieurs minutes. Attaque réelle démontrée contre des laptops saisis allumés. Défense : utiliser des modes de sommeil profond qui purgent la RAM, privilégier l’extinction complète pour un appareil non utilisé, et choisir un OS qui efface la clé maître à la mise en veille (FileVault et BitLocker récents le font dans certaines configurations).
- **DMA via Thunderbolt / FireWire (historique)** : attaque par accès direct mémoire via port physique. Thunderbolt expose un canal DMA qui, mal configuré, permet à un périphérique connecté de lire la RAM. Démontrée par les attaques *Thunderspy* (2020) contre Thunderbolt 1/2/3. Mitigations : Intel a introduit Kernel DMA Protection sur les machines modernes ; macOS et Windows ont des modes d’autorisation des périphériques Thunderbolt. Défense additionnelle : désactiver Thunderbolt si non nécessaire, ou configurer IOMMU. Sur Linux, vérifier que IOMMU est actif (`dmesg | grep -i iommu`).
- **Sleep mode** : sur certains OS et configurations, le sleep maintient les clés de chiffrement disque en RAM pour permettre une reprise rapide. Saisir un laptop en sleep est donc proche de le saisir en AFU. La protection ne tient pleinement que sur appareil **éteint complètement**. Sur macOS, la commande `pmset -a destroyfvkeyonstandby 1` détruit la clé FileVault à l’entrée en hibernation. Sur Linux avec LUKS, `cryptsetup luksSuspend` purge la clé pendant le sleep. Sur Windows, BitLocker en mode TPM seul est vulnérable au démarrage sans intervention ; activer BitLocker avec PIN renforce.
- **Direct Memory Access via FireWire (obsolète mais culture utile)** : ancienne attaque sur laptops anciens, désormais rare.
- **Évolution récente — attaques sur TPM bus** : démontré par Andrew Tierney (Pen Test Partners, 2021) et chercheurs en 2023-2024, certains TPM discrets (puce séparée sur la carte mère) exposent les communications avec le CPU sur un bus LPC ou SPI qui peut être sniffé physiquement par un attaquant disposant du matériel. La clé BitLocker (en mode TPM seul) peut alors être extraite. Les TPM firmware (intégrés au CPU comme Pluton ou la Secure Enclave Apple) ne sont pas vulnérables à cette attaque. **Conséquence** : sur laptop Windows avec TPM 2.0 discret, BitLocker + PIN est meilleur que BitLocker TPM-only.
- **Côté SSD** : certains SSD revendiquent un chiffrement matériel transparent (self-encrypting drives, SED). Plusieurs travaux (Meijer & van Gastel, 2018) ont démontré que des implémentations SED commerciales étaient gravement défaillantes. Conclusion pratique : ne pas se reposer sur le chiffrement matériel SSD seul ; utiliser BitLocker / FileVault / LUKS par-dessus.

### 12.8 BFU vs AFU

**BFU (Before First Unlock)** : l’appareil a été redémarré et n’a pas encore été déverrouillé. La plupart des données utilisateur sont chiffrées avec une clé non encore dérivée. C’est l’état le plus sécurisé.

**AFU (After First Unlock)** : l’appareil a été déverrouillé au moins une fois depuis le démarrage. Beaucoup de clés sont en mémoire ou dans le keychain. Un appareil saisi en AFU est largement plus accessible aux outils forensiques (Cellebrite, GrayKey).

**Conséquence opérationnelle critique** : avant une frontière, une manifestation, une situation à risque de saisie — *éteindre complètement* l’appareil, pas seulement le verrouiller. La différence BFU/AFU est l’un des arbitrages les plus importants du quotidien sécurisé. iPhone : maintenir bouton + volume jusqu’à arrêt complet. Android : même principe. Une fonction « Lockdown Mode » sur certaines versions Android entraîne aussi un mode équivalent à BFU partiel.

### 12.9 Quand le chiffrement ne sert à rien

Si l’appareil est saisi *allumé et déverrouillé*, le chiffrement disque est sans effet : les clés sont actives, les fichiers sont en clair pour le système. C’est pourquoi la coercition (saisie avec personne consciente, déverrouillage par biométrie sans consentement actif) est si efficace, et pourquoi les juridictions divergent fortement sur l’admissibilité de l’usage forcé de biométrie (cf. Ch 37).

-----

## Chapitre 13 — Air gap, appareils dédiés et environnements isolés

### 13.1 Ce qu’est vraiment un air gap

Un **air gap** est l’isolation physique d’un système : aucune connexion réseau, aucune liaison sans fil active, idéalement aucune connexion Bluetooth, NFC, USB en service. L’air gap est une mesure radicale, utile pour des actifs cryptographiques d’extrême sensibilité : clés PGP maîtres, clés de signature de logiciels, semences de portefeuilles cryptomonnaie, archives ultra-sensibles.

L’air gap n’est pas la solution du quotidien. Il a un coût opérationnel élevé (transfert manuel par USB ou QR code, maintenance des mises à jour, latence d’usage). Il est valable seulement pour des cas où la valeur protégée justifie ce coût.

### 13.2 Cas d’usage légitimes

- **Clés PGP de signature** : si tu signes des logiciels distribués à grande échelle, la compromission de ta clé est catastrophique. Une station offline pour générer et utiliser cette clé est rationnelle.
- **Cold wallet cryptomonnaie** : la même logique. La majorité des vols de crypto provient de wallets connectés.
- **Archives sensibles** : documents source d’une enquête, exemplaires de référence.
- **Génération de secrets long terme** : clés racines, phrases de récupération.

### 13.3 Limites pratiques

Le transfert de données vers/depuis l’air gap est le maillon faible. Trois options :

- **USB** : risque BadUSB, malware. Mitigation : ne brancher sur l’air gap que des USB neuves, marquées, jamais re-circulées.
- **QR code** : pour de petits volumes (clé publique, transaction crypto signée). Sécurité visuelle.
- **Data diode** : matériel unidirectionnel (transfert que dans un sens). Existe commercialement, coûteux. Utilisé en environnement industriel et gouvernemental.

### 13.4 TEMPEST et side channels : culture générale

Les **side channels** sont des fuites d’information par des canaux non prévus : émissions électromagnétiques (écran, câble), acoustique (clavier audible), thermique, consommation électrique. La discipline TEMPEST (NSA / OTAN) standardise les mesures de blindage.

Pour un individu : ces attaques sont rares et coûteuses. Elles deviennent réalistes pour des HVT extrêmes. Mesures basiques de prudence : pas de travail sensible visible par fenêtre, pas de clavier proche de micro non sécurisé, pas de transmission radio (Wi-Fi/Bluetooth) sur l’air gap.

### 13.5 Quand l’air gap est utile, inutile ou dangereux

**Utile** : protection d’un secret extrêmement coûteux à recréer, dont la compromission est catastrophique.

**Inutile** : protection d’usages quotidiens (mail, navigation). L’air gap pour tout = inopérant.

**Dangereux** : faux sentiment de sécurité. Un air gap mal entretenu (USB infectés, mises à jour absentes, manipulation imprudente) peut être pire qu’une station sécurisée connectée, parce qu’on ne le surveille pas.

### 13.6 Workflow d’un appareil dédié

Un appareil air-gap typique :

1. **Acquisition** : matériel acheté en personne, payé cash idéalement (au moins pour profils Niveau 3), ouvert et photographié à l’achat. Pour des HVT extrêmes : achat dans un magasin choisi au dernier moment, après plusieurs heures de marche sans téléphone, dans une ville différente de la résidence.
1. **Installation initiale** : système d’exploitation minimal (Linux durci comme Debian ou Tails persisté, Qubes vault, OpenBSD pour profil exotique sérieux), aucun service réseau actif. Désactiver Bluetooth et Wi-Fi *au niveau matériel* si possible (cartes amovibles retirées physiquement sur certains laptops). Effacer le module Bluetooth/Wi-Fi de la BIOS-UEFI.
1. **Mise en service** : génération des secrets directement sur l’appareil. **Jamais d’import** depuis un autre système, car cela mettrait les secrets en contact avec un environnement non éprouvé. Pour une clé PGP maîtresse : `gpg --full-generate-key` avec 4096 bits RSA ou Ed25519, après avoir vérifié que l’entropie est suffisante.
1. **Sous-clés et révocation** : générer des sous-clés (signature, chiffrement, authentification) avec expiration courte (6-12 mois) qui seront exportées vers un appareil connecté pour usage quotidien. La clé maîtresse reste sur l’air gap. **Générer immédiatement le certificat de révocation** et le stocker hors-ligne (papier dans coffre, par exemple) : il sera la seule façon de révoquer la clé en cas de compromission ou de perte de l’air gap.
1. **Transfert sécurisé** : entrée des données par canal contrôlé.
- **USB neuve** : marquer la clé physiquement, n’écrire qu’une fois, formater en read-only après écriture, jamais réutiliser entre l’air gap et un autre système après une seule rotation.
- **QR code** : pour de petits volumes (clé publique, transaction crypto signée). Sécurité visuelle, scan via caméra du système connecté qui reste isolé du système air-gap.
- **Audio modem** (rare, profil HVT extrême) : transfert de petite quantité par audio entre deux machines.
- **Data diode** : matériel unidirectionnel commercial (Owl Cyber Defense, Waterfall Security) ; coûte plusieurs k€, utilisé en environnements industriels et gouvernementaux.
1. **Stockage** : coffre-fort physique, ou faraday bag, dans un lieu non public. Plusieurs copies dans des lieux distincts pour résilience (un exemplaire chez l’avocat ou parent de confiance) pour les secrets critiques (clés maîtres, semences crypto). Les copies doivent être identiques et l’usage doit garder la traçabilité.
1. **Audit** : périodicité régulière (semestrielle pour Niveau 3), vérification d’intégrité physique (vis, photos macro internes comparées), test de fonctionnement.
1. **Mise à jour** : difficulté structurelle de l’air gap. Soit on accepte de ne pas mettre à jour (et on accepte le risque CVE), soit on prépare une procédure de mise à jour disciplinée : téléchargement signé du paquet sur un système séparé, vérification de signature, transfert par USB neuve, application, retrait de l’USB. Cette procédure introduit un risque résiduel d’evil USB ; à arbitrer selon le threat model.
1. **Retraite** : effacement par `shred` sur tous les disques (HDD), `cryptographic erase` sur SSD via `hdparm --security-erase` ou équivalent, puis destruction physique (broyage, perçage de chaque plateau ou puce). Documentation de la destruction pour audit.

> 🟧 **Note de niveau** : l’air gap est typiquement une mesure Niveau 3. Pour Niveau 1, c’est inutile et excessif. Pour Niveau 2, c’est utile pour quelques secrets long terme (clé maître PGP de journaliste, semence d’un cold wallet familial conséquent) mais pas pour des opérations courantes.

-----

## Chapitre 14 — Durcissement Windows, macOS et Linux pour le quotidien

> **Niveau de posture (cf. Ch 2.6)** : ce chapitre couvre essentiellement le **Niveau 1** (hygiène essentielle de l’OS quotidien) avec des extensions vers le **Niveau 2** (sandboxing applicatif sérieux, AppArmor/SELinux personnalisés, Lockdown Mode macOS). Le **Niveau 3** se construit sur la base d’un OS durci selon ce chapitre, puis ajoute la compartimentation Qubes (Ch 17-18), Tails ou Whonix.

### 14.1 Windows 11 : baseline raisonnable

**Édition** : Pro ou Enterprise pour avoir BitLocker complet, Hyper-V, Windows Sandbox, et plus de contrôle sur la télémétrie. Home est limité.

**Compte** : préférer un compte local (contournement possible à l’installation en désactivant le Wi-Fi avant l’écran de connexion Microsoft, ou via `oobe\BypassNRO`). Si compte Microsoft requis, dissocier le compte cloud de l’usage local autant que possible.

**Télémétrie** : Group Policy `Allow Telemetry = Security` sur Enterprise, `Basic` ailleurs. Désactivation via Settings → Privacy. Limites : Microsoft conserve un niveau de télémétrie irréductible.

**Defender, SmartScreen, Tamper Protection** : activés, par défaut, fonctionnent bien sur Windows 11. Ne pas les désactiver sauf raison spécifique.

**Audit minimal** : sessions Microsoft account, audit `Sysmon` si tu es technique, désactivation des services inutiles via `services.msc` (avec prudence).

### 14.2 macOS

**FileVault** : activer dès la première utilisation.

**Gatekeeper et SIP** : laisser activés. Gatekeeper vérifie les signatures des applications installées. SIP (System Integrity Protection) empêche même root de modifier certaines parties système.

**XProtect** : antivirus intégré, mis à jour silencieusement. Pas de scan visible, mais protections actives.

**Lockdown Mode** (macOS Sonoma et plus, Ventura partiel) : conçu pour cibles à haut risque. Désactive certaines fonctionnalités (pièces jointes complexes en Messages, certaines APIs JS dans Safari, certains profils de configuration). Active uniquement si HVT.

**iCloud** : activer **Advanced Data Protection** dans Réglages → ton nom → iCloud → Protection avancée des données. Cela bascule en E2EE : iCloud Drive, photos, sauvegardes iCloud, notes, rappels, signets Safari, Mémos, et plus. Restent en non-E2EE : Mail, Contacts, Calendrier (pour raisons d’interopérabilité). ADP nécessite tous tes appareils sous version récente et une clé de récupération à conserver.

**Audit en 30 min** : Système → Confidentialité (revue des permissions par catégorie), Système → Sécurité (FileVault, Firewall, Lockdown Mode), désactivation des notifications sur écran verrouillé pour comptes sensibles.

### 14.3 Linux : choix de distribution

- **Debian stable** : ennuyeux au bon sens du terme. Stable, sûr, ennuyeux. Recommandé pour serveur ou usage discipliné.
- **Fedora Workstation** : récent, sécurité par défaut sérieuse (SELinux, sandboxing), bonne intégration GNOME.
- **Ubuntu LTS** : pragmatique, large communauté, certaines préoccupations sur Snap.
- **Kicksecure** : Debian durcie au démarrage (config sécurisée par défaut, plus de durcissement kernel). Base technique de Whonix. Pour usage régulier hors anonymat Tor.
- **Arch** : pour qui veut tout contrôler. Coût d’apprentissage élevé.
- **NixOS, Fedora Silverblue** : intéressants conceptuellement (système immuable, rollback). Pour utilisateurs avancés.

Le choix est moins important que la discipline qui suit.

### 14.4 AppArmor / SELinux : contrôle d’accès obligatoire

Linux moderne propose des modèles de **Mandatory Access Control** : règles obligatoires que même root respecte.

- **AppArmor** (Debian, Ubuntu, SUSE) : profils par application, syntaxe accessible.
- **SELinux** (Fedora, RHEL, CentOS) : plus puissant, syntaxe plus complexe.

Pour la plupart des utilisateurs : laisser le profil par défaut, sans désactiver. Pour usage durci : créer ou raffiner des profils pour les applications sensibles (navigateur, gestionnaire de mots de passe).

### 14.5 Sandboxing applicatif

- **Flatpak + bubblewrap** : isolement par défaut des applications Flatpak. Utile pour navigateurs (Firefox flatpak isolé), clients de messagerie.
- **Firejail** : sandbox basée sur namespaces et seccomp. Profils existants pour la plupart des applications courantes. Limite réelle de Firejail signalée par certains audits : peut élever des privilèges si mal configuré. Préférer Flatpak quand possible.
- **systemd-nspawn** : conteneurs légers, utile pour usages avancés.
- **Windows Sandbox** : sur Windows 11 Pro/Enterprise, environnement jetable pour test rapide.

### 14.6 Pare-feu local

Sortant souvent oublié. Les pare-feux par défaut bloquent l’entrant. Le sortant est par défaut autorisé : une application compromise peut exfiltrer.

- **Linux** : nftables (moderne) ou firewalld (Fedora) avec règles sortantes explicites pour applications sensibles. `OpenSnitch` propose un pare-feu interactif type Little Snitch.
- **macOS** : Little Snitch (commercial, référence) ou LuLu (open source) pour contrôler le sortant par application.
- **Windows** : Windows Defender Firewall permet règles sortantes (peu utilisé en pratique). GlassWire pour vue ergonomique.

### 14.7 Wayland vs X11

X11, hérité des années 80, n’isole pas les fenêtres entre elles : toute application connectée au serveur X peut lire les frappes clavier de toutes les autres, capturer l’écran, simuler des entrées. C’est un keylogger structurel.

**Wayland**, son remplaçant, isole. La plupart des distributions Linux desktop sont passées à Wayland par défaut (GNOME, KDE, Fedora). Pour usage durci : vérifier que tu es sur Wayland (`echo $XDG_SESSION_TYPE` → `wayland`).

### 14.8 Audit post-installation : checklist 30 minutes

1. Vérifier chiffrement disque actif.
1. Activer le pare-feu (par défaut Linux/macOS, vérifier Windows).
1. Auditer les comptes utilisateurs (un seul admin nécessaire, sessions sécurisées).
1. Désactiver les services non utilisés (Bluetooth si pas utilisé, Wi-Fi si filaire, partage SMB).
1. Activer les mises à jour automatiques pour le système et les drivers/firmware.
1. Configurer le gestionnaire de mots de passe (Ch 29).
1. Auditer les permissions de microphone, caméra, localisation pour chaque application.

### 14.9 Mention culturelle : OpenBSD, Fedora Silverblue, NixOS

- **OpenBSD** : focalisé sécurité depuis 30 ans, code audité, ergonomie spartiate. Pour serveurs ou utilisateurs convaincus.
- **Fedora Silverblue** : système immuable, rollback transactionnel. Concept séduisant, ergonomie en progression.
- **NixOS** : configuration entièrement déclarative, reproductibilité totale. Courbe d’apprentissage élevée.

Aucun n’est requis pour un cours générique. Les mentionner permet aux profils techniques d’explorer plus loin.

-----

## Chapitre 15 — Mobile : iOS durci, Android, GrapheneOS

> **Niveau de posture (cf. Ch 2.6)** : iPhone à jour + ADP + permissions auditées + reboot hebdomadaire = **Niveau 1**. iPhone + Lockdown Mode + reboot quotidien + Contact Key Verification, *ou* GrapheneOS sur Pixel dédié avec profils = **Niveau 2**. GrapheneOS avec profils stricts + MVT mensuel + iVerify + reboot biquotidien + sans aucune app Google Play Services privilégiée = **Niveau 3**.

### 15.1 Le constat brutal

Le smartphone est, pour la plupart des gens, le plus gros risque privacy. Il contient :

- L’historique de localisation continu.
- Les contacts et leurs métadonnées de communication.
- Les photos avec EXIF.
- Les comptes bancaires et messageries.
- La biométrie (empreinte, visage).
- Le microphone et la caméra (potentiellement actifs).

Aucun durcissement ne compense l’usage d’un smartphone non sécurisé pour des activités sensibles. Le choix de la plateforme et de sa configuration est plus important que l’ordinateur.

### 15.2 Identifiants mobiles

- **IMEI** : identifiant matériel du téléphone, transmis à chaque connexion cellulaire.
- **IMSI** : identifiant de la SIM, transmis au réseau (IMSI catchers le captent).
- **Numéro de téléphone** : visible à chaque appel/SMS.
- **eSIM** : équivalent fonctionnel à SIM physique, gérée logiciellement.
- **Wi-Fi MAC, BT MAC** : adresses uniques, randomisées sur les OS modernes (Ch 22).
- **Advertising ID** (IDFA iOS, AAID Android) : désactivables.

Les identifiants publicitaires mobiles — IDFA sur iOS, AAID sur Android, plus généralement MAID — ne doivent pas être vus comme de simples paramètres marketing. Dans l’écosystème publicitaire, ils peuvent servir de pivots de corrélation entre applications, lieux, horaires et comportements. Dans une logique ADINT, un identifiant publicitaire peut devenir un quasi-identifiant de renseignement : il ne donne pas directement le nom civil de la personne, mais permet souvent de la réidentifier par ses routines, ses lieux de vie, ses lieux de travail et ses déplacements récurrents. 

À côté des identifiants publicitaires fournis par l’OS, il faut également surveiller les initiatives d’identification publicitaire portées par les opérateurs télécoms. Des systèmes comme Utiq illustrent une tendance post-cookie : exploiter des signaux opérateur et des jetons pseudonymes pour permettre du ciblage publicitaire sans s’appuyer uniquement sur les cookies tiers ou les identifiants publicitaires classiques. Pour l’OPSEC, cela confirme qu’un téléphone personnel connecté à son abonnement mobile habituel reste un fort pivot de corrélation.

Pour un téléphone sensible, la règle est simple : moins il contient d’applications financées par la publicité, moins il émet de signaux exploitables. Un téléphone destiné à une manifestation, un rendez-vous source, une mission terrain ou une réunion confidentielle ne devrait pas contenir d’applications grand public à SDK publicitaires.

### 15.3 Téléphone personnel et lieux sensibles

Pour un profil exposé, le téléphone personnel ne doit pas être considéré comme un simple outil de communication. C’est un capteur permanent : localisation, Wi-Fi, Bluetooth, identifiants publicitaires, applications installées, SDK tiers, comptes personnels, habitudes de déplacement.

Dans un lieu sensible — base militaire, site industriel critique, réunion confidentielle, rendez-vous source, manifestation à risque, cabinet d’avocat, rédaction, ambassade, centrale nucléaire, site de défense — le téléphone personnel peut créer une fuite sans aucune compromission technique. Il suffit qu’une application collecte de la localisation ou qu’un identifiant publicitaire soit réobservé à plusieurs reprises pour reconstruire une routine.

Règle pratique : plus le lieu est sensible, plus l’appareil doit être minimaliste. Pour les usages critiques, préférer un téléphone dédié, sans compte personnel, sans applications publicitaires, avec localisation strictement limitée, identifiant publicitaire désactivé ou réinitialisé, et applications installées selon une logique de liste blanche.

### 15.4 Localisation

Cinq sources, agrégées :

- **GPS** : précision 5-10 m.
- **Wi-Fi** : géolocalisation par triangulation des SSID environnants (bases Google, Apple, Skyhook).
- **Bluetooth/BLE** : beacons commerciaux dans les magasins, AirTags.
- **Cellulaire** : antennes-relais, précision 100 m à 1 km en zone dense.
- **Magnétomètre, baromètre** : utilisés pour étage dans bâtiment.

Désactiver le « Service de localisation » d’un cran n’éteint pas les couches passives. Wi-Fi et Bluetooth peuvent renseigner sur ta position même avec GPS coupé.

### 15.5 iOS comme baseline

**Code long** : 6 chiffres minimum, alphanumérique idéalement. Face ID/Touch ID = confort, mais peuvent être contournés sous coercition.

**Lockdown Mode** (iOS 16+) : désactive des fonctionnalités exploitées par les spyware mercenaires : pièces jointes complexes en Messages, certaines APIs WebKit (JIT JavaScript), profils de configuration, accessoires filaires sur appareil verrouillé, etc. Coût ergonomique modéré, gain de sécurité réel. **À activer** pour les HVT (journalistes, dissidents, lanceurs d’alerte, avocats sensibles).

**Restrictions sur écran verrouillé** : désactiver les notifications, Siri, contrôle USB en lock screen, Wallet, retour d’appel.

**iCloud** : ADP activée (cf. Ch 14).

**Permissions** : audit Réglages → Confidentialité → revue par catégorie (Localisation, Contacts, Photos, Micro, Caméra, Suivi). Le « Tracking » d’apps (ATT) est désactivable globalement.

### 15.6 Advanced Data Protection iCloud

ADP, depuis fin 2022 (US) et étendu mondialement en 2023, bascule en chiffrement de bout en bout les catégories suivantes :

- iCloud Drive
- Photos
- Sauvegardes iCloud de l’appareil (incluant les sauvegardes WhatsApp si stockées dans iCloud)
- Notes, Rappels
- Signets et historique Safari
- Mémos vocaux
- et plusieurs autres catégories (Apple liste précisément sur https://support.apple.com)

**Important — ce qui reste NON chiffré de bout en bout, même avec ADP activé** : iCloud Mail, Contacts iCloud, et Calendrier iCloud restent accessibles à Apple. Apple le documente explicitement : ces trois services utilisent des standards d’interopérabilité (SMTP/IMAP pour Mail, CalDAV/CardDAV pour Calendrier et Contacts) qui imposent que les serveurs Apple traitent les contenus en clair pour pouvoir communiquer avec les autres fournisseurs et appareils tiers. Si la confidentialité de Mail, Contacts ou Calendrier est critique, il faut soit utiliser un autre fournisseur (Proton Mail, Proton Contacts, Proton Calendar), soit accepter que ces données restent visibles à Apple et exposées en cas de réquisition judiciaire.

**Conditions d’activation** : tous tes appareils Apple doivent être sur une version récente (iOS 16.2+, macOS 13.1+). Une clé de récupération doit être conservée (sinon perte totale des données ADP en cas d’oubli du code d’appareil et impossibilité d’utiliser un appareil de confiance). Apple ne peut plus aider à la récupération une fois ADP activé — c’est l’objet même du dispositif.

### 15.7 Android stock vs OEM

Android **AOSP** (Android Open Source Project) : propre, mais aucun OEM ne livre AOSP pur.

**Google Pixel + Android stock** : meilleure version d’Android pour mises à jour rapides, sécurité, mais entièrement intégré aux services Google.

**Samsung, Xiaomi, Oppo, Vivo, Huawei…** : surcouches OEM avec collecte propre, télémétrie additionnelle, apps préinstallées. Mises à jour de sécurité variables. Pour les Chinois (Xiaomi, Oppo, Vivo, Honor, Huawei) : préoccupations spécifiques liées à la juridiction d’origine et à des cas documentés de collecte excessive.

### 15.8 GrapheneOS

**Philosophie** : OS Android dégooglisé, durci, focalisé privacy et sécurité. Développement actif, mise à jour rapide des patches Android upstream.

**Caractéristiques** :

- Hardening kernel et userspace.
- Sandboxed Google Play : les services Google Play installés dans une sandbox utilisateur normale, pas en privilégié système. Tu peux utiliser des apps qui en dépendent sans donner à Google les privilèges habituels.
- **Profils utilisateurs** : isolation forte entre profils. Idéal pour séparer pro/perso/sensible.
- **Storage Scopes** : permission granulaire « cette app peut accéder à *ce dossier* seulement », alternative à « toutes les photos ».
- **Contact Scopes** : équivalent pour les contacts.
- **Network permission** : un toggle pour empêcher une app d’accéder au réseau, indépendamment du fait qu’elle le demande.
- Verified Boot avec clés signées par GrapheneOS, attestable.

**Limites** :

- Pixel uniquement (Pixel 6 et supérieurs sont privilégiés).
- Certaines apps (banking, gouvernementales) refusent de fonctionner sur ROM custom (anti-tampering).
- Pas de Google Wallet (Google Pay) — paiement sans contact via app bancaire dépend des apps.
- Carplay/Android Auto support limité.

**Pour qui** : tous ceux qui veulent un mobile sérieusement durci et peuvent vivre avec les contraintes. Recommandé pour journalistes, activistes, dirigeants exposés, professionnels cyber.

### 15.9 CalyxOS, LineageOS (et le cas DivestOS)

- **CalyxOS** : alternative à GrapheneOS, philosophie similaire mais MicroG préinstallé (réimplémentation libre des Google Play Services). Moins de hardening que GrapheneOS, mais position éthique intéressante. Maintenu activement.
- **LineageOS** : Android communautaire générique. Pas focalisé sécurité, mais utile pour prolonger la vie d’appareils non supportés par OEM. Important : LineageOS sans signatures Verified Boot du constructeur réduit la sécurité matérielle. À utiliser pour des appareils secondaires non sensibles.
- **DivestOS** : fork LineageOS focalisé sécurité, supportait plus de modèles que GrapheneOS. **Le projet a annoncé son arrêt fin 2024**, le développeur principal ayant cessé la maintenance active. À ne plus utiliser comme recommandation pour un déploiement nouveau ; les utilisateurs existants doivent planifier une migration vers une plateforme maintenue (GrapheneOS si Pixel disponible, CalyxOS sinon, ou retour à un OS constructeur à jour selon profil).

### 15.10 Choix matériel et support

GrapheneOS exige du **Pixel récent** (Pixel 6+). Pixel 8 et Pixel 8a sont actuellement (2025-2026) de bons points d’entrée : support OEM jusqu’en 2030-2031, Titan M2, performances correctes.

**Durée de mises à jour** : Pixel 8/8a → 7 ans (2030 pour le 8). iPhone → environ 6-7 ans en pratique. Samsung → 7 ans (Galaxy S22+ et plus). Reste du marché : 2-4 ans.

Acheter un téléphone sans support de mises à jour pour 5+ ans est une erreur d’investissement sécuritaire.

### 15.11 Permissions et hygiène applicative

- **Claviers tiers** : SwiftKey, Gboard avec sync cloud → mauvaise idée pour usage sensible. Pour GrapheneOS : utiliser le clavier intégré, ou AnySoftKeyboard sans cloud.
- **Presse-papiers** : surveillance possible par apps en arrière-plan. iOS 14+ alerte. Android 12+ aussi. Vigilance.
- **Trackers dans applis** : la plupart des applis grand public en intègrent. Outil utile : **Exodus Privacy** (analyse des trackers d’une app).
- **Permissions à scopes** : sur GrapheneOS, Storage Scopes et Contact Scopes ; sur iOS, sélection de photos précises plutôt que photo library complète.

### 15.12 Séparation pro/perso/sensible

Sur GrapheneOS : profils utilisateurs distincts. Chaque profil a son propre espace, ses apps, ses comptes. Bascule par swipe down.

Sur iOS : pas de profils utilisateurs (limitation iOS persistante). Solution : appareils distincts pour usages sensibles, ou « Focus Modes » avec filtres d’apps.

### 15.13 Reboot quotidien

Les spyware mercenaires modernes (Pegasus, Predator, Graphite) reposent souvent sur des exploits **non persistants** : un redémarrage les efface. L’attaquant doit alors re-infecter, ce qui multiplie ses traces et son coût.

Le **reboot quotidien** (ou hebdomadaire pour les moins exposés) est l’une des mesures les plus simples et les plus efficaces contre les attaques avancées. Cinq secondes par jour. À adopter systématiquement pour les HVT.

### 15.14 *Fil rouge* — Léa migre vers Pixel 8a + GrapheneOS

Léa, après son audit, achète un Pixel 8a en magasin (cash, anonymement), flashe GrapheneOS le soir même, et configure :

- **Profil principal** : usage quotidien sans Google, Signal, Proton Mail, navigateur Vanadium.
- **Profil pro** : son compte journalistique, Slack rédaction, outils pros.
- **Profil enquête** : compartiment dédié, SimpleX, Tor Browser sur mobile, aucun compte personnel.

Elle conserve son iPhone perso pour la vie civile (banque, photos famille), avec ADP activée. Reboot quotidien le matin. Six semaines de transition pour s’habituer.

> 🟩 **À retenir de la Partie 3**
> 
> - Hardware = racine de confiance. Tout ce qui suit en dépend.
> - Secure Boot + TPM = colonne vertébrale de la sécurité moderne. À activer, à comprendre, à mettre à jour.
> - FDE est indispensable, mais ne protège pas si l’appareil est saisi AFU.
> - Air gap : pour des secrets rares, pas pour le quotidien.
> - Mobile = plus gros risque privacy. iPhone durci ou GrapheneOS sont aujourd’hui les meilleurs choix.
> - Reboot quotidien : 5 secondes, gain réel.

-----
