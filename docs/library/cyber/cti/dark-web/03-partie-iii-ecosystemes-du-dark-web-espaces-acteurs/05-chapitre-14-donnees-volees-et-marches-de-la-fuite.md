---
title: Chapitre 14 — Données volées et marchés de la fuite
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture'
  - index.md
---

Les données volées sont l'un des produits les plus échangés sur le dark web. Credentials, identités, dossiers médicaux, données d'entreprise — chaque type a son marché, son prix, ses acheteurs.

## 14.1 Types de données en circulation

**Credentials**. Couples email/mot de passe issus de breaches. Vendus en bulk (combo lists de millions d'entrées pour 5-50 USD) ou au détail (5-50 USD/pièce pour des credentials vérifiés sur services spécifiques).

**Logs d'infostealers**. Sessions complètes avec credentials, cookies, données machine — traités au Ch.15 en détail.

**Données bancaires**. Numéros de carte, CVV, accès aux comptes. Marché organisé (BriansClub, WWH Club, successeurs). Prix selon fraîcheur et pays.

**Données personnelles (fullz)**. Identité complète : nom, adresse, SSN/NIR, date de naissance, documents d'identité scannés. Utilisées pour fraude à l'identité, ouverture de comptes frauduleux.

**Données d'entreprise**. Documents internes, propriété intellectuelle, emails, bases clients. Les volumes exfiltrés par ransomware alimentent cette catégorie.

**Données de santé**. Dossiers médicaux, très prisés pour la fraude à l'assurance (US), le chantage, et la fraude à l'identité. Prix relativement élevés par unité (50-250 USD/dossier).

**Données gouvernementales**. Accès ou exfiltrations concernant administrations. Rareté élevée, prix variables selon sensibilité.

**Données industrielles / défense**. Spécifications techniques, plans, documents classifiés. Niche — DARKSTREAM s'inscrit dans cette catégorie. Acheteurs : concurrents industriels, services de renseignement étrangers, parfois groupes ransomware cherchant un levier de revente.

## 14.2 Grille de prix indicative 2025-2026

Sources : rapports SOCRadar (Annual Dark Web Report 2025), Privacy Affairs (Dark Web Price Index), observations Recorded Future, Flare. **Fortement indicatif** — varie par fraîcheur, spécificité, vendeur, marché.

| Type de donnée | Prix indicatif |
|---|---|
| Combo list (millions d'entrées, dates variables) | 5-50 USD |
| Credentials vérifiés, service spécifique | 5-50 USD / pièce |
| Carte bancaire avec CVV (compte actif) | 5-30 USD |
| Carte bancaire avec PIN / full access | 30-150 USD |
| Compte PayPal vérifié | 20-200 USD selon balance |
| Compte bancaire vérifié avec online banking | 100-1 000 USD selon balance |
| Fullz (identité complète) | 10-70 USD |
| Passeport scanné | 20-150 USD |
| Permis de conduire scanné | 15-70 USD |
| Log d'infostealer basique | 1-15 USD |
| Log d'infostealer avec VPN corporate | 50-500 USD |
| Accès VPN/RDP corporate (IAB) | 500-50 000 USD |
| Base de données d'entreprise | 500-100 000 USD+ |
| Dossier médical US | 50-250 USD |
| 0-day exploit (selon plateforme) | 5 000 - 2 500 000 USD |
| RaaS affiliation (droit d'affiliation) | 1 000 - 100 000 USD |

> **⚠️ ALERTE ANALYSTE** : Ces prix sont des moyennes indicatives à date (2025-2026) et fluctuent selon la réputation du vendeur, la fraîcheur, la verification, et les dynamiques de marché. Les prix des données bancaires simples ont tendance à se stabiliser ou baisser (saturation) tandis que les credentials d'accès corporate et les stealer logs avec tokens de session augmentent (demande RaaS).

## 14.3 Le lifecycle d'un breach

Les données volées suivent un cycle prévisible.

**Phase 1 — Exploitation privée**. Le groupe auteur du breach exploite d'abord les données pour son propre compte — ransomware, fraude, chantage de la victime. Durée : jours à mois.

**Phase 2 — Vente exclusive**. Les données sont mises en vente à prix élevé, avec clause d'exclusivité (pas de revente par le vendeur). Acheteurs : autres groupes cybercriminels cherchant un levier, concurrents industriels (rare et risqué), services de renseignement (cas politiques).

**Phase 3 — Revente large**. Si les données ne sont pas exclusivement vendues, ou si les termes d'exclusivité sont violés, revente à multiple acheteurs avec prix décroissant.

**Phase 4 — Publication publique / gratuite**. Après que la valeur commerciale a été extraite, les données sont souvent publiées gratuitement sur des canaux Telegram, pastebins, forums. Sert à construire la réputation d'un vendeur ou à publier sous couvert idéologique.

**Phase 5 — Intégration dans les bases publiques**. Have I Been Pwned, DeHashed, et autres services indexent les données pour vérification défensive. Les données deviennent **un asset défensif** — les DSI peuvent vérifier si leurs emails sont compromis.

La durée entre phase 1 et phase 5 varie considérablement — quelques semaines pour des petits breaches de moindre intérêt, plusieurs années pour des breaches majeurs gardés exclusifs longtemps.

## 14.4 Vérification de l'authenticité

Les annonces de données volées sont **massivement polluées par des scams, des recyclages, et des fabrications**. La vérification d'authenticité est un skill central de l'analyste.

**Échantillons**. Un vendeur sérieux fournit des échantillons gratuits vérifiables — emails avec domaine cohérent, formats réalistes. Un vendeur refusant systématiquement tout échantillon est suspect.

**Fraîcheur**. Les données déjà vues dans des breaches publics (via HIBP, DeHashed) sont recyclées — pas un nouveau breach, valeur réduite.

**Spécificité**. Des données très spécifiques à une organisation (noms d'employés internes, codes produit internes, contrats signés) sont plus crédibles que des templates génériques.

**Corroboration externe**. La victime confirme-t-elle ? Un CERT ou prestataire IR est-il impliqué ? Des indices publics confirment-ils la compromission (notifications régulateurs, communiqué de presse) ?

**Cohérence interne**. Les formats, conventions, horodatages sont-ils cohérents ? Une base de données avec des inconsistances format (dates parfois US, parfois EU) signale potentiellement un assemblage factice.

**Échantillon ciblé**. Demander au vendeur un échantillon spécifique (par exemple, un fichier contenant un certain nom). S'il peut le produire, authenticité probable. S'il refuse ou produit quelque chose d'incohérent, probable scam.

Voir Annexe E pour une grille d'évaluation complète de crédibilité.

## 14.5 La dimension sectorielle

Les données volées ne sont pas distribuées uniformément. Rapport Cyberint 2025 documente une concentration sur les secteurs à forte valeur : institutions financières (cartes, credentials bancaires, accès systèmes de trading), santé (dossiers médicaux, chantage, fraude assurance), télécommunications (SIM swapping, accès réseaux), gouvernement (données classifiées, identités fonctionnaires). Chaque secteur a son **modèle de monétisation** propre — détaillé au Ch.35.

## 14.6 Fil rouge — DARKSTREAM : premiers échantillons

> **🌐 DARKSTREAM — Épisode 8 : analyse des échantillons**
>
> Lucas reçoit 5 fichiers d'échantillons initiaux + 3 additionnels via XMPP. Protocole Athéna strict : fichiers ouverts **uniquement** dans une VM isolée (Whonix + Windows 10 jetable), jamais sur la machine de production. Scan antivirus préalable. Extraction des métadonnées avec exiftool.
>
> **Fichier 1** — « Propulsion_specs_Rev7.pdf ». 14 pages, schémas techniques. Métadonnées internes : auteur « M. Dubois », entreprise « Vectris Aerospace », créé en Nov 2025, modifié en Dec 2025. Softare MS Word → PDF. Numéro de révision cohérent avec conventions Vectris.
>
> **Fichier 2** — « Supplier_list_2025.xlsx ». 340 lignes de fournisseurs. Formatage Excel, adresses cohérentes (pays UE, US, Asie). Contient un fournisseur de test interne reconnu par le RSSI de Vectris (confidentiel — nom de fantaisie utilisé comme marker).
>
> **Fichier 3** — extrait email. Export de boîte mail interne d'un ingénieur R&D. Discussions techniques, jamais publiées publiquement. Content cohérent avec un vol Office 365.
>
> Les 3 échantillons additionnels : d'autres spécifications techniques, notes de réunion, extrait budgétaire.
>
> **Verdict Lucas** : authenticité **confirmée** au niveau échantillon. Cohérence avec la compromission initiale identifiée par Mandiant chez Vectris. Le marker interne présent dans le fichier 2 est un signe fort que le dump provient bien de la compromission Vectris. Lucas escalade immédiatement à la cellule de crise Vectris et à la DGSI. Le post aero_source est authentique ; la compromission est confirmée ; l'exfiltration circule bien sur le dark web.
>
> Question suivante : qui est aero_source ? Est-ce l'attaquant initial, un proxy, un courtier ? Prochaine étape : élargir le profiling via les autres activités du pseudonyme et via l'analyse des flux crypto associés.

---
