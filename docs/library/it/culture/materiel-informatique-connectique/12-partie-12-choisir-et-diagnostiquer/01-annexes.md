---
title: Annexes
source: IT/Culture/Materiel_informatique-connectique-andco.md
note: Matériel informatique & connectique
up:
- - Matériel informatique & connectique
  - ../index.md
- - Partie 12 — Choisir et diagnostiquer
  - index.md
---

---

## Annexe A — Sources et standards à surveiller

Le matériel évolue, et les chiffres de ce cours (débits, puissances, versions) bougent avec les normes. Pour vérifier une information ou suivre les évolutions, voici les **organismes officiels** qui publient et maintiennent chaque standard. En cas de doute, ce sont eux qui font foi — avant les blogs et revendeurs.

| Domaine | Organisme | Ce qu'il définit |
|---|---|---|
| Vidéo HDMI | **HDMI Forum** / HDMI Licensing Administrator | Versions HDMI (2.0, 2.1, 2.2), câbles (Ultra High Speed, Ultra96) |
| Vidéo PC | **VESA** | DisplayPort (1.4, 2.1), DisplayHDR, Adaptive-Sync |
| USB & USB-C | **USB-IF** (USB Implementers Forum) | USB 2.0/3.x, USB4, USB Power Delivery, logos de certification |
| Thunderbolt | **Intel** | Thunderbolt 3/4/5 |
| Wi-Fi | **Wi-Fi Alliance** / **IEEE 802.11** | Certifications Wi-Fi 6/6E/7, normes 802.11 sous-jacentes |
| Bus interne | **PCI-SIG** | PCI Express (3.0, 4.0, 5.0…) |
| Mémoire | **JEDEC** | DDR4, DDR5, vitesses en MT/s, ECC |
| Stockage flash | **NVM Express (NVMe)** | Interface NVMe des SSD |
| Stockage entreprise | **SNIA** | Concepts et standards de stockage (RAID, SAN…) |
| Réseau filaire | **IEEE 802.3** | Ethernet, catégories de câbles, PoE (802.3af/at/bt) |
| Électricité / sécurité | **IEC** (+ normes nationales) | Normes électriques, connecteurs, sécurité |

> **🎯 À retenir**
> Quand une fiche produit annonce un chiffre flatteur (« HDMI 2.1 », « 240 W », « Wi-Fi 7 »), le réflexe est de croiser avec l'organisme officiel correspondant : le standard autorise souvent des supports *partiels*, et c'est la source officielle qui dit ce que la mention garantit réellement.

---

## Annexe B — Fiches réflexes

Sept aide-mémoires condensés, à consulter en situation. Chacun renvoie au chapitre détaillé.

### B.1 — Choisir un câble USB-C (ch. 28)

1. **Vidéo ?** → le port hôte doit gérer DisplayPort Alt Mode (logo DP) ou Thunderbolt (⚡), et le câble être « full featured » (pas charge seule).
2. **Charge > 60 W ?** → câble **e-marked** obligatoire, repérable au logo **« 240 W »**.
3. **Haut débit ?** → vérifier la mention USB-IF (« 40 Gbps », « 80 Gbps ») et la longueur (1 m max en passif pour 80 Gb/s).
4. **Thunderbolt / eGPU / dock ?** → câble **certifié Thunderbolt** (éclair + chiffre), pas un câble de charge.
5. **Règle d'or** : un câble est spécialisé. Étiqueter ses câbles évite des heures de diagnostic.

### B.2 — Choisir un écran (ch. 19-21, 45)

1. **Usage** : bureautique/code (IPS, 16:10), jeu (haute fréquence + VRR), création (IPS/OLED calibrable, % DCI-P3).
2. **Densité** = résolution rapportée à la taille, pas la résolution seule.
3. **Fréquence** : vérifier *via quelle connectique* l'atteindre (DisplayPort pour 144 Hz+).
4. **HDR** : ignorer « DisplayHDR 400 » (faux HDR) ; viser 600+ nits, Mini-LED ou OLED.
5. **Connectique** : croiser résolution + fréquence + version de port + câble.

### B.3 — Choisir un chargeur (ch. 1, 39, 28)

1. La puissance annoncée est un **plafond**, pas une dose imposée : un gros chargeur ne « grille » pas un petit appareil.
2. Privilégier un **USB-PD multiport** de qualité ; vérifier la puissance *par port* (elle se partage).
3. Pour un PC portable : viser la puissance réelle de pointe (un PC gaming peut tirer 130-200 W).
4. Charge rapide « maison » = souvent **propriétaire** (bon chargeur + bon câble de la marque requis).
5. Câble à la hauteur : e-marked (logo 240 W) si > 60 W.

### B.4 — Diagnostiquer un écran noir (ch. 47.2)

1. Écran allumé, sur la **bonne entrée** (HDMI 1/2, DP) ? (cause la plus fréquente)
2. Tester **autre câble** + **autre port**.
3. Brancher sur le **GPU dédié**, pas la carte mère.
4. Isoler : écran sur un autre PC, PC sur un autre écran.
5. Si le POST réussit (LED de diagnostic), c'est l'affichage, pas le démarrage.

### B.5 — Diagnostiquer un problème réseau (ch. 43, 47.8-47.9)

1. **Filaire fonctionne-t-il ?** Si oui → problème Wi-Fi, pas Internet.
2. Si rien : **voyants box/ONT** → panne opérateur ?
3. Décomposer la chaîne : opérateur → routeur → réseau local → Wi-Fi.
4. Filaire lent : catégorie du **câble** (paire coupée → bridé à 100 Mb/s), carte réseau, port du switch.
5. Wi-Fi lent : comparer près/loin, bonne bande (5/6 GHz près, 2,4 GHz loin), mesh si grande surface.

### B.6 — Lire une fiche PC portable (ch. 45)

1. **CPU** : génération + suffixe (U/H/HX) bien plus que le nom.
2. **RAM** : quantité, et surtout **soudée ou non**.
3. **Stockage** : SSD NVMe, emplacement libre ?
4. **Connectiques** : quels ports USB-C sortent la vidéo / font Thunderbolt ?
5. **Autonomie** (Wh, à minorer d'un tiers) et **réparabilité**.

### B.7 — Sécuriser une box / NAS / imprimante (ch. 44)

1. **Changer les identifiants par défaut** (le réflexe n°1).
2. **Mettre à jour le firmware** régulièrement.
3. **Ne jamais exposer** un NAS / une interface d'admin (BMC, box) directement à Internet → VPN.
4. **Segmenter** : IoT, caméras et invités sur un réseau séparé (VLAN/Wi-Fi invité).
5. Activer la **double authentification** là où c'est possible (NAS, accès distant).

---

## Annexe C — Cinq mini-labs de diagnostic (optionnels)

Des exercices pratiques pour ancrer la méthode. Chacun se fait avec du matériel courant ; l'objectif n'est pas de « réparer » mais d'**appliquer la démarche** : isoler une variable à la fois, identifier le maillon faible, vérifier connecteur/câble/protocole. Les pistes de correction renvoient au chapitre 47.

### Lab 1 — L'écran capricieux
**Mise en situation.** Un écran 1440p 144 Hz n'affiche que 60 Hz une fois branché à un PC.
**À faire.** Lister, dans l'ordre, les vérifications à mener. Identifier les trois maillons possibles.
**Attendu.** (1) Réglage de fréquence dans l'OS ; (2) version/qualité du câble pour le couple 1440p+144 Hz ; (3) version du port utilisé. Tester en changeant *une* variable à la fois. → *ch. 47.4*

### Lab 2 — La charge qui n'avance pas
**Mise en situation.** Un PC portable branché en USB-C se décharge quand même en pleine charge de travail.
**À faire.** Déterminer si c'est une panne ou un sous-dimensionnement, et le prouver.
**Attendu.** Comparer puissance du chargeur vs consommation de pointe ; vérifier câble (e-marked / logo 240 W) et port (entrée d'alimentation). Test décisif : ça charge au repos mais se vide en charge lourde → sous-dimensionnement, pas panne. → *ch. 47.11 et 1*

### Lab 3 — Le SSD fantôme
**Mise en situation.** Un SSD M.2 neuf n'apparaît nulle part après installation.
**À faire.** Proposer les causes par ordre de probabilité et la vérification associée.
**Attendu.** Type M.2 (SATA vs NVMe) compatible avec le port ? Tableau de partage des lignes PCIe (un 2e M.2 peut désactiver des ports SATA) ? SSD bien enfiché/vissé ? Disque neuf à initialiser/formater ? → *ch. 47.7, 6 et 8*

### Lab 4 — Le Gigabit qui n'en est pas
**Mise en situation.** Une liaison Ethernet censée faire 1 Gb/s plafonne à 100 Mb/s.
**À faire.** Identifier le maillon faible le plus probable et le test pour le confirmer.
**Attendu.** Un câble bridé à 100 Mb/s a souvent une **paire coupée** (le Gigabit utilise les 4 paires). Vérifier catégorie/état du câble, port du switch, carte réseau, auto-négociation. Tester un autre câble certifié. → *ch. 47.8 et 34*

### Lab 5 — La baie mystère (orienté admin sys / homelab)
**Mise en situation.** Dans une petite baie, une prise murale ne donne plus de réseau, et un serveur ne répond plus.
**À faire.** Décrire la démarche en s'appuyant sur le brassage et la gestion hors-bande.
**Attendu.** Côté prise : suivre l'étiquetage jusqu'au patch panel, tester le cordon de brassage (souvent coupable), puis la liaison fixe au testeur. Côté serveur figé : se connecter à l'**iDRAC/iLO** (hors-bande) pour voir l'écran et forcer un redémarrage sans déplacement ; en dernier recours, couper/relancer via la **PDU** pilotable. → *ch. 47.8, 38, 15 et 18*

> **🎯 À retenir**
> Les cinq labs partagent la même colonne vertébrale : on ne devine pas, on **isole**. Une variable change à la fois, du plus probable au plus complexe, en se demandant toujours : est-ce le connecteur, le câble, ou le protocole ? Et quel est le maillon faible de la chaîne ?

---

*Fin des annexes — Édition 2.1.*
