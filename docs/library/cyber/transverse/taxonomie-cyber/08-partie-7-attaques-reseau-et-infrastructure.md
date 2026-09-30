---
title: Partie 7 — Attaques réseau et infrastructure
source: Cyber/Taxonomie_Cyber.md
note: Taxonomie cyber
chapter: 8
chapters: 15
---

### Vue d'ensemble taxonomique

Les attaques réseau se rangent en grandes intentions :

- **Reconnaissance** : découvrir la cible (scan, énumération).
- **Interception** : lire ce qui n'est pas pour soi (sniffing, MITM).
- **Usurpation** : se faire passer pour un autre élément du réseau (spoofing ARP/DNS/DHCP).
- **Rejeu et dégradation** : réutiliser ou affaiblir (replay, downgrade).
- **Exploitation et déplacement** : entrer puis circuler (services exposés, SMB/RDP/VPN, pivoting, lateral movement).
- **Disponibilité** : empêcher de fonctionner (DoS, DDoS, amplification, reflection, botnets).
- **Couche 2 / sans fil / routage** : abuser de l'infrastructure elle-même (VLAN hopping, evil twin, rogue AP, deauth, BGP hijacking).

🧭 **Taxonomie** — Beaucoup de ces attaques correspondent aux tactiques MITRE ATT&CK *Reconnaissance, Discovery, Lateral Movement, Collection, Impact*.

---

### Chapitre 127 — Reconnaissance et scan

1. **Définition.** Phase de collecte d'informations sur une cible : identifier hôtes, ports, services, versions, technologies.
2. **Famille.** Reconnaissance (ATT&CK *Reconnaissance/Discovery*).
3. **Principe.** Avant d'attaquer, l'adversaire cartographie la surface : reconnaissance *passive* (sources ouvertes, OSINT, sans toucher la cible) et *active* (scan de ports/services qui interroge directement la cible).
4. **Sous-types.** Reconnaissance passive (OSINT, DNS public, fuites), scan de ports, détection de services/versions, balayage réseau, découverte d'hôtes.
5. **Exemple conceptuel.** Recenser les sous-domaines et services exposés d'une organisation pour repérer une cible vulnérable, sans interaction intrusive.
6. **Impacts.** Préparation d'attaque ciblée ; en soi, peu de dommage, mais signal d'intention.
7. **Détection.** Pics de connexions vers de nombreux ports/hôtes, schémas de balayage, requêtes inhabituelles, signatures IDS.
8. **Prévention.** Réduction de surface (chapitre 22), minimisation de l'exposition, masquage des bannières/versions, surveillance, gestion de l'empreinte externe (ASM), pare-feu.
9. ⚠️ **Erreur fréquente.** Exposer des services et bannières détaillées qui facilitent le ciblage.
10. 🎯 **À retenir.** La reconnaissance précède tout : réduire ce qui est visible et exposé limite les options de l'attaquant dès le départ.

### Chapitre 128 — Énumération

1. **Définition.** Approfondissement de la reconnaissance : extraire des détails précis (comptes, partages, utilisateurs, configurations) d'un service identifié.
2. **Famille.** Reconnaissance/Discovery.
3. **Principe.** Une fois un service repéré, l'attaquant l'interroge pour lister ses objets : utilisateurs, groupes, partages réseau, informations d'annuaire, points d'API.
4. **Sous-types.** Énumération de comptes, de partages, d'annuaire (LDAP/AD), de services, d'API/endpoints.
5. **Exemple conceptuel.** Interroger un service pour distinguer les noms de comptes valides des invalides (énumération d'utilisateurs).
6. **Impacts.** Cartographie fine, préparation du brute force/spraying ciblé, découverte de chemins.
7. **Détection.** Requêtes répétitives systématiques, réponses différenciées exploitées, volume anormal.
8. **Prévention.** Réponses uniformes (anti-énumération), durcissement des services, limitation de débit, restriction d'accès, surveillance.
9. ⚠️ **Erreur fréquente.** Renvoyer des messages d'erreur qui distinguent « compte inexistant » de « mauvais mot de passe » (énumération offerte).
10. 🎯 **À retenir.** L'énumération transforme une liste vague en cibles précises : uniformiser les réponses et limiter les requêtes la freine.

### Chapitre 129 — Sniffing

1. **Définition.** Capture passive du trafic réseau pour en lire le contenu.
2. **Famille.** Interception (ATT&CK *Collection — Network Sniffing*) ; lié à l'absence de chiffrement (chapitre 68).
3. **Principe.** Sur un réseau partagé ou après un détournement de flux, l'attaquant écoute les paquets ; tout ce qui n'est pas chiffré (identifiants, données, jetons) est lisible.
4. **Sous-types.** Sniffing passif (sur média partagé), sniffing après spoofing/MITM, capture sur Wi-Fi.
5. **Exemple conceptuel.** Sur un réseau mal segmenté, des identifiants transmis en clair par un protocole non chiffré sont capturés.
6. **Impacts.** Vol d'identifiants et de données, atteinte à la confidentialité, préparation d'autres attaques.
7. **Détection.** Difficile (passif) ; indices via la détection de mode promiscuité, d'équipements suspects, d'attaques de redirection associées.
8. **Prévention.** **Chiffrement de bout en bout** (TLS), segmentation, commutation (vs hubs), 802.1X, désactivation des protocoles en clair, VPN sur réseaux non fiables.
9. ⚠️ **Erreur fréquente.** Supposer que le réseau interne est « sûr » et y laisser circuler des données en clair.
10. 🎯 **À retenir.** Le sniffing ne lit que ce qui n'est pas chiffré : chiffrer en transit neutralise l'essentiel de la menace.

### Chapitre 130 — Spoofing (vue d'ensemble)

1. **Définition.** Usurpation d'identité d'un élément du réseau (adresse, hôte, service) pour tromper d'autres systèmes.
2. **Famille.** Usurpation. Englobe ARP (131), DNS (132), DHCP (134) spoofing, et le spoofing d'adresses en général.
3. **Principe.** De nombreux protocoles historiques font *confiance par défaut* sans authentifier l'origine ; l'attaquant se fait passer pour une entité légitime (passerelle, serveur DNS, etc.).
4. **Sous-types.** Spoofing d'adresse IP/MAC, ARP, DNS, DHCP, d'e-mail (Partie 9), d'identité de service.
5. **Exemple conceptuel.** Se présenter comme la passerelle du réseau pour que les autres machines envoient leur trafic à l'attaquant.
6. **Impacts.** MITM, interception, redirection, déni de service, base de nombreuses autres attaques réseau.
7. **Détection.** Incohérences d'association (adresse/identité), changements anormaux de tables, surveillance réseau.
8. **Prévention.** Authentification des protocoles, fonctions de sécurité des commutateurs (inspection ARP dynamique, snooping DHCP), segmentation, chiffrement, supervision.
9. ⚠️ **Erreur fréquente.** S'appuyer sur des protocoles non authentifiés sans activer les protections des équipements.
10. 🎯 **À retenir.** Le spoofing exploite la confiance non vérifiée des protocoles : authentifier et activer les protections de commutateur sont les parades clés.

### Chapitre 131 — ARP spoofing

1. **Définition.** Usurpation au niveau de la résolution adresse IP↔MAC (protocole ARP) sur un réseau local.
2. **Famille.** Spoofing (chapitre 130), couche 2.
3. **Principe.** ARP n'authentifie pas les réponses ; l'attaquant annonce que sa propre adresse MAC correspond à l'IP de la passerelle (ou d'un hôte), détournant le trafic vers lui (MITM/sniffing).
4. **Sous-types.** Détournement vers l'attaquant (MITM), déni de service (associations erronées).
5. **Exemple conceptuel.** Les machines du réseau local sont amenées à envoyer leur trafic « vers la passerelle » à l'attaquant, qui relaie en écoutant.
6. **Impacts.** MITM, sniffing, vol d'identifiants, manipulation de trafic, DoS local.
7. **Détection.** Associations IP/MAC changeantes ou dupliquées, surveillance ARP, alertes des outils dédiés.
8. **Prévention.** **Inspection ARP dynamique (DAI)**, snooping DHCP, entrées statiques pour les actifs critiques, segmentation, chiffrement (limite l'impact), 802.1X.
9. ⚠️ **Erreur fréquente.** Réseau local plat sans protections de commutateur.
10. 🎯 **À retenir.** L'ARP spoofing rend le MITM local trivial ; l'inspection ARP dynamique et la segmentation sont les défenses de référence.

### Chapitre 132 — DNS spoofing

1. **Définition.** Falsification des réponses DNS pour rediriger une victime vers une adresse contrôlée par l'attaquant.
2. **Famille.** Spoofing (chapitre 130).
3. **Principe.** En répondant à une requête DNS avant le serveur légitime (ou en empoisonnant un cache), l'attaquant fait correspondre un nom de domaine à une mauvaise adresse.
4. **Sous-types.** Réponse falsifiée locale (souvent après MITM), empoisonnement de cache DNS, manipulation de résolveur.
5. **Exemple conceptuel.** Une victime saisit un nom de site légitime mais est dirigée vers un serveur malveillant à cause d'une réponse DNS falsifiée.
6. **Impacts.** Redirection vers phishing/malware, MITM, interception, contournement de confiance.
7. **Détection.** Réponses DNS incohérentes, résolutions anormales, surveillance DNS.
8. **Prévention.** **DNSSEC** (intégrité des réponses), DNS chiffré (DoH/DoT), résolveurs de confiance, protection contre l'ARP/MITM en amont, surveillance.
9. ⚠️ **Erreur fréquente.** Faire confiance aveuglément à la résolution DNS sur un réseau non maîtrisé.
10. 🎯 **À retenir.** Le DNS spoofing détourne la « carte » du réseau ; DNSSEC et DNS chiffré renforcent l'intégrité des résolutions.

### Chapitre 133 — DNS tunneling

1. **Définition.** Détournement du protocole DNS comme *canal caché* pour exfiltrer des données ou commander un implant (C2).
2. **Famille.** Exfiltration / commande et contrôle (ATT&CK *Exfiltration/C2*).
3. **Principe.** Le DNS est souvent autorisé à sortir même quand le reste est filtré ; l'attaquant encode des données dans les requêtes/réponses DNS pour traverser discrètement le pare-feu.
4. **Sous-types.** Exfiltration de données via DNS, canal C2 via DNS, selon l'encodage et la fréquence.
5. **Exemple conceptuel.** Des données sont encodées dans des noms de sous-domaines résolus vers un serveur DNS contrôlé par l'attaquant, qui les reconstitue.
6. **Impacts.** Exfiltration furtive, contrôle d'implants, contournement du filtrage.
7. **Détection.** Volumes/longueurs de requêtes DNS anormaux, domaines à forte entropie, fréquence inhabituelle, analyse DNS.
8. **Prévention.** Filtrage et inspection DNS, résolveurs internes contrôlés, détection d'anomalies, limitation des résolutions sortantes, filtrage de réputation.
9. ⚠️ **Erreur fréquente.** Laisser le DNS sortir sans inspection ni journalisation, le considérant « inoffensif ».
10. 🎯 **À retenir.** Le DNS peut servir de tunnel furtif : inspecter et journaliser le DNS sortant est essentiel.

### Chapitre 134 — DHCP spoofing

1. **Définition.** Usurpation d'un serveur DHCP pour distribuer aux clients une configuration réseau malveillante.
2. **Famille.** Spoofing (chapitre 130), couche 2/3.
3. **Principe.** Un faux serveur DHCP (rogue) répond aux demandes des clients en fournissant une passerelle/DNS contrôlés par l'attaquant, le plaçant en position de MITM.
4. **Sous-types.** Rogue DHCP, épuisement d'adresses (DHCP starvation) précédant l'installation du rogue.
5. **Exemple conceptuel.** Un client obtient une configuration réseau d'un serveur DHCP pirate, désignant l'attaquant comme passerelle.
6. **Impacts.** MITM, redirection DNS, interception, déni de service.
7. **Détection.** Présence de serveurs DHCP non autorisés, baux incohérents, surveillance.
8. **Prévention.** **DHCP snooping** (n'autoriser le DHCP que sur des ports de confiance), segmentation, surveillance, 802.1X.
9. ⚠️ **Erreur fréquente.** Ne pas activer le DHCP snooping, laissant n'importe quel hôte jouer au serveur DHCP.
10. 🎯 **À retenir.** Le DHCP snooping empêche les serveurs DHCP pirates et coupe ce vecteur de MITM.

### Chapitre 135 — Man-in-the-Middle (MITM)

1. **Définition.** Position d'attaque où l'adversaire s'intercale entre deux parties pour lire et/ou altérer leurs échanges.
2. **Famille.** Interception/usurpation (ATT&CK *Collection — Adversary-in-the-Middle*).
3. **Principe.** Après un détournement de flux (ARP/DNS/DHCP spoofing, rogue AP), l'attaquant relaie les communications en les écoutant, voire en les modifiant, idéalement sans que les parties s'en aperçoivent.
4. **Sous-types.** MITM passif (écoute) vs actif (modification), sur LAN, sur Wi-Fi, via proxy malveillant, downgrade TLS.
5. **Exemple conceptuel.** L'attaquant relaie le trafic entre une victime et un service, capturant ce qui transite et pouvant l'altérer.
6. **Impacts.** Vol d'identifiants/données, manipulation de contenu, contournement d'intégrité, injection.
7. **Détection.** Anomalies de certificats, alertes de spoofing en amont, latences/erreurs TLS, surveillance.
8. **Prévention.** **Chiffrement fort et authentifié** (TLS validé, HSTS), épinglage le cas échéant, protections couche 2 (DAI, DHCP snooping), VPN sur réseaux non fiables, vigilance aux avertissements de certificat.
9. ⚠️ **Erreur fréquente.** Ignorer/accepter les avertissements de certificat (qui signalent souvent un MITM).
10. 🎯 **À retenir.** Le MITM est l'aboutissement de l'interception : le chiffrement *authentifié* (et le respect des alertes de certificat) le rend inefficace.

### Chapitre 136 — Replay attack

1. **Définition.** Réémission de données légitimes capturées (jetons, requêtes authentifiées) pour reproduire une action sans connaître les secrets.
2. **Famille.** Rejeu (CWE-294).
3. **Principe.** Si un message d'authentification/transaction n'est pas lié à un usage unique (nonce, horodatage, séquence), l'attaquant qui l'a capturé peut le « rejouer » pour se faire passer pour l'émetteur.
4. **Sous-types.** Rejeu de jetons/sessions, de requêtes de paiement, de messages d'authentification.
5. **Exemple conceptuel.** Un message d'autorisation capturé est renvoyé tel quel plus tard pour répéter l'action autorisée.
6. **Impacts.** Usurpation, transactions répétées, contournement d'authentification.
7. **Détection.** Messages identiques répétés, horodatages incohérents, séquences anormales.
8. **Prévention.** **Nonces**, horodatages avec fenêtre courte, numéros de séquence, jetons à usage unique, canaux chiffrés authentifiés, idempotence.
9. ⚠️ **Erreur fréquente.** Authentifier sans garantir la *fraîcheur* du message (pas de nonce/horodatage).
10. 🎯 **À retenir.** Sans élément de fraîcheur (nonce/horodatage), un message valide peut être rejoué : lier chaque message à un usage unique.

### Chapitre 137 — Downgrade attack

1. **Définition.** Forcer deux parties à utiliser une version/un algorithme *plus faible* d'un protocole, exploitable ensuite.
2. **Famille.** Dégradation / cryptographie faible (chapitre 68).
3. **Principe.** Pendant la négociation, l'attaquant supprime/altère les options fortes pour imposer un mode vulnérable (chiffrement obsolète, protocole ancien), qu'il peut alors attaquer.
4. **Sous-types.** Downgrade de version TLS/protocole, de suite cryptographique, désactivation forcée du chiffrement (strip).
5. **Exemple conceptuel.** Une négociation est manipulée pour retomber sur une version ancienne et faible d'un protocole, ouvrant la voie à l'interception.
6. **Impacts.** Interception, MITM, cassage cryptographique, contournement de protections.
7. **Détection.** Usage de versions/suites obsolètes, négociations anormales, surveillance TLS.
8. **Prévention.** **Désactiver les versions/algorithmes faibles**, exiger des minimums (TLS récent), HSTS, options anti-downgrade des protocoles, surveillance de la configuration.
9. ⚠️ **Erreur fréquente.** Garder, « pour compatibilité », des protocoles/suites obsolètes activés.
10. 🎯 **À retenir.** On ne peut pas être rétrogradé vers ce qui est désactivé : supprimer les versions et algorithmes faibles ferme la porte au downgrade.

### Chapitre 138 — Exploitation de service exposé

1. **Définition.** Exploitation d'une vulnérabilité dans un service réseau accessible (souvent depuis Internet) pour obtenir un accès.
2. **Famille.** Exploitation (ATT&CK *Initial Access / Exploitation of Remote Services*).
3. **Principe.** Un service exposé et vulnérable (non patché, mal configuré) est attaqué pour exécuter du code ou s'authentifier indûment, fournissant un point d'entrée.
4. **Sous-types.** Exploitation de RCE, de contournement d'authentification, de mauvaise configuration ; sur services web, VPN, bases, partages.
5. **Exemple conceptuel.** Une passerelle exposée et non patchée est exploitée pour obtenir un premier accès au réseau interne.
6. **Impacts.** Accès initial, exécution de code, point de départ du mouvement latéral et de la compromission.
7. **Détection.** Tentatives d'exploitation (signatures IDS/IPS), comportements anormaux du service, alertes EDR, journaux.
8. **Prévention.** **Gestion des vulnérabilités** (patch prioritaire des services exposés), réduction de surface, segmentation, durcissement, accès via bastion/VPN+MFA, supervision.
9. ⚠️ **Erreur fréquente.** Exposer sur Internet des services d'administration ou non patchés (cf. KEV — chapitre 32).
10. 🎯 **À retenir.** Un service exposé non patché est la porte d'entrée n°1 des intrusions : patcher en priorité ce qui est exposé.

### Chapitre 139 — SMB abuse

1. **Définition.** Abus du protocole de partage de fichiers Windows (SMB) pour accès, propagation ou exécution.
2. **Famille.** Exploitation / lateral movement (environnement Windows).
3. **Principe.** SMB sert au partage de fichiers et à diverses opérations administratives ; mal configuré, exposé ou vulnérable, il permet l'accès aux partages, la capture/le relais d'authentification, ou l'exécution à distance.
4. **Sous-types.** Accès à des partages mal protégés, relais d'authentification (NTLM relay), exécution distante via SMB, propagation de malware/ransomware.
5. **Exemple conceptuel.** Un partage accessible et des authentifications relayées permettent de se déplacer vers d'autres machines.
6. **Impacts.** Accès aux données, mouvement latéral, propagation de ransomware, exécution de code.
7. **Détection.** Connexions SMB anormales, relais NTLM, accès massifs aux partages, alertes EDR.
8. **Prévention.** Désactiver SMBv1, signature SMB, segmentation, ne jamais exposer SMB sur Internet, durcissement de l'authentification, moindre privilège, surveillance.
9. ⚠️ **Erreur fréquente.** Laisser SMBv1 activé ou des partages largement accessibles ; exposer SMB hors du réseau interne.
10. 🎯 **À retenir.** SMB est un vecteur classique de propagation interne : le durcir (signature, pas de v1) et le segmenter est crucial. Détaillé côté identité en Partie 8.

### Chapitre 140 — RDP abuse

1. **Définition.** Abus du Bureau à distance (RDP) pour accès interactif non autorisé.
2. **Famille.** Exploitation / accès distant.
3. **Principe.** RDP donne un contrôle interactif d'une machine ; exposé sur Internet ou protégé par des identifiants faibles, il est ciblé par brute force, credential stuffing, ou exploitation de vulnérabilités.
4. **Sous-types.** Brute force/spraying RDP, exploitation de vulnérabilités RDP, détournement de session, pivot via RDP.
5. **Exemple conceptuel.** Un serveur RDP exposé avec un mot de passe faible est compromis, offrant un accès interactif au réseau.
6. **Impacts.** Accès initial, contrôle interactif, mouvement latéral, déploiement de ransomware (vecteur très courant).
7. **Détection.** Pics d'échecs/réussites RDP, connexions depuis l'extérieur ou à des heures anormales, alertes.
8. **Prévention.** **Ne pas exposer RDP sur Internet** (bastion/VPN+MFA), MFA, comptes forts, verrouillage anti-brute-force, restriction réseau, patch, surveillance.
9. ⚠️ **Erreur fréquente.** Exposer directement RDP sur Internet : l'un des vecteurs de rançongiciel les plus exploités.
10. 🎯 **À retenir.** RDP ne doit jamais être exposé nu sur Internet : passer par bastion/VPN + MFA et surveiller les accès.

### Chapitre 141 — VPN exploitation

1. **Définition.** Compromission des passerelles/accès VPN (chapitre 55) pour pénétrer le réseau interne.
2. **Famille.** Exploitation / accès initial.
3. **Principe.** Le VPN, exposé par conception et donnant accès au cœur du réseau, est ciblé via vulnérabilités critiques de la passerelle, vol/réutilisation d'identifiants, ou contournement de MFA.
4. **Sous-types.** Exploitation de CVE de passerelle (RCE), credential stuffing/spraying, contournement/absence de MFA.
5. **Exemple conceptuel.** Une vulnérabilité critique non patchée d'une passerelle VPN permet un accès au réseau interne sans identifiants valides.
6. **Impacts.** Accès initial direct au cœur du réseau, mouvement latéral, compromission étendue.
7. **Détection.** Connexions VPN anormales (lieux, horaires), tentatives d'exploitation, échecs MFA, surveillance.
8. **Prévention.** Patch prioritaire des passerelles, MFA résistant au phishing, moindre privilège d'accès, segmentation post-connexion, migration vers ZTNA, journalisation.
9. ⚠️ **Erreur fréquente.** Retarder les patchs de passerelle VPN ou ne pas y imposer le MFA.
10. 🎯 **À retenir.** Le VPN est une cible de choix : patch immédiat + MFA + moindre privilège, et envisager le ZTNA.

### Chapitre 142 — Pivoting

1. **Définition.** Utiliser une machine compromise comme *relais* pour atteindre des segments réseau autrement inaccessibles.
2. **Famille.** Mouvement latéral / post-exploitation (ATT&CK *Lateral Movement*).
3. **Principe.** Une fois un hôte compromis, l'attaquant l'emploie comme tremplin pour rebondir vers d'autres réseaux qu'il « voit » mais que l'attaquant ne pouvait pas joindre directement.
4. **Sous-types.** Pivot via proxy, redirection de ports, tunneling (chapitre 143).
5. **Exemple conceptuel.** Un poste compromis dans une zone bureautique sert de relais pour atteindre une zone serveur reliée à lui.
6. **Impacts.** Extension de l'accès, contournement de la segmentation imparfaite, progression vers les cibles de valeur.
7. **Détection.** Flux inhabituels entre segments via un hôte, relais/proxy anormaux, trafic est-ouest atypique, EDR/NDR.
8. **Prévention.** **Segmentation/microsegmentation** stricte, moindre privilège, surveillance est-ouest, restriction des flux entre zones, EDR.
9. ⚠️ **Erreur fréquente.** Compter sur une segmentation « partielle » qu'un hôte à cheval sur deux zones annule.
10. 🎯 **À retenir.** Le pivoting transforme un hôte compromis en pont entre zones : une segmentation rigoureuse et la surveillance est-ouest le contrent.

### Chapitre 143 — Tunneling

1. **Définition.** Encapsuler un trafic dans un autre protocole autorisé pour contourner filtrage et détection.
2. **Famille.** Évasion / exfiltration / C2 (ATT&CK *Command and Control — Protocol Tunneling*).
3. **Principe.** L'attaquant fait passer son trafic « interdit » à l'intérieur d'un protocole « autorisé » (DNS, HTTP/S, ICMP), traversant les contrôles qui n'inspectent pas le contenu.
4. **Sous-types.** Tunnel DNS (chapitre 133), HTTP/S, ICMP, via services cloud légitimes.
5. **Exemple conceptuel.** Un canal de commande est dissimulé dans du trafic web sortant chiffré, indistinct du trafic légitime.
6. **Impacts.** Contournement du filtrage, C2 furtif, exfiltration discrète.
7. **Détection.** Anomalies de volume/forme dans les protocoles autorisés, destinations inhabituelles, analyse comportementale, inspection.
8. **Prévention.** Filtrage et inspection en sortie, proxys avec inspection TLS maîtrisée, allowlist de destinations, détection d'anomalies, journalisation, restriction des protocoles sortants.
9. ⚠️ **Erreur fréquente.** N'inspecter que les ports/protocoles « à risque » et laisser HTTP/S/DNS sortir sans analyse.
10. 🎯 **À retenir.** Le tunneling cache l'interdit dans l'autorisé : seules l'inspection et l'analyse comportementale des flux sortants le révèlent.

### Chapitre 144 — Lateral movement

1. **Définition.** Déplacement d'un attaquant d'un système à un autre *au sein* du réseau, après l'accès initial, pour progresser vers ses objectifs.
2. **Famille.** ATT&CK *Lateral Movement* — pivot central de toute intrusion sérieuse.
3. **Principe.** Rarement l'accès initial atteint-il directement la cible. L'attaquant rebondit de machine en machine, en réutilisant des identifiants, en abusant de services d'administration (SMB/RDP/WinRM) et de relations de confiance, jusqu'aux actifs de valeur.
4. **Sous-types.** Via identifiants volés (pass-the-hash/ticket — Partie 8), via SMB/RDP/WinRM, via tâches planifiées, via outils d'administration légitimes (living-off-the-land).
5. **Exemple conceptuel.** Des identifiants récupérés sur un poste servent à se connecter à un serveur, puis à un contrôleur de domaine, de proche en proche.
6. **Impacts.** Extension de la compromission, accès aux joyaux, préalable au ransomware/exfiltration.
7. **Détection.** Connexions inter-machines anormales, usage atypique de comptes/outils d'administration, trafic est-ouest, EDR/NDR, corrélation SIEM.
8. **Prévention.** **Segmentation/microsegmentation**, **tiering** (chapitre 19), moindre privilège, MFA, LAPS (mots de passe locaux uniques), durcissement de l'administration (bastion/PAM), détection comportementale.
9. ⚠️ **Erreur fréquente.** Mots de passe d'administrateur local identiques partout : un seul vol permet de se déplacer sur tout le parc.
10. 🎯 **À retenir.** Le mouvement latéral est le cœur des intrusions réelles : segmentation, tiering, identifiants locaux uniques (LAPS) et moindre privilège le rendent coûteux. Approfondi en Partie 8.

### Chapitre 145 — DoS (Denial of Service)

1. **Définition.** Attaque visant à rendre un service indisponible, en l'épuisant ou en exploitant une faiblesse.
2. **Famille.** Disponibilité (CIA — chapitre 5 ; ATT&CK *Impact*). CWE-400.
3. **Principe.** Submerger les ressources (calcul, mémoire, bande passante, connexions) ou déclencher un plantage par une entrée pathologique, jusqu'à l'arrêt du service pour les utilisateurs légitimes.
4. **Sous-types.** DoS volumétrique (saturation), applicatif (requêtes coûteuses), par exploitation (crash), par épuisement d'état.
5. **Exemple conceptuel.** Une requête particulièrement coûteuse, répétée, sature les ressources et rend le service injoignable.
6. **Impacts.** Indisponibilité, perte de revenus/réputation, parfois diversion pour masquer une autre attaque.
7. **Détection.** Pics de trafic/charge, requêtes coûteuses répétées, dégradation des performances, surveillance.
8. **Prévention.** Limitation de débit (chapitre 79), dimensionnement/élasticité, optimisation des opérations coûteuses, filtrage, time-outs, protections en amont.
9. ⚠️ **Erreur fréquente.** Ignorer le DoS applicatif (peu de trafic mais requêtes très coûteuses) en se focalisant sur le volumétrique.
10. 🎯 **À retenir.** Le DoS attaque la disponibilité ; au-delà du volume, surveiller le coût unitaire des requêtes et plafonner.

### Chapitre 146 — DDoS (Distributed Denial of Service)

1. **Définition.** DoS mené depuis de *nombreuses sources* distribuées (souvent un botnet), démultipliant la puissance.
2. **Famille.** Disponibilité (ATT&CK *Impact — Network Denial of Service*).
3. **Principe.** Des milliers de machines compromises (ou des techniques d'amplification) génèrent simultanément du trafic vers la cible, rendant le filtrage par source difficile et saturant la capacité.
4. **Sous-types.** Volumétrique distribué, par épuisement de protocole, applicatif distribué, combiné à l'amplification/reflection (chapitres 147–148).
5. **Exemple conceptuel.** Un grand nombre d'hôtes répartis envoient simultanément du trafic vers un service, dépassant sa capacité.
6. **Impacts.** Indisponibilité massive, coûts, parfois extorsion (DDoS for ransom), diversion.
7. **Détection.** Pics massifs multi-sources, signatures de DDoS, alertes des protections amont.
8. **Prévention.** **Services anti-DDoS** (scrubbing, CDN), absorption à grande échelle, filtrage en amont (chez l'opérateur), surdimensionnement, plans de réponse, anycast.
9. ⚠️ **Erreur fréquente.** Tenter d'absorber un DDoS volumétrique uniquement sur sa propre infrastructure (capacité insuffisante).
10. 🎯 **À retenir.** Le DDoS exige une défense *en amont* (opérateur/CDN/scrubbing) : on ne le bloque pas seul à la porte de ses serveurs.

### Chapitre 147 — Reflection attack

1. **Définition.** DDoS où l'attaquant envoie des requêtes à des serveurs tiers en *usurpant l'adresse de la victime*, qui reçoit alors toutes les réponses.
2. **Famille.** DDoS (chapitre 146), technique de réflexion.
3. **Principe.** En falsifiant l'adresse source (spoofing), l'attaquant fait répondre des serveurs légitimes *vers la victime*, masquant l'origine réelle et concentrant le trafic sur la cible.
4. **Sous-types.** Réflexion via divers protocoles UDP sans état ; souvent combinée à l'amplification (chapitre 148).
5. **Exemple conceptuel.** De nombreux serveurs tiers, sollicités avec l'adresse usurpée de la victime, lui renvoient leurs réponses simultanément.
6. **Impacts.** Saturation de la victime, anonymisation de l'attaquant.
7. **Détection.** Afflux de réponses non sollicitées vers la victime, sources multiples « légitimes », surveillance.
8. **Prévention.** **Anti-spoofing** (filtrage des adresses source côté opérateurs — BCP38), durcissement des services réflecteurs, anti-DDoS amont, limitation.
9. ⚠️ **Erreur fréquente.** Laisser des services exploitables comme réflecteurs accessibles publiquement.
10. 🎯 **À retenir.** La réflexion détourne des serveurs tiers contre la victime ; l'anti-spoofing réseau et le durcissement des réflecteurs la limitent.

### Chapitre 148 — Amplification attack

1. **Définition.** Variante de réflexion où la *réponse* est bien plus grande que la requête, multipliant le volume envoyé à la victime.
2. **Famille.** DDoS (chapitre 146), couplée à la réflexion.
3. **Principe.** L'attaquant choisit des protocoles dont une petite requête déclenche une grosse réponse ; combiné au spoofing, un faible effort génère un trafic massif vers la victime (facteur d'amplification).
4. **Sous-types.** Selon les protocoles à fort facteur d'amplification.
5. **Exemple conceptuel.** Une petite requête usurpée déclenche une réponse volumineuse dirigée vers la victime, démultipliant le débit d'attaque.
6. **Impacts.** Saturation très efficace avec peu de ressources côté attaquant.
7. **Détection.** Trafic entrant volumineux d'un protocole donné, réponses massives non sollicitées, surveillance.
8. **Prévention.** Identiques à la réflexion (anti-spoofing, durcissement des services amplificateurs, anti-DDoS amont, désactivation/limitation des services exposés exploitables).
9. ⚠️ **Erreur fréquente.** Exposer publiquement des services connus pour leur fort facteur d'amplification, sans restriction.
10. 🎯 **À retenir.** L'amplification rend le DDoS « pas cher » pour l'attaquant : durcir les services amplificateurs et filtrer le spoofing en amont.

### Chapitre 149 — Botnet

1. **Définition.** Réseau de machines compromises (bots) contrôlées à distance par un attaquant pour des actions coordonnées.
2. **Famille.** Infrastructure offensive / C2 (ATT&CK *Command and Control*, *Impact*).
3. **Principe.** Des hôtes infectés (postes, serveurs, IoT) reçoivent des ordres d'un serveur de commande et contrôle (C2) et exécutent collectivement des tâches : DDoS, spam, minage, exfiltration, relais.
4. **Sous-types.** Botnets DDoS, de spam, de minage, IoT, à C2 centralisé vs pair-à-pair, à C2 furtif (DNS/HTTP).
5. **Exemple conceptuel.** Des milliers d'objets connectés mal sécurisés sont enrôlés pour lancer un DDoS sur commande.
6. **Impacts.** DDoS massif, spam/phishing à grande échelle, minage, relais d'attaques, exfiltration.
7. **Détection.** Trafic C2 (balises périodiques), connexions vers des domaines/IP malveillants, comportements coordonnés, EDR/NDR, renseignement (CTI).
8. **Prévention.** Hygiène anti-malware (EDR, patch), durcissement IoT (chapitre 52), filtrage sortant et de réputation, détection de C2, segmentation, sensibilisation.
9. ⚠️ **Erreur fréquente.** Négliger les objets connectés peu sécurisés, principal réservoir de bots.
10. 🎯 **À retenir.** Un botnet transforme des machines négligées en armée offensive : l'hygiène (patch, EDR, IoT durci) tarit la source, la détection de C2 repère l'enrôlement.

### Chapitre 150 — VLAN hopping

1. **Définition.** Attaque permettant à un hôte de communiquer avec un VLAN auquel il ne devrait pas avoir accès, brisant la segmentation de couche 2.
2. **Famille.** Couche 2 / contournement de segmentation.
3. **Principe.** En exploitant des configurations de commutateur permissives (négociation de trunk automatique, double étiquetage), un attaquant fait sortir son trafic du VLAN attribué vers un autre.
4. **Sous-types.** Via usurpation de commutateur (switch spoofing), via double tagging.
5. **Exemple conceptuel.** Un hôte se fait passer pour un commutateur et négocie un lien trunk, accédant à des VLAN normalement isolés.
6. **Impacts.** Contournement de la segmentation, accès à des zones sensibles, MITM inter-VLAN.
7. **Détection.** Négociations de trunk inattendues, trafic inter-VLAN anormal, surveillance des commutateurs.
8. **Prévention.** **Désactiver la négociation automatique de trunk**, fixer explicitement les ports en mode accès, VLAN natif dédié, durcissement des commutateurs, restriction des ports.
9. ⚠️ **Erreur fréquente.** Laisser les ports en négociation automatique (DTP) et un VLAN natif partagé.
10. 🎯 **À retenir.** La segmentation VLAN n'est sûre que si les commutateurs sont durcis : désactiver la négociation de trunk et fixer les modes de port.

### Chapitre 151 — Wi-Fi Evil Twin

1. **Définition.** Faux point d'accès Wi-Fi imitant un réseau légitime pour capter les connexions des victimes.
2. **Famille.** Sans fil / usurpation / MITM.
3. **Principe.** L'attaquant diffuse un point d'accès portant le même nom (SSID) qu'un réseau de confiance ; les appareils s'y connectent, plaçant l'attaquant en position de MITM.
4. **Sous-types.** Evil twin sur réseau ouvert, avec portail captif factice, couplé à la deauth (chapitre 153) pour forcer la reconnexion.
5. **Exemple conceptuel.** Dans un lieu public, un faux réseau au nom familier capte les appareils qui s'y connectent automatiquement.
6. **Impacts.** MITM, vol d'identifiants, interception, injection, redirection vers phishing.
7. **Détection.** Points d'accès dupliqués (même SSID, BSSID différent), détection de rogue AP (WIPS), surveillance.
8. **Prévention.** WPA2/WPA3-Enterprise (authentification mutuelle), VPN sur Wi-Fi non fiable, désactivation de la connexion automatique, sensibilisation, WIPS.
9. ⚠️ **Erreur fréquente.** Se connecter automatiquement à des réseaux ouverts au nom familier.
10. 🎯 **À retenir.** L'evil twin exploite la confiance dans un nom de réseau : l'authentification mutuelle (WPA-Enterprise) et le VPN le neutralisent.

### Chapitre 152 — Rogue access point

1. **Définition.** Point d'accès non autorisé branché sur le réseau (souvent par un employé bien intentionné ou un attaquant), créant une entrée incontrôlée.
2. **Famille.** Sans fil / extension non maîtrisée de surface.
3. **Principe.** Un AP non géré relié au réseau interne ouvre un accès sans fil échappant aux contrôles, contournant le périmètre filaire sécurisé.
4. **Sous-types.** Rogue AP interne (employé), AP malveillant (attaquant), distinct de l'evil twin (qui imite, sans forcément être branché au réseau).
5. **Exemple conceptuel.** Un petit point d'accès personnel branché sur une prise réseau interne crée une porte d'entrée sans fil non sécurisée.
6. **Impacts.** Accès non contrôlé au réseau interne, contournement des défenses, point d'entrée.
7. **Détection.** Détection de points d'accès non autorisés (WIPS), inventaire, surveillance des ports, balayage radio.
8. **Prévention.** Contrôle d'accès réseau (802.1X/NAC), détection WIPS, politique stricte, désactivation des ports inutilisés, sensibilisation.
9. ⚠️ **Erreur fréquente.** Ne pas surveiller l'apparition d'AP non autorisés ni verrouiller les ports réseau.
10. 🎯 **À retenir.** Un rogue AP perce un trou sans fil dans le périmètre : NAC et détection WIPS sont les parades.

### Chapitre 153 — Deauthentication

1. **Définition.** Attaque sans fil forçant la déconnexion d'appareils d'un réseau Wi-Fi.
2. **Famille.** Sans fil / disponibilité / préparation MITM.
3. **Principe.** En exploitant des trames de gestion non protégées, l'attaquant envoie des ordres de déconnexion qui éjectent les clients, provoquant un DoS ou les poussant à se reconnecter (vers un evil twin, ou pour capturer la reconnexion).
4. **Sous-types.** Deauth comme DoS, deauth comme déclencheur de reconnexion (vers evil twin/capture).
5. **Exemple conceptuel.** Des trames de déconnexion répétées empêchent les clients de rester connectés, ou les forcent à se reconnecter sur un faux point d'accès.
6. **Impacts.** Déni de service Wi-Fi, facilitation de l'evil twin et de la capture d'authentification.
7. **Détection.** Volume anormal de trames de déconnexion, WIPS, déconnexions répétées.
8. **Prévention.** **Protection des trames de gestion** (802.11w/PMF), WPA3, WIPS, surveillance, réseaux filaires pour le critique.
9. ⚠️ **Erreur fréquente.** Utiliser un Wi-Fi sans protection des trames de gestion (PMF).
10. 🎯 **À retenir.** La deauth abuse de trames non protégées : activer la protection des trames de gestion (802.11w/WPA3) la contre.

### Chapitre 154 — BGP hijacking et route leak

1. **Définition.** Manipulation du routage Internet : détourner (hijack) ou divulguer par erreur (leak) des routes pour rediriger ou intercepter du trafic à grande échelle.
2. **Famille.** Routage / infrastructure Internet / intégrité-disponibilité.
3. **Principe.** BGP, protocole de routage entre opérateurs, repose historiquement sur la confiance ; une annonce illégitime de routes peut détourner du trafic destiné à un réseau vers un autre (interception, blackhole, MITM).
4. **Sous-types.** Hijack (annonce malveillante d'un préfixe), route leak (propagation accidentelle de routes), détournement vers interception ou indisponibilité.
5. **Exemple conceptuel.** Un opérateur annonce à tort être le meilleur chemin vers un réseau, attirant et détournant son trafic.
6. **Impacts.** Interception/détournement de trafic à l'échelle d'Internet, indisponibilité, MITM, atteinte massive.
7. **Détection.** Surveillance des annonces BGP, anomalies de chemins, services de monitoring du routage, alertes.
8. **Prévention.** **RPKI** (validation de l'origine des routes), filtrage des préfixes, bonnes pratiques opérateurs (MANRS), surveillance BGP, relations de peering maîtrisées.
9. ⚠️ **Erreur fréquente.** Absence de validation d'origine (RPKI) et de filtrage de préfixes côté opérateur.
10. 🎯 **À retenir.** Le BGP hijacking détourne le trafic à l'échelle d'Internet ; la validation d'origine (RPKI) et le filtrage des préfixes sont les défenses structurantes.

---

> **Fin du Volume 4/8.**
>
> Vous savez désormais analyser les attaques réseau par intention (reconnaissance, interception, usurpation, rejeu/dégradation, exploitation/déplacement, disponibilité, abus d'infrastructure) et leurs défenses (chiffrement authentifié, protections de commutateur, segmentation, anti-DDoS amont, durcissement sans fil et routage).
>
> **Suite — Volume 5 : Partie 8, Identité, Active Directory et privilèges** (l'identité comme périmètre ; Kerberos/NTLM/LDAP ; tiering ; Kerberoasting, AS-REP roasting, password spraying, pass-the-hash/ticket, overpass-the-hash, golden/silver ticket, DCSync/DCShadow, abus de délégation/RBCD, GPO/ACL abuse, shadow credentials, AD CS abuse, credential dumping, lateral movement Windows, PAM/bastion).


---


## Taxonomie de la cybersécurité — Volume 5/8

> Partie 8 : Identité, Active Directory et privilèges
>
> « L'identité est le nouveau périmètre. » Cette partie est centrale : la majorité des intrusions sérieuses convergent vers la compromission de l'annuaire et des comptes privilégiés. On y décrit les *fondations* (Kerberos, NTLM, LDAP, tiering), puis les grandes familles d'attaques d'identité, toujours côté défensif et conceptuel.
>
> **Posture** : on explique *pourquoi* et *comment se défendre*, sans procédure offensive opérationnelle ni commande exploitable.

---
