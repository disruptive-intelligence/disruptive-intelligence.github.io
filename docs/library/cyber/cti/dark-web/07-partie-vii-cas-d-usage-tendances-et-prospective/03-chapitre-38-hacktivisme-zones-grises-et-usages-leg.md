---
title: Chapitre 38 — Hacktivisme, zones grises et usages légitimes
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie VII — Cas d'usage, tendances et prospective
  - index.md
---

Le **hacktivisme** — action cyber à motivation idéologique ou politique — occupe une zone grise importante du dark web. Ce chapitre distingue ses formes, ses acteurs, et aborde les usages légitimes qui partagent l'infrastructure.

## 38.1 Les grandes traditions hacktivistes

**Anonymous (depuis 2003)**. Mouvement décentralisé, symbole Guy Fawkes. Opérations cibles variées — Église de Scientologie (Project Chanology 2008), PayPal/Visa (Operation Payback 2010), PRISM révélations supporting (2013), ISIS (post-attentats Paris 2015), KKK, polices accusées d'abus, régimes autoritaires. Actions : DDoS, defacement, leaks, doxing. Pas de hiérarchie formelle — opérations revendiquées par qui veut.

**WikiLeaks (depuis 2006)**. Julian Assange, plateforme de publication de documents classifiés ou secrets. Cablegate (2010), Vault 7 (2017 — outils CIA), multiples leaks politiques. Plus plateforme que acteur, mais impact hacktiviste majeur.

**LulzSec (2011)**. Spin-off Anonymous, opérations médiatiquement marquantes (PBS, Sony, Nintendo, InfraGard FBI). Courte durée de vie, arrestations rapides (Sabu retourné informateur FBI).

**Chaos Computer Club (depuis 1981)**. Plus ancien, allemand, plus institutionnel. Activisme éthique, recherche sécurité, positions sur politique numérique.

**Telecomix**. Support technique aux révolutionnaires du printemps arabe (2011-2012), contournement de censure.

**Cult of the Dead Cow (depuis 1984)**. Très ancien collectif, influence sur éthique hacker, outils historiques (Back Orifice).

## 38.2 Les hacktivismes contemporains (2022-2026)

**Contexte de la guerre en Ukraine** a relancé massivement l'hacktivisme, des deux côtés.

**IT Army of Ukraine**. Créé par le gouvernement ukrainien (Mykhailo Fedorov, ministre) fin février 2022 après l'invasion russe. Plus de 200 000 volontaires déclarés. Operations : DDoS contre cibles russes (gouvernement, banques, médias), défacement, leaks de données russes.

**Caractéristique unique** : mouvement hacktiviste **officiellement soutenu par un État** — ligne parfois floue entre volontaires citoyens et coordination étatique.

**KillNet**. Côté russe, pro-Kremlin. Créé 2022, opérations DDoS contre cibles occidentales (gouvernements EU, infrastructures, hôpitaux US). Positionnement « cyber armée » mais compétences limitées (surtout DDoS). Sanctionné par UE en 2023.

**NoName057(16)**. Autre groupe pro-russe, DDoS contre cibles occidentales. Sanctionné UE 2024. Plus technique que KillNet.

**Cyber Av3ngers**. Iranien, pro-gouvernement. Cibles : infrastructures eau US (compromission PLC Unitronics 2023-2024 — exploitation default passwords, impact symbolique).

**Groupes pro-palestiniens et anti-israéliens** (post-7 octobre 2023). Intensification des opérations, DDoS contre cibles israéliennes, leaks de données, défacement. Composition diverse — certains soutenus par Iran (via IRGC), d'autres hacktivistes indépendants.

**Anonymous actuels**. Fragmentés, opérations sporadiques. « Anonymous Russia » (pro-Ukraine), différents chapters nationaux. Moins structuré qu'historiquement.

**Ghost Security**. Anti-ISIS, anti-extrémisme.

## 38.3 La zone grise : hacktivisme ou cybercrime ?

La frontière entre hacktivisme sincère et cybercrime déguisé est **floue**.

**Cas mixtes** :

- **Lapsus$ (2021-2022)**. Groupe d'adolescents, motivation mixte (argent + gloire + idéologie floue). Compromissions majeures (Okta, Microsoft, Nvidia, Samsung). Arrestations 2022-2023.
- **BianLian narratif**. Revendications parfois politiques malgré motivation financière claire.
- **Some Anonymous operations qui tournent à l'extorsion**.

**Instrumentalisation**. Des États utilisent l'apparence hacktiviste pour opérations étatiques (plausible deniability). KillNet/NoName : hacktivistes réels ? Proxies étatiques ? La frontière est difficile.

**Recrutement**. Des groupes cybercriminels recrutent des hacktivistes motivés idéologiquement comme collaborateurs — travail pour une cause, mais avec bénéfices financiers.

**Hacktivisme mercenaire**. Entreprises qui proposent des services « hacktivistes » à la commande, pour dénigrer concurrents, activistes, journalistes. Team Jorge documenté 2023.

## 38.4 Les usages légitimes du dark web

Au-delà du crime et de l'hacktivisme (qui peut être contesté), le dark web sert **d'autres usages, parfaitement légitimes et essentiels**.

**Journalisme et protection des sources**. SecureDrop déployé par NYT, Guardian, Le Monde, Der Spiegel, WaPo, ProPublica, BBC, The Intercept. Plateforme permettant à des sources de transmettre documents aux journalistes de manière anonyme. Sans ces canaux, beaucoup de journalisme d'investigation serait impossible.

**Contournement de censure**. Dans régimes autoritaires (Chine, Iran, Russie post-2022, Biélorussie, Myanmar, Érythrée) :

- Accès à médias bloqués (BBC Persian, Voice of America, Deutsche Welle).
- Wikipedia accessible via .onion.
- Plateformes sociales bloquées (X, Facebook, Instagram) accessibles.
- Outils de communication chiffrée.

**Lanceurs d'alerte**. Plateformes type GlobaLeaks, hébergement de PublicLeaks. Protection de l'anonymat pour signaler actes illégaux depuis une organisation.

**Défense des droits humains**. ONG opérant dans régions hostiles (Reporters Sans Frontières, Amnesty International, Human Rights Watch) utilisent Tor et .onion pour coordination sécurisée, transmission de rapports, accès aux victimes.

**Communications d'activistes**. Dissidents politiques, opposants dans régimes autoritaires, manifestants. Tor permet communication sans traçage étatique.

**Recherche en cybersécurité**. Chercheurs accédant à marchés/forums pour investigation, threat intelligence, collecte d'indicators.

**Protection de la vie privée**. Utilisateurs simples qui veulent naviguer sans traçage commercial, sans profiling publicitaire. Argument philosophique valide indépendamment de toute activité « sensible ».

**Services légitimes hébergés en .onion**. Wikipedia, ProPublica, DuckDuckGo, Facebook, Twitter historique, Protonmail — tous maintiennent miroirs .onion pour servir utilisateurs sensibles.

## 38.5 Les défenses et réponses

**Côté acteurs** (journalistes, dissidents, activistes) : formations à l'OPSEC, usage de Tails, Whonix, Signal, PGP. Écosystème d'outils et de guides (Freedom of the Press Foundation, Tactical Tech, EFF).

**Côté plateformes** : SecureDrop (Freedom of the Press Foundation), GlobaLeaks, OnionShare — infrastructures dédiées.

**Côté sensibilisation** : éducation à la protection de la vie privée, à la reconnaissance de la surveillance.

**Côté régulation** : équilibre délicat entre sécurité (contre-terrorisme, lutte contre cybercrime) et libertés publiques (vie privée, liberté d'expression, protection sources). Débat vivant et loin d'être résolu.

## 38.6 La nuance éthique pour l'analyste

Un analyste CTI qui travaille sur le dark web doit maintenir une **nuance éthique**.

**Ne pas assimiler** tout ce qui est sur .onion à du cybercrime. Beaucoup d'activité légitime.

**Respecter les acteurs légitimes**. Un journaliste qui utilise Tor pour protéger sa source n'est pas une cible d'investigation. Un dissident en exil qui communique via .onion n'est pas un criminel.

**Différencier les cibles d'investigation**. Vrais cybercriminels (forums de vente de données, leak sites ransomware, marchés illicites) = cibles légitimes. Journalistes, activistes, dissidents = **non-cibles**.

**Protéger l'anonymat des sources légitimes**. Si l'investigation révèle incidemment l'identité de sources légitimes (d'un journaliste, d'un dissident), ces informations ne sont pas exploitées ni partagées.

**Considérer les motivations**. Un hacktiviste qui cible un régime autoritaire n'a pas les mêmes motivations qu'un ransomware qui chiffre un hôpital. L'analyste peut observer les deux, mais les qualifie différemment.

**Éviter le prisme idéologique**. Un analyste ne favorise pas un camp parce qu'il y adhère idéologiquement. Factualité et neutralité.

## 38.7 Implications pratiques

Pour une entreprise, l'hacktivisme représente un risque selon les contextes.

**Profil à risque hacktiviste** :

- Entreprise avec position politique visible.
- Secteur controversé (défense, fossiles, pharma sur sujets sensibles).
- Présence dans pays / contextes sensibles.
- Dirigeants exposés médiatiquement.

**Mitigations** :

- Monitoring mentions de l'organisation dans canaux hacktivistes.
- Protection DDoS robuste (CDN, services anti-DDoS professionnels).
- Protection des dirigeants (monitoring VIP sur dark web).
- Plans de communication de crise adaptés aux revendications idéologiques.
- Segmentation des ressources critiques pour résister à leaks possibles.

Pour la plupart des organisations, l'hacktivisme est un risque **modéré** comparé aux cybercriminels et APT. Mais il peut exploser en volume lors de contextes politiques tendus.

---
