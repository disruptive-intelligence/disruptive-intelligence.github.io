---
title: Chapitre 18 — Lab de l'investigateur
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE III — Méthodologie d'enquête et gestion du dossier
  - index.md
---

## 18.1 Le lab comme actif professionnel

Le **lab** désigne l'environnement matériel, logiciel et organisationnel de l'investigateur. C'est un actif professionnel structuré, comparable à l'atelier d'un artisan. Sa qualité conditionne directement la productivité et la sécurité du travail.

Trois niveaux : **lab minimal** (analyste débutant, missions ponctuelles), **lab professionnel** (analyste indépendant, missions régulières), **lab d'équipe** (cabinet, cellule interne).

## 18.2 Matériel

**Poste principal.** Laptop professionnel récent (CPU correct, 16+ Go RAM, SSD 512+ Go). Système d'exploitation : Linux (Ubuntu 24.04, Pop!_OS, Fedora) ou Windows 11 Pro (avec BitLocker activé), ou macOS récent (FileVault activé). Linux est préféré pour des raisons de souveraineté et de transparence.

**Second poste** (recommandé). Pour cloisonner enquêtes sensibles. Peut être un mini-PC dédié, un laptop d'investigation séparé.

**Téléphone d'investigation.** Séparé physiquement, SIM dédiée. Voir Ch.9.

**Clés YubiKey** (ou équivalent). 2FA matériel pour comptes critiques. Au moins deux clés (principale + backup).

**Disques externes chiffrés.** Pour sauvegardes 3-2-1.

**Imprimante sécurisée locale.** Pas de cloud printing. Pour livrables papier confidentiels.

## 18.3 Logiciels système et OPSEC

- **Système chiffré** (LUKS, BitLocker, FileVault).
- **Conteneurs VeraCrypt** par enquête.
- **VirtualBox** ou **VMware Workstation** pour VM dédiées.
- **VPN** : Mullvad, IVPN, ProtonVPN. Pas de VPN gratuit.
- **Gestionnaire mots de passe** : KeePassXC (local), Bitwarden self-hosted (équipe).
- **Tails** sur clé USB pour missions ponctuelles sensibles.
- **Whonix** VM pour Tor durable.
- **Signal Desktop** pour communication confidentielle.

## 18.4 Suite navigateur et OSINT web

- **Firefox** profil dédié : extensions uBlock Origin, NoScript (avec parcimonie), Cookie AutoDelete, Privacy Badger, CanvasBlocker, **Wayback Machine extension**, **OneTab** (gestion onglets), **Hunchly** (capture).
- **Chromium / Brave** profil secondaire pour compatibilité.
- **Tor Browser** pour missions Tor.

## 18.5 Suite OSINT logicielle

**Note & vault.**

- **Obsidian** (gratuit, vault local, plugins riches). Standard 2026.
- Alternatives : Logseq, Joplin (open source).

**Capture et journal.**

- **Hunchly** (payant, standard professionnel).
- **SingleFile** (extension, gratuit).
- **yt-dlp** (téléchargement vidéo multi-plateformes).

**Graphes.**

- **Maltego CE** (Community Edition, gratuit) + **Casefile** (offline).
- **Maltego Pro** (payant) pour transforms automatiques.
- **Gephi** (open source, analyses statistiques).
- **Neo4j Community** (graph DB locale).

**Timeline.**

- **Timeline Explorer** (Zimmerman, gratuit).
- **Aeon Timeline** (payant).

**Réseaux et infrastructure.**

- **Amass** (sous-domaines), **subfinder**, **dnsx**.
- **WHOIS clients** (terminal).
- **nmap**, **masscan** (avec prudence légale).

**Image & GEOINT.**

- **ExifTool** (métadonnées).
- **QGIS** (cartographie).
- **Google Earth Pro** (gratuit, riche).
- **FotoForensics**, **Forensically** (analyses).

**Crypto / blockchain.** *(renvoi → OSINT Crypto vFULL)*

**Code & automatisation.**

- **Python** (3.11+) + venv ou pyenv.
- **Jupyter Lab** pour notebooks reproductibles.
- **Git** local (chiffré) pour versioning.
- **Playwright** ou Selenium pour scraping résilient.

**IA locale.**

- **Ollama** (LLMs locaux). Llama 3, Mistral, Qwen.
- **LM Studio** (interface graphique).
- **GPT4All**.

## 18.6 Outils SaaS et abonnements

Selon budget et menace acceptable :

- **Hunter.io** (email lookup).
- **DeHashed** (breaches).
- **Intelligence X** (deep search, leaks).
- **Shodan** (infrastructure Internet).
- **Censys** (idem, complémentaire).
- **PimEyes** (recherche faciale, attention légale).
- **OpenSanctions** (gratuit, sanctions).
- **Pappers** (gratuit/payant, registres français).
- **OpenCorporates** (registres internationaux).
- **Hive Moderation** / **Sensity** (détection IA).

Choisir selon enquêtes types. Renouveler annuellement, vérifier la pertinence.

## 18.7 Arborescence type d'un dossier d'enquête

Présentée au Ch.17 (vault Obsidian). Le principe :

- Un dossier racine par enquête (code projet, pas le nom de la cible).
- Sous-dossiers standardisés.
- Versioning Git.
- Conteneur VeraCrypt englobant le tout.

## 18.8 Routines opérationnelles

**Au démarrage de chaque enquête.**

- Création conteneur VeraCrypt dédié.
- Création vault Obsidian.
- Snapshot VM d'investigation.
- Génération sous-domaines hashes initiaux.
- Activation VPN si non permanent.

**En cours.**

- Backup quotidien du dossier d'enquête.
- Hash vérification hebdomadaire.
- Point de revue toutes les 48-72h.

**À la fin de l'enquête.**

- Export final.
- Backup chiffré sur support séparé.
- Destruction sécurisée des éléments non conservés (selon SOR).
- Capitalisation : leçons apprises documentées.

## 18.9 Lab d'équipe : spécificités

- **Outil collaboratif** : Element/Matrix self-hosted ou Slack chiffré.
- **Stockage partagé** : Nextcloud self-hosted ou équivalent.
- **Wiki interne** : pour SOPs, modèles, leçons.
- **CI/CD pour scripts internes** : Gitea ou GitLab self-hosted.
- **Briefing OPSEC mensuel** : revues d'incidents, mises à jour outils.

## 18.10 Veille outils

L'écosystème OSINT évolue mensuellement. Une **veille outils** est nécessaire.

- **OSINT Framework** (osintframework.com) — catalogue maintenu.
- **OSINT-FR ressources**.
- **Bellingcat Online Investigation Toolkit**.
- **IntelTechniques** (Michael Bazzell).
- **OSINT Curious** podcast et blog.
- Newsletters spécialisées : ConductORE, OSINT Daily, Bellingcat newsletter.

**Discipline.** Garder une liste maître à jour. Tester les nouveaux outils dans un environnement isolé avant adoption. Documenter dans le wiki interne.

> **MIRAGE — Épisode 3 : OPSEC et plan de collecte**
>
> Mardi 20 mai 2026. L'analyste finalise son environnement d'enquête.
>
> Création d'un conteneur VeraCrypt 50 Go nommé `MIRAGE_2026`. Création d'un vault Obsidian dedans, avec l'arborescence type. Création d'une VM Ubuntu dédiée, snapshot initial. Activation Mullvad VPN avec port forwarding sur un nœud français (cohérence géographique avec l'enquête sur cible française).
>
> Évaluation du threat model : Delaunay est techniquement compétent (DAF expérimenté), sa structure offshore suppose des partenaires (cabinet d'avocats spécialisé, fiduciaire), la branche désinformation suggère un prestataire criminel actif. Threat model : entre « sensible » et « criminelle ». Pas d'enjeu étatique identifié à ce stade.
>
> Conséquence OPSEC :
> - VM dédiée, jamais de connexion personnelle dessus.
> - Profil Firefox dédié, Hunchly activé en permanence.
> - Trois avatars LinkedIn matures déjà disponibles dans le parc du cabinet, l'un d'eux (« Camille Roux », créé en 2024, profil RH) sera utilisé pour observation LinkedIn de Delaunay.
> - Téléphone d'investigation séparé, SIM prépayée déclarée.
> - Pas de connexion depuis le wifi domicile, uniquement depuis le bureau (réseau dédié) ou hotspot téléphone investigation.
>
> Plan de collecte détaillé sur 6 semaines validé avec Me Legrand. Premier jalon à J+15 (29 mai). Critères d'arrêt précisés : faisceau d'indices convergents suffisant pour saisine PNF sur IR1, IR2, IR4, IR5 ; IR3 (patrimoine) à profondeur d'orientation.
>
> L'enquête peut désormais entrer dans sa phase de collecte active. Le Chapitre 19 ouvre la Partie IV — Moteurs, recherche web et restrictions plateformes.

-----
