---
title: Chapitre 11 — Firmware, UEFI, Secure Boot, TPM et chaîne de démarrage
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 3 — Sécurité matérielle, racine de confiance et isolation
  - index.md
---

## 11.1 Qu’est-ce que le firmware et pourquoi c’est critique

Le **firmware** est le code qui s’exécute avant ton système d’exploitation, et qui le charge. Il vit dans une puce de la carte mère, accessible avant tout antivirus, tout chiffrement, tout système de détection. Un firmware compromis = persistance totale, invisible, irrémédiable par réinstallation du système.

UEFI a remplacé le BIOS historique en apportant : démarrage plus rapide, prise en charge de disques > 2 To, et surtout *Secure Boot*, qui vérifie cryptographiquement chaque étape de la chaîne de démarrage.

## 11.2 Secure Boot : principe et limites

Secure Boot vérifie que chaque composant chargé (bootloader, noyau, drivers) est signé par une autorité de confiance. Ce qui n’est pas signé ne s’exécute pas. Cela bloque les rootkits qui s’injectaient au démarrage.

Mais Secure Boot a été attaqué :

- **BlackLotus** (2022-2023) : bootkit UEFI capable de bypass Secure Boot via une signature légitime mais vulnérable de bootloader Windows.
- **LogoFAIL** (2023) : exploit dans le parsing d’images BMP/PNG affichées au démarrage permettant l’exécution de code avant Secure Boot.

Conséquence : Secure Boot est *nécessaire* mais pas *suffisant*. Sa désactivation laisse une fenêtre d’attaque ouverte ; son activation, sans mise à jour firmware, laisse aussi des fenêtres connues.

## 11.3 TPM 2.0

Le **Trusted Platform Module** est une puce dédiée au stockage de clés cryptographiques et à la mesure de l’état du système. Il est utilisé typiquement pour :

- Stocker la clé de déchiffrement disque (FileVault, BitLocker, LUKS+systemd-cryptenroll).
- Mesurer la chaîne de démarrage (Measured Boot) et libérer ces clés *seulement* si l’état correspond à un état attendu.
- Attester à un service distant que l’appareil n’a pas été modifié.

**Effet pratique** : avec TPM 2.0 et déverrouillage automatique du disque, ton ordinateur déverrouille tout seul s’il démarre dans un état attendu, mais si quelqu’un a modifié le firmware, le bootloader ou les paramètres TPM, le déverrouillage échoue et tu es prévenu d’une intrusion. C’est puissant — mais cela suppose que tu surveilles les échecs (souvent un échec TPM est interprété par l’utilisateur comme un bug à contourner, ce qui annule la protection).

## 11.4 Coreboot, Heads, Pureboot

Pour qui veut sortir du firmware constructeur (souvent opaque) :

- **Coreboot** : firmware open source minimaliste, supporté sur certains ThinkPad et autres modèles.
- **Heads** : firmware sécurisé basé sur Coreboot, conçu pour la sécurité physique (vérification cryptographique de tout le boot + clé GPG matérielle).
- **PureBoot** : commercial (Purism), basé sur Coreboot + Heads.

Ces options sont réservées à un public technique et acceptant une perte de fonctionnalités (suspend parfois cassé, certaines fonctions matérielles indisponibles).

## 11.5 Mises à jour firmware

Sur Linux, **fwupd** + le LVFS (Linux Vendor Firmware Service) permettent des mises à jour automatiques de firmware pour les marques compatibles (Dell, Lenovo récents, HP, Framework, certains autres). C’est l’un des chantiers les plus aboutis de Linux desktop ces dernières années.

Sur Windows, les mises à jour firmware passent par Windows Update pour les marques OEM intégrées.

Sur macOS, les mises à jour firmware sont incluses dans les mises à jour système.

Sur Android, dépend du constructeur. Pixel et iPhone reçoivent les mises à jour rapidement. Marques moyennes : variable. Marques basses : souvent rien après deux ans.

## 11.6 Limites : Intel ME, AMD PSP

Tous les CPU Intel récents intègrent un **Management Engine** (ME), tous les AMD un **Platform Security Processor** (PSP). Ce sont des sous-systèmes propriétaires fonctionnant à un niveau supérieur au système d’exploitation, avec accès complet à la mémoire, au réseau, à tous les périphériques.

Ils sont *nécessaires* au fonctionnement (gestion d’énergie, boot, etc.) et *non désactivables* complètement par l’utilisateur. Certains laptops permettent de neutraliser partiellement Intel ME (`me_cleaner`), au prix de fonctionnalités. Pour la plupart des usages : on vit avec, en sachant que le matériel n’est pas totalement transparent.

## 11.7 *Fil rouge* — Olivier soupçonne une modification UEFI

Olivier M., dirigeant d’une PME de chiffrement, rentre d’un séjour à Pékin où son laptop a passé deux heures hors de sa vue à l’hôtel. À son retour, il constate que l’écran de démarrage met deux secondes de plus à afficher. Possible coïncidence, possible LogoFAIL. Il :

1. N’utilise pas l’appareil pour quoi que ce soit de sensible.
1. Compare la photo macro qu’il avait prise du boîtier interne avant départ avec une nouvelle photo.
1. Sort le disque et le déchiffre depuis un autre poste sain pour récupérer ses documents.
1. Retire le SSD, le détruit physiquement, considère le laptop comme grillé.

Le coût (un MacBook) est inférieur à l’incertitude.

-----
