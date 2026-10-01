---
title: Chapitre 27 — Veille dark web
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie V — Investigation, veille et collecte
  - index.md
---

surveillance, alerting, réduction du bruit

La **veille dark web** n'est pas une investigation ponctuelle — c'est un programme durable. Ce chapitre couvre la structuration d'une veille efficace, les outils, et la gestion du bruit.

## 27.1 Les objectifs de la veille

Pour une organisation, plusieurs objectifs distincts peuvent justifier une veille dark web.

**Détection de compromission**. Mentions de la marque sur forums/marchés/leak sites → possible breach à investiguer. Détection de credentials de l'organisation sur marchés de logs → possible vecteur de compromission. Détection d'IAB proposant des accès compatibles → menace imminente.

**Monitoring de dirigeants et VIP**. Mentions de personnalités (CEO, CFO, membres du conseil) — risques de fraude, chantage, usurpation.

**Veille concurrentielle / réputationnelle**. Activité malveillante autour de la marque — deepfakes, impersonations, phishing ciblant clients.

**Renseignement sectoriel**. Tendances dans le secteur : quelles campagnes ransomware ciblent l'aerospace ? quels vecteurs utilisés pour compromettre manufacturers ? Alimentation de la threat intel.

**Renseignement géographique**. Tendances par pays : quelles entités françaises sont ciblées ? quels groupes actifs en Europe ?

**Renseignement sur adversaires spécifiques**. Suivi d'APT ou groupes ransomware identifiés comme menaces prioritaires pour l'organisation.

## 27.2 Les sources à surveiller

**Leak sites ransomware**. Monitoring via Ransomwatch, Ransomfeed, plateformes commerciales. Alerting sur mentions de la marque ou du secteur.

**Forums majeurs**. XSS, Exploit, BreachForums — via crawling (si capacités) ou via plateformes qui le font.

**Marchés de logs**. Russian Market principalement. Monitoring par domaine.

**Marchés de fraude**. BriansClub, successeurs. Moins critique pour la plupart des organisations non-financières.

**Canaux Telegram**. Canaux identifiés comme pertinents — cybercrime russophone, leaks, hacktivisme pro/anti-pays X.

**Pastebins et assimilés**. Pastebin (partiellement désactivé pour usage criminel), Ghostbin, Rentry, Doxbin, etc.

**Feeds CTI**. VirusTotal, URLhaus, ThreatFox, etc. — indicateurs partagés communautairement.

**GitHub**. Fuites de credentials dans repos publics (GitHub dorking). Secrets committed par erreur, puis effacés mais toujours dans l'historique.

**Réseaux sociaux**. Twitter/X, Mastodon pour signaux de mentions, revendications hacktivistes, réactions de la communauté.

**Deep web non-tor**. Forums clearnet à accès restreint (payment, invite), souvent plus faciles d'accès que les .onion et riches en contenu.

## 27.3 Les outils de monitoring

**Plateformes commerciales CTI** (budget 50 k - 500 k USD/an) :

- **Recorded Future** : leader du marché, intelligence mondiale, intégration étendue.
- **Flashpoint** : forte expertise russophone et Telegram.
- **Intel471** : focus acteurs et écosystème cybercriminel.
- **SOCRadar** : plus abordable, bon rapport qualité/prix pour PME.
- **Flare** : niche dark web et data leaks, prix compétitif.
- **DarkOwl** : crawling .onion étendu.
- **Cybersixgill** (Zenity) : profilage et attribution.
- **Hudson Rock** : spécialisé stealer logs.
- **KELA** : forte couverture russophone.
- **Group-IB** : vision Europe/Asie.

**Outils open source** :

- **Ahmia** : moteur de recherche .onion, partiellement open source.
- **TorBot, Dark-Scrape** : crawlers open source (maintenance variable).
- **OnionScan** : audit de services .onion.
- **GitHub dorking** : outils pour détecter secrets dans repos.
- **Ransomwatch** : agrégateur public de leak sites ransomware.

**Services sectoriels**. Certains ISAC (par secteur) partagent de la threat intel par abonnement ou gratuitement pour leurs membres.

**Services gouvernementaux**. En France, partage d'information via l'ANSSI (CERT-FR, signalement d'incidents). Bulletins d'alerte publics.

## 27.4 Le défi du bruit

La veille dark web produit **énormément de faux positifs**. Un programme mal configuré génère des centaines d'alertes par semaine, dont la majorité ne nécessitent aucune action. Gérer le bruit est la compétence centrale du programme de veille.

**Sources de bruit** :

- **Homonymies** : « Vectris » est une marque, mais aussi possiblement un prénom, un nom commun dans d'autres langues, une entité sans lien.
- **Mentions éditoriales** : articles de presse, rapports CTI mentionnent l'entreprise sans être des signaux de compromission.
- **Credentials anciens** : comptes employés exposés dans breaches antérieurs (Adobe 2013, LinkedIn 2012, Collection #1 en 2019), re-mis en vente ou re-publiés.
- **Scams et fakes** : annonces de breach inexistants.
- **Typos et variantes** : « Vectriss », « Vectris_corp », « Victreis » — à filtrer ou à surveiller.

**Stratégies de réduction du bruit** :

**Keywords précis**. Utiliser des termes spécifiques (noms de produits internes, codes clients, adresses email pro, identifiants propriétaires) plutôt que seulement la marque générique.

**Whitelist éditoriale**. Filtrer les sources éditoriales (presse, rapports publics) qui mentionnent légitimement la marque sans menace.

**Filtrage temporel**. Dépriorer les mentions anciennes, prioritiser les nouvelles.

**Priorisation par criticité**. Mention sur forum XSS russophone > mention sur pastebin anonyme > mention éditoriale. Logs VPN corporate > logs consumer perso d'un employé.

**Machine learning**. Les plateformes commerciales appliquent du ML pour scorer la pertinence. Efficacité variable — complément de l'humain, pas remplaçant.

**Triage humain**. En fin de chaîne, un analyste trie les alertes résiduelles. 80-90% classées en quelques secondes chacune, 10-20% méritent investigation plus poussée.

## 27.5 Workflow de veille type

**Quotidien** (1-2h/jour pour un analyste dédié) :

- Revue des alertes automatiques (plateforme commerciale).
- Triage initial — classement en « ignorer », « surveiller », « investiguer ».
- Investigations légères sur les alertes ambigües.
- Mise à jour des indicateurs suivis.

**Hebdomadaire** (demi-journée) :

- Revue des leak sites ransomware ciblage sectoriel.
- Veille sur forums prioritaires (top 5-10 identifiés).
- Synthèse hebdomadaire pour le CISO et la direction.
- Mise à jour de la liste de surveillance.

**Mensuel** :

- Rapport mensuel structuré : tendances, incidents majeurs, évolutions observées.
- Revue du scope de monitoring — ajouts, retraits.
- Évaluation de la qualité des sources et outils.

**Trimestriel** :

- Audit du programme de veille.
- Évolution du budget et des ressources.
- Formation continue des analystes.
- Partage avec pairs sectoriels (ISAC, RSSIs par secteur).

## 27.6 Le programme de veille comme outil défensif

Au-delà de la détection d'incidents, un programme de veille bien structuré sert plusieurs fonctions défensives.

**Threat intelligence pour le SOC**. Les observations alimentent les règles de détection (IoC à surveiller, TTP à anticiper, vulnérabilités exploitées activement par acteurs connus).

**Aide à la priorisation défensive**. Si les stealers ciblent massivement un secteur, durcir les politiques correspondantes. Si un vecteur spécifique (phishing kit, vulnérabilité edge device) est en croissance, mitiger en priorité.

**Sensibilisation**. Les exemples observés nourrissent les campagnes de sensibilisation employés. « Regardez, voici un log d'infostealer vendu pour 15 USD qui contenait les credentials d'un collègue » fait plus d'impact qu'une théorie abstraite.

**Préparation stratégique**. Les tendances observées (convergence crime-étatique, montée de tel groupe, décl in de tel autre) alimentent la planification pluriannuelle de sécurité.

**Posture de négociation**. En cas de crise (ransomware subi, données exposées), une bonne veille préalable permet de connaître l'adversaire et de négocier en position informée.

---
