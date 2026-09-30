---
title: Chapitre 17 — Tails, Whonix et Qubes OS
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 4 — Environnements de session sensible
  - index.md
---

choisir le bon modèle d’isolation

## 17.1 Trois outils, trois logiques différentes

Ces trois noms reviennent constamment ensemble dans la littérature privacy. Ils ne sont pas concurrents : ils répondent à des besoins distincts.

|Besoin                                         |Outil approprié                       |
|-----------------------------------------------|--------------------------------------|
|Action ponctuelle sensible, faible trace locale|**Tails**                             |
|Identité pseudonyme durable, anonymat réseau   |**Whonix**                            |
|Séparation durable d’activités multiples       |**Qubes OS**                          |
|Profil HVT, journaliste, ONG sensible          |**Qubes + Whonix**                    |
|Quotidien grand public durci                   |*Aucun des trois — un OS durci suffit*|

## 17.2 Tails : session temporaire, live USB, amnésie

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

## 17.3 Whonix : anonymat Tor persistant via Gateway / Workstation

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

## 17.4 Qubes OS : compartimentation par VM (vue rapide, détail Ch 18)

**Qubes OS** est un système d’exploitation basé sur Xen, qui compartimente *tout* en VMs séparées. Chaque activité tourne dans son propre qube : un qube pour le travail, un qube pour le perso, un qube pour le banking, un qube pour le suspect.

**Ce n’est pas un outil d’anonymat**. Qubes compartimente, il n’anonymise pas. Combiné à Whonix (un qube Whonix), il offre les deux.

Le détail de Qubes est traité au chapitre 18.

## 17.5 Qubes + Whonix : la combinaison avancée

Pour les profils les plus exposés : Qubes OS comme système hôte, avec un qube `sys-whonix` (Gateway) et des qubes `anon-whonix` (Workstations) pour les activités nécessitant anonymat réseau. Les autres activités (perso, pro non sensible) restent dans leurs qubes propres, sans Tor (parce que Tor pour tout est *contre-productif* — usage repérable, comptes nominaux exposés).

## 17.6 Comparaison par ergonomie, coût, complexité

|Critère                   |Tails                                 |Whonix             |Qubes                                 |
|--------------------------|--------------------------------------|-------------------|--------------------------------------|
|**Persistance**           |Amnésie par défaut, persistance opt-in|Persistante        |Persistante                           |
|**Matériel requis**       |Tout PC moderne + USB                 |PC raisonnable + VM|PC avec ≥ 16 GB RAM, virtualisation HW|
|**Courbe d’apprentissage**|Modérée                               |Modérée            |Élevée                                |
|**Coût**                  |Gratuit                               |Gratuit            |Gratuit                               |
|**Ergonomie quotidienne** |Inadaptée                             |Possible           |Friction réelle                       |
|**Anonymat réseau**       |Tor par défaut                        |Tor par défaut     |Aucun (sauf qube Whonix)              |
|**Compartimentation**     |Faible                                |Modérée            |Forte                                 |

## 17.7 Erreurs fréquentes

- **Utiliser Tails comme OS quotidien** : impossible à tenir. Tails est conçu pour des sessions, pas pour de la durée.
- **Croire que Qubes anonymise** : Qubes compartimente. Si tu utilises Firefox dans un qube non-Tor sur ton compte Facebook, Facebook te voit avec ton IP normale.
- **Croire que Whonix protège l’hôte** : Whonix protège l’identité réseau de la VM Workstation. Si l’hôte est compromis, Whonix ne peut rien.
- **Empiler les trois sans comprendre** : Tails dans une VM, Whonix dans Tails, Qubes en VM sur autre Qubes → architecture inopérante et probablement contre-productive.

## 17.8 Matrice de décision finale

- **Action one-shot sensible, sans persistance** → Tails.
- **Identité pseudonyme durable, anonymat réseau permanent** → Whonix.
- **Compartimentation forte de plusieurs activités** → Qubes.
- **Profil HVT avec besoin des deux** → Qubes + Whonix.
- **Usage quotidien grand public** → ni l’un ni les autres : un OS durci (Ch 14) + GrapheneOS ou iOS durci + bonnes pratiques.

-----
