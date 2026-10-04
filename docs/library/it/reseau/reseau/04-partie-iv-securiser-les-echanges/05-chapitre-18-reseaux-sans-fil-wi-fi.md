---
title: Chapitre 18 — Réseaux sans fil (Wi-Fi)
source: IT/04 Réseau/Réseau.md
note: Réseau
up:
- - Réseau
  - ../index.md
- - Partie IV — Sécuriser les échanges
  - index.md
---

## 18.1 Principe

Le Wi-Fi (norme **IEEE 802.11**) transmet les données par **radiofréquence**, sur les bandes **2,4 GHz**, **5 GHz** (et 6 GHz en Wi-Fi 6E/7). L'adaptateur sans fil de chaque appareil convertit les données en signaux radio et inversement. Le **point d'accès** (WAP) coordonne les échanges et sert de passerelle vers le réseau filaire.

## 18.2 Se connecter

Pour rejoindre un réseau, il faut son **SSID** (nom du réseau) et le secret ou les identifiants exigés. L'appareil envoie une **association request** au point d'accès :

| Champ | Contenu |
|---|---|
| Adresse MAC | Identifiant de l'adaptateur |
| SSID | Nom du réseau demandé |
| Débits supportés | Liste des débits |
| Canaux supportés | Fréquences utilisables |
| Protocoles de sécurité supportés | WPA2, WPA3… |

Le point d'accès annonce lui-même le réseau par des **trames balises** (*beacons*) régulières.

## 18.3 Les protocoles de sécurité

| Protocole | Chiffrement | Statut |
|---|---|---|
| **WEP** | RC4, clé de 40 ou 104 bits + vecteur d'initialisation (IV) de 24 bits | **Cassé**, à proscrire |
| **WPA** | TKIP (RC4 amélioré) | Obsolète |
| **WPA2** | AES (CCMP) 128 bits | Minimum acceptable |
| **WPA3** | AES, échange SAE (résistant aux attaques hors ligne sur le mot de passe) | Recommandé |

**Pourquoi WEP est cassé.** Il utilise la même clé partagée pour authentifier et chiffrer ; son IV est trop court et finit par se répéter, ce qui permet de retrouver la clé ; et son contrôle d'intégrité (un CRC calculé sur les données en clair) ne protège pas contre la modification des paquets.

**Personnel ou Entreprise.**

| Mode | Authentification |
|---|---|
| **WPA2/WPA3-Personal** | Une clé pré-partagée (PSK) commune à tous |
| **WPA2/WPA3-Enterprise** | **802.1X** : chaque utilisateur ou machine s'authentifie auprès d'un serveur **RADIUS** (ou TACACS+ pour l'administration des équipements) |

## 18.4 Les protocoles d'authentification EAP

Le mode Entreprise repose sur **EAP** (*Extensible Authentication Protocol*) :

| Méthode | Principe | Statut |
|---|---|---|
| **LEAP** | Méthode Cisco, mot de passe protégé par un mécanisme faible | Obsolète |
| **PEAP** | Tunnel TLS (certificat du serveur) dans lequel l'utilisateur s'authentifie par mot de passe | Courant |
| **EAP-TLS** | Authentification mutuelle par **certificats** (client et serveur), adossée à une PKI | Le plus robuste |

## 18.5 Menaces et durcissement

| Menace | Principe |
|---|---|
| **Déconnexion forcée** (*deauthentication / disassociation*) | Des trames de gestion forgées déconnectent les clients (WPA3 et 802.11w protègent ces trames) |
| **Point d'accès pirate** (*rogue AP*, *evil twin*) | Un faux réseau au même SSID capte les connexions |
| **Attaque du mot de passe** | Une PSK faible se retrouve hors ligne à partir d'une poignée de main capturée (WPA2-Personal) |

| Mesure | Remarque |
|---|---|
| WPA3, ou WPA2 avec une phrase de passe longue | Base indispensable |
| WPA2/3-Enterprise avec **EAP-TLS** | Authentification par certificat, révocable individuellement |
| Réseau invité séparé (VLAN) | Les visiteurs n'atteignent pas le LAN |
| Masquer le SSID, filtrer les MAC | **Faible** : le SSID réapparaît dans les échanges et une MAC s'usurpe ; jamais une mesure suffisante seule |
| Pare-feu du point d'accès, détection des points d'accès pirates (WIDS) | Défense en profondeur |

---
