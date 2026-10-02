---
title: 'Chapitre 43 — Revente, don et réparation : effacer avant de céder'
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie VIII — Quand ça tourne mal : réagir et se reconstruire'
  - index.md
---

*Un appareil cédé sans précaution emporte des années de données personnelles. Ce chapitre traite la fin de vie numérique des appareils — un angle mort fréquent.*

## 43.1 Pourquoi c'est sérieux

Un téléphone, un ordinateur, ou un disque dur revendu sur Leboncoin ou Vinted contient potentiellement : photos, conversations, emails, mots de passe enregistrés, sessions ouvertes vers des comptes bancaires, documents administratifs, contacts. Une réinitialisation rapide ne suffit pas toujours — surtout sur des PC anciens où un « formatage simple » laisse les données récupérables avec des outils gratuits. Plusieurs études ont montré que les disques achetés d'occasion contiennent encore des données personnelles dans 40 à 60 % des cas.

## 43.2 Téléphone : la procédure correcte

**iPhone** : (1) sauvegarder ce qu'on veut conserver (iCloud ou ordinateur), (2) se déconnecter de l'iCloud — Réglages > [votre nom] > Déconnexion (cette étape désactive Find My et le verrouillage d'activation, sans quoi le nouvel utilisateur ne pourra rien faire de l'appareil), (3) Réglages > Général > Transférer ou réinitialiser l'iPhone > Effacer contenu et réglages, (4) retirer la SIM physique et désactiver l'eSIM si présente.

**Android** : (1) sauvegarder, (2) chiffrer le téléphone si ce n'est pas déjà fait (le chiffrement préalable garantit que les données résiduelles sont illisibles après réinitialisation), (3) déconnecter le compte Google — Paramètres > Comptes > Google > Supprimer le compte (essentiel pour désactiver le verrouillage d'activation FRP — Factory Reset Protection), (4) Paramètres > Système > Réinitialisation > Effacer toutes les données, (5) retirer SIM et eSIM.

## 43.3 Ordinateur : la procédure correcte

**Windows** : la réinitialisation native de Windows (Paramètres > Système > Récupération > Réinitialiser ce PC) propose une option « Supprimer mes fichiers et nettoyer le lecteur » — choisir cette option, qui écrase les données après suppression et rend la récupération beaucoup plus difficile. Pour un appareil avec données très sensibles : un effacement sécurisé (outil DBAN, ou commande `cipher /w:` sur la partition concernée) est plus rigoureux.

**macOS** : Préférences/Réglages > Effaçeur des contenus et réglages (sur les Mac Apple Silicon et T2 — l'opération est rapide et sécurisée car les données sont chiffrées par défaut, et l'effacement détruit la clé de chiffrement, rendant les données irrécupérables). Sur les Mac Intel sans T2 : Utilitaire de disque depuis le mode récupération + réinstallation de macOS.

**Disques durs externes et SSD** : un disque dur classique (HDD) doit être écrasé en plusieurs passes (DBAN, ou outil natif). Un SSD doit être effacé avec la commande secure erase (souvent disponible dans le BIOS ou via un outil constructeur — Samsung Magician, Crucial Storage Executive, etc.). En cas de doute, ou pour un disque très ancien : la destruction physique (perceuse, marteau sur les plateaux pour un HDD) reste la solution la plus sûre.

## 43.4 Le cas du SAV et de la réparation

Confier un téléphone, un ordinateur, ou un disque pour réparation = donner accès aux données. Avant de l'envoyer : sauvegarder, et idéalement réinitialiser si le SAV n'a pas besoin d'accéder aux données pour diagnostiquer (souvent le cas pour les pannes physiques — écran, batterie, port). Si le SAV demande le mot de passe pour faire des tests : changer ce mot de passe pour un mot de passe temporaire, et le re-changer au retour. Au retour de SAV : vérifier que rien n'a été ajouté (apps installées, profils MDM, comptes liés), changer le mot de passe principal, et idéalement faire une nouvelle réinitialisation si on a des doutes.

## 43.5 Cartes SD, clés USB, NAS

**Cartes SD et clés USB** : un formatage rapide n'efface pas les données. Utiliser un outil d'effacement sécurisé (Eraser sur Windows, sdelete, ou la commande `dd if=/dev/zero` sur Linux/macOS) avant de les céder ou de les jeter.

**NAS, anciens disques internes d'ordinateurs** : les retirer physiquement avant de céder un PC (ou les effacer rigoureusement comme indiqué plus haut). Une vente d'occasion d'un ordinateur avec disque non effacé est l'un des cas les plus fréquents de fuite de données personnelles.

**Imprimantes connectées et photocopieurs** : la mémoire interne peut contenir des copies des documents imprimés/scannés. Vérifier dans le manuel s'il existe une procédure de réinitialisation de la mémoire interne avant la cession.

---

<a id="chapitre-44"></a>
