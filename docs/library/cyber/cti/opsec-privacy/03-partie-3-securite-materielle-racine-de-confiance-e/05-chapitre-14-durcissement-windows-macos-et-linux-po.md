---
title: Chapitre 14 — Durcissement Windows, macOS et Linux pour le quotidien
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 3 — Sécurité matérielle, racine de confiance et isolation
  - index.md
---

> **Niveau de posture (cf. Ch 2.6)** : ce chapitre couvre essentiellement le **Niveau 1** (hygiène essentielle de l’OS quotidien) avec des extensions vers le **Niveau 2** (sandboxing applicatif sérieux, AppArmor/SELinux personnalisés, Lockdown Mode macOS). Le **Niveau 3** se construit sur la base d’un OS durci selon ce chapitre, puis ajoute la compartimentation Qubes (Ch 17-18), Tails ou Whonix.

## 14.1 Windows 11 : baseline raisonnable

**Édition** : Pro ou Enterprise pour avoir BitLocker complet, Hyper-V, Windows Sandbox, et plus de contrôle sur la télémétrie. Home est limité.

**Compte** : préférer un compte local (contournement possible à l’installation en désactivant le Wi-Fi avant l’écran de connexion Microsoft, ou via `oobe\BypassNRO`). Si compte Microsoft requis, dissocier le compte cloud de l’usage local autant que possible.

**Télémétrie** : Group Policy `Allow Telemetry = Security` sur Enterprise, `Basic` ailleurs. Désactivation via Settings → Privacy. Limites : Microsoft conserve un niveau de télémétrie irréductible.

**Defender, SmartScreen, Tamper Protection** : activés, par défaut, fonctionnent bien sur Windows 11. Ne pas les désactiver sauf raison spécifique.

**Audit minimal** : sessions Microsoft account, audit `Sysmon` si tu es technique, désactivation des services inutiles via `services.msc` (avec prudence).

## 14.2 macOS

**FileVault** : activer dès la première utilisation.

**Gatekeeper et SIP** : laisser activés. Gatekeeper vérifie les signatures des applications installées. SIP (System Integrity Protection) empêche même root de modifier certaines parties système.

**XProtect** : antivirus intégré, mis à jour silencieusement. Pas de scan visible, mais protections actives.

**Lockdown Mode** (macOS Sonoma et plus, Ventura partiel) : conçu pour cibles à haut risque. Désactive certaines fonctionnalités (pièces jointes complexes en Messages, certaines APIs JS dans Safari, certains profils de configuration). Active uniquement si HVT.

**iCloud** : activer **Advanced Data Protection** dans Réglages → ton nom → iCloud → Protection avancée des données. Cela bascule en E2EE : iCloud Drive, photos, sauvegardes iCloud, notes, rappels, signets Safari, Mémos, et plus. Restent en non-E2EE : Mail, Contacts, Calendrier (pour raisons d’interopérabilité). ADP nécessite tous tes appareils sous version récente et une clé de récupération à conserver.

**Audit en 30 min** : Système → Confidentialité (revue des permissions par catégorie), Système → Sécurité (FileVault, Firewall, Lockdown Mode), désactivation des notifications sur écran verrouillé pour comptes sensibles.

## 14.3 Linux : choix de distribution

- **Debian stable** : ennuyeux au bon sens du terme. Stable, sûr, ennuyeux. Recommandé pour serveur ou usage discipliné.
- **Fedora Workstation** : récent, sécurité par défaut sérieuse (SELinux, sandboxing), bonne intégration GNOME.
- **Ubuntu LTS** : pragmatique, large communauté, certaines préoccupations sur Snap.
- **Kicksecure** : Debian durcie au démarrage (config sécurisée par défaut, plus de durcissement kernel). Base technique de Whonix. Pour usage régulier hors anonymat Tor.
- **Arch** : pour qui veut tout contrôler. Coût d’apprentissage élevé.
- **NixOS, Fedora Silverblue** : intéressants conceptuellement (système immuable, rollback). Pour utilisateurs avancés.

Le choix est moins important que la discipline qui suit.

## 14.4 AppArmor / SELinux : contrôle d’accès obligatoire

Linux moderne propose des modèles de **Mandatory Access Control** : règles obligatoires que même root respecte.

- **AppArmor** (Debian, Ubuntu, SUSE) : profils par application, syntaxe accessible.
- **SELinux** (Fedora, RHEL, CentOS) : plus puissant, syntaxe plus complexe.

Pour la plupart des utilisateurs : laisser le profil par défaut, sans désactiver. Pour usage durci : créer ou raffiner des profils pour les applications sensibles (navigateur, gestionnaire de mots de passe).

## 14.5 Sandboxing applicatif

- **Flatpak + bubblewrap** : isolement par défaut des applications Flatpak. Utile pour navigateurs (Firefox flatpak isolé), clients de messagerie.
- **Firejail** : sandbox basée sur namespaces et seccomp. Profils existants pour la plupart des applications courantes. Limite réelle de Firejail signalée par certains audits : peut élever des privilèges si mal configuré. Préférer Flatpak quand possible.
- **systemd-nspawn** : conteneurs légers, utile pour usages avancés.
- **Windows Sandbox** : sur Windows 11 Pro/Enterprise, environnement jetable pour test rapide.

## 14.6 Pare-feu local

Sortant souvent oublié. Les pare-feux par défaut bloquent l’entrant. Le sortant est par défaut autorisé : une application compromise peut exfiltrer.

- **Linux** : nftables (moderne) ou firewalld (Fedora) avec règles sortantes explicites pour applications sensibles. `OpenSnitch` propose un pare-feu interactif type Little Snitch.
- **macOS** : Little Snitch (commercial, référence) ou LuLu (open source) pour contrôler le sortant par application.
- **Windows** : Windows Defender Firewall permet règles sortantes (peu utilisé en pratique). GlassWire pour vue ergonomique.

## 14.7 Wayland vs X11

X11, hérité des années 80, n’isole pas les fenêtres entre elles : toute application connectée au serveur X peut lire les frappes clavier de toutes les autres, capturer l’écran, simuler des entrées. C’est un keylogger structurel.

**Wayland**, son remplaçant, isole. La plupart des distributions Linux desktop sont passées à Wayland par défaut (GNOME, KDE, Fedora). Pour usage durci : vérifier que tu es sur Wayland (`echo $XDG_SESSION_TYPE` → `wayland`).

## 14.8 Audit post-installation : checklist 30 minutes

1. Vérifier chiffrement disque actif.
1. Activer le pare-feu (par défaut Linux/macOS, vérifier Windows).
1. Auditer les comptes utilisateurs (un seul admin nécessaire, sessions sécurisées).
1. Désactiver les services non utilisés (Bluetooth si pas utilisé, Wi-Fi si filaire, partage SMB).
1. Activer les mises à jour automatiques pour le système et les drivers/firmware.
1. Configurer le gestionnaire de mots de passe (Ch 29).
1. Auditer les permissions de microphone, caméra, localisation pour chaque application.

## 14.9 Mention culturelle : OpenBSD, Fedora Silverblue, NixOS

- **OpenBSD** : focalisé sécurité depuis 30 ans, code audité, ergonomie spartiate. Pour serveurs ou utilisateurs convaincus.
- **Fedora Silverblue** : système immuable, rollback transactionnel. Concept séduisant, ergonomie en progression.
- **NixOS** : configuration entièrement déclarative, reproductibilité totale. Courbe d’apprentissage élevée.

Aucun n’est requis pour un cours générique. Les mentionner permet aux profils techniques d’explorer plus loin.

-----
