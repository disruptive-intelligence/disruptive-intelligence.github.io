---
title: Chapitre 17 — Le social engineering dans les APT
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - 'Partie IV — L''attaquant : perspectives offensives'
  - index.md
---

## 17.1 Les techniques APT de social engineering

Les groupes APT (Advanced Persistent Threat) utilisent le social engineering comme vecteur d'accès initial avec un niveau de sophistication et de patience sans commune mesure avec la cybercriminalité opportuniste.

**Le spear-phishing sur mesure.** APT28 (Fancy Bear / GRU russe) est connu pour ses campagnes de spear-phishing ciblant les institutions gouvernementales, les organisations militaires et les médias, avec des leurres construits à partir d'une reconnaissance approfondie du contexte politique et institutionnel de la cible. APT35 (Charming Kitten / MOIS iranien) cible les chercheurs, les diplomates et les journalistes spécialisés Moyen-Orient avec des approches par email se faisant passer pour des pairs académiques ou des organisateurs de conférences.

**Les faux profils professionnels.** Le groupe Lazarus (DPRK / Corée du Nord) a industrialisé l'utilisation de faux profils LinkedIn dans son opération « Dream Job » : des recruteurs fictifs de grandes entreprises technologiques (Google, Meta, défense) contactent des développeurs et des ingénieurs pour leur proposer des opportunités d'emploi fictives. La conversation se déplace vers WhatsApp ou email, et le candidat reçoit un « test technique » ou un « document de description de poste » qui est en réalité un malware. Cette technique est redoutablement efficace parce qu'elle exploite un comportement professionnel normal (répondre à un recruteur) et que le pretexte (offre d'emploi attractive) est un puissant levier motivationnel.

**L'impersonation de journalistes et chercheurs.** APT35 se fait régulièrement passer pour des journalistes de médias crédibles (Wall Street Journal, CNN) ou des chercheurs d'universités prestigieuses pour approcher des cibles. L'approche initiale est une demande d'interview ou une invitation à contribuer à une publication — activités normales et flatteuses pour la cible. La conversation s'étend sur des jours ou des semaines avant l'envoi du payload.

## 17.2 Le social engineering de longue durée

La patience est la signature des opérations APT de social engineering. Là où le cybercriminel opportuniste veut des résultats en heures, l'acteur APT investit des semaines ou des mois dans la construction d'une relation de confiance.

Le modèle APT35 est illustratif : le faux journaliste contacte sa cible, échange des emails polis sur plusieurs semaines, partage des articles intéressants (vrais articles, pas de malware — la phase de cultivation ne contient aucun élément malveillant), demande un premier entretien téléphonique (élicitation — collecte d'information sur les projets, les contacts, l'environnement de travail), puis finalement propose l'envoi d'un « document de travail » ou d'un « lien vers la plateforme d'interview » qui est le véritable vecteur d'attaque.

Cette approche contourne les défenses techniques (le premier email n'est pas malveillant, donc il passe les filtres) et psychologiques (la relation de confiance est établie avant la demande risquée). Elle est également très difficile à détecter par les équipes de sécurité : les emails sont légitimes dans leur contenu, la relation est construite progressivement, et la cible ne signale pas un échange professionnel qui lui semble normal.

## 17.3 Le supply chain humain dans les APT

Le ciblage des prestataires et des partenaires est une technique APT en expansion. Plutôt que d'attaquer directement une cible hautement sécurisée (entreprise de défense, agence gouvernementale), l'attaquant cible un maillon faible de la chaîne humaine : le prestataire IT (qui a accès VPN aux systèmes de la cible), le fournisseur de services cloud (qui gère les environnements de production), le cabinet de conseil (qui a accès à des documents confidentiels), ou l'assistant personnel d'un dirigeant (qui a accès à l'agenda, aux emails, aux contacts).

Les cas de DPRK IT workers représentent une évolution radicale : des agents nord-coréens utilisent des identités fictives complètes (CV fabriqués, profils LinkedIn artificiels, photos deepfake) pour se faire embaucher comme développeurs freelances dans des entreprises technologiques occidentales. Une fois en poste, ils ont un accès légitime aux systèmes internes et au code source. Le rapport Unit 42 2025 documente la construction d'identités synthétiques multi-couches incluant faux CV et profils sociaux pour soutenir ces infiltrations.

## 17.4 L'insider recruitment par les services de renseignement

Le recrutement d'insiders par les services de renseignement suit le cycle HUMINT décrit au Ch.3, mais appliqué au contexte industriel et technologique.

Les phases sont identifiables : repérage (identification d'individus ayant accès à l'information recherchée — souvent via LinkedIn), assessment (évaluation de la vulnérabilité — motivation financière, ego, frustration professionnelle), developmental contact (approche sous couvert de networking professionnel, proposition de consulting, invitation à un séminaire), cultivation (renforcement de la relation, petits avantages — invitation à dîner, cadeaux, rémunération pour des « consultations » anodines), escalade (demandes progressivement plus sensibles), et éventuellement recrutement formel ou maintien dans un état d'ignorance quant à la nature réelle de l'interlocuteur.

Les signaux d'alerte pour l'employeur incluent : un employé qui développe des contacts inhabituels avec des interlocuteurs étrangers non identifiés, des changements de comportement (accès à des documents hors de son périmètre, horaires de travail inhabituels, utilisation de dispositifs de stockage personnels), et des signes de vie au-dessus de ses moyens. Les dispositifs de détection et de signalement sont traités au Ch.22 et Ch.24.

## 17.5 Cas documentés

**Lazarus « Dream Job » (2020-2025).** Ciblage systématique d'ingénieurs et développeurs dans les secteurs défense, aérospatial et crypto-monnaie via de faux recruteurs LinkedIn. Des centaines de victimes dans le monde. L'opération a évolué : en 2023-2025, les faux recruteurs utilisent des deepfakes vidéo en entretien d'embauche.

**DPRK IT Workers (2022-2025).** Des milliers de travailleurs nord-coréens opérant sous des identités fictives sont employés comme freelances dans des entreprises américaines et européennes. Revenu estimé : des centaines de millions de dollars reversés au régime nord-coréen.

**APT35 — Faux journalistes (2019-2025).** Campagnes récurrentes ciblant des chercheurs, diplomates et journalistes spécialisés. Pretextes d'interview et de collaboration académique. Durée de cultivation : 2 à 8 semaines avant l'envoi du payload.

---
