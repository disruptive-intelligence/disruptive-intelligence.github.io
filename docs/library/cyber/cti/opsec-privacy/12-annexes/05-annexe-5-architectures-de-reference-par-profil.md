---
title: Annexe 5 — Architectures de référence par profil
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Annexes
  - index.md
---

*(récapitulatif synthétique)*

> Renvoi détaillé : Chapitre 38. Cette annexe en propose la forme synthétique tabulaire.

|Profil                            |Mobile                                 |Laptop                              |Stack messageries         |Email                            |VPN                     |OS sensible             |MFA                            |Spécificités                               |
|----------------------------------|---------------------------------------|------------------------------------|--------------------------|---------------------------------|------------------------|------------------------|-------------------------------|-------------------------------------------|
|**Particulier grand public durci**|iPhone + ADP, Lockdown Mode off        |macOS ou Win11 Pro + FDE            |Signal + WhatsApp E2EE    |Proton Mail + alias              |Mullvad ponctuel        |–                       |YubiKey                        |Routines mensuelles                        |
|**Journaliste freelance**         |Pixel + GrapheneOS dédié + iPhone perso|MacBook Pro + MacBook Air enquête   |SimpleX (sources) + Signal|Proton + alias + PGP             |Mullvad permanent       |Tails + Qubes possible  |YubiKey x2                     |Page contact confidentiel publique         |
|**Activiste manifestation**       |Pixel GrapheneOS burner                |Laptop classique perso (non emporté)|Signal + Briar            |Standard                         |Mullvad mobile          |–                       |TOTP                           |Faraday bag, BFU absolu, papier d’urgence  |
|**Dirigeant PME tech**            |iPhone Lockdown + GrapheneOS voyage    |MacBook + burner voyage             |Signal + iMessage CKV     |Pro corporate + perso Proton     |Mullvad                 |–                       |YubiKey x2 + 1Password Business|Procédure anti-BEC, formation équipe       |
|**Opposant politique exil**       |GrapheneOS strict                      |Qubes OS                            |Signal + SimpleX          |Proton via Tor                   |Mullvad + Tor           |Qubes + Whonix          |YubiKey                        |MVT/iVerify mensuel, documentation publique|
|**RSSI ONG terrain**              |iPhone ou Pixel selon contexte         |Qubes OS sur laptops équipe         |Signal Business + Wire    |Proton Drive Business ou Tresorit|Mullvad ou IVPN business|Qubes standardisé       |Clés matérielles équipe        |Formation continue, audits annuels         |
|**Victime ex-partenaire abusif**  |Téléphone neuf cash                    |Laptop neuf si possible             |Signal + Briar urgence    |Email neuf E2EE                  |Mullvad                 |–                       |YubiKey                        |Audit stalkerware, soutien associatif      |
|**HVT extrême**                   |GrapheneOS + reboot 2x/jour            |Qubes OS + air-gap                  |SimpleX + Signal          |Proton via Tor permanent         |Tor + VPN obfusqué      |Qubes + Whonix + air-gap|YubiKey                        |Forensique mensuelle, équipe juridique     |

-----
