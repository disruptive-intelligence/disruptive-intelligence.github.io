---
title: Chapitre 12 — Chiffrement complet du disque
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 3 — Sécurité matérielle, racine de confiance et isolation
  - index.md
---

## 12.1 Pourquoi le chiffrement de session ne suffit pas

Un mot de passe utilisateur sans chiffrement disque est un théâtre. Quiconque démonte le disque accède aux fichiers via un autre système. Le chiffrement complet du disque (Full Disk Encryption, FDE) rend les données illisibles sans la clé de déchiffrement.

## 12.2 LUKS / dm-crypt sous Linux

**LUKS** (Linux Unified Key Setup) est la norme Linux. AES-XTS 256 bits par défaut, multiples slots de clés, possibilité d’utiliser TPM via `systemd-cryptenroll` pour déverrouillage automatique. Configuration typique : volume chiffré contenant un volume LVM, avec partition racine et home.

LUKS2 (2018+) apporte Argon2id pour la dérivation de clé — résistance aux attaques par force brute matérielle.

**Déni plausible** : LUKS ne le propose pas nativement. VeraCrypt (hérité de TrueCrypt) propose des volumes cachés, mais leur efficacité dépend du modèle d’adversaire. Si l’adversaire sait que VeraCrypt est installé, l’existence d’un volume caché est probable, ce qui peut tourner contre toi.

## 12.3 BitLocker

BitLocker chiffre les volumes Windows. AES-XTS 128 ou 256 bits, intégré au TPM 2.0. Trois modes :

- **TPM only** (par défaut sur Windows 11 Home) : déverrouillage automatique. Vulnérable à attaque physique BFU si attaquant compétent (extraction de clé via debug du TPM ou contournement contextuel).
- **TPM + PIN** : ajout d’un code court tapé au démarrage. Bien plus solide.
- **Startup key** sur USB : variation rare.

**Récupération** : par défaut, la clé de récupération est sauvegardée dans ton compte Microsoft cloud. C’est un compromis : tu n’es pas verrouillé hors de tes données si oubli du mot de passe, mais Microsoft (et qui le force) peut accéder à ta clé. Pour profil sensible : désactiver la sauvegarde cloud de la clé et la stocker hors ligne.

## 12.4 FileVault

FileVault chiffre les volumes macOS. AES-XTS 128 bits, intégré au Secure Enclave sur Apple Silicon. La clé est protégée par le Secure Enclave : impossible à extraire même avec accès physique total (à l’état de l’art public).

**Récupération** : par défaut, optionnel via iCloud ou clé de récupération imprimable. Choix : iCloud = confort, clé = autonomie.

## 12.5 Pre-Boot Authentication vs auto-déverrouillage TPM

**Pre-Boot Authentication (PBA)** : tu tapes le mot de passe au démarrage, avant que l’OS charge. Plus sécurisé, moins ergonomique.

**Auto-déverrouillage TPM** : le TPM libère la clé si l’état du système est conforme. Plus ergonomique. Le compromis : un attaquant qui maintient la cohérence d’état (par exemple en clonant l’appareil) peut potentiellement déverrouiller hors de ta présence.

Profil journaliste/HVT : PBA. Profil quotidien : TPM + PIN.

## 12.6 Conteneurs chiffrés

Au-dessus du chiffrement disque, des outils pour conteneurs individuels :

- **VeraCrypt** : conteneurs portables, support multi-OS, volumes cachés.
- **Cryptomator** : focalisé cloud (chiffre des dossiers destinés à Dropbox, Google Drive, etc.).
- **gocryptfs / EncFS** : montage chiffré transparent sous Linux.
- **Zed!** (Prim’X) : usage spécifique francophone (justice, AAI, secteur public) ; conteneurs auto-extractibles chiffrés ; reconnu CC EAL3+ et qualifié ANSSI ; pratique pour transmettre un dossier sensible à un correspondant non technique.

## 12.7 Attaques connues contre FDE

- **Cold boot attack** : la RAM conserve les données quelques secondes après extinction. Avec spray refroidisseur (azote ou simplement air comprimé inversé), ce délai s’étend à plusieurs minutes. Attaque réelle démontrée contre des laptops saisis allumés. Défense : utiliser des modes de sommeil profond qui purgent la RAM, privilégier l’extinction complète pour un appareil non utilisé, et choisir un OS qui efface la clé maître à la mise en veille (FileVault et BitLocker récents le font dans certaines configurations).
- **DMA via Thunderbolt / FireWire (historique)** : attaque par accès direct mémoire via port physique. Thunderbolt expose un canal DMA qui, mal configuré, permet à un périphérique connecté de lire la RAM. Démontrée par les attaques *Thunderspy* (2020) contre Thunderbolt 1/2/3. Mitigations : Intel a introduit Kernel DMA Protection sur les machines modernes ; macOS et Windows ont des modes d’autorisation des périphériques Thunderbolt. Défense additionnelle : désactiver Thunderbolt si non nécessaire, ou configurer IOMMU. Sur Linux, vérifier que IOMMU est actif (`dmesg | grep -i iommu`).
- **Sleep mode** : sur certains OS et configurations, le sleep maintient les clés de chiffrement disque en RAM pour permettre une reprise rapide. Saisir un laptop en sleep est donc proche de le saisir en AFU. La protection ne tient pleinement que sur appareil **éteint complètement**. Sur macOS, la commande `pmset -a destroyfvkeyonstandby 1` détruit la clé FileVault à l’entrée en hibernation. Sur Linux avec LUKS, `cryptsetup luksSuspend` purge la clé pendant le sleep. Sur Windows, BitLocker en mode TPM seul est vulnérable au démarrage sans intervention ; activer BitLocker avec PIN renforce.
- **Direct Memory Access via FireWire (obsolète mais culture utile)** : ancienne attaque sur laptops anciens, désormais rare.
- **Évolution récente — attaques sur TPM bus** : démontré par Andrew Tierney (Pen Test Partners, 2021) et chercheurs en 2023-2024, certains TPM discrets (puce séparée sur la carte mère) exposent les communications avec le CPU sur un bus LPC ou SPI qui peut être sniffé physiquement par un attaquant disposant du matériel. La clé BitLocker (en mode TPM seul) peut alors être extraite. Les TPM firmware (intégrés au CPU comme Pluton ou la Secure Enclave Apple) ne sont pas vulnérables à cette attaque. **Conséquence** : sur laptop Windows avec TPM 2.0 discret, BitLocker + PIN est meilleur que BitLocker TPM-only.
- **Côté SSD** : certains SSD revendiquent un chiffrement matériel transparent (self-encrypting drives, SED). Plusieurs travaux (Meijer & van Gastel, 2018) ont démontré que des implémentations SED commerciales étaient gravement défaillantes. Conclusion pratique : ne pas se reposer sur le chiffrement matériel SSD seul ; utiliser BitLocker / FileVault / LUKS par-dessus.

## 12.8 BFU vs AFU

**BFU (Before First Unlock)** : l’appareil a été redémarré et n’a pas encore été déverrouillé. La plupart des données utilisateur sont chiffrées avec une clé non encore dérivée. C’est l’état le plus sécurisé.

**AFU (After First Unlock)** : l’appareil a été déverrouillé au moins une fois depuis le démarrage. Beaucoup de clés sont en mémoire ou dans le keychain. Un appareil saisi en AFU est largement plus accessible aux outils forensiques (Cellebrite, GrayKey).

**Conséquence opérationnelle critique** : avant une frontière, une manifestation, une situation à risque de saisie — *éteindre complètement* l’appareil, pas seulement le verrouiller. La différence BFU/AFU est l’un des arbitrages les plus importants du quotidien sécurisé. iPhone : maintenir bouton + volume jusqu’à arrêt complet. Android : même principe. Une fonction « Lockdown Mode » sur certaines versions Android entraîne aussi un mode équivalent à BFU partiel.

## 12.9 Quand le chiffrement ne sert à rien

Si l’appareil est saisi *allumé et déverrouillé*, le chiffrement disque est sans effet : les clés sont actives, les fichiers sont en clair pour le système. C’est pourquoi la coercition (saisie avec personne consciente, déverrouillage par biométrie sans consentement actif) est si efficace, et pourquoi les juridictions divergent fortement sur l’admissibilité de l’usage forcé de biométrie (cf. Ch 37).

-----
