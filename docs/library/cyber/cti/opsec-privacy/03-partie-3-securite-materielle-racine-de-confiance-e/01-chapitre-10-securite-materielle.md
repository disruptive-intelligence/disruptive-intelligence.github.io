---
title: Chapitre 10 — Sécurité matérielle
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 3 — Sécurité matérielle, racine de confiance et isolation
  - index.md
---

choix, supply chain, intégrité physique

## 10.1 Modèle d’attaque physique

L’attaquant physique est radicalement plus dangereux que l’attaquant distant. S’il a accès à ton appareil, même brièvement, la plupart des défenses logicielles s’effondrent. Quatre scénarios :

- **Vol opportuniste** : sac arraché, ordinateur oublié au café. Adversaire faible, mais accès total à l’appareil éteint puis allumé.
- **Evil maid** : accès temporaire pendant ton absence (chambre d’hôtel, bureau, frontière). Adversaire compétent : modification de firmware, ajout de keylogger matériel, clonage de disque, implantation de backdoor.
- **Saisie** : douane, perquisition, arrestation. Adversaire étatique avec accès quasi illimité à l’appareil.
- **Coercition** : tu es présent et contraint de fournir codes et accès. Aucune défense technique pure n’y résiste totalement.

Le chiffrement complet (Ch 12) protège contre vol et saisie *si l’appareil est en BFU (Before First Unlock)*. Il protège peu contre evil maid (qui agit sur l’appareil éteint mais peut pré-installer des éléments qui s’activeront après ton déverrouillage). Il ne protège pas contre coercition.

## 10.2 Choix de matériel : coprocesseurs de sécurité

Les laptops modernes intègrent souvent un coprocesseur dédié à la sécurité, qui isole les opérations cryptographiques sensibles du processeur principal :

- **Apple Silicon (M1/M2/M3/M4)** : Secure Enclave intégré au SoC, gère les clés de chiffrement FileVault, Touch ID, déverrouillage. Architecture mature et auditée.
- **Microsoft Pluton** : disponible sur certains processeurs AMD Ryzen et Intel récents (à partir de 2022, généralisé en 2024-2025). Coprocesseur sécurisé directement dans le CPU.
- **Google Titan M2** sur Pixel : équivalent Secure Enclave côté Android, gère le déverrouillage, l’attestation, le stockage de clés.
- **TPM 2.0 discret** : sur la majorité des laptops Windows depuis 2021. Moins intégré qu’un coprocesseur dédié mais offre des garanties cryptographiques sérieuses (Ch 11).

**Conséquence pratique** : un Pixel récent + GrapheneOS, un MacBook Apple Silicon, ou un laptop Windows avec Pluton offrent aujourd’hui de bien meilleures garanties matérielles qu’un laptop générique sans TPM.

## 10.3 ThinkPad, Framework et le choix Linux

Pour ceux qui veulent du Linux durci, deux choix s’imposent en 2025-2026 :

- **ThinkPad** récents (T14, X1 Carbon, P-series) : bon support Linux, TPM 2.0, qualité industrielle, certaines références supportent Coreboot ou Heads (cf. Ch 11).
- **Framework Laptop** : modulaire, support Linux excellent, choix éthique sur la réparabilité.

Risque commun : les **mises à jour firmware** dépendent du constructeur. Sur ThinkPad, fwupd/LVFS gère bien. Sur d’autres marques, les firmwares restent obscurs et rarement mis à jour côté Linux.

## 10.4 Supply chain

L’attaquant peut intercepter ton matériel entre la commande et la livraison. Cas documentés : NSA TAO interceptait des routeurs Cisco avant livraison pour y implanter des backdoors (révélations Snowden). Pour un individu :

- Acheter directement en magasin physique limite l’interception postale.
- L’achat d’occasion expose à un matériel déjà compromis ou modifié.
- Le refurbishing professionnel certifié réduit ce risque sans l’éliminer.
- Pour les cibles à haut risque : achat en personne, dans un magasin choisi au dernier moment, paiement cash.

## 10.5 Détection d’intrusion physique

Tu ne peux pas empêcher l’evil maid si l’attaquant est compétent. Tu peux le *détecter*, ce qui change la stratégie défensive : un appareil suspecté de compromission n’est plus utilisé pour le sensible.

Techniques élémentaires :

- **Vis non standard** sur les panneaux d’accès (Torx Security, etc.).
- **Vernis à ongles glittery** sur les vis et joints du boîtier : motif unique, photographié pour comparaison ultérieure.
- **Photo macro** de la disposition des composants internes lors de l’achat, pour comparaison.
- **Scellés** sur les ports USB inutilisés.
- **Câble Kensington** ou solution équivalente quand l’appareil est en lieu non sûr.

Aucune de ces techniques n’arrête un attaquant gouvernemental sérieux, mais elles arrêtent l’attaquant moyen et imposent un coût supérieur au reste.

## 10.6 Disposal sécurisé

Quand un appareil sort de ton circuit (revente, recyclage, défaillance), il emporte tes données. Trois niveaux :

- **Disque mécanique (HDD)** : effacement multipasses (DBAN, NIST 800-88 Clear) reste valide.
- **SSD** : l’effacement logique est moins fiable (wear leveling). La commande `cryptographic erase` via le firmware SSD (souvent `hdparm --security-erase`) est plus efficace. En dernier recours : broyage physique. ANSSI recommande la destruction physique pour les SSD contenant des secrets sensibles.
- **Téléphones** : reset usine + chiffrement actif est généralement suffisant. Sur GrapheneOS, la procédure inclut un effacement complet du stockage chiffré.

## 10.7 Périphériques non fiables

USB et ports d’extension sont les vecteurs sous-estimés. BadUSB (Hak5 Rubber Ducky et clones) émule un clavier et tape des commandes à grande vitesse dès le branchement. Les câbles peuvent être piégés (O.MG cables).

Règles : ne jamais brancher un USB inconnu ; pour le chargement public, préférer un câble *data-only-off* (ou un USB condom comme PortaPow) ; sur Linux, paquet `usbguard` qui bloque les périphériques USB non whitelistés ; sur Windows, Device Guard et Credential Guard.

## 10.8 Webcam, micro, capteurs

Couverture caméra physique : trivial, efficace. Apple le déconseille sur MacBook (risque d’écraser le mécanisme), mais une fine pellicule autocollante reste sans risque. Pour le micro : sur certains laptops, un interrupteur matériel (Framework, certains ThinkPad). Sinon, désactivation logicielle (qui peut être contournée par malware) ou retrait physique du module si nécessaire.

Sur smartphone, les modes « micro/caméra coupés au niveau OS » de iOS (indicateurs verts) et GrapheneOS (toggle système) offrent des garanties matérielles. Sur Android stock, ces indicateurs existent mais l’OS reste contournable par exploits.

> 🟩 **À retenir du chapitre 10**
> 
> - Attaquant physique > attaquant distant. Le matériel est la racine.
> - Coprocesseurs de sécurité (Secure Enclave, Pluton, Titan M2) changent la donne.
> - Tu ne peux pas empêcher l’evil maid compétent, tu peux le détecter.
> - Disposal sécurisé : SSD = effacement crypto ou broyage.
> - Le minimum réaliste pour la plupart : laptop récent avec TPM 2.0, BitLocker/FileVault/LUKS, vis vernies, vigilance sur les USB.

-----
