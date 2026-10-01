---
title: Partie 12 — Taxonomie des défenses
source: Cyber/11 Concepts/Taxonomie de la cybersécurité.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - index.md
---

> Cette partie classe les contrôles défensifs et les *relie aux attaques* qu'ils contrent. C'est le pendant « D3FEND » du cours : à chaque famille d'attaque, une famille de défenses. On peut classer chaque défense par fonction (préventive/détective/corrective — chapitre 8) et par couche (hôte, réseau, identité, données, application, organisation).


## Chapitre 270 — Hardening

**Définition.** Durcissement : réduire la vulnérabilité d'un système par configuration (rappel du chapitre 21).
**Contre quoi.** Exploitation de services, mauvaise configuration, réduction de surface.
**Principe.** Appliquer des référentiels (CIS), désactiver l'inutile, sécuriser les réglages par défaut.
🎯 **À retenir** — Le durcissement ferme les portes ouvertes « par défaut » ; base de toute défense préventive.


## Chapitre 271 — Patch management

**Définition.** Processus d'application maîtrisée des correctifs de sécurité.
**Contre quoi.** Exploitation de vulnérabilités connues (services exposés, vers).
**Principe.** Prioriser selon gravité × exploitabilité × exposition (CVSS/EPSS/KEV — chapitre 32), tester, déployer vite ce qui est exposé.
⚠️ **Erreur fréquente** — Retarder les patchs des actifs exposés (porte d'entrée n°1).
🎯 **À retenir** — Patcher *vite et bien* ce qui est exposé est l'un des contrôles les plus rentables.


## Chapitre 272 — Antivirus / EDR

**Définition.** Protection des hôtes par signatures (antivirus) et par comportement/réponse (EDR — chapitre 250).
**Contre quoi.** Malwares, fileless, LOLBins, TTP sur l'hôte.
**Principe.** L'EDR ajoute la détection comportementale et la réponse (isolation, télémétrie) que l'antivirus seul n'offre pas.
🎯 **À retenir** — L'EDR voit le comportement, pas seulement les fichiers : indispensable face aux menaces modernes.


## Chapitre 273 — Firewall

**Définition.** Filtrage du trafic réseau selon des règles (et, pour les NGFW, selon applications/identités/contenus).
**Contre quoi.** Accès non autorisés, réduction de surface réseau, contrôle des flux.
**Principe.** Filtrer entrant *et sortant* (le sortant limite C2/exfiltration), par défaut en deny.
🎯 **À retenir** — Le firewall contrôle les flux ; ne pas négliger le filtrage *sortant*.


## Chapitre 274 — WAF

**Définition.** *Web Application Firewall* : filtrage spécialisé du trafic web applicatif.
**Contre quoi.** Attaques web (injection, XSS, etc. — Partie 6), en *défense en profondeur*.
**Principe.** Détecte/bloque des motifs d'attaque web ; utile mais *ne remplace pas* un code sûr (contournable).
⚠️ **Erreur fréquente** — Compter sur le WAF au lieu de corriger le code (le WAF se contourne).
🎯 **À retenir** — Le WAF est une couche supplémentaire, pas un substitut au développement sécurisé.


## Chapitre 275 — Reverse proxy

**Définition.** Intermédiaire en façade des services, masquant et filtrant l'accès aux serveurs.
**Contre quoi.** Exposition directe, réduction de surface, point de contrôle (TLS, filtrage).
**Principe.** Centralise terminaison TLS, filtrage, journalisation, et cache la topologie interne.
🎯 **À retenir** — Le reverse proxy concentre contrôle et discrétion en façade des services.


## Chapitre 276 — Bastion

**Définition.** Point d'accès unique et durci pour l'administration (rappel du chapitre 20).
**Contre quoi.** Vol/réutilisation d'identifiants d'administration, lateral movement vers le Tier 0.
**Principe.** Tous les accès privilégiés transitent par le bastion, journalisés/enregistrés.
🎯 **À retenir** — Le bastion canalise et trace l'administration : pilier du tiering et du PAM.


## Chapitre 277 — Segmentation réseau

**Définition.** Découpage du réseau en zones filtrées (rappel du chapitre 15).
**Contre quoi.** Lateral movement, pivoting, propagation (vers/ransomware).
**Principe.** Contenir un incident dans une zone ; limiter les flux est-ouest.
🎯 **À retenir** — La segmentation compartimente le naufrage : un incident local ne devient pas global.


## Chapitre 278 — Microsegmentation

**Définition.** Segmentation fine au niveau de la charge de travail (rappel du chapitre 16).
**Contre quoi.** Lateral movement est-ouest, dans datacenter/cloud.
**Principe.** Autoriser uniquement les flux applicatifs explicitement nécessaires.
🎯 **À retenir** — La microsegmentation passe du « cloisonner par zones » au « cloisonner par flux » : socle du Zero Trust.


## Chapitre 279 — VPN

**Définition.** Tunnel chiffré d'accès distant (rappel du chapitre 55).
**Contre quoi.** Interception sur réseaux non fiables, accès distant non sécurisé.
**Principe.** Chiffrer l'accès distant ; mais exposé et donnant un accès large — d'où MFA, patch, moindre privilège.
⚠️ **Erreur fréquente** — VPN sans MFA donnant un accès réseau plat.
🎯 **À retenir** — Le VPN protège le transport mais reste une cible : MFA + patch + moindre privilège, et envisager le ZTNA.


## Chapitre 280 — ZTNA

**Définition.** *Zero Trust Network Access* : accès *par application* (et non par réseau), vérifié en continu selon l'identité et le contexte.
**Contre quoi.** Accès réseau trop large (défaut du VPN), lateral movement.
**Principe.** Pas de confiance par localisation ; chaque accès applicatif est réévalué (identité, posture, contexte).
🎯 **À retenir** — Le ZTNA remplace l'accès réseau large du VPN par un accès applicatif minimal et contextuel : mise en œuvre concrète du Zero Trust.


## Chapitre 281 — IAM

**Définition.** Gestion des identités et des accès (rappel des chapitres 57, 219).
**Contre quoi.** Accès non autorisés, élévation, comptes orphelins.
**Principe.** Cycle de vie des identités, moindre privilège, revue d'accès, SSO, gouvernance (IGA).
🎯 **À retenir** — L'IAM gouverne le « nouveau périmètre » : moindre privilège et revue d'accès en sont le cœur.


## Chapitre 282 — MFA

**Définition.** Authentification multi-facteur (rappel du chapitre 6).
**Contre quoi.** Vol/devinette d'identifiants (phishing, spraying, stuffing, brute force).
**Principe.** Exiger ≥2 familles de facteurs ; privilégier le **MFA résistant au phishing** (FIDO2/passkeys, number matching) contre le phishing et la MFA fatigue.
⚠️ **Erreur fréquente** — MFA par simple push (vulnérable à la fatigue) ; pas de protection contre le vol de jeton de session.
🎯 **À retenir** — Le MFA est la parade reine au vol d'identifiants ; la version résistante au phishing est désormais la cible.


## Chapitre 283 — PAM

**Définition.** Gestion des accès privilégiés (rappel du chapitre 20).
**Contre quoi.** Abus/vol de comptes privilégiés, lateral movement vers le Tier 0.
**Principe.** Coffre-fort de secrets, accès just-in-time, rotation, enregistrement de session.
🎯 **À retenir** — Le PAM supprime les secrets privilégiés permanents : antidote central des attaques d'identité.


## Chapitre 284 — Chiffrement

**Définition.** Protection cryptographique des données au repos, en transit, en usage (rappel du chapitre 68).
**Contre quoi.** Interception (sniffing/MITM), vol de données/supports.
**Principe.** Algorithmes éprouvés, gestion de clés rigoureuse ; protège la donnée même volée.
🎯 **À retenir** — Le chiffrement rend la donnée volée inexploitable — si la *gestion des clés* est sérieuse.


## Chapitre 285 — DLP

**Définition.** *Data Loss Prevention* : prévention de la fuite de données sensibles (détection/blocage des exfiltrations).
**Contre quoi.** Exfiltration, fuite involontaire ou malveillante de données.
**Principe.** Identifier les données sensibles (classification — chapitre 34) et contrôler leurs mouvements (mail, web, supports).
⚠️ **Erreur fréquente** — DLP sans classification fiable (faux positifs massifs, contournements).
🎯 **À retenir** — Le DLP surveille les mouvements de données sensibles : il dépend d'une bonne classification.


## Chapitre 286 — Sauvegardes

**Définition.** Copies de récupération des données (rappel du chapitre 28).
**Contre quoi.** Ransomware, wiper, panne, erreur, corruption.
**Principe.** Règle 3-2-1, tester la restauration.
🎯 **À retenir** — La sauvegarde testée est la dernière ligne de défense ; non testée, c'est un pari.


## Chapitre 287 — Sauvegardes immuables

**Définition.** Sauvegardes non modifiables/supprimables pendant une période définie (WORM, hors-ligne, air-gap).
**Contre quoi.** Ransomware/wiper qui ciblent justement les sauvegardes.
**Principe.** Garantir qu'au moins une copie résiste au chiffrement/à la suppression par l'attaquant.
🎯 **À retenir** — L'immutabilité (ou l'air-gap) est ce qui sauve réellement face au ransomware moderne.


## Chapitre 288 — Supervision

**Définition.** Surveillance continue de l'état de sécurité (rappel du chapitre 27).
**Contre quoi.** Détection tardive, angles morts.
**Principe.** Sources + SIEM/EDR/NDR + cas d'usage ; réduire le temps de détection (MTTD).
🎯 **À retenir** — On maintient la sécurité par la surveillance continue, pas par des contrôles ponctuels.


## Chapitre 289 — Threat hunting

**Définition.** Recherche *proactive* de menaces non détectées par les alertes automatiques.
**Contre quoi.** Attaquants furtifs (APT, fileless, LotL) passés sous les radars.
**Principe.** Formuler des hypothèses (souvent basées sur des TTP ATT&CK) et chercher activement leurs traces dans la télémétrie.
🎯 **À retenir** — Le threat hunting cherche ce que les alertes ratent : posture *assume breach* en action.


## Chapitre 290 — Deception et honeypot

**Définition.** Leurres (honeypots, comptes/données pièges) destinés à attirer et détecter les attaquants.
**Contre quoi.** Intrusions furtives, reconnaissance interne, lateral movement.
**Principe.** Un leurre n'a aucune raison légitime d'être touché : toute interaction est un signal *à très faible faux positif*.
🎯 **À retenir** — La déception transforme la curiosité de l'attaquant en alerte fiable : peu de bruit, fort signal.


## Chapitre 291 — Sandbox

**Définition.** Environnement isolé pour exécuter/analyser un contenu suspect sans risque pour le système réel.
**Contre quoi.** Malwares, pièces jointes/fichiers piégés.
**Principe.** Détoner le suspect en isolation pour observer son comportement (détection dynamique).
⚠️ **Erreur fréquente** — Oublier que certains malwares détectent la sandbox et restent inertes.
🎯 **À retenir** — La sandbox révèle le comportement d'un fichier en isolation, en complément des signatures.


## Chapitre 292 — Filtrage DNS

**Définition.** Contrôle des résolutions DNS pour bloquer domaines malveillants et détecter abus.
**Contre quoi.** C2, phishing, DNS tunneling, malvertising/SEO poisoning.
**Principe.** Bloquer/journaliser les résolutions vers des domaines malveillants ou anormaux.
🎯 **À retenir** — Le filtrage DNS coupe de nombreux canaux (C2, phishing) à peu de frais et révèle les abus.


## Chapitre 293 — Sécurité mail

**Définition.** Ensemble des protections de la messagerie (filtrage, sandbox, analyse de liens).
**Contre quoi.** Phishing, malspam, BEC, pièces jointes/liens piégés (Partie 9).
**Principe.** Filtrer, analyser, authentifier l'expéditeur, réécrire/inspecter les liens, bloquer les charges dangereuses.
🎯 **À retenir** — La messagerie étant le vecteur n°1, sa protection (filtrage + authentification + sensibilisation) est prioritaire.


## Chapitre 294 — SPF, DKIM, DMARC

**Définition.** Mécanismes d'*authentification de l'expéditeur* d'e-mail.

- **SPF** : déclare quels serveurs peuvent envoyer pour un domaine.
- **DKIM** : signe les messages (intégrité + origine).
- **DMARC** : politique combinant SPF/DKIM et reporting (que faire des messages non authentifiés).

**Contre quoi.** Usurpation de domaine (spoofing), phishing/BEC par usurpation directe.
⚠️ **Erreur fréquente** — DMARC en mode permissif (« none ») jamais durci, donc sans effet.
🎯 **À retenir** — SPF+DKIM+DMARC (en mode actif) empêchent l'usurpation directe du domaine : socle anti-phishing/BEC.


## Chapitre 295 — CSP

**Définition.** *Content Security Policy* : politique côté navigateur restreignant les sources de contenu/scripts d'une page web.
**Contre quoi.** XSS (défense en profondeur), injection de contenu (Partie 6).
**Principe.** Limiter ce que le navigateur exécute/charge ; couplée à Trusted Types contre le DOM-XSS.
⚠️ **Erreur fréquente** — CSP trop permissive (annule son intérêt).
🎯 **À retenir** — La CSP est une couche anti-XSS côté navigateur, en complément de l'encodage de sortie.


## Chapitre 296 — SAST

**Définition.** *Static Application Security Testing* : analyse du *code source* (sans l'exécuter) à la recherche de vulnérabilités.
**Contre quoi.** Vulnérabilités de code (injection, secrets en dur, etc.) — au plus tôt.
**Principe.** Intégré au développement/CI (« shift left ») ; détecte tôt mais génère des faux positifs.
🎯 **À retenir** — Le SAST trouve les failles dans le code, tôt : à intégrer en CI, avec tri des faux positifs.


## Chapitre 297 — DAST

**Définition.** *Dynamic Application Security Testing* : test de l'application *en exécution* (boîte noire), comme un attaquant.
**Contre quoi.** Vulnérabilités observables au runtime (injection, configuration, auth).
**Principe.** Complète le SAST en testant le comportement réel ; ne voit pas le code mais les effets.
🎯 **À retenir** — Le DAST teste l'application qui tourne : complémentaire du SAST (code) pour une couverture large.


## Chapitre 298 — IAST

**Définition.** *Interactive Application Security Testing* : analyse depuis *l'intérieur* de l'application en cours d'exécution (instrumentation).
**Contre quoi.** Vulnérabilités runtime, avec plus de précision (moins de faux positifs).
**Principe.** Combine vision interne (comme SAST) et exécution réelle (comme DAST), pendant les tests.
🎯 **À retenir** — L'IAST marie code et runtime pour une détection précise pendant les tests.


## Chapitre 299 — SCA

**Définition.** *Software Composition Analysis* : analyse des *dépendances tierces* (rappel des chapitres 71, 240).
**Contre quoi.** Dépendances vulnérables, paquets malveillants, problèmes de licence.
**Principe.** Inventorier (SBOM) et confronter les dépendances aux vulnérabilités connues ; surveiller les mises à jour.
🎯 **À retenir** — Le SCA surveille ce qu'on importe : indispensable, le code moderne étant surtout fait de dépendances.


## Chapitre 300 — Secrets scanning

**Définition.** Détection automatisée de secrets exposés (dans le code, l'historique, les images, les journaux).
**Contre quoi.** Exposition de secrets (chapitres 77, 221, 222).
**Principe.** Scanner en continu (pré-commit, CI, dépôts) pour détecter et révoquer/roter rapidement.
🎯 **À retenir** — Le secrets scanning attrape les fuites de secrets avant (ou dès) qu'elles surviennent : à coupler au coffre-fort.


## Chapitre 301 — Pentest

**Définition.** *Test d'intrusion* : évaluation offensive *autorisée et encadrée*, simulant un attaquant pour révéler des failles exploitables.
**Contre quoi.** Failles réelles, validation de l'efficacité défensive.
**Principe.** Périmètre et règles définis ; produit un rapport de vulnérabilités priorisées. Photographie à un instant T.
⚠️ **Erreur fréquente** — Confondre pentest (exploitation manuelle ciblée) et scan de vulnérabilités (automatisé, large).
🎯 **À retenir** — Le pentest révèle l'exploitable réel à un instant T, dans un cadre autorisé strict.


## Chapitre 302 — Bug bounty

**Définition.** Programme rémunérant des chercheurs externes qui signalent des vulnérabilités, dans un cadre défini.
**Contre quoi.** Failles non détectées en interne, en continu et à grande échelle.
**Principe.** Mobiliser une communauté de chercheurs (vs un test ponctuel) avec des règles (scope, divulgation responsable) et des récompenses.
🎯 **À retenir** — Le bug bounty étend la recherche de failles dans le temps et en diversité, en complément du pentest.


## Chapitre 303 — Purple teaming

**Définition.** Collaboration entre équipe offensive (red) et défensive (blue) pour *améliorer la détection/réponse*.
**Contre quoi.** Angles morts de détection, lacunes de réponse.
**Principe.** Le red rejoue des TTP (ATT&CK) pendant que le blue mesure ce qu'il détecte et améliore en boucle.
🎯 **À retenir** — Le purple teaming transforme l'attaque simulée en amélioration mesurable de la défense.


## Chapitre 304 — Tabletop exercise

**Définition.** Exercice de crise *sur table* (simulation discutée d'un scénario), sans impact réel sur les systèmes.
**Contre quoi.** Impréparation organisationnelle à la crise (chapitre 39).
**Principe.** Faire répéter décisions, rôles, communication et coordination à froid, pour révéler les lacunes avant le jour J.
🎯 **À retenir** — Le tabletop entraîne l'organisation à la crise sans risque : la crise se répète avant d'arriver.


## Chapitre 305 — Sensibilisation

**Définition.** Programme d'élévation de la vigilance humaine (rappel du chapitre 37).
**Contre quoi.** Ingénierie sociale, phishing, erreurs humaines (Partie 9).
**Principe.** Formations, simulations, culture du signalement *sans punition* ; transformer l'humain en capteur.
🎯 **À retenir** — La sensibilisation est un contrôle de sécurité à part entière, au rendement élevé : l'humain formé devient une ligne de détection.

---

> Suite et fin dans la **Partie 13 (synthèse transversale)** et les **Annexes**, fournies dans le document complémentaire de ce volume.


> Partie 13 : Synthèse transversale · Annexes A à I
>
> Après avoir *compris, classé, relié, défendu et répondu*, cette dernière partie apprend à **raisonner** : transformer la taxonomie en méthode de pensée. Les annexes sont des outils de référence à garder sous la main.

---
