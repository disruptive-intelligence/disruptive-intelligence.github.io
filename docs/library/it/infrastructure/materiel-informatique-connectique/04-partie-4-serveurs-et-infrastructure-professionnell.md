---
title: Partie 4 — Serveurs et infrastructure professionnelle
source: IT/Culture/Materiel_informatique-connectique-andco.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - index.md
---

C'est l'une des parties les plus densifiées, car c'est aussi la moins couverte dans les cours grand public.

---

## 14. Qu'est-ce qu'un serveur ? Formats et redondance

Un serveur n'est pas un « gros PC » : c'est une machine conçue pour **rester disponible en continu**.

Différences clés :

- **Disponibilité** : tourner 24/7 pendant des années.
- **Redondance** : composants doublés (alimentations, disques, parfois ventilateurs) pour qu'une panne n'arrête pas le service.
- **Maintenance à chaud (hot-swap)** : remplacer un élément sans éteindre.
- **Gestion hors-bande** : administration même OS planté (chapitre 15).

### Formats

- **Tower** : comme une tour PC, pour PME sans baie.
- **Rack** : format plat vissé dans une **baie 19 pouces**, mesuré en **U** (1U ≈ 4,4 cm). Serveurs 1U, 2U, 4U… Plus de U = plus de disques et un meilleur refroidissement. On dimensionne une baie en additionnant les U.
- **Blade** : lames ultra-compactes partageant un châssis commun (alimentation, refroidissement, réseau). Densité maximale en datacenter.
- **Appliance** : matériel + logiciel livrés ensemble pour une fonction (pare-feu, sauvegarde, stockage).

> **🎯 À retenir**
> Philosophie d'un PC : « être rapide ». Philosophie d'un serveur : « ne jamais s'arrêter ». Tout le matériel (redondance, ECC, hot-swap, gestion hors-bande) découle de cette différence.

---

## 15. Composants serveur et gestion hors-bande

- **CPU Xeon (Intel) / EPYC (AMD)** : beaucoup de cœurs, grande capacité de RAM ECC, multi-socket possible.
- **RAM ECC** : correction d'erreurs (chapitre 7), indispensable quand une corruption silencieuse aurait des conséquences graves.
- **Alimentations redondantes** : deux blocs (ou plus), souvent sur **deux circuits électriques distincts**. L'un lâche, l'autre prend le relais sans coupure.
- **Disques hot-swap** : extractibles à chaud par la façade (voir backplane, chapitre 16).
- **Ventilation redondante** et flux d'air contraint (couloirs chaud/froid en datacenter).

### Gestion hors-bande (out-of-band) : iDRAC / iLO / IPMI

C'est un point essentiel et spécifique au monde serveur. Un **contrôleur de gestion (BMC, Baseboard Management Controller)** est un **mini-ordinateur indépendant intégré au serveur**, avec sa **propre adresse réseau** et sa propre alimentation de veille. Il fonctionne **même si le serveur principal est éteint ou planté**.

- **iDRAC** (Dell), **iLO** (HPE) : interfaces propriétaires.
- **IPMI** : le standard ouvert sous-jacent.

Ce qu'il permet, à distance, sans se déplacer :

- allumer / éteindre / redémarrer le serveur ;
- voir l'écran depuis le POST (console distante / KVM-over-IP) ;
- monter une image ISO pour **réinstaller l'OS à distance** ;
- lire l'état matériel (températures, ventilateurs, pannes de disque).

> **🔧 Cas concret (admin sys)**
> Un serveur ne répond plus à 3 h du matin. Via l'iDRAC/iLO (accessible indépendamment de l'OS), l'administrateur voit l'écran bloqué au démarrage, force un redémarrage, entre dans l'UEFI, corrige — depuis chez lui. C'est tout l'intérêt du hors-bande.

> **🔒 Sécurité**
> Un BMC est une cible de choix : il a un contrôle total sur le serveur et tourne en permanence. On ne l'expose **jamais** sur Internet, on le place sur un **réseau d'administration isolé (VLAN dédié)**, on change les identifiants par défaut et on maintient son firmware à jour. Un iLO/iDRAC compromis = serveur entièrement compromis, sous l'OS.

---

## 16. RAID matériel vs logiciel, HBA, backplane

### Les niveaux de RAID

Le RAID assemble plusieurs disques pour la sécurité et/ou la performance.

| Niveau | Principe | Tolérance de panne | Remarque |
|---|---|---|---|
| **RAID 0** | Données réparties (striping) | ❌ Aucune | 1 disque mort = tout perdu. Rapide mais risqué. |
| **RAID 1** | Miroir (copie identique) | 1 disque | Simple et sûr, capacité divisée par 2. |
| **RAID 5** | Données + 1 parité (3+ disques) | 1 disque | Reconstruction longue et risquée sur gros disques. |
| **RAID 6** | Double parité (4+ disques) | 2 disques | Plus sûr que RAID 5 pour les grosses grappes. |
| **RAID 10** | Miroir + striping (4+ disques) | 1 par paire | Rapide *et* sûr, bon compromis. |

> **🎯 À retenir — LE point capital**
> **Un RAID n'est PAS une sauvegarde.** Il protège contre la *panne matérielle d'un disque*, pas contre la suppression accidentelle, un ransomware, une corruption logique ou un incendie — qui se répliquent instantanément sur toute la grappe. Une vraie sauvegarde est *séparée*, *versionnée*, et idéalement *hors site et déconnectée*.

### RAID matériel vs logiciel : une distinction qui change la gestion

| | **RAID matériel** | **RAID logiciel** |
|---|---|---|
| Géré par | Une **carte contrôleur RAID** dédiée | L'OS (mdadm Linux, Storage Spaces Windows, **ZFS**, Btrfs) |
| Charge CPU | Déportée sur la carte | Sur le CPU de la machine (négligeable aujourd'hui) |
| Cache + batterie (BBU) | Souvent, protège le cache en cas de coupure | Géré autrement (journal, onduleur) |
| Portabilité | Liée au modèle de contrôleur (panne = même modèle requis) | Lisible sur n'importe quelle machine compatible |
| Visibilité des disques | Le contrôleur masque souvent l'état réel | L'OS voit chaque disque (SMART direct) |

> **🎯 À retenir**
> Le RAID **logiciel moderne** (ZFS en tête) est devenu très répandu, y compris en entreprise et en homelab : il offre intégrité des données (détection de corruption silencieuse), snapshots et portabilité, sans dépendre d'une carte propriétaire. Le RAID **matériel** reste fréquent sur les serveurs de marque pour le hot-swap intégré et le cache protégé par batterie.

### HBA : le composant souvent confondu avec un contrôleur RAID

Un **HBA** (Host Bus Adapter) est une carte qui connecte des disques (SAS/SATA) à la machine **en les présentant directement à l'OS**, sans couche RAID intermédiaire. C'est précisément ce qu'on veut pour un RAID **logiciel** comme ZFS, qui a besoin d'un accès brut à chaque disque (et à son SMART).

> **⚠️ Erreur fréquente**
> Utiliser une carte RAID matériel configurée en RAID pour faire tourner ZFS par-dessus : ZFS perd la vision directe des disques et son intégrité est compromise. La bonne pratique est un **HBA** (ou une carte RAID basculée en mode « IT »/pass-through) qui expose les disques tels quels.

### Backplane

Le **backplane** (fond de panier) est la carte à l'arrière des baies de disques en façade d'un serveur. Les disques hot-swap s'y enfichent directement : il distribue alimentation et données (SAS/SATA) et permet l'extraction à chaud sans câbler chaque disque individuellement. C'est ce qui rend possible le remplacement d'un disque défaillant en quelques secondes, sans éteindre la machine.

> **🔧 Cas concret**
> Une LED orange s'allume sur un tiroir de disque en façade. L'admin extrait le disque à chaud, insère un disque neuf : le backplane et le contrôleur lancent automatiquement la **reconstruction** (rebuild) de la grappe RAID, sans interruption de service. Pendant le rebuild, la grappe est vulnérable à une seconde panne — d'où l'intérêt du RAID 6 sur les grosses grappes.

---

## 17. Stockage en réseau : DAS, NAS, SAN

Trois façons de présenter du stockage, souvent confondues.

- **DAS** (Direct Attached Storage) : disques branchés *directement* à une machine (disque externe, baie reliée par SAS). Simple, non partagé sur le réseau.
- **NAS** (Network Attached Storage) : un boîtier de stockage *sur le réseau* qui partage des **fichiers** (SMB, NFS). Idéal maison/PME, accès multi-utilisateurs.
- **SAN** (Storage Area Network) : un réseau **dédié** haute performance (Fibre Channel ou iSCSI) qui présente du stockage *en mode bloc* — la machine le voit comme un disque local. Pour la virtualisation à grande échelle.

Distinction clé : **NAS = niveau fichier**, **SAN = niveau bloc**. Un NAS dit « voici un dossier partagé » ; un SAN dit « voici un disque, fais-en ce que tu veux ».

- **Snapshots** : « photos » instantanées de l'état du stockage pour revenir en arrière. Utiles mais ne remplacent pas une sauvegarde externe.

> **🔧 Cas concret (cyber)**
> Une entreprise touchée par un ransomware avait un NAS en RAID 6 « pour la sécurité ». Le rançongiciel a chiffré les fichiers, répliqués aussitôt sur toute la grappe. Sans sauvegarde déconnectée (*air gap*) ou hors site immuable, tout était perdu. La règle **3-2-1** (3 copies, 2 supports, 1 hors site) et des snapshots immuables auraient sauvé les données. RAID ≠ sauvegarde, en grandeur réelle.

---

## 18. La baie : switch, routeur, firewall, PDU, brassage

Les équipements d'une armoire réseau :

- **Switch** : aiguille le trafic *au sein* d'un réseau local (relie les machines). Notion détaillée en Partie 9.
- **Routeur** : relie *plusieurs réseaux* (typiquement le LAN à Internet).
- **Pare-feu (firewall)** : filtre le trafic selon des règles ; souvent une appliance dédiée.
- **Patch panel** : panneau où aboutissent les câbles fixes du bâtiment, reliés aux switchs par de courts cordons (**brassage**). Détaillé au chapitre 38.
- **Onduleur (UPS)** : batterie de secours (chapitre 42).
- **PDU** (Power Distribution Unit) : multiprise professionnelle de baie, parfois pilotable à distance (redémarrer électriquement un équipement bloqué — utile combiné au hors-bande du chapitre 15).

> **🎯 À retenir**
> Le **brassage** via patch panel distingue une baie pro propre d'un nid de câbles : les câbles fixes du bâtiment ne bougent jamais, on ne touche qu'aux cordons courts en façade. Une PDU pilotable + un BMC (iDRAC/iLO) permettent de relancer à distance un équipement totalement figé, sans déplacement.

---
