---
title: Partie 4 — Environnements de session sensible
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
chapter: 5
chapters: 8
---

> **Objectif** : aller au-delà du durcissement quotidien pour les sessions qui exigent une compartimentation forte ou une isolation réseau. Comprendre que Tails, Whonix et Qubes OS répondent à *trois besoins différents*, et choisir lequel s’applique à quel cas.

-----

## Chapitre 16 — Machines virtuelles, live USB et environnements jetables

### 16.1 Principe : enveloppe jetable autour d’une activité

Les machines virtuelles et les environnements live permettent d’exécuter un système isolé du système hôte. L’activité sensible se déroule dans cette enveloppe, qui est jetée à la fin. C’est l’inverse de la logique « durcir l’OS principal pour tout » : on accepte que l’OS principal n’est pas immunisé, on l’utilise pour ce qui ne risque pas, et on bascule en environnement séparé pour ce qui risque.

### 16.2 Hyperviseurs courants

- **VirtualBox** (Oracle) : gratuit, multi-plateforme, populaire. Performances modestes. Récents soucis de support sur Apple Silicon.
- **KVM/QEMU** (Linux) : intégré au noyau, performant. virt-manager pour interface graphique.
- **Hyper-V** (Windows Pro/Enterprise) : intégré, bonne intégration.
- **VMware Workstation Pro** (devenu gratuit en 2024 pour usage personnel) : commercial historique, performant.
- **UTM** (macOS, gratuit) : surcouche QEMU, support Apple Silicon, références pour macOS.

### 16.3 Snapshots et restauration

Le **snapshot** capture un état complet de la VM. Avant chaque session sensible : snapshot. Après : revert au snapshot propre. Cela garantit qu’aucun artefact (cookies, fichiers, malware potentiel) ne survit à la session.

Discipline minimale : un snapshot « propre » initial, un revert systématique en fin de session, jamais d’usage long terme sans rotation.

### 16.4 Limites de l’isolation par VM

- **Évasion de VM** : sortir d’une VM pour compromettre l’hôte est techniquement possible mais reste rare. Demande typiquement un zero-day sur l’hyperviseur, ressources et motivation. Des CVE existent régulièrement (Xen, KVM, VMware, VirtualBox) — la pratique défensive est de garder l’hyperviseur à jour et de ne pas utiliser une VM seule comme barrière critique pour activité ultra-sensible.
- **Évasion par périphérique partagé** : USB passthrough, audio, presse-papiers, clipboard partagé entre VM et hôte sont des vecteurs de fuite. Sur VirtualBox et VMware, désactiver le partage clipboard et drag-and-drop par défaut. Sur Qubes, ces canaux sont gérés explicitement par qrexec avec validation utilisateur à chaque transfert.
- **Fuites matérielles** : information CPU (CPUID, modèle, microcode), adresse MAC virtuelle qui peut être prévisible, configuration réseau de la VM peuvent renseigner sur l’hôte. Une VM ne te rend pas anonyme — elle isole l’application.
- **Performance** : émulation graphique, accélération limitée. Pas pour gaming sensible ou tâches GPU-intensives. Pour usages standard (bureautique, navigation), KVM/QEMU avec virtio est très performant.
- **Sortie réseau** : la VM utilise par défaut le réseau de l’hôte. Pour anonymat, ajouter Tor (cf. Whonix Ch 17). Pour isolation forte, configurer la VM en NAT (et non bridged) pour éviter l’exposition directe au LAN.
- **Side channels** : Spectre, Meltdown et leurs successeurs ont permis dans certaines conditions à une VM de lire de la mémoire hôte. Patches kernel et microcode CPU restent indispensables. Pour profil Niveau 3 : préférer la compartimentation par appareil physique aux VMs pour les secrets vraiment critiques.

### 16.5 Cas d’usage typiques

- **Ouverture de document suspect** : reçu d’une source inconnue, lien Telegram non vérifié, PDF d’apparence douteuse → VM jetable, revert immédiat.
- **Navigation à risque** : exploration de site OSINT borderline, test de comportement applicatif → VM avec snapshot.
- **Environnement de développement séparé** : projets clients distincts isolés.

### 16.6 Dangerzone

**Dangerzone** (Freedom of the Press Foundation) automatise le scénario « j’ai reçu un PDF, je veux le lire sans risquer mon système ». Le PDF est converti dans un conteneur isolé en image puis re-rendu en PDF propre. Tous les éléments actifs (JavaScript, formulaires, liens malveillants) disparaissent. Pratique pour journalistes recevant des documents.

### 16.7 Live USB

Booter depuis une clé USB un OS qui n’écrit rien sur le disque local. Le système est en RAM et meurt à l’extinction. Tails et Kicksecure proposent des images live. Avantages : trivial à déployer, aucune persistance. Inconvénients : pas de configuration personnalisée sauvegardée (sauf persistance chiffrée Tails), démarrage lent.

### 16.8 Erreur fréquente

Une VM **ne cache pas ton IP**. Elle ne te rend pas anonyme. Elle isole l’application. Confondre les deux conduit à utiliser une VM pour « être sûr d’être anonyme sur ce site », ce qui ne fonctionne pas. Pour anonymat réseau, il faut Tor (Ch 21) ou Whonix.

-----

## Chapitre 17 — Tails, Whonix et Qubes OS : choisir le bon modèle d’isolation

### 17.1 Trois outils, trois logiques différentes

Ces trois noms reviennent constamment ensemble dans la littérature privacy. Ils ne sont pas concurrents : ils répondent à des besoins distincts.

|Besoin                                         |Outil approprié                       |
|-----------------------------------------------|--------------------------------------|
|Action ponctuelle sensible, faible trace locale|**Tails**                             |
|Identité pseudonyme durable, anonymat réseau   |**Whonix**                            |
|Séparation durable d’activités multiples       |**Qubes OS**                          |
|Profil HVT, journaliste, ONG sensible          |**Qubes + Whonix**                    |
|Quotidien grand public durci                   |*Aucun des trois — un OS durci suffit*|

### 17.2 Tails : session temporaire, live USB, amnésie

**Tails** est un système live, basé sur Debian, qui démarre depuis une clé USB. Il ne touche pas au disque local. Tout le trafic réseau est routé via Tor (sauf paramétrage avancé). À l’extinction, la RAM est purgée et il ne reste rien de la session.

**Persistance chiffrée optionnelle** : sur la même clé USB, une partition chiffrée peut stocker certains éléments (bookmarks, clés PGP, configuration Tor, certains fichiers). C’est un opt-in conscient.

**Workflow complet** :

1. Télécharger l’image Tails depuis tails.net.
1. Vérifier la signature GPG.
1. Flasher la clé USB (avec balenaEtcher ou `dd`).
1. Démarrer depuis l’USB sur n’importe quel ordinateur (BIOS/UEFI).
1. Travailler. Tout passe par Tor.
1. Éteindre. Tout disparaît.

**Cas d’usage idéaux** : journaliste en mission ponctuelle reçoit un document d’une source ; lanceur d’alerte transmet des fichiers ; opposant utilise un cybercafé.

**Limites** :

- Tails ne protège pas contre un adversaire local actif (firmware compromis, BIOS implanté, keylogger matériel).
- L’usage répétitif sur la même machine peut laisser des artefacts dans la RAM persistante de certains modèles, et dans les logs du modem cellulaire si connexion 4G/5G.
- Tor a ses propres limites (Ch 21).
- L’usage de Tails depuis chez soi sans précaution réseau (FAI voit du Tor) peut signaler ton activité même si le contenu reste protégé.

**Fil rouge** : Karim B., lanceur d’alerte, utilise Tails depuis un cybercafé pour transmettre à Léa des documents. Une seule session, jamais réutilisée. Le cybercafé est choisi loin de son domicile et de son travail, payé cash.

### 17.3 Whonix : anonymat Tor persistant via Gateway / Workstation

**Whonix** est conçu pour l’anonymat réseau durable. Architecture en **deux VMs** :

- **Gateway** : seul accès réseau, force tout le trafic via Tor. C’est un point d’isolation.
- **Workstation** : l’environnement de travail, qui ne peut sortir que via la Gateway.

**Effet** : même si la Workstation est compromise par un malware, ce malware ne peut pas révéler l’IP réelle, parce qu’il n’y a pas de chemin réseau direct. Le seul trafic possible passe par la Gateway, donc par Tor.

**Streaming isolation** : Whonix configure des circuits Tor distincts par destination, ce qui réduit la corrélation cross-services.

**Usage** : sur VirtualBox/KVM en VM normale, ou en qubes sur Qubes OS (la combinaison ultime).

**Limites** :

- La Workstation peut être compromise par malware (l’IP reste cachée, mais les autres données peuvent fuiter par d’autres canaux : credentials, contenus).
- L’hôte n’est pas protégé : si l’OS hôte est compromis avant la VM, Whonix n’aide pas.
- Performance Tor : latence et débit limités.

### 17.4 Qubes OS : compartimentation par VM (vue rapide, détail Ch 18)

**Qubes OS** est un système d’exploitation basé sur Xen, qui compartimente *tout* en VMs séparées. Chaque activité tourne dans son propre qube : un qube pour le travail, un qube pour le perso, un qube pour le banking, un qube pour le suspect.

**Ce n’est pas un outil d’anonymat**. Qubes compartimente, il n’anonymise pas. Combiné à Whonix (un qube Whonix), il offre les deux.

Le détail de Qubes est traité au chapitre 18.

### 17.5 Qubes + Whonix : la combinaison avancée

Pour les profils les plus exposés : Qubes OS comme système hôte, avec un qube `sys-whonix` (Gateway) et des qubes `anon-whonix` (Workstations) pour les activités nécessitant anonymat réseau. Les autres activités (perso, pro non sensible) restent dans leurs qubes propres, sans Tor (parce que Tor pour tout est *contre-productif* — usage repérable, comptes nominaux exposés).

### 17.6 Comparaison par ergonomie, coût, complexité

|Critère                   |Tails                                 |Whonix             |Qubes                                 |
|--------------------------|--------------------------------------|-------------------|--------------------------------------|
|**Persistance**           |Amnésie par défaut, persistance opt-in|Persistante        |Persistante                           |
|**Matériel requis**       |Tout PC moderne + USB                 |PC raisonnable + VM|PC avec ≥ 16 GB RAM, virtualisation HW|
|**Courbe d’apprentissage**|Modérée                               |Modérée            |Élevée                                |
|**Coût**                  |Gratuit                               |Gratuit            |Gratuit                               |
|**Ergonomie quotidienne** |Inadaptée                             |Possible           |Friction réelle                       |
|**Anonymat réseau**       |Tor par défaut                        |Tor par défaut     |Aucun (sauf qube Whonix)              |
|**Compartimentation**     |Faible                                |Modérée            |Forte                                 |

### 17.7 Erreurs fréquentes

- **Utiliser Tails comme OS quotidien** : impossible à tenir. Tails est conçu pour des sessions, pas pour de la durée.
- **Croire que Qubes anonymise** : Qubes compartimente. Si tu utilises Firefox dans un qube non-Tor sur ton compte Facebook, Facebook te voit avec ton IP normale.
- **Croire que Whonix protège l’hôte** : Whonix protège l’identité réseau de la VM Workstation. Si l’hôte est compromis, Whonix ne peut rien.
- **Empiler les trois sans comprendre** : Tails dans une VM, Whonix dans Tails, Qubes en VM sur autre Qubes → architecture inopérante et probablement contre-productive.

### 17.8 Matrice de décision finale

- **Action one-shot sensible, sans persistance** → Tails.
- **Identité pseudonyme durable, anonymat réseau permanent** → Whonix.
- **Compartimentation forte de plusieurs activités** → Qubes.
- **Profil HVT avec besoin des deux** → Qubes + Whonix.
- **Usage quotidien grand public** → ni l’un ni les autres : un OS durci (Ch 14) + GrapheneOS ou iOS durci + bonnes pratiques.

-----

## Chapitre 18 — Qubes OS en pratique : compartimentation avancée et workflows sensibles

### 18.1 Architecture

Qubes OS repose sur Xen. **Dom0** est le qube administrateur, isolé, sans réseau direct. Au-dessus, des **templates** (Fedora, Debian, Whonix Gateway, Whonix Workstation) servent de base aux **app qubes**, légers, qui partagent le template mais ont leurs propres `/home`.

Trois qubes système :

- **sys-net** : gère les interfaces réseau physiques. C’est le seul qube avec accès direct aux périphériques réseau.
- **sys-firewall** : entre sys-net et les app qubes, applique des règles de pare-feu.
- **sys-usb** : isole les périphériques USB. Aucun USB ne touche dom0.

### 18.2 Qubes critiques

- **vault** : qube *offline* (aucune connexion réseau autorisée), stocke gestionnaire de mots de passe, clés GPG, secrets. Communication avec autres qubes via copier-coller contrôlé ou qrexec.
- **work** : usage professionnel.
- **personal** : usage personnel.
- **banking** : un qube par institution si paranoïaque, isolé.
- **anon-whonix** : un qube Workstation Whonix pour navigation anonyme.
- **disposable VMs** (dispVM) : qubes éphémères, créés à la demande, détruits à la fermeture. Idéal pour ouvrir un fichier suspect.

### 18.3 Workflow « ouvrir un fichier suspect »

Tu reçois un PDF de provenance douteuse. Sur Qubes :

1. Fichier reçu dans `personal`.
1. Clic droit → « Open in DisposableVM ».
1. Un qube jetable Fedora se crée, ouvre le PDF.
1. Si le PDF contient un exploit, seule la dispVM est compromise.
1. Tu ferme la fenêtre → la dispVM est détruite.
1. Ton `personal` est intact.

### 18.4 Workflow « identités séparées »

Tu sépares pseudo et identité civile. Sur Qubes :

- `personal` : compte Google, Facebook, identité civile, réseau via sys-firewall direct.
- `journalist-pub` : ton compte Twitter de plume publique, ProtonMail dédié, idem.
- `journalist-anon` : qube relié à sys-whonix, pour les comptes vraiment anonymes (Tor pour tout).

Chaque identité a son qube. Tu ne mélanges jamais.

### 18.5 Qubes + Whonix en production

Configuration :

- **sys-whonix** : Gateway, route le trafic via Tor.
- **anon-whonix** : Workstation, configuré pour utiliser sys-whonix comme réseau. Navigation Tor Browser, comptes pseudonymes.
- Autres qubes (banking, personal) routent via sys-firewall (réseau direct, pas Tor) — parce que tu ne veux *pas* de Tor pour ton banking.

### 18.6 Modèle de menace contre lequel Qubes est efficace

- Malware classique : confiné à un qube, ne se propage pas.
- Exploit navigateur : confiné au qube qui héberge le navigateur.
- Compromission d’une app spécifique : la dispVM est jetée.
- Erreur humaine : ouvrir un fichier dans le mauvais qube est plus difficile, parce que les qubes sont visuellement codés par couleur.

### 18.7 Modèle de menace contre lequel Qubes n’est PAS efficace

- Compromission de **dom0** : si dom0 tombe, tout tombe. Donc dom0 doit rester minimaliste, sans réseau, sans installation tierce.
- Exploit de l’hyperviseur Xen : possible mais rare. Mises à jour critiques.
- Attaques matérielles (Spectre, Meltdown, et successeurs) : nécessitent attention et patches.
- Attaque physique avec accès non détecté : Qubes ne change pas la donne.

### 18.8 Coût et ergonomie

- **Matériel** : 16 GB RAM minimum (32 recommandé), CPU avec virtualisation et IOMMU, GPU compatible, SSD rapide.
- **Apprentissage** : compter 2-4 semaines pour fluidité opérationnelle.
- **Friction quotidienne** : copier-coller inter-qubes intentionnel, gestion réseau par qubes, raccourcis à apprendre.
- **Compatibilité** : pas de Wayland pour l’instant, certaines applis graphiques moins fluides.

### 18.9 Architectures de référence

- **Journaliste exposé** : dom0 + sys-net + sys-firewall + sys-usb + sys-whonix + personal + work + journalist-pub + anon-whonix + vault + dispVM template.
- **RSSI / cyber pro** : dom0 + sys-* + work + lab + research + analysis + vault.
- **Profil ultra-compartimenté HVT** : multiples qubes Whonix avec rotation, vault offline, disposables pour tout fichier externe, qube banking isolé.

### 18.10 *Fil rouge* — Yann déploie Qubes pour son équipe terrain

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
