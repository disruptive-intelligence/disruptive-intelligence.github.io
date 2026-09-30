---
title: Chapitre 5 — Reconnaissance et OSINT préparatoire
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 5.1 L'OSINT comme préalable obligatoire

Toute opération de social engineering commence par la reconnaissance. C'est un axiome, pas une recommandation. La qualité de l'information collectée en phase de reconnaissance détermine directement la crédibilité du pretexte, le choix de la cible et le taux de succès de l'opération. Un pretexte construit sans reconnaissance est un pretexte générique — et un pretexte générique échoue face à un employé moyennement vigilant.

L'OSINT (Open Source Intelligence) fournit au social engineer trois types d'information critiques : l'information organisationnelle (structure, processus, culture d'entreprise), l'information individuelle (profils, intérêts, vulnérabilités professionnelles des cibles potentielles) et l'information technique (systèmes utilisés, configurations de sécurité, vecteurs d'attaque potentiels). Le cours OSINT Mastery de la bibliothèque couvre en profondeur les méthodologies de collecte — le présent chapitre se concentre sur l'application spécifique de l'OSINT au social engineering.

## 5.2 Reconnaissance organisationnelle

La reconnaissance organisationnelle vise à comprendre l'entreprise cible comme un système : sa structure, ses processus, sa culture, ses partenaires et ses vulnérabilités structurelles.

**L'organigramme.** LinkedIn est la source principale. En croisant les profils des employés, le red teamer reconstitue l'organigramme fonctionnel : qui dirige quoi, qui reporte à qui, quels sont les liens hiérarchiques et fonctionnels. Les signatures d'emails (collectées via des interactions légitimes ou des fuites) complètent le tableau. L'organigramme identifie les cibles à haute valeur (accès à des informations sensibles, pouvoir de décision sur les virements) et les cibles à basse résistance (nouveaux arrivants, postes à fort turnover, prestataires).

**La terminologie interne.** Chaque organisation a son jargon : noms de projets, acronymes internes, noms de systèmes, appellations de services. Maîtriser cette terminologie est un marqueur de crédibilité majeur. Un phishing qui mentionne « le projet Vega » ou « la migration vers SAP S/4HANA » sera infiniment plus crédible qu'un email générique. Les sources de terminologie incluent les offres d'emploi (qui décrivent les outils et les projets), les publications des employés (articles LinkedIn, présentations en conférence), les documents publics (rapports annuels, communiqués de presse) et les fuites involontaires (photos de tableaux blancs sur les réseaux sociaux).

**Les prestataires et fournisseurs.** Les prestataires sont des vecteurs d'intrusion majeurs — ils ont souvent un accès physique ou logique aux locaux et aux systèmes sans être soumis aux mêmes contrôles que les employés internes. Identifier les prestataires (IT, ménage, maintenance, restauration, sécurité) permet de construire des pretextes d'impersonation crédibles. Les sources incluent LinkedIn (employés des prestataires mentionnant leurs clients), les réseaux sociaux (photos de véhicules de prestataires sur le parking), les offres d'emploi des prestataires eux-mêmes et les documents publics (appels d'offres, marchés publics pour les entreprises du secteur public).

**Le calendrier.** Les périodes de vulnérabilité sont prévisibles : fin de trimestre (pression sur les résultats), période de vacances (effectifs réduits, intérimaires moins formés), événements d'entreprise (soirées, séminaires — ouverture sociale accrue), audits prévus (les employés s'attendent à des demandes inhabituelles).

## 5.3 Reconnaissance individuelle

La reconnaissance individuelle cible les personnes spécifiques qui seront approchées pendant l'opération.

**LinkedIn.** C'est la mine d'or du social engineer. Un profil LinkedIn complet fournit : le poste exact et les responsabilités, le parcours professionnel (ancienneté dans l'entreprise, postes précédents), les compétences techniques (outils maîtrisés, certifications), le réseau professionnel (collègues, anciens collègues, contacts communs exploitables pour le name-dropping), les publications et partages (intérêts professionnels, opinions, expertise revendiquée), les recommandations (relations de confiance identifiées) et la photo (reconnaissance visuelle pour l'intrusion physique). La restriction de visibilité d'un profil LinkedIn n'est que partiellement efficace : les noms, les titres et les entreprises restent souvent visibles même pour les profils restreints.

**Réseaux sociaux personnels.** Facebook, Instagram, Twitter/X, TikTok fournissent des informations complémentaires sur les centres d'intérêt (sport, voyage, cuisine — autant de sujets pour construire un rapport), les habitudes (horaires, lieux fréquentés), l'environnement personnel (famille, animaux) et les opinions. Ces informations permettent de personnaliser l'approche et de créer une connexion rapide. Un red teamer qui découvre que sa cible est passionnée de course à pied peut se présenter comme coureur pour établir un lien. L'exploitation de ces informations est légitime en red team (information publique) mais doit rester dans les limites éthiques (ne pas exploiter de données sensibles).

**Publications professionnelles.** Articles de blog, interventions en conférence, brevets, publications académiques révèlent l'expertise de la cible et fournissent un vocabulaire technique précis pour l'élicitation. Un faux chercheur universitaire qui cite les travaux publiés de sa cible gagne immédiatement en crédibilité.

## 5.4 Reconnaissance technique

La reconnaissance technique alimente les vecteurs d'attaque numériques et physiques.

**Domaines et email.** L'identification du format d'adresse email (prenom.nom@helios-aero.fr vs p.nom@helios-aero.fr) est critique pour le spear-phishing. Les outils de collecte d'emails (Hunter.io, Snov.io — attention aux limites de quotas et aux conditions d'utilisation) et les fuites de données (Have I Been Pwned, Dehashed) permettent de confirmer les formats et d'identifier des comptes potentiellement compromis.

**Technologies.** Les offres d'emploi sont la source la plus riche : une annonce pour un « Administrateur Microsoft 365 / Azure AD » révèle la stack d'identité. Les en-têtes d'email (SPF, DKIM, DMARC — ou leur absence) indiquent le niveau de protection email. Les sous-domaines (vpn.helios-aero.fr, owa.helios-aero.fr) révèlent les services exposés.

**Contrôle d'accès physique.** Les photos sur les réseaux sociaux sont une source sous-estimée. Une photo de badge visible sur une selfie d'employé peut révéler le format du badge (taille, couleur, logo, position de la puce), le type de technologie (RFID, NFC — la présence d'une antenne circulaire visible indique du HF 13,56 MHz ; une puce simple du LF 125 kHz), le niveau de personnalisation (photo, nom, service) et le système de contrôle d'accès (les lecteurs visibles sur les photos d'entrée identifient souvent le fabricant).

## 5.5 Les limites de la reconnaissance

La reconnaissance en sources ouvertes opère dans un cadre éthique et juridique qui diffère selon le contexte.

En **contexte red team**, l'OSINT est réalisée dans le cadre de la lettre de mission. Toute information publiquement accessible est exploitable, mais l'exploitation doit rester dans le scope autorisé (par exemple, la reconnaissance sur les réseaux sociaux personnels des employés peut être autorisée pour construire des pretextes, mais l'exploitation de données sensibles — santé, opinions politiques, vie sexuelle — est exclue même si ces informations sont publiques).

En **contexte attaquant réel**, aucune limite n'est respectée. L'attaquant exploitera toute information disponible, y compris les données personnelles les plus intimes. Cette asymétrie est l'une des difficultés fondamentales de la défense : le red teamer opère avec des contraintes éthiques que l'attaquant n'a pas. Le test autorisé sous-estime donc systématiquement la surface d'attaque réelle.

En **contexte défensif** (contre-ingérence, évaluation de la surface d'exposition), la reconnaissance est réalisée sur sa propre organisation pour identifier les informations exposées et réduire la surface d'attaque. C'est l'une des actions les plus rentables en matière de défense contre le social engineering : savoir ce que l'attaquant sait de vous avant qu'il ne s'en serve.


---
