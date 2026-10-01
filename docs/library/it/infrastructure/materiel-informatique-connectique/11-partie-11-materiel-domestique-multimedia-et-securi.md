---
title: Partie 11 — Matériel domestique, multimédia et sécurité matérielle
source: IT/06 Infrastructure & architecture/Matériel informatique & connectique.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

---

## 43. Box, TV connectée, consoles, NAS, impression

### La box internet : plusieurs appareils en un

- **Modem** : convertit le signal opérateur (via ONT en fibre) en réseau utilisable.
- **Routeur** : distribue Internet et gère le réseau local.
- **Switch** : les ports Ethernet à l'arrière.
- **Point d'accès Wi-Fi** : la partie sans fil.

Fonctions intégrées : **NAT** (partage d'une IP publique), **DHCP** (attribution d'IP locales), **DNS** (traduit les noms de sites en adresses IP).

> **🔧 Cas concret (support)**
> « Internet est coupé. » Premier réflexe : un appareil en **Ethernet** fonctionne-t-il ? Si oui → problème Wi-Fi, pas Internet. Si non → voyants de la box/ONT, panne opérateur ? On décompose la chaîne (opérateur → routeur → local → Wi-Fi) au lieu de tout redémarrer au hasard. (Détaillé au chapitre 47.)

### TV connectée

La qualité d'image dépend autant du **processeur vidéo** (upscaling, gestion du mouvement) que de la dalle. Le **système Smart TV** soulève des questions de mises à jour (limitées dans le temps) et de **collecte de données (ACR**, reconnaissance automatique de contenu pour la pub ciblée), souvent désactivable dans les réglages de confidentialité.

### Consoles de jeu

Architecture proche du PC (CPU/GPU AMD, SSD NVMe), **HDMI 2.1** pour la 4K 120 Hz et le VRR, manettes sans fil, réseau Ethernet (recommandé) ou Wi-Fi.

### NAS

Petit serveur de stockage en réseau : centralise les fichiers, héberge les sauvegardes des PC, parfois des services (médiathèque, conteneurs). RAID pour la tolérance de panne — mais **RAID ≠ sauvegarde** (chapitre 16), donc une copie hors NAS reste nécessaire.

### Imprimantes et scanners

Connexion USB-B / Ethernet / Wi-Fi. **Jet d'encre** (photo/couleur, encre qui sèche si peu utilisée) vs **laser** (rapide, économique, idéal usage irrégulier et texte).

> **⚠️ Erreur fréquente**
> Une imprimante jet d'encre utilisée rarement coûte cher en têtes bouchées. Pour un usage occasionnel surtout textuel, une **laser** est plus économique et fiable sur la durée.

---

## 44. Sécurité matérielle

USB malveillant, firmware, DMA, équipements exposés

Chapitre transversal : tout le matériel vu jusqu'ici a une **surface d'attaque physique**. C'est un angle mort fréquent, et un sujet clé en cyber.

### USB malveillant

Le port USB est une porte d'entrée privilégiée parce qu'il combine données et confiance implicite.

- **BadUSB** : une clé (ou un câble, un chargeur) dont le **firmware** a été reprogrammé pour se faire passer pour un autre périphérique — typiquement un **clavier**. Branchée, elle « tape » à toute vitesse des commandes malveillantes. L'OS lui fait confiance car « c'est un clavier ».
- **Rubber Ducky / câbles piégés** : des outils prêts à l'emploi de ce principe, parfois cachés dans un câble de charge d'apparence normale.
- **Juice jacking** : une borne de recharge USB publique (aéroport, gare) modifiée pour exfiltrer des données ou injecter du code via le port.

> **🔒 Sécurité — défenses USB**
> Ne jamais brancher une clé/un câble trouvé ou d'origine inconnue. Sur poste sensible : désactiver l'autorun, restreindre les classes USB autorisées (politiques d'OS, ports verrouillés), utiliser un **« USB condom »** (adaptateur data-blocker) sur les bornes publiques, ou charger sur une prise secteur plutôt qu'un port USB inconnu. En entreprise, le contrôle des périphériques (device control) bloque les classes non autorisées.

### Attaques DMA (Thunderbolt / PCIe)

Parce que Thunderbolt (et le PCIe en général) donne un **accès mémoire direct (DMA)** pour la performance, un périphérique malveillant branché peut tenter de **lire/écrire directement dans la RAM** sans passer par l'OS — pour extraire des clés de chiffrement, des mots de passe, ou injecter du code (famille « Thunderspy »).

> **🔒 Sécurité — défenses DMA**
> Les protections modernes existent : **IOMMU / VT-d / Kernel DMA Protection** cloisonnent ce qu'un périphérique peut adresser en mémoire. Les réglages **Thunderbolt Security Levels** (autorisation utilisateur avant qu'un périphérique fonctionne) et le verrouillage de l'écran (qui bloque les nouveaux périphériques DMA) limitent le risque. À retenir : un ordinateur **verrouillé mais allumé**, laissé sans surveillance avec un port Thunderbolt ouvert, n'est pas à l'abri.

### Sécurité du firmware

Le **firmware** (chapitre 11) s'exécute *sous* l'OS : une compromission y est très grave (persistante, invisible, survit à une réinstallation). Concerne UEFI, mais aussi BMC (iDRAC/iLO), cartes réseau, SSD.

> **🔒 Sécurité — défenses firmware**
> Maintenir les firmwares à jour (UEFI, BMC, périphériques), activer **Secure Boot** pour bloquer un bootkit non signé, s'appuyer sur le **TPM** pour mesurer l'intégrité du démarrage, et ne jamais exposer un **BMC (iDRAC/iLO/IPMI)** sur Internet — réseau d'administration isolé obligatoire (chapitre 15).

### Équipements réseau souvent oubliés : box, NAS, imprimantes, caméras

Ce sont des **ordinateurs connectés à part entière** (CPU, firmware, parfois disque), et des cibles fréquentes parce qu'on les sécurise rarement :

- **Box / routeur** : changer les identifiants par défaut, mettre à jour le firmware, désactiver l'administration distante inutile, segmenter l'IoT sur un réseau séparé.
- **NAS** : ne **jamais** l'exposer directement à Internet ; accès via **VPN**, double authentification, mises à jour. Les NAS grand public sont des cibles régulières de ransomwares.
- **Imprimantes** : changer les mots de passe par défaut, mettre à jour le firmware ; elles stockent parfois des documents et offrent un point d'entrée discret sur le réseau.
- **Caméras IP / objets connectés** : mots de passe par défaut notoirement exploités (réseaux de botnets). À isoler sur un VLAN/réseau invité.

> **🎯 À retenir**
> La règle d'or de la sécurité matérielle tient en une phrase : **tout ce qui a un firmware et une adresse réseau est un ordinateur à sécuriser** — y compris la box, le NAS, l'imprimante et la caméra. Les trois réflexes universels : changer les identifiants par défaut, mettre à jour le firmware, segmenter le réseau (séparer l'IoT et l'administration du reste).

---
