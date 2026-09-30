---
title: Chapitre 22 — Wi-Fi, Bluetooth, cellulaire, MAC, IMSI
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 5 — Réseau, anonymat et navigation web
  - index.md
---

## 22.1 Le téléphone éteint qui n’est pas éteint

Le modem baseband d’un smartphone fonctionne souvent même en mode avion (selon implémentation OEM et version OS). Sur certains téléphones, retirer la batterie était la seule garantie d’isolement radio — mais les batteries modernes sont rarement amovibles. La seule garantie d’isolement physique aujourd’hui : **faraday bag** (sac de Faraday qui bloque les ondes).

## 22.2 IMSI catchers et générations cellulaires

Un **IMSI catcher** (Stingray, DRT box, Hailstorm) simule une antenne-relais légitime. Le téléphone du sujet, par fonctionnement normal du protocole cellulaire, se connecte à l’antenne offrant le meilleur signal sans authentifier en retour cette antenne — c’est l’asymétrie d’authentification historique du GSM. L’IMSI catcher capture les IMSI (identifiants SIM) des téléphones présents, peut downgrader la connexion vers du 2G (où le chiffrement est faible ou absent), et selon les variantes, intercepter ou injecter des SMS/appels.

**Génération par génération** :

- **2G (GSM)** : authentification du téléphone par le réseau, *pas* d’authentification du réseau par le téléphone. IMSI catcher trivial. Chiffrement A5/1 et A5/2 cassables.
- **3G (UMTS)** : authentification mutuelle introduite. IMSI catchers doivent forcer un downgrade vers 2G ou exploiter des failles. Beaucoup d’opérateurs en 2025 ont éteint la 2G ; le downgrade devient plus difficile.
- **4G (LTE)** : authentification mutuelle. IMSI catchers 4G existent mais plus complexes (capture du TMSI plutôt que de l’IMSI dans certaines configurations).
- **5G NSA (Non Standalone)** : architecture mixte qui réutilise le cœur 4G ; pas de réelle protection IMSI supplémentaire en pratique.
- **5G SA (Standalone)** : chiffre l’IMSI (devenu SUPI) à l’aide d’une clé publique du réseau (SUCI). Réellement protecteur si l’opérateur déploie en mode SA, ce qui reste partiel en Europe (déploiement progressif 2024-2026, plus avancé en Asie).

**Usages documentés des IMSI catchers** : forces de l’ordre (US, Allemagne, France pour terrorisme et certaines enquêtes graves, Suisse, etc.), services de renseignement, criminalité organisée (cas documentés, notamment au Mexique). Déploiement sur manifestations rapporté en plusieurs pays. ACLU et La Quadrature du Net ont documenté l’usage en juridictions diverses.

**Détection** : applications comme AIMSICD (Android), SnoopSnitch (Android, nécessite un modem Qualcomm spécifique et un téléphone rooté) tentent de détecter par anomalies du réseau cellulaire. Fiabilité limitée et taux de faux positifs élevé. Sur iOS, pas d’option utilisateur (l’accès au baseband est verrouillé).

**Défenses** :

- Vérifier si l’opérateur propose 5G SA et basculer si possible.
- Éteindre complètement la radio en zone à risque (faraday bag, *vrai* mode avion vérifié).
- Pour profils Niveau 3 : usage d’un téléphone sans SIM (Wi-Fi only via routeur de voyage VPN), ou téléphone burner avec eSIM jetable.

## 22.3 MAC randomization

L’adresse MAC d’une interface réseau (Wi-Fi, Bluetooth) est en théorie unique et permanente. Les OS modernes la **randomisent** par défaut pour réduire le tracking :

- **iOS** : MAC aléatoire par SSID depuis iOS 14.
- **Android 10+** : MAC aléatoire par SSID.
- **Windows 10+** : option à activer manuellement.
- **macOS** : randomisation depuis Big Sur.
- **Linux** : via NetworkManager (option `wifi.cloned-mac-address=random`) ou `macchanger`.

**Limite** : MAC aléatoire *par SSID*, pas à chaque connexion. Donc deux connexions au même réseau gardent la même MAC randomisée → corrélation locale possible.

## 22.4 Wi-Fi probing

Quand le Wi-Fi est activé, ton téléphone émet en continu des **probe requests** pour rechercher les réseaux qu’il connaît : « Hé, le réseau ‹MaisonJean› est-il là ? Et ‹BureauX› ? Et ‹AirportDubai› ? ». Cette liste de SSID *que tu connais* est en clair dans l’air. Elle révèle ton historique de lieux.

**Mitigation** : iOS et Android modernes randomisent et limitent ces probes. Mais l’historique reste parfois exploitable par appareils de surveillance Wi-Fi. **Action** : sur appareils sensibles, désactiver Wi-Fi quand non utilisé, et supprimer périodiquement les SSID enregistrés.

## 22.5 Bluetooth et BLE beacons

Le Bluetooth Low Energy (BLE) permet aux magasins, aéroports, transports de te tracker passivement via beacons. AirTags d’Apple et équivalents (Tile, Samsung) permettent aussi le tracking. Apple et Google ont introduit des protections (alertes en cas de tracker inconnu qui te suit), mais elles ne sont pas parfaites.

**Cas d’usage offensif** : un harceleur peut glisser un AirTag dans tes affaires. iOS et Android alertent (depuis 2024-2025), mais le délai peut être de plusieurs heures.

## 22.6 Hotspots Wi-Fi publics

Vraies vs fausses menaces 2025 :

- **Faux Wi-Fi (« evil twin »)** : reste un risque. Atténué par HTTPS partout.
- **Sniffing** : la quasi-totalité du trafic est en HTTPS aujourd’hui. Le risque a baissé.
- **Captive portal** : peut injecter des cookies ou rediriger.
- **Réinjection MITM sur applications mal configurées** : applications mobiles avec certificat pinning défaillant.

Le Wi-Fi public est moins dangereux qu’il y a 10 ans. Un VPN reste utile pour cacher le trafic à l’opérateur du Wi-Fi, et pour éviter les captive portals intrusifs.

## 22.7 Routeur domestique et box opérateur

La box opérateur est une boîte noire dont le firmware est contrôlé par l’opérateur. Pour profil sérieusement durci : remplacer par un routeur sous OpenWrt ou pfSense en pont, et reléguer la box à un rôle minimal de modem.

Configuration minimale du routeur :

- Wi-Fi WPA3 si supporté, WPA2-AES sinon.
- SSID non identifiable (pas ton nom).
- Réseau invité séparé pour visiteurs.
- DNS chiffré au niveau routeur (DNS via DoH/DoT vers résolveur de confiance).
- Pas d’UPnP (ouverture automatique de ports) sauf si vraiment nécessaire.
- Firmware à jour.

## 22.8 Routeur de voyage

Pour voyage à risque, un **routeur de voyage** (GL.iNet, Mango, Slate) peut faire un VPN au niveau routeur, fournir un Wi-Fi local à tes appareils, et router tout via VPN ou Tor (avec firmware OpenWrt). Tu te connectes à *un seul* routeur, tes appareils restent simples.

## 22.9 Segmentation réseau domestique

Quatre VLANs typiques :

- **Pro** : appareils de travail.
- **Perso** : appareils personnels.
- **IoT** : tout l’IoT (TV connectée, thermostat, etc.) isolé.
- **Invités** : pour visiteurs.

Aucune communication entre VLANs sauf règles explicites. La TV connectée compromise ne peut pas joindre ton laptop.

## 22.10 Modes avion, faraday bag, isolation

- **Mode avion logiciel** : suffit pour 99 % des usages, mais peut laisser des fonctions actives sur certains OS.
- **Faraday bag** : garantie physique. Pour manifestation, frontière, contexte à haut risque.
- **Retrait de batterie** : ancienne mesure ultime. Plus possible sur la plupart des téléphones modernes.

## 22.11 *Fil rouge* — Sophie en manifestation

Sophie R., activiste, prépare une manifestation à risque d’arrestation. Configuration :

- Téléphone secondaire (vieux Pixel avec GrapheneOS, profil dédié manifestation), aucune donnée personnelle, contacts limités à 3 numéros essentiels.
- Téléphone principal **laissé à la maison**, vraiment éteint (longueur d’extinction complète vérifiée).
- Dans son sac, le téléphone secondaire en faraday bag, sorti seulement si nécessaire.
- Une carte SIM prépayée non liée à son identité (jurisprudence locale à vérifier : en France et Belgique, achat anonyme de SIM prépayée n’est plus possible depuis 2017-2021).
- Numéros importants notés sur papier (avocat, contact d’urgence, hotline juridique).

-----
