---
title: Annexe 4 — Matrices de décision
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Annexes
  - index.md
---

## 4.1 Quelle messagerie pour quel usage ?

|Usage                         |Premier choix         |Second choix                                     |
|------------------------------|----------------------|-------------------------------------------------|
|Famille / amis grand public   |Signal                |iMessage (Apple) ou WhatsApp avec sauvegarde E2EE|
|Source journalistique sensible|SimpleX               |Signal avec username                             |
|Manifestation, offline        |Briar                 |Signal avec disappearing messages                |
|Équipe pro (ONG, rédaction)   |Signal                |Wire ou Matrix                                   |
|Profil ultra-HVT              |SimpleX sur GrapheneOS|Signal sur GrapheneOS avec username              |

## 4.2 Quel environnement de session sensible ?

|Besoin                                       |Choix                        |
|---------------------------------------------|-----------------------------|
|Action ponctuelle, traces nulles             |Tails                        |
|Identité pseudonyme durable + anonymat réseau|Whonix                       |
|Séparation durable plusieurs activités       |Qubes OS                     |
|HVT avec tous les besoins                    |Qubes + Whonix               |
|Quotidien grand public durci                 |OS durci classique (Ch 14-15)|

## 4.3 Quelle MFA ?

|Compte                                 |MFA recommandée                    |
|---------------------------------------|-----------------------------------|
|Email principal                        |FIDO2 matériel (YubiKey)           |
|Comptes financiers                     |FIDO2 matériel + TOTP secondaire   |
|Réseaux sociaux                        |FIDO2 ou TOTP                      |
|Comptes utilitaires (boutique en ligne)|TOTP                               |
|Services SMS-only                      |Tenter de migrer ou minimum d’usage|

## 4.4 Quel chiffrement disque selon OS ?

|OS               |Chiffrement               |Notes                                 |
|-----------------|--------------------------|--------------------------------------|
|macOS            |FileVault                 |Activer dès première utilisation      |
|Windows          |BitLocker (Pro/Enterprise)|TPM + PIN si profil sensible          |
|Linux            |LUKS2                     |Argon2id, systemd-cryptenroll pour TPM|
|Multi-OS portable|VeraCrypt                 |Conteneurs portables                  |

## 4.5 Quel cloud selon profil ?

|Profil                               |Recommandation                                 |
|-------------------------------------|-----------------------------------------------|
|Grand public Apple                   |iCloud + ADP activée                           |
|Grand public privacy                 |Proton Drive                                   |
|Cloud générique gardé pour écosystème|Cryptomator par-dessus                         |
|Self-hosting                         |Nextcloud + Cryptomator pour E2EE additionnelle|
|Profil pro très sensible             |Tresorit (Suisse, entreprise)                  |

## 4.6 Quel routage réseau selon contexte ?

| Contexte                               | Choix                                                     |
| -------------------------------------- | --------------------------------------------------------- |
| Quotidien grand public                 | DNS chiffré (DoH/DoT) + + navigateur durci + uBlock       |
| Wi-Fi public                           | + VPN (Mullvad/IVPN)                                      |
| Recherche anonyme                      | Mullvad Browser sur VPN ou Tor Browser                    |
| Action anonyme                         | Tor Browser sur Tor seul                                  |
| Environnement bloquant (Iran, etc.)    | Tor avec bridges obfs4 ou Snowflake                       |
| HVT durable                            | Whonix sur Qubes                                          |
| Navigation privacy quotidienne         | Mullvad Browser + Mullvad VPN                             |
| Session source / journalisme sensible  | Tor Browser sur Tails ou Whonix                           |
| Réduction de métadonnées réseau        | NymVPN Anonymous mode                                     |
| Usage rapide avec routage décentralisé | NymVPN Fast mode                                          |
| Pays censuré / DPI agressif            | AmneziaVPN avec AmneziaWG, XRay Reality ou Cloak          |
| Self-host VPN personnel                | AmneziaVPN sur VPS                                        |
| HVT durable                            | Qubes + Whonix ; VPN seulement comme outil complémentaire |


-----
