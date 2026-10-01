---
title: Chapitre 18 — Qubes OS en pratique
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 4 — Environnements de session sensible
  - index.md
---

compartimentation avancée et workflows sensibles

## 18.1 Architecture

Qubes OS repose sur Xen. **Dom0** est le qube administrateur, isolé, sans réseau direct. Au-dessus, des **templates** (Fedora, Debian, Whonix Gateway, Whonix Workstation) servent de base aux **app qubes**, légers, qui partagent le template mais ont leurs propres `/home`.

Trois qubes système :

- **sys-net** : gère les interfaces réseau physiques. C’est le seul qube avec accès direct aux périphériques réseau.
- **sys-firewall** : entre sys-net et les app qubes, applique des règles de pare-feu.
- **sys-usb** : isole les périphériques USB. Aucun USB ne touche dom0.

## 18.2 Qubes critiques

- **vault** : qube *offline* (aucune connexion réseau autorisée), stocke gestionnaire de mots de passe, clés GPG, secrets. Communication avec autres qubes via copier-coller contrôlé ou qrexec.
- **work** : usage professionnel.
- **personal** : usage personnel.
- **banking** : un qube par institution si paranoïaque, isolé.
- **anon-whonix** : un qube Workstation Whonix pour navigation anonyme.
- **disposable VMs** (dispVM) : qubes éphémères, créés à la demande, détruits à la fermeture. Idéal pour ouvrir un fichier suspect.

## 18.3 Workflow « ouvrir un fichier suspect »

Tu reçois un PDF de provenance douteuse. Sur Qubes :

1. Fichier reçu dans `personal`.
1. Clic droit → « Open in DisposableVM ».
1. Un qube jetable Fedora se crée, ouvre le PDF.
1. Si le PDF contient un exploit, seule la dispVM est compromise.
1. Tu ferme la fenêtre → la dispVM est détruite.
1. Ton `personal` est intact.

## 18.4 Workflow « identités séparées »

Tu sépares pseudo et identité civile. Sur Qubes :

- `personal` : compte Google, Facebook, identité civile, réseau via sys-firewall direct.
- `journalist-pub` : ton compte Twitter de plume publique, ProtonMail dédié, idem.
- `journalist-anon` : qube relié à sys-whonix, pour les comptes vraiment anonymes (Tor pour tout).

Chaque identité a son qube. Tu ne mélanges jamais.

## 18.5 Qubes + Whonix en production

Configuration :

- **sys-whonix** : Gateway, route le trafic via Tor.
- **anon-whonix** : Workstation, configuré pour utiliser sys-whonix comme réseau. Navigation Tor Browser, comptes pseudonymes.
- Autres qubes (banking, personal) routent via sys-firewall (réseau direct, pas Tor) — parce que tu ne veux *pas* de Tor pour ton banking.

## 18.6 Modèle de menace contre lequel Qubes est efficace

- Malware classique : confiné à un qube, ne se propage pas.
- Exploit navigateur : confiné au qube qui héberge le navigateur.
- Compromission d’une app spécifique : la dispVM est jetée.
- Erreur humaine : ouvrir un fichier dans le mauvais qube est plus difficile, parce que les qubes sont visuellement codés par couleur.

## 18.7 Modèle de menace contre lequel Qubes n’est PAS efficace

- Compromission de **dom0** : si dom0 tombe, tout tombe. Donc dom0 doit rester minimaliste, sans réseau, sans installation tierce.
- Exploit de l’hyperviseur Xen : possible mais rare. Mises à jour critiques.
- Attaques matérielles (Spectre, Meltdown, et successeurs) : nécessitent attention et patches.
- Attaque physique avec accès non détecté : Qubes ne change pas la donne.

## 18.8 Coût et ergonomie

- **Matériel** : 16 GB RAM minimum (32 recommandé), CPU avec virtualisation et IOMMU, GPU compatible, SSD rapide.
- **Apprentissage** : compter 2-4 semaines pour fluidité opérationnelle.
- **Friction quotidienne** : copier-coller inter-qubes intentionnel, gestion réseau par qubes, raccourcis à apprendre.
- **Compatibilité** : pas de Wayland pour l’instant, certaines applis graphiques moins fluides.

## 18.9 Architectures de référence

- **Journaliste exposé** : dom0 + sys-net + sys-firewall + sys-usb + sys-whonix + personal + work + journalist-pub + anon-whonix + vault + dispVM template.
- **RSSI / cyber pro** : dom0 + sys-* + work + lab + research + analysis + vault.
- **Profil ultra-compartimenté HVT** : multiples qubes Whonix avec rotation, vault offline, disposables pour tout fichier externe, qube banking isolé.

## 18.10 *Fil rouge* — Yann déploie Qubes pour son équipe terrain

Yann T., RSSI d’une ONG des droits humains à Genève, déploie Qubes sur les laptops de cinq enquêteurs terrain qui travaillent en Asie centrale et au Moyen-Orient. Configuration standardisée : qubes par projet, sys-whonix pour les comptes pseudonymes, vault offline pour les clés PGP, dispVM templates Fedora et Debian. Formation : 2 jours sur place + manuel interne. Six mois plus tard, il constate que la principale source de friction est la gestion des pièces jointes (les enquêteurs envoient beaucoup de PDF). Solution déployée : un workflow dispVM + Dangerzone systématique.

-----

> 🟦 **Capstone 2 — Chaîne complète de session sensible**
> 
> **Scénario** : Tu reçois sur Signal un message d’une nouvelle source. Elle annonce avoir des documents. Elle propose de les envoyer via un lien Onion en clic-bouton. Tu sais qu’elle est exposée et que les documents sont sensibles. Comment procèdes-tu, étape par étape ?
> 
> **Procédure attendue** :
> 
> 1. **Vérifier l’identité de la source** sur Signal (Safety Number, cf. Ch 26) avant tout échange substantiel.
> 1. **Préparer un environnement jetable** : Tails sur USB dédiée à cette enquête, ou un qube disposable sur Qubes si tu travailles sur Qubes au quotidien.
> 1. **Routage Tor** : Tails route tout via Tor par défaut ; pour Qubes, utiliser anon-whonix.
> 1. **Téléchargement** : depuis l’environnement isolé, accéder au lien Onion et récupérer les fichiers.
> 1. **Vérification d’intégrité** : si la source a fourni un hash (SHA-256), le vérifier hors bande (canal Signal ou téléphone). Sinon, accepter le risque.
> 1. **Sas de transition** : passer les fichiers par Dangerzone (Ch 16) pour produire des PDF propres.
> 1. **Archivage chiffré** : chiffrer les fichiers source (avec GPG + clé PGP de stockage, ou conteneur VeraCrypt/Cryptomator) avant de les sortir de l’environnement isolé.
> 1. **Stockage** : sur un disque chiffré séparé, idéalement dans un qube vault si Qubes, ou sur un disque externe chiffré rangé physiquement.
> 1. **Destruction des traces** : si Tails, redémarrage = traces effacées ; si dispVM Qubes, fermeture = destruction.
> 1. **Documentation** : noter dans un journal d’enquête (chiffré) : date, source, hash des fichiers, environnement utilisé. Pour traçabilité interne, pas pour partage.
> 
> Léa, dans le fil rouge, applique cette procédure quand Karim B. lui transmet son premier paquet de documents : Tails sur USB neuve achetée pour cette enquête, ouverture des PDF via Dangerzone, archivage dans un conteneur VeraCrypt sur disque externe rangé dans un coffre.

-----
