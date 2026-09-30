---
title: 'PARTIE IV — L''ATTAQUANT : PERSPECTIVES OFFENSIVES'
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
chapter: 4
chapters: 7
---

---

## Chapitre 17 — Le social engineering dans les APT

### 17.1 Les techniques APT de social engineering

Les groupes APT (Advanced Persistent Threat) utilisent le social engineering comme vecteur d'accès initial avec un niveau de sophistication et de patience sans commune mesure avec la cybercriminalité opportuniste.

**Le spear-phishing sur mesure.** APT28 (Fancy Bear / GRU russe) est connu pour ses campagnes de spear-phishing ciblant les institutions gouvernementales, les organisations militaires et les médias, avec des leurres construits à partir d'une reconnaissance approfondie du contexte politique et institutionnel de la cible. APT35 (Charming Kitten / MOIS iranien) cible les chercheurs, les diplomates et les journalistes spécialisés Moyen-Orient avec des approches par email se faisant passer pour des pairs académiques ou des organisateurs de conférences.

**Les faux profils professionnels.** Le groupe Lazarus (DPRK / Corée du Nord) a industrialisé l'utilisation de faux profils LinkedIn dans son opération « Dream Job » : des recruteurs fictifs de grandes entreprises technologiques (Google, Meta, défense) contactent des développeurs et des ingénieurs pour leur proposer des opportunités d'emploi fictives. La conversation se déplace vers WhatsApp ou email, et le candidat reçoit un « test technique » ou un « document de description de poste » qui est en réalité un malware. Cette technique est redoutablement efficace parce qu'elle exploite un comportement professionnel normal (répondre à un recruteur) et que le pretexte (offre d'emploi attractive) est un puissant levier motivationnel.

**L'impersonation de journalistes et chercheurs.** APT35 se fait régulièrement passer pour des journalistes de médias crédibles (Wall Street Journal, CNN) ou des chercheurs d'universités prestigieuses pour approcher des cibles. L'approche initiale est une demande d'interview ou une invitation à contribuer à une publication — activités normales et flatteuses pour la cible. La conversation s'étend sur des jours ou des semaines avant l'envoi du payload.

### 17.2 Le social engineering de longue durée

La patience est la signature des opérations APT de social engineering. Là où le cybercriminel opportuniste veut des résultats en heures, l'acteur APT investit des semaines ou des mois dans la construction d'une relation de confiance.

Le modèle APT35 est illustratif : le faux journaliste contacte sa cible, échange des emails polis sur plusieurs semaines, partage des articles intéressants (vrais articles, pas de malware — la phase de cultivation ne contient aucun élément malveillant), demande un premier entretien téléphonique (élicitation — collecte d'information sur les projets, les contacts, l'environnement de travail), puis finalement propose l'envoi d'un « document de travail » ou d'un « lien vers la plateforme d'interview » qui est le véritable vecteur d'attaque.

Cette approche contourne les défenses techniques (le premier email n'est pas malveillant, donc il passe les filtres) et psychologiques (la relation de confiance est établie avant la demande risquée). Elle est également très difficile à détecter par les équipes de sécurité : les emails sont légitimes dans leur contenu, la relation est construite progressivement, et la cible ne signale pas un échange professionnel qui lui semble normal.

### 17.3 Le supply chain humain dans les APT

Le ciblage des prestataires et des partenaires est une technique APT en expansion. Plutôt que d'attaquer directement une cible hautement sécurisée (entreprise de défense, agence gouvernementale), l'attaquant cible un maillon faible de la chaîne humaine : le prestataire IT (qui a accès VPN aux systèmes de la cible), le fournisseur de services cloud (qui gère les environnements de production), le cabinet de conseil (qui a accès à des documents confidentiels), ou l'assistant personnel d'un dirigeant (qui a accès à l'agenda, aux emails, aux contacts).

Les cas de DPRK IT workers représentent une évolution radicale : des agents nord-coréens utilisent des identités fictives complètes (CV fabriqués, profils LinkedIn artificiels, photos deepfake) pour se faire embaucher comme développeurs freelances dans des entreprises technologiques occidentales. Une fois en poste, ils ont un accès légitime aux systèmes internes et au code source. Le rapport Unit 42 2025 documente la construction d'identités synthétiques multi-couches incluant faux CV et profils sociaux pour soutenir ces infiltrations.

### 17.4 L'insider recruitment par les services de renseignement

Le recrutement d'insiders par les services de renseignement suit le cycle HUMINT décrit au Ch.3, mais appliqué au contexte industriel et technologique.

Les phases sont identifiables : repérage (identification d'individus ayant accès à l'information recherchée — souvent via LinkedIn), assessment (évaluation de la vulnérabilité — motivation financière, ego, frustration professionnelle), developmental contact (approche sous couvert de networking professionnel, proposition de consulting, invitation à un séminaire), cultivation (renforcement de la relation, petits avantages — invitation à dîner, cadeaux, rémunération pour des « consultations » anodines), escalade (demandes progressivement plus sensibles), et éventuellement recrutement formel ou maintien dans un état d'ignorance quant à la nature réelle de l'interlocuteur.

Les signaux d'alerte pour l'employeur incluent : un employé qui développe des contacts inhabituels avec des interlocuteurs étrangers non identifiés, des changements de comportement (accès à des documents hors de son périmètre, horaires de travail inhabituels, utilisation de dispositifs de stockage personnels), et des signes de vie au-dessus de ses moyens. Les dispositifs de détection et de signalement sont traités au Ch.22 et Ch.24.

### 17.5 Cas documentés

**Lazarus « Dream Job » (2020-2025).** Ciblage systématique d'ingénieurs et développeurs dans les secteurs défense, aérospatial et crypto-monnaie via de faux recruteurs LinkedIn. Des centaines de victimes dans le monde. L'opération a évolué : en 2023-2025, les faux recruteurs utilisent des deepfakes vidéo en entretien d'embauche.

**DPRK IT Workers (2022-2025).** Des milliers de travailleurs nord-coréens opérant sous des identités fictives sont employés comme freelances dans des entreprises américaines et européennes. Revenu estimé : des centaines de millions de dollars reversés au régime nord-coréen.

**APT35 — Faux journalistes (2019-2025).** Campagnes récurrentes ciblant des chercheurs, diplomates et journalistes spécialisés. Pretextes d'interview et de collaboration académique. Durée de cultivation : 2 à 8 semaines avant l'envoi du payload.

---

## Chapitre 18 — L'ingénierie sociale dans la fraude et la criminalité organisée

### 18.1 La fraude au président : modèle opérationnel

La fraude au président est une industrie criminelle structurée. Les groupes opèrent à partir de « call centers » organisés (principalement en Afrique de l'Ouest, Europe de l'Est, Asie du Sud-Est) avec une répartition des rôles : les « researchers » collectent l'OSINT sur les cibles, les « callers » exécutent les appels de vishing, les « email operators » gèrent les communications email, et les « money mules » blanchissent les fonds via des chaînes de comptes bancaires.

Le modèle opérationnel suit une séquence : reconnaissance OSINT (identification de la cible et du circuit de validation financière) → approche initiale (email et/ou appel) → manipulation (urgence, confidentialité, autorité) → exfiltration des fonds (virement vers un compte contrôlé) → blanchiment (transfert rapide vers d'autres comptes, conversion en crypto-monnaie). La chaîne complète peut se dérouler en quelques heures — la vitesse est critique pour devancer les mécanismes de rappel de virement.

### 18.2 Les romance scams et le pig butchering

Les romance scams (arnaques sentimentales) ont évolué vers un modèle industriel appelé « pig butchering » (sha zhu pan) : la victime est « engraissée » (cultivée pendant des semaines ou des mois) avant d'être « abattue » (escroquée de sommes importantes, souvent en investissements crypto frauduleux).

Le modèle repose sur des « compound » en Asie du Sud-Est (Cambodge, Myanmar, Laos) où des victimes de traite humaine sont forcées d'opérer comme scammers. Les conversations sont gérées via des scripts et, de plus en plus, assistées par des chatbots IA qui maintiennent des conversations cohérentes sur la durée. Les pertes individuelles sont typiquement de 5 000 à 500 000 € et les pertes globales se chiffrent en milliards.

### 18.3 Le SIM swapping

Le SIM swapping est une technique de social engineering ciblant les opérateurs télécom. L'attaquant contacte l'opérateur mobile de la victime (par téléphone ou en boutique) et, en utilisant des informations personnelles collectées par OSINT (nom, adresse, date de naissance, dernier montant facturé), convainc l'opérateur de transférer le numéro de téléphone vers une nouvelle carte SIM contrôlée par l'attaquant.

L'objectif est de prendre le contrôle du numéro de téléphone pour intercepter les codes MFA envoyés par SMS. Une fois le numéro transféré, l'attaquant peut reset les mots de passe de tous les comptes liés au numéro (email, banque, réseaux sociaux, crypto). Les pertes financières peuvent être considérables, en particulier dans le monde des crypto-monnaies.

**Défense** : ne pas utiliser le SMS comme second facteur pour les comptes critiques (préférer une app d'authentification ou une clé FIDO2), activer les protections anti-SIM swap de l'opérateur (code PIN, alerte sur les changements de SIM), utiliser un numéro de téléphone dédié et non public pour le MFA.

### 18.4 L'évolution avec l'IA

L'IA transforme l'industrie du social engineering criminel de trois manières convergentes.

**La personnalisation à l'échelle.** Les LLM permettent de générer des emails de phishing personnalisés pour chaque cible à partir de données OSINT, dans n'importe quelle langue, avec une qualité linguistique native. Ce qui nécessitait auparavant un opérateur humain qualifié est maintenant automatisable.

**Le deepfake vocal et vidéo.** Le clonage vocal en temps réel permet des vishings d'un réalisme sans précédent. La vidéo deepfake en temps réel permet des visioconférences frauduleuses (cas de Hong Kong). Le coût de ces technologies diminue rapidement et leur accessibilité augmente.

**Les chatbots de social engineering.** Des agents conversationnels autonomes capables de maintenir des conversations d'élicitation ou de romance scam sur des jours ou des semaines, avec une cohérence et une adaptabilité que les scripts manuels ne permettaient pas. C'est le passage à l'échelle de l'ingénierie sociale relationnelle.

---

## Chapitre 19 — Red team social engineering : méthodologie professionnelle et OPSEC du praticien

### 19.1 Le cadre du red team

Le red team social engineering est une prestation professionnelle encadrée par un contrat, une lettre de mission et des rules of engagement qui définissent précisément ce qui est autorisé et ce qui ne l'est pas.

**La lettre de mission** est le document fondateur. Elle doit être signée par un représentant habilité de l'organisation (pouvoir de signature vérifié juridiquement) et doit couvrir : l'identité du prestataire et des testeurs, le scope géographique (quels sites), le scope humain (quels employés — tous, un service, des profils spécifiques), le scope technique (quels vecteurs — phishing, vishing, intrusion physique, élicitation), la durée, les objectifs, les limites explicites, le protocole d'urgence (safe word, contact de référence), et la clause de confidentialité.

**Les rules of engagement** complètent la lettre de mission avec les détails opérationnels : horaires autorisés, zones interdites (zones classifiées, locaux syndicaux, infirmerie), techniques exclues, procédure de communication avec le commanditaire (reports intermédiaires, alertes), gestion des découvertes incidentes (si le red team découvre une intrusion réelle pendant le test — qui prévenir et comment).

### 19.2 La planification

La planification couvre : les objectifs opérationnels (mesurables et réalistes), la reconnaissance (OSINT + reconnaissance physique), la construction des pretextes (chaque pretexte avec un pretexte de secours), l'infrastructure technique (domaines, landing pages, implants, communications sécurisées), la logistique (déplacements, tenues, matériel, hébergement si test multi-sites), la timeline (séquencement des phases — reconnaissance, phishing, vishing, intrusion physique, élicitation), et les points de décision (go/no-go à chaque phase).

### 19.3 L'exécution

L'exécution d'un test de social engineering est une opération à haute tension. Le red teamer est lui-même sous pression (risque d'être intercepté, nécessité de maintenir le pretexte en temps réel, gestion du stress de l'imposture) et doit prendre des décisions en quelques secondes (pivoter si le pretexte ne fonctionne pas, abandonner si le risque est trop élevé, escalader si l'opportunité se présente).

**La documentation en temps réel** est critique : photos (discrètes), notes, horodatage de chaque action, enregistrements audio/vidéo si autorisés par la lettre de mission et la législation locale. Chaque élément de documentation sera utilisé dans le rapport pour démontrer les vulnérabilités identifiées et proposer des remédiations.

**L'adaptation en temps réel** est la compétence la plus difficile à acquérir. Les plans ne survivent pas au contact — un gardien plus vigilant que prévu, un employé qui pose une question inattendue, une porte fermée qui devait être ouverte. Le red teamer doit improviser tout en maintenant la cohérence de son pretexte.

### 19.4 Le rapport

Le rapport de red team social engineering est le livrable final et le document qui justifie l'investissement du commanditaire. Il doit être factuel, constructif et actionnable.

**Structure type** : résumé exécutif (une page — résultats clés, risques majeurs, recommandations prioritaires), méthodologie (vecteurs utilisés, timeline, outils), résultats par vecteur (phishing : taux de clic, taux de compromission, temps de signalement ; vishing : taux de succès, informations obtenues ; intrusion physique : accès obtenus, temps de présence non détecté, implants posés), évaluation de l'impact (ce qu'un attaquant réel aurait pu faire avec les accès obtenus — sans les contraintes éthiques du red team), recommandations classées P0/P1/P2.

**Le ton** : le rapport documente des faits et propose des améliorations. Il ne blâme pas les individus, ne nomme pas les employés qui se sont fait piéger (sauf exception justifiée et avec l'accord du commanditaire), et ne ridiculise pas les défenses existantes. Un rapport humiliant ne produit pas de changement — il produit de la résistance.

### 19.5 L'éthique du red teamer

Le red teamer a un pouvoir de manipulation — et la responsabilité qui va avec est non négociable. Le debriefing post-test est une obligation éthique : les employés qui ont été piégés doivent être informés (individuellement ou collectivement, selon le format choisi avec le commanditaire), le mécanisme exploité doit être expliqué (pas le nom de l'employé, mais la technique), et la finalité doit être claire (améliorer les défenses, pas sanctionner les individus).

La confidentialité des résultats individuels est un impératif. Le rapport ne doit pas permettre au commanditaire d'identifier et de sanctionner un employé spécifique sur la base de sa vulnérabilité au social engineering — sauf si cette vulnérabilité révèle un manquement grave et délibéré aux procédures (ce qui est différent d'un échec face à un social engineering sophistiqué).

### 19.6 OPSEC du praticien

L'OPSEC (Operational Security) du praticien est un aspect souvent négligé de la formation au red team social engineering. Le praticien doit protéger sa propre sécurité, sa couverture opérationnelle et la traçabilité de sa mission.

**Préparation de la légende.** Chaque pretexte nécessite une identité crédible et compartimentée. Le red teamer ne doit jamais utiliser sa vraie identité pendant un test (sauf en phase de rapport). Les éléments de la légende (nom, entreprise, carte de visite, numéro de téléphone dédié, adresse email de pretexte, profils en ligne si nécessaire) doivent être préparés et testés avant le début de l'opération.

**La compartimentation.** Les identités de pretexte ne doivent pas être croisables entre elles ni traçables vers l'identité réelle du red teamer. Téléphones dédiés (burner ou SIM dédiée), adresses email distinctes, profils en ligne séparés, véhicule sans lien avec l'entreprise de red team.

**La gestion des supports.** Les photos, enregistrements, notes de terrain et copies de documents collectés pendant le test doivent être stockés de manière sécurisée (chiffrement), transmis au commanditaire via un canal sécurisé, et détruits après la livraison du rapport final (sauf obligation de conservation contractuelle). La perte d'un dispositif contenant des preuves de test peut constituer une fuite de données sensibles.

**La gestion de la confrontation.** Si le red teamer est intercepté, arrêté ou confronté par la sécurité ou les forces de l'ordre, il doit pouvoir s'identifier immédiatement comme testeur autorisé. La lettre de mission et le contact du commanditaire doivent être accessibles en permanence (version papier dans une poche intérieure, version numérique sur le téléphone). Le safe word doit être connu de toute l'équipe et du contact de référence.

**Les limites légales.** Le red teamer doit connaître le cadre juridique local. En France, même avec une lettre de mission signée par le DG, certaines actions restent juridiquement risquées si elles sont mal encadrées : l'enregistrement de conversations sans consentement est illégal (sauf dans le cadre strictement défini de la lettre de mission qui vaut consentement de l'employeur), la fabrication de faux documents peut constituer une infraction si elle est utilisée en dehors du cadre du test, l'usurpation de l'identité d'un vrai prestataire (et non d'un prestataire fictif) peut entraîner des complications juridiques. Le cadre juridique est détaillé à l'Annexe F.

---

## Chapitre 20 — Capstone Partie IV : planification d'un red team SE complet

**Exercice intégrateur.** L'étudiant produit un plan de mission red team social engineering complet pour un scénario donné (groupe pharmaceutique, 3 sites, 800 employés, programme de R&D sensible, contexte de fusion-acquisition récente).

**Livrables attendus :**
1. Analyse du scope et des contraintes (lettre de mission rédigée, rules of engagement, limites éthiques explicites)
2. Plan de reconnaissance (OSINT + physique, sources, méthodologie, timeline)
3. Matrice des pretextes (par vecteur : phishing, vishing, intrusion physique, élicitation — pretexte principal et pretexte de secours pour chaque)
4. Timeline d'exécution (6 semaines, séquencement des phases)
5. Liste du matériel et de l'infrastructure
6. Plan OPSEC (légendes, compartimentation, gestion des preuves)
7. Protocole d'urgence (safe word, contacts, procédure de désescalade)
8. Modèle de rapport (structure, métriques, format de recommandations)

**Erreur fréquente** : produire un plan techniquement solide mais éthiquement fragile (limites floues, absence de protocole d'urgence, oubli de la gestion des résultats individuels).

---

> **🔴 FIL ROUGE — Opération CONFIANCE — Épisode 5**
>
> **L'incident réel.** En parallèle du red team, Lucie Ferraro alerte Nathan. Un ingénieur R&D senior du bureau parisien, Alexandre Petit, 45 ans, spécialiste des systèmes de navigation inertielle, a été contacté il y a trois mois sur LinkedIn par un certain « David Chen », se présentant comme recruteur chez « Meridian Consulting Asia ». Les échanges ont débuté par des compliments sur les publications d'Alexandre et une proposition de « consulting rémunéré » pour un client asiatique du secteur aéronautique.
>
> La conversation s'est déplacée vers WhatsApp. David Chen est passé progressivement de questions générales sur le secteur à des questions de plus en plus spécifiques : « Quelles sont les principales innovations en navigation inertielle actuellement ? », « Votre entreprise travaille sur des systèmes MEMS ou fibre optique ? », « Quels sont les principaux défis techniques du programme européen ? ». Alexandre a d'abord répondu avec enthousiasme (flatterie, intérêt professionnel, perspective de rémunération), puis a commencé à avoir des doutes quand David Chen a proposé un « rendez-vous confidentiel » lors d'un salon à Singapour.
>
> Nathan analyse les échanges et reconnaît un schéma d'élicitation classique : spotting (LinkedIn), assessment (publications, poste clé), developmental contact (connexion LinkedIn, flattery), cultivation (échanges WhatsApp, proposition de consulting), et escalade (questions de plus en plus spécifiques, proposition de rendez-vous physique). La progression suit le continuum HUMINT décrit au Ch.3. Le profil LinkedIn de David Chen présente des incohérences : photo qui ne retourne aucun résultat sur les recherches d'image inversée (probablement générée par IA), entreprise « Meridian Consulting Asia » sans présence web vérifiable, parcours professionnel vague.
>
> Nathan recommande d'alerter la DGSI (ingérence économique potentielle) et de débriefer Alexandre sans le blâmer — il est un insider involontaire, pas un traître. L'ingénieur est débriefé par la RSSI et Nathan : explication du mécanisme d'élicitation, rappel des signaux d'alerte, aucune sanction. La DGSI est informée et ouvre une enquête.

---
