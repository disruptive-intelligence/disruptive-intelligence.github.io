---
title: Chapitre 16 — Machines virtuelles, live USB et environnements jetables
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 4 — Environnements de session sensible
  - index.md
---

## 16.1 Principe : enveloppe jetable autour d’une activité

Les machines virtuelles et les environnements live permettent d’exécuter un système isolé du système hôte. L’activité sensible se déroule dans cette enveloppe, qui est jetée à la fin. C’est l’inverse de la logique « durcir l’OS principal pour tout » : on accepte que l’OS principal n’est pas immunisé, on l’utilise pour ce qui ne risque pas, et on bascule en environnement séparé pour ce qui risque.

## 16.2 Hyperviseurs courants

- **VirtualBox** (Oracle) : gratuit, multi-plateforme, populaire. Performances modestes. Récents soucis de support sur Apple Silicon.
- **KVM/QEMU** (Linux) : intégré au noyau, performant. virt-manager pour interface graphique.
- **Hyper-V** (Windows Pro/Enterprise) : intégré, bonne intégration.
- **VMware Workstation Pro** (devenu gratuit en 2024 pour usage personnel) : commercial historique, performant.
- **UTM** (macOS, gratuit) : surcouche QEMU, support Apple Silicon, références pour macOS.

## 16.3 Snapshots et restauration

Le **snapshot** capture un état complet de la VM. Avant chaque session sensible : snapshot. Après : revert au snapshot propre. Cela garantit qu’aucun artefact (cookies, fichiers, malware potentiel) ne survit à la session.

Discipline minimale : un snapshot « propre » initial, un revert systématique en fin de session, jamais d’usage long terme sans rotation.

## 16.4 Limites de l’isolation par VM

- **Évasion de VM** : sortir d’une VM pour compromettre l’hôte est techniquement possible mais reste rare. Demande typiquement un zero-day sur l’hyperviseur, ressources et motivation. Des CVE existent régulièrement (Xen, KVM, VMware, VirtualBox) — la pratique défensive est de garder l’hyperviseur à jour et de ne pas utiliser une VM seule comme barrière critique pour activité ultra-sensible.
- **Évasion par périphérique partagé** : USB passthrough, audio, presse-papiers, clipboard partagé entre VM et hôte sont des vecteurs de fuite. Sur VirtualBox et VMware, désactiver le partage clipboard et drag-and-drop par défaut. Sur Qubes, ces canaux sont gérés explicitement par qrexec avec validation utilisateur à chaque transfert.
- **Fuites matérielles** : information CPU (CPUID, modèle, microcode), adresse MAC virtuelle qui peut être prévisible, configuration réseau de la VM peuvent renseigner sur l’hôte. Une VM ne te rend pas anonyme — elle isole l’application.
- **Performance** : émulation graphique, accélération limitée. Pas pour gaming sensible ou tâches GPU-intensives. Pour usages standard (bureautique, navigation), KVM/QEMU avec virtio est très performant.
- **Sortie réseau** : la VM utilise par défaut le réseau de l’hôte. Pour anonymat, ajouter Tor (cf. Whonix Ch 17). Pour isolation forte, configurer la VM en NAT (et non bridged) pour éviter l’exposition directe au LAN.
- **Side channels** : Spectre, Meltdown et leurs successeurs ont permis dans certaines conditions à une VM de lire de la mémoire hôte. Patches kernel et microcode CPU restent indispensables. Pour profil Niveau 3 : préférer la compartimentation par appareil physique aux VMs pour les secrets vraiment critiques.

## 16.5 Cas d’usage typiques

- **Ouverture de document suspect** : reçu d’une source inconnue, lien Telegram non vérifié, PDF d’apparence douteuse → VM jetable, revert immédiat.
- **Navigation à risque** : exploration de site OSINT borderline, test de comportement applicatif → VM avec snapshot.
- **Environnement de développement séparé** : projets clients distincts isolés.

## 16.6 Dangerzone

**Dangerzone** (Freedom of the Press Foundation) automatise le scénario « j’ai reçu un PDF, je veux le lire sans risquer mon système ». Le PDF est converti dans un conteneur isolé en image puis re-rendu en PDF propre. Tous les éléments actifs (JavaScript, formulaires, liens malveillants) disparaissent. Pratique pour journalistes recevant des documents.

## 16.7 Live USB

Booter depuis une clé USB un OS qui n’écrit rien sur le disque local. Le système est en RAM et meurt à l’extinction. Tails et Kicksecure proposent des images live. Avantages : trivial à déployer, aucune persistance. Inconvénients : pas de configuration personnalisée sauvegardée (sauf persistance chiffrée Tails), démarrage lent.

## 16.8 Erreur fréquente

Une VM **ne cache pas ton IP**. Elle ne te rend pas anonyme. Elle isole l’application. Confondre les deux conduit à utiliser une VM pour « être sûr d’être anonyme sur ce site », ce qui ne fonctionne pas. Pour anonymat réseau, il faut Tor (Ch 21) ou Whonix.

-----
