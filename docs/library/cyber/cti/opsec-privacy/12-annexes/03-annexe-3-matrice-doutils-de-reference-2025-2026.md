---
title: Annexe 3 — Matrice d’outils de référence (2025-2026)
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Annexes
  - index.md
---

## Communication

|Outil             |Type               |Usage                 |Notes                                               |
|------------------|-------------------|----------------------|----------------------------------------------------|
|**Signal**        |Messagerie E2EE    |Quotidien             |Référence. Username permet de ne plus exposer numéro|
|**SimpleX**       |Messagerie E2EE    |Sources, HVT          |Pas d’identifiant utilisateur global                |
|**Briar**         |Messagerie P2P     |Manifestation, offline|Bluetooth/Tor, sans serveur                         |
|**iMessage**      |E2EE (Apple)       |Quotidien Apple       |Contact Key Verification recommandée                |
|**Matrix/Element**|Fédéré             |Communautés           |E2EE optionnelle, métadonnées chez homeserver       |
|**WhatsApp**      |E2EE (Meta)        |Compatibilité large   |Métadonnées chez Meta. Sauvegarde E2EE à activer    |
|**Telegram**      |Pas E2EE par défaut|Diffusion             |Seuls Secret Chats E2EE                             |

## Email

|Outil                    |Type                       |Notes                             |
|-------------------------|---------------------------|----------------------------------|
|**Proton Mail**          |E2EE entre Proton          |Suisse. Alias SimpleLogin intégrés|
|**Tuta**                 |E2EE complet (objet inclus)|Allemagne. Pas d’IMAP             |
|**Mailbox.org**          |Email propre + PGP         |Allemagne                         |
|**Fastmail**             |Mail propre sans E2EE      |Australie (Five Eyes)             |
|**SimpleLogin / Addy.io**|Alias email                |À ajouter en front de tout        |

## Navigateurs

|Outil                          |Usage                                |
|-------------------------------|-------------------------------------|
|**Tor Browser**                |Anonymat (ne jamais modifier)        |
|**Mullvad Browser**            |Anti-fingerprint quotidien (sans Tor)|
|**Brave**                      |Quotidien Chromium durci             |
|**Firefox + uBlock + arkenfox**|Quotidien Firefox durci              |
|**LibreWolf**                  |Firefox durci pré-configuré          |
|**Vanadium**                   |Mobile GrapheneOS                    |

## VPN

| Outil                               | Usage principal                                      | Notes                                                                                                                                                    |
| ----------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mullvad VPN**                     | Privacy quotidienne                                  | Suède. Compte numéroté sans email. Paiement cash/Monero possible. No-log détaillé. Très bon choix par défaut.                                            |
| **IVPN**                            | Privacy quotidienne                                  | Gibraltar. Audits réguliers. Cure53. Très bon positionnement privacy.                                                                                    |
| **Proton VPN**                      | Privacy + confort                                    | Suisse. Bon compromis grand public, écosystème Proton, plan gratuit sérieux.                                                                             |
| **NymVPN**                          | Métadonnées / mixnet                                 | VPN décentralisé. Fast mode 2-hop, Anonymous mode 5-hop mixnet. Plus ambitieux contre l’analyse de trafic, mais plus jeune et potentiellement plus lent. |
| **AmneziaVPN**                      | Anti-censure / self-host                             | Multi-protocoles. AmneziaWG, XRay Reality, Shadowsocks, OpenVPN over Cloak. Très pertinent contre DPI et blocage VPN.                                    |
| **À éviter pour profils sensibles** | NordVPN/ExpressVPN pour HVT, VPN gratuits, Surfshark | Risque de logs, revente de données, juridiction opaque, propriété complexe.                                                                              |

## Gestionnaires de mots de passe

|Outil          |Notes                                                          |
|---------------|---------------------------------------------------------------|
|**Bitwarden**  |Open source. Audits réguliers. Vaultwarden self-hosted possible|
|**KeePassXC**  |100 % local, sync manuelle                                     |
|**1Password**  |Commercial canadien. UX excellent                              |
|**Proton Pass**|Intégré Proton                                                 |
|**À éviter**   |LastPass (fuites 2022-2023)                                    |

## Clés matérielles

|Outil               |Notes                           |
|--------------------|--------------------------------|
|**YubiKey 5 series**|Référence commerciale           |
|**Nitrokey 3**      |Open source hardware (Allemagne)|
|**SoloKey**         |Open source plus militant       |

## Cloud E2EE

|Outil                      |Notes                               |
|---------------------------|------------------------------------|
|**Proton Drive**           |Suisse, E2EE par design             |
|**Tresorit**               |Suisse, focalisé pro                |
|**Mega**                   |Nouvelle-Zélande                    |
|**Cryptomator**            |Surcouche E2EE sur cloud generaliste|
|**Nextcloud + Cryptomator**|Self-hosted                         |

## OS sensible

|Outil         |Usage                        |
|--------------|-----------------------------|
|**Tails**     |Sessions ponctuelles anonymes|
|**Whonix**    |Anonymat Tor persistant      |
|**Qubes OS**  |Compartimentation forte      |
|**GrapheneOS**|Mobile durci sur Pixel       |
|**Kicksecure**|Debian durcie au démarrage   |

## Détection / monitoring

|Outil             |Notes                                 |
|------------------|--------------------------------------|
|**MVT**           |Détection Pegasus/Predator post-mortem|
|**iVerify**       |Monitoring iOS/Android au quotidien   |
|**HaveIBeenPwned**|Notifications de fuites               |
|**Exodus Privacy**|Audit trackers d’apps Android         |

## Métadonnées et fichiers

|Outil         |Notes                                 |
|--------------|--------------------------------------|
|**MAT2**      |Nettoyage automatique métadonnées     |
|**ExifTool**  |Référence lecture/écriture métadonnées|
|**Dangerzone**|Reconstruction PDF propre             |

## Partage de fichiers

|Outil             |Notes                   |
|------------------|------------------------|
|**OnionShare**    |Service onion temporaire|
|**SecureDrop**    |Plateforme rédactions   |
|**GlobaLeaks**    |Équivalent ONG          |
|**CryptPad**      |Suite collaborative E2EE|
|**Bitwarden Send**|Lien temporaire chiffré |

-----
