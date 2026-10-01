---
title: Chapitre 13 — Air gap, appareils dédiés et environnements isolés
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 3 — Sécurité matérielle, racine de confiance et isolation
  - index.md
---

## 13.1 Ce qu’est vraiment un air gap

Un **air gap** est l’isolation physique d’un système : aucune connexion réseau, aucune liaison sans fil active, idéalement aucune connexion Bluetooth, NFC, USB en service. L’air gap est une mesure radicale, utile pour des actifs cryptographiques d’extrême sensibilité : clés PGP maîtres, clés de signature de logiciels, semences de portefeuilles cryptomonnaie, archives ultra-sensibles.

L’air gap n’est pas la solution du quotidien. Il a un coût opérationnel élevé (transfert manuel par USB ou QR code, maintenance des mises à jour, latence d’usage). Il est valable seulement pour des cas où la valeur protégée justifie ce coût.

## 13.2 Cas d’usage légitimes

- **Clés PGP de signature** : si tu signes des logiciels distribués à grande échelle, la compromission de ta clé est catastrophique. Une station offline pour générer et utiliser cette clé est rationnelle.
- **Cold wallet cryptomonnaie** : la même logique. La majorité des vols de crypto provient de wallets connectés.
- **Archives sensibles** : documents source d’une enquête, exemplaires de référence.
- **Génération de secrets long terme** : clés racines, phrases de récupération.

## 13.3 Limites pratiques

Le transfert de données vers/depuis l’air gap est le maillon faible. Trois options :

- **USB** : risque BadUSB, malware. Mitigation : ne brancher sur l’air gap que des USB neuves, marquées, jamais re-circulées.
- **QR code** : pour de petits volumes (clé publique, transaction crypto signée). Sécurité visuelle.
- **Data diode** : matériel unidirectionnel (transfert que dans un sens). Existe commercialement, coûteux. Utilisé en environnement industriel et gouvernemental.

## 13.4 TEMPEST et side channels : culture générale

Les **side channels** sont des fuites d’information par des canaux non prévus : émissions électromagnétiques (écran, câble), acoustique (clavier audible), thermique, consommation électrique. La discipline TEMPEST (NSA / OTAN) standardise les mesures de blindage.

Pour un individu : ces attaques sont rares et coûteuses. Elles deviennent réalistes pour des HVT extrêmes. Mesures basiques de prudence : pas de travail sensible visible par fenêtre, pas de clavier proche de micro non sécurisé, pas de transmission radio (Wi-Fi/Bluetooth) sur l’air gap.

## 13.5 Quand l’air gap est utile, inutile ou dangereux

**Utile** : protection d’un secret extrêmement coûteux à recréer, dont la compromission est catastrophique.

**Inutile** : protection d’usages quotidiens (mail, navigation). L’air gap pour tout = inopérant.

**Dangereux** : faux sentiment de sécurité. Un air gap mal entretenu (USB infectés, mises à jour absentes, manipulation imprudente) peut être pire qu’une station sécurisée connectée, parce qu’on ne le surveille pas.

## 13.6 Workflow d’un appareil dédié

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
