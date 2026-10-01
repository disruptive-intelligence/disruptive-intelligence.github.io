---
title: Chapitre 16 — Temporalité et chronologie d’enquête
source: Cyber/02 OSINT/OSINT & cryptoactifs.md
note: OSINT & cryptoactifs
up:
- - OSINT & cryptoactifs
  - ../index.md
- - Partie III — Méthodologie d’enquête
  - index.md
---

La dimension **temporelle** est centrale en enquête crypto. Les transactions sont horodatées avec précision, et leur **séquence** porte de l’information. Mal traiter la temporalité = manquer des patterns clés.

## 16.1 Les timestamps blockchain

Toute transaction blockchain a un **timestamp précis**, en **UTC**. Précision :

- Bitcoin : timestamp du bloc, ~10 minutes de granularité.
- Ethereum : timestamp du bloc, ~12 secondes de granularité (post-Merge).
- TRON, Solana : seconde près.

**Important** : le timestamp est celui d’**inclusion dans un bloc**, pas de **broadcast**. Une transaction émise à 14:23:00 peut être incluse dans un bloc à 14:25:30. Pour les analyses fines, cette différence importe.

**Mempool** : sur Bitcoin notamment, les transactions « attendent » dans le mempool avant inclusion. Si congestion, elles peuvent attendre plusieurs heures. L’analyste sophistiqué regarde aussi les **logs mempool** (si disponibles) pour saisir le moment exact d’émission.

## 16.2 Patterns temporels remarquables

**Activité par fuseau horaire**. Les acteurs actifs uniquement entre 9h et 18h dans une fenêtre cohérente avec un fuseau (Moscou, Pyongyang, etc.) trahissent leur localisation probable. Adresses gérées par humains ont des patterns horaires ; bots ont des patterns non-humains.

**Jours fériés / chômés**. Inactivité pendant jours fériés russes (1-8 janvier, 8 mars, 1-9 mai), chinois (Nouvel An lunaire), iraniens (Nowruz), nord-coréens (Chuseok, Day of the Foundation), etc. — signal sur la juridiction d’opération.

**Cohérence horaire avec autres événements**. Un paiement crypto à H+0 d’une demande de rançon, un transfert post-hack à H+5 minutes, un dépôt exchange juste après hop d’obfuscation = patterns cohérents avec acteur unique pilotant l’opération.

**Bursts d’activité**. Soudaine multiplication de transactions sur 1-2h = signal de **dispersion en urgence** (peur d’alerte) ou **automatisation** (bot consolidant).

**Inactivité longue avec activité subite**. Wallet dormant pendant des mois qui se réveille = signal fort. Soit l’attaquant change de tactique, soit un nouveau cycle d’opération démarre.

## 16.3 Délais entre événements

**Délai paiement-rançon → premier mouvement**. Mesure le **temps de réaction** de l’opérateur. Quelques minutes = automatisation. Quelques heures = supervision humaine. Plusieurs jours = peut-être pas le vrai propriétaire (revente, intermédiaire).

**Délai dépôt exchange → retrait en autre actif**. Mesure le **temps de blanchiment**. Conversion BTC → USDT en 5 minutes = pattern automatisé. En 24h = manuel.

**Délai entre branches d’un peeling chain**. Trop régulier (toutes les heures pile) = bot. Variable et erratique = humain.

## 16.4 Construire une timeline d’enquête

Pour rapports, une **timeline** synthétise les événements clés en ordre chronologique.

**Format type** (Annexe D pour template) :

```markdown
## Timeline MIXSHADOW

| Date UTC | Événement | Adresse | Montant | Source |
|---|---|---|---|---|
| 2026-03-08 03:47 | Compromission initiale Aurélien Médical | - | - | Forensics Mandiant |
| 2026-03-08 04:30 | Démarrage chiffrement Akira | - | - | Logs internes |
| 2026-03-12 11:00 | Demande rançon initiale 80 BTC | bc1q[Akira-receive] | 80 BTC | Note ransomware |
| 2026-03-13 16:30 | Négociation : 35 BTC accepté | - | - | Comm. cellule crise |
| 2026-03-14 09:12 | Paiement Aurélien Médical | bc1q[Akira-receive] | 35 BTC | Mempool TXID [...] |
| 2026-03-14 15:28 | Réception clé déchiffrement | - | - | Comm. portail Akira |
| 2026-03-17 03:42 | Premier mouvement sortant Akira | bc1q[H1] | 35 BTC | Mempool TXID [...] |
| 2026-03-17 04:18 | Début peeling chain | bc1q[H2] | 0,5 + 34,5 BTC | Mempool TXID [...] |
| ... | ... | ... | ... | ... |
| 2026-03-19 11:43 | Conversion BTC → ETH via FixedFloat | 0xFixedFloat → 0xAk1 | 12,5 ETH | Etherscan TXID [...] |
| 2026-03-19 12:55 | Dépôts Tornado Cash (3 dépôts) | 0xAk1 → Tornado | 12 ETH | Etherscan TXIDs [...] |
| 2026-03-22 08:30 | Conversion via exchange non-KYC X | bc1q[H12] → exchange | 3 BTC | Mempool + monitoring |
| 2026-03-22 12:30 | Retrait USDT-TRON | exchange → TR[Akira-TRON] | 290 000 USDT | Tronscan TXID [...] |
| ... | ... | ... | ... | ... |
```


La timeline est **synthétique** (pas exhaustive — elle synthétise le journal complet). Elle est **enrichie de sources** (TXID, références internes). Elle est **chronologique stricte**.

## 16.5 Corrélation avec événements off-chain

L’enquête crypto **gagne** quand on corrèle avec des événements off-chain.

**Avec logs internes victime**. Le timestamp d’une transaction crypto peut être corrélé avec :

- Logs SIEM (compromission initiale, activité suspecte).
- Logs réseau (exfiltration de données précédant le ransomware).
- Logs téléphone/email du RSSI (notifications, négociations).

**Avec comms négociation**. Les portails de négociation Tor utilisés par les opérateurs ransomware ont leurs propres timelines (messages, deadlines, ultimatums). Croiser avec timeline crypto.

**Avec leak site**. La publication sur le leak site Akira d’Aurélien Médical (s’il y en a eu) a un timing à corréler. Avant paiement, après paiement, etc.

**Avec presse / médias**. Les annonces publiques de rançonnage / paiement / récupération forment une trame externe.

**Avec d’autres victimes**. Si Akira a frappé 5 victimes la même semaine, leurs timelines comparées peuvent révéler **patterns opérationnels** du groupe (séquencement d’attaques, ressource humaine consacrée, etc.).

## 16.6 Fuseaux horaires : la rigueur

**Toujours en UTC dans les rapports techniques**. Évite ambiguïté. Les blockchains sont en UTC.

**Conversion explicite si nécessaire**. « 09:12 UTC, soit 10:12 heure de Paris (UTC+1, hiver) ». Évite confusion lecteur.

**Ne jamais faire de raisonnement sans timezone**. « La transaction a eu lieu à 9h12 » est insuffisant. **9h12 où ?**

**Cohérence dans tout le rapport**. Si le rapport mélange UTC pour blockchain et heure locale pour comms, expliciter au début et marquer chaque mention.

## 16.7 Fil rouge — MIXSHADOW : insight temporel

> **🔗 MIXSHADOW — Épisode 11 : pattern horaire Akira**
> 
> Sarah analyse les **patterns temporels** des opérations Akira observées dans MIXSHADOW.
> 
> **Activité par heure UTC** (sur les 30+ transactions Akira analysées) :
> 
> - 0h-4h UTC : 35% de l’activité.
> - 4h-8h UTC : 8%.
> - 8h-12h UTC : 12%.
> - 12h-16h UTC : 5%.
> - 16h-20h UTC : 15%.
> - 20h-24h UTC : 25%.
> 
> **Décodage** : pic d’activité en deux fenêtres : 0h-4h UTC et 20h-24h UTC. Si on convertit :
> 
> - 0h-4h UTC = 3h-7h MSK (Moscou), ou 9h-13h KST (Séoul/Pyongyang).
> - 20h-24h UTC = 23h-3h MSK, ou 5h-9h KST.
> 
> Le pattern est **plus cohérent avec un fuseau Asie de l’Est** (KST, Pyongyang ou Séoul) qu’avec MSK. Heure de travail KST = pic d’activité crypto.
> 
> Mais Sarah reste prudente : c’est un **signal**, pas une preuve. Hypothèses alternatives :
> 
> - Acteur en Russie qui travaille de nuit (par choix ou contrainte).
> - Acteur dans une autre TZ qui imite délibérément patterns asiatiques.
> - Plusieurs membres dans des TZ différentes coordonnant.
> 
> WEP : « possible profil opérateur en fuseau Asie de l’Est (40%), profil russophone toujours plausible (30%), autre / mixte (30%) ».
> 
> Cette observation est **incertaine** mais alimente l’attribution. Elle est combinée avec d’autres signaux (langue dans portail négociation, infrastructure technique, patterns d’attaques précédentes) pour profiler Akira. Akira pourrait avoir des liens DPRK (cf Lazarus, Ch.29), ce qui collerait avec KST. Mais aussi des liens russophones documentés. Le profil pourrait être **hybride** (opérateurs DPRK + affiliés russophones, modèle observé chez d’autres groupes).
> 
> Sarah note dans le rapport : « les patterns horaires sont cohérents avec une activité d’opérateur en fuseau UTC+9 (KST), mais cette observation est insuffisamment robuste pour conclure sur localisation géographique ». Calibration honnête.

-----
