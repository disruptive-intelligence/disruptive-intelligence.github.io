---
title: Chapitre 32 — Identité numérique administrative
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie VI — VIE privée, images, documents ET surexposition
  - index.md
---

FranceConnect, Ameli, impôts, CAF

*Pour un particulier en France en 2025-2026, l'identité numérique administrative est devenue centrale. FranceConnect est le mécanisme de fédération qui permet de se connecter à plus de 1 400 services publics via un fournisseur d'identité partenaire (Ameli, impots, La Poste, etc.). Si un de ces fournisseurs pivots est compromis, l'accès à l'ensemble des services connectables via FranceConnect avec ce fournisseur l'est aussi — déclarations fiscales, droits sociaux, démarches d'état civil, dossiers santé. C'est une catégorie de comptes que beaucoup d'utilisateurs sécurisent moins bien que leur banque, alors qu'elle a un potentiel d'usurpation comparable.*

## 32.1 FranceConnect : la clé maîtresse de l'administration

**FranceConnect** est le système d'identification fédéré de l'administration française. Il permet de se connecter à plus de 1 400 sites publics avec un identifiant unique (Ameli, impôts, CAF, ANTS, Mon Compte Formation, France Travail, etc.). En 2025-2026, c'est devenu le maillon central de l'identité administrative.

FranceConnect n'est pas « un compte unique » avec un mot de passe propre — c'est un **mécanisme de fédération d'identité** qui permet de se connecter à un service public via un fournisseur d'identité partenaire au choix. Le mot de passe n'est donc pas « le mot de passe FranceConnect » mais celui du fournisseur utilisé (Ameli, impots, La Poste, etc.) — c'est chez ce fournisseur qu'il se modifie.

Les **fournisseurs d'identité partenaires** de FranceConnect évoluent dans le temps. Au moment de la rédaction, on trouve notamment : impots.gouv.fr (DGFiP), ameli.fr (Assurance Maladie), L'Identité Numérique La Poste, MSA, France Identité (l'application gouvernementale liée à la CNI électronique), ainsi que des fournisseurs privés agréés comme Yris ou TrustMe selon les disponibilités du moment. **Cette liste évolue** : à titre d'illustration, le service Yris doit être retiré de FranceConnect à compter du 1er juillet 2026. Il faut donc toujours vérifier la liste officielle des fournisseurs d'identité disponibles au moment de la lecture sur **franceconnect.gouv.fr**. Si l'un des fournisseurs d'identité que vous utilisez est compromis, l'accès à tous les services connectables via FranceConnect avec ce fournisseur est compromis.

Les **conséquences d'une compromission** sont concrètes et lourdes : modification des coordonnées bancaires pour un remboursement de la Sécurité Sociale ou un crédit d'impôt (les fonds partent vers le compte de l'attaquant), accès à des documents administratifs, fiscaux, sociaux ou médicaux selon les services concernés (avis d'imposition, attestations, données CAF, dossier médical dans Mon espace santé, démarches de titres ANTS ou de formation), modification de l'adresse fiscale (et donc rerouting des courriers officiels y compris fiscaux), souscription frauduleuse à Mon Compte Formation, modification de droits sociaux.

Les **bonnes pratiques** :

- **Mot de passe unique et fort** sur chaque compte pivot (Ameli, impots.gouv, etc.) — le gestionnaire de mots de passe est indispensable. Un compte Ameli compromis = un accès FranceConnect compromis.
- **MFA activé** sur les comptes pivots : Ameli propose un code à usage unique par SMS (en attendant des options plus robustes), impots.gouv.fr propose un code par email. C'est moins robuste qu'une app TOTP, mais c'est mieux que rien.
- **Préférer France Identité** quand c'est possible. L'application France Identité, basée sur la puce NFC de la CNI électronique nouvelle génération (depuis 2021), est qualifiée au **niveau de garantie élevé** au sens du règlement européen eIDAS — le niveau le plus haut. Elle nécessite la possession physique de la CNI + un code personnel + le téléphone — trois facteurs combinés. **FranceConnect+** est la variante de FranceConnect qui exige un moyen d'identification de niveau **substantiel ou élevé** (selon le fournisseur utilisé) ; il est requis pour les démarches les plus sensibles (procurations en ligne, démarches notariales dématérialisées, etc.).
- **Vérifier régulièrement** dans son espace FranceConnect (sur franceconnect.gouv.fr) la liste des connexions récentes — chaque utilisation est tracée.
- **Vigilance phishing** : les emails « Ameli », « impôts », « CAF », « ANTS » sont parmi les phishings les plus répandus (parfois en pic saisonnier — campagne de déclaration fiscale au printemps, rentrée scolaire pour la CAF). Aucune administration ne demande JAMAIS un mot de passe ou un code par email ou SMS. En cas de doute, accéder au site directement en tapant l'URL.

## 32.2 Les services administratifs principaux

**impots.gouv.fr** : compte fiscal personnel, déclarations, avis d'imposition, prélèvements à la source, espace particulier. Le compromettre permet de modifier l'IBAN de remboursement, falsifier des avis d'imposition (utilisables pour souscrire un prêt frauduleux), et accéder à des informations financières détaillées. **Mot de passe unique, MFA actif.**

**Ameli (Assurance Maladie)** : remboursements, attestations, carte Vitale numérique, accès partiel à Mon espace santé. Le compromettre permet de modifier les coordonnées bancaires pour les remboursements et d'accéder à des éléments médicaux. **Mot de passe unique, code temporaire actif.**

**CAF** : aides sociales, allocations, déclarations de ressources, attestations. Conséquence d'une compromission : modification de l'IBAN de versement des aides, fraudes aux déclarations.

**ANTS (Agence nationale des titres sécurisés)** : démarches d'état civil et de titres (CNI, passeport, permis de conduire, carte grise). Compromission = possibilité de demander frauduleusement des duplicatas de titres au nom de la victime.

**Mon Compte Formation (CPF)** : crédits formation, démarches de financement. Cible historique d'arnaques (« votre CPF expire » — il n'expire jamais ; « récupérez vos droits avant la fin de l'année » — c'est faux). En 2022-2024, des arnaques massives ont consisté à se faire passer pour un organisme de formation et à siphonner les droits CPF des victimes en signant des inscriptions fictives. Le service a été durci (authentification renforcée obligatoire), mais la vigilance reste de mise.

**France Travail** (anciennement Pôle Emploi) : déclarations mensuelles, allocations chômage, candidatures. Compromission = fraude aux allocations.

**Mon espace santé** : dossier médical numérique, carnet de santé, ordonnances, comptes-rendus. Sujet traité spécifiquement au Ch.33.

**La Poste Identité Numérique** : moyen d'identification alternatif (niveau Substantiel) basé sur la vérification physique en bureau de poste. Utilisable pour FranceConnect+ (les démarches les plus sensibles). Si activé, le sécuriser avec le même soin qu'un compte bancaire.

## 32.3 Phishing administratif : les pièges fréquents

Les phishings administratifs exploitent l'autorité institutionnelle et la crainte des conséquences fiscales/sociales. Quelques scénarios récurrents :

**« Vous bénéficiez d'un remboursement d'impôts de X €, cliquez ici pour confirmer »** (faux site impots.gouv.fr) → capture des identifiants fiscaux + RIB. La DGFiP ne demande JAMAIS de « confirmer » par email. Les remboursements arrivent automatiquement sur le compte déjà déclaré.

**« Votre dossier Ameli est incomplet, mettez à jour vos coordonnées sous 48h »** → faux site Ameli, capture des identifiants. Ameli n'envoie jamais ce type de message ; un dossier incomplet fait l'objet d'un courrier postal ou d'un message dans l'espace Ameli.

**« Votre carte Vitale arrive à expiration, commandez la nouvelle ici »** → arnaque classique. La carte Vitale n'expire pas (elle n'a aucune date d'expiration imprimée). Les renouvellements se font automatiquement par l'Assurance Maladie en cas de besoin (mariage, perte, etc.).

**« Votre CPF expire le X — récupérez vos droits maintenant »** → le CPF n'expire pas. La mention d'expiration est un mensonge récurrent.

**« Votre ANTS — votre carte grise / permis est en attente de validation »** → faux site ANTS qui capture les identifiants et les informations de carte bancaire (sous prétexte de « frais de dossier »). Les démarches ANTS légitimes se font UNIQUEMENT sur ants.gouv.fr.

**« Avis de procès-verbal — payez votre amende »** → faux site qui imite l'ANTAI (Agence nationale de traitement automatisé des infractions). Le vrai site est antai.gouv.fr. Les vrais avis de contravention arrivent par courrier postal ; les paiements légitimes ne se font que sur le site officiel.

## 32.3 bis — Abus autour des aides publiques

*(MaPrimeRénov', CPF, énergie, mutuelle)*

Les arnaques aux aides publiques sont en forte croissance. Le mécanisme classique : un démarchage (téléphone, SMS, email, réseau social, voire à domicile) propose d'aider la victime à « ne pas perdre ses droits » ou « récupérer une aide à laquelle elle a droit » — en échange d'informations personnelles ou d'un paiement.

**MaPrimeRénov'** et aides à la rénovation énergétique : aucun organisme public ne démarche pour MaPrimeRénov'. Les vrais conseils sont gratuits et accessibles via les Espaces Conseil France Rénov' (france-renov.gouv.fr). Les artisans agréés RGE (Reconnu Garant de l'Environnement) figurent sur l'annuaire officiel. Les arnaques : faux conseillers qui collectent RIB et avis d'imposition pour monter un dossier au nom de la victime puis détourner la prime, ou entreprises non RGE qui font signer des travaux non éligibles à l'aide promise.

**CPF (Compte Personnel de Formation)** : le CPF n'expire jamais, ne se transfère pas, et ne se retire pas en liquide. Toute communication qui annonce le contraire est une arnaque. Les formations CPF légitimes passent par le site officiel **moncompteformation.gouv.fr**, et seuls les organismes certifiés Qualiopi peuvent y être référencés. Le démarchage commercial pour le CPF est interdit par la loi depuis décembre 2022.

**Aides énergie / chèque énergie / boucliers tarifaires** : aucun démarchage commercial n'est nécessaire. Le chèque énergie est envoyé automatiquement aux foyers éligibles (vérification sur chequeenergie.gouv.fr). Les arnaques : faux SMS « votre chèque énergie est disponible », faux site qui demande le numéro fiscal et un RIB.

**Mutuelle santé / complémentaire santé solidaire (CSS)** : démarchages frauduleux par téléphone (« votre mutuelle est résiliée », « vous avez droit à la mutuelle gratuite, communiquez-moi vos coordonnées »). Les vraies démarches de CSS passent par Ameli ou le formulaire officiel sur ameli.fr. Aucun appel proactif d'un « conseiller mutuelle officiel » n'est légitime.

**Aides CAF et allocations** : la CAF ne demande jamais de saisir RIB ou identifiants par SMS ou email, ni de « débloquer » une aide via un lien. Les démarches passent par caf.fr et l'app Caf - Mon Compte officielle.

Le réflexe commun à toutes ces aides : (1) si on n'a rien demandé, c'est une arnaque ; (2) les aides publiques se demandent depuis le site officiel, jamais via un intermédiaire qui démarche ; (3) un intermédiaire légitime (artisan RGE, organisme de formation Qualiopi) ne demande pas le numéro fiscal, le RIB, ou la copie de la CNI avant un échange physique ou contractualisé ; (4) signaler les démarchages frauduleux via SignalConso (signal.conso.gouv.fr) en plus des canaux habituels.

## 32.4 Le réflexe administratif

Pour toutes les démarches publiques :

- Accéder UNIQUEMENT en tapant l'URL officielle (les sites publics ont tous un domaine en .gouv.fr ou .fr clairement identifiable — ameli.fr, impots.gouv.fr, caf.fr, ants.gouv.fr).
- Préférer **service-public.fr** comme point d'entrée — ce site annuaire de l'administration redirige toujours vers les vrais services.
- Ne jamais cliquer sur un lien dans un email/SMS prétendument administratif. Les administrations préviennent par courrier postal pour les sujets importants.
- Pour les emails/SMS suspects, signaler via Signal Spam ou 33700.

> **🔵 Lina — Épisode 8 :** Lina reçoit un email « impots.gouv.fr — votre remboursement de 247 € est en attente de confirmation ». L'email est très bien fait : logo Marianne, mise en page officielle, ton administratif. Le lien pointe vers « impots-gouv-particuliers.fr » — domaine qui ressemble mais n'est PAS impots.gouv.fr (le vrai domaine n'a pas de « particuliers » dans le nom). Lina ne clique pas et va directement sur impots.gouv.fr en tapant l'URL : aucun remboursement en attente. Elle signale l'email à Signal Spam et le supprime. Réflexe : 30 secondes, zéro dégât.

---

<a id="chapitre-33"></a>
