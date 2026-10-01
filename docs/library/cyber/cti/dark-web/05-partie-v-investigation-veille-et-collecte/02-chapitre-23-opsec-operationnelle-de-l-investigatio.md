---
title: Chapitre 23 — OPSEC opérationnelle de l'investigation
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie V — Investigation, veille et collecte
  - index.md
---

L'**OPSEC** (Operations Security) de l'analyste dark web est le pilier de la réussite d'une investigation. Une OPSEC défaillante expose l'analyste, compromet la mission, et peut mettre en danger les sources coopératives ou les collègues.

## 23.1 La séparation des univers

Principe fondamental : **séparation totale** entre l'univers personnel de l'analyste, son univers professionnel hors investigation, et son univers d'investigation.

**Machines séparées**. Ordinateur dédié à l'investigation dark web. Jamais utilisé pour activités personnelles (réseaux sociaux, emails, banque), jamais pour activités professionnelles générales (mails corporate, documents, visioconférences). Configuration minimale : OS dédié (Whonix, Tails), navigateur Tor Browser uniquement, outils strictement nécessaires.

**Comptes séparés**. Emails jetables (protonmail, ctemplar, services .onion) pour les comptes d'investigation. Jamais de lien avec emails corporate ou personnels.

**Identités séparées**. Les personas d'investigation (pseudonymes, handles Telegram, JID XMPP) sont **strictement cloisonnées** de l'identité réelle de l'analyste. Aucune réutilisation d'un pseudo entre personas. Aucun lien traçable entre les personas et l'identité réelle.

**Financier séparé**. Wallets crypto dédiés à l'investigation, financés par un circuit professionnel (exchange corporate avec KYC de l'entreprise, pas de l'analyste personnellement). Transactions tracées par l'entreprise pour audit.

**Temporel séparé**. L'investigation se fait dans des créneaux dédiés. Le mélange entre activités dark web et tâches personnelles dans le même créneau temporel crée des risques de contamination (oubli de fermer Tor Browser avant d'ouvrir son email personnel, etc.).

## 23.2 La persona

Une **persona** est un personnage fictif construit pour l'investigation. Elle doit être **crédible** et **cohérente**.

**Éléments de la persona** :

- **Pseudonyme** : unique, ne ressemble pas à d'autres pseudonymes utilisés par l'analyste (pas de pattern identifiable).
- **Histoire** : d'où vient-elle ? quel métier ? quelles compétences ? quels intérêts ?
- **Langue** : style d'écriture cohérent avec l'origine prétendue. Un analyste français qui joue un persona russophone doit maîtriser les codes linguistiques russophones — sinon se cantonne à l'anglais.
- **Niveau technique** : si persona « script kiddie » prétend avoir peu de skills, elle ne doit pas poser des questions trop sophistiquées. Si persona « pro » doit comprendre les concepts avancés.
- **Activité historique** : la persona a-t-elle des posts dans des forums parallèles ? Une présence sur Telegram ? Un historique crédible ?
- **Infrastructure cohérente** : serveur XMPP utilisé, méthodes de paiement préférées, heures d'activité.

**Construction préalable**. Une persona utilisable pour une investigation sérieuse prend **3-6 mois** à construire — inscription sur un forum, posts graduels, participation communautaire, construction d'une histoire minimale. Les personas « jetables » (créées le jour, utilisées le lendemain) sont facilement identifiables comme non-authentiques.

**Maintenance**. Une persona doit être **active** même quand pas utilisée sur une investigation active. Posts occasionnels, participation à des discussions générales. Une persona inactive pendant 6 mois puis réactivée pour une enquête ciblée déclenche la méfiance.

**Burnability**. Accepter qu'une persona peut être brûlée. En ce cas, ne pas chercher à la « sauver » — l'abandonner, en construire une nouvelle. Toute tentative de réactiver une persona suspecte aggrave l'exposition.

## 23.3 La sécurité technique

**Tor Browser en mode Safest**. JavaScript désactivé. Beaucoup de fonctionnalités cassées, mais pas d'exécution de code exploitable. Certains sites nécessitent JS — évaluer le risque au cas par cas, activer temporairement si site considéré sûr.

**VM isolée**. Toute interaction au-delà de la simple navigation (téléchargements, fichiers exécutables) dans une VM jetable. Snapshot avant action, restauration après. Ne jamais exposer l'OS hôte à du contenu dark web non-simple-HTML.

**Pas de JavaScript actif sur sites suspects**. Les NIT (Network Investigative Techniques) et les exploits navigateur exploitent JS (Ch.30). Mode Safest le bloque ; si on l'active, on doit comprendre les risques.

**Pas de WebRTC**. Tor Browser désactive WebRTC ; ne pas l'activer manuellement. WebRTC peut leaker l'IP réelle.

**Pas de plugins**. Flash, Java, PDF readers intégrés — désactivés ou absents. Tor Browser configure ça par défaut.

**Vérification des .onion**. Les adresses .onion sont longues (56 caractères v3). Les scammers créent des adresses similaires via vanity generation. **Toujours vérifier l'adresse complète**, via source fiable (site officiel du service, post établi sur forum réputé, backup en dur pré-validé).

**Hashing des fichiers**. Tout fichier téléchargé est hashé (SHA-256 minimum) avant ouverture. Le hash sert de référence pour la chain of custody et pour vérifier que le fichier n'a pas été altéré entre collecte et analyse.

**Pas de métadonnées**. Les screenshots sont pris puis **strippés de métadonnées** (exiftool). Les documents créés pendant l'investigation (notes, rapports) ne doivent pas contenir de métadonnées personnelles (nom d'auteur dans Word, etc.).

## 23.4 Les erreurs classiques

**Réutilisation de pseudonymes**. Un analyste qui utilise le même pseudo sur plusieurs enquêtes risque la corrélation. Les forums observent les patterns — un pseudo qui demande des échantillons de données industrielles aerospace sur un forum et des échantillons bancaires sur un autre est soit un acheteur éclectique, soit un investigateur.

**Corrélation temporelle**. Pseudo actif aux heures ouvrables françaises systématiquement. Indique fuseau horaire Europe occidentale, incompatible avec un persona prétendument russophone.

**Fuites linguistiques**. Expressions françaises dans un persona anglophone, conventions de dates françaises (DD/MM) dans un persona américain (MM/DD), traduction littérale d'idiomes français.

**Over-sharing**. Par nervosité ou tentative de crédibilité, l'analyste donne trop d'infos sur sa « persona » — détails sur son entreprise fictive, anecdotes personnelles vérifiables. Chaque détail est une surface d'attaque pour la contre-investigation.

**Accès depuis infrastructure corporate**. L'analyste qui accède à Tor depuis l'IP corporate de son bureau (même via VPN Tor) expose son organisation. Poste dédié dans un réseau isolé recommandé.

**Comptes personnels sur la machine d'investigation**. Un analyste qui check ses emails personnels sur la machine dark web compromet tout le cloisonnement.

**Documentation défaillante**. Une investigation sans logs précis de chaque action (heure, URL visitée, fichier téléchargé, hash, pseudonyme utilisé) ne produit pas de preuves utilisables.

**Abandon de prudence sur la durée**. Au début de l'enquête, OPSEC rigoureuse. Après 3 mois, fatigue, relâchement. L'erreur survient plus tard, pas au début.

## 23.5 Le programme OPSEC d'équipe

Pour une équipe CTI, l'OPSEC doit être **institutionnelle**, pas individuelle.

**Procédures documentées**. Playbook formalisé : comment créer une persona, comment ouvrir un compte, comment gérer les paiements, comment capturer les preuves, comment documenter.

**Peer review**. Chaque action sensible (création de persona, premier contact vendeur, téléchargement d'échantillon) est validée par un pair ou la hiérarchie.

**Supervision**. Un responsable CTI a visibilité sur les investigations en cours, alloue les personas, valide les escalades.

**Formation continue**. L'OPSEC évolue (nouvelles techniques de dé-anonymisation, nouveaux pièges). Formation périodique, veille sur les techniques offensives utilisées contre les analystes.

**Incident response OPSEC**. Plan d'action en cas de compromission de persona — quoi abandonner, quoi sauvegarder, qui prévenir, comment communiquer.

**Débriefing psychologique**. Les missions longues dans l'écosystème dark web sont éprouvantes. Sessions régulières avec psychologue ou pair expérimenté.

---
