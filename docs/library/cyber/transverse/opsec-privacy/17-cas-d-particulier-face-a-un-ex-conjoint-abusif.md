---
title: Cas D — Particulier face à un ex-conjoint abusif
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - index.md
---

## D.1 Contexte

Catherine, 39 ans, sépare de son conjoint Marc après 8 ans de relation marquée par violences psychologiques et économiques croissantes. Marc, ingénieur informatique de formation, a eu accès à tous les comptes et appareils du couple pendant la relation. Il a installé des outils de tracking sur ses appareils (Catherine suspecte mais ne l’a pas vérifié), connaît les mots de passe de la plupart des comptes, est ajouté comme contact de récupération sur plusieurs services, a accès au compte iCloud familial. Catherine quitte le domicile conjugal pour s’installer dans un studio. Elle craint :

- Que Marc accède à ses communications et localisation.
- Que Marc utilise leurs comptes joint contre elle dans la procédure judiciaire en cours.
- Que Marc l’agresse physiquement (un incident a déjà eu lieu, plainte déposée).
- Que Marc fasse pression sur leurs enfants (garde partagée en cours d’attribution).

Adversaires plausibles :

- **Marc lui-même** : capacité technique réelle, motivation très forte, accès historique considérable.
- **Cercle social et familial de Marc** : capacité variable, motivation modérée.
- **Plateformes et services** : non hostiles mais procédures de récupération exploitables par Marc.

Hors périmètre :

- Disparition complète (Catherine doit rester atteignable juridiquement, dans l’intérêt des enfants).
- Anonymat sur les comptes nominatifs (bancaires, administratifs).

**Particularité éditoriale** : ce profil est sous-traité dans la majorité des cours cyber, qui se focalisent sur l’étatique. Pour une fraction non négligeable de la population — femmes essentiellement — c’est *le* threat model réel.

## D.2 Procédure d’urgence (J0-J7)

**Jour 0 (jour de la séparation effective)** :

- Catherine quitte le domicile avec ses affaires essentielles. Elle conserve son téléphone actuel pour le moment, mais avec discipline (ne pas s’y connecter à des comptes nouveaux).
- Établissement d’un téléphone neuf, acheté cash dans un magasin, opérateur différent (nouveau numéro non communiqué à Marc).
- Ce téléphone neuf reçoit immédiatement une nouvelle SIM nominale Catherine (KYC normal, pas tentative d’anonymisation — Catherine veut être joignable juridiquement, et c’est plus discret de fonctionner avec un compte normal).

**Jour 1** :

- Audit du téléphone précédent par une personne tierce de confiance (un cousin technicien). Recherche de stalkerware : examen des applications installées (sur Android avec écran de gestion des apps en mode usage avancé ; sur iOS, gestion des profils MDM installés). Résultat : présence d’une application déguisée en « calculatrice » (mSpy renommé), profil MDM Apple installé permettant suivi de localisation. Marc avait installé.
- Catherine décide : *ne pas* effacer immédiatement le téléphone (preuves utiles pour la procédure pénale en cours sur violences). Photos des installations malveillantes, dépôt de plainte additionnelle pour violation de vie privée et installation de logiciel espion (cf. art. 226-1 et 323-1 CP).

**Jour 2-3** :

- **Tous les mots de passe critiques changés** depuis le nouveau téléphone (ou depuis un cybercafé sécurisé) :
  - Apple ID Catherine (sortie du « Family Sharing » avec Marc, création nouveau compte distinct si elle migre vers iPhone neuf).
  - Compte Google.
  - Compte Microsoft.
  - Comptes bancaires (et procédure spécifique avec la banque pour bloquer Marc de l’accès en ligne sur comptes joints).
  - Messageries : Signal, WhatsApp réinstallés sur nouveau téléphone, anciennes sessions révoquées.
  - Réseaux sociaux : changement de mots de passe, retrait de Marc des contacts (Facebook, Instagram, LinkedIn).
  - Compte impôts, sécurité sociale, et autres administratifs.
  - Email principal (Gmail Catherine) : mot de passe, MFA, contacts de récupération vérifiés (retrait de Marc s’il était listé), questions de récupération mises à jour.
- **Contacts de récupération audités** : Apple Account Recovery Contacts (retrait de Marc s’il l’avait été), Google (idem).
- **Numéro de récupération** : remplacement par le nouveau numéro.
- **Comptes joints non clos immédiatement** (procédure légale en cours pour le partage), mais surveillés activement et logs préservés.

**Jour 4-5** :

- **Réseau social** : Facebook → profil verrouillé, audit des amis (suppression du cercle de Marc), publications passées masquées, retrait de toutes les photos taguées par Marc.
- **Localisation** : audit Find My iPhone et services Google (retrait du partage de localisation avec Marc s’il existait). Catherine a constaté qu’elle partageait sa localisation avec Marc sur Google Maps : retiré.
- **AirTags et trackers** : Catherine fait scan de ses affaires (sac, voiture, vêtements neufs) avec son téléphone neuf qui détecte les AirTags inconnus. iOS et Android (depuis 2023-2024) alertent en cas de tracker tiers suivant. Catherine trouve un AirTag dans sa voiture (Marc avait accès au véhicule). Retrait et archivage pour la procédure pénale.

**Jour 6-7** :

- Achat d’un PC neuf si ressources le permettent (laptop d’entrée de gamme, FileVault/BitLocker activés immédiatement, comptes neufs).
- Configuration d’un gestionnaire de mots de passe (Bitwarden gratuit) avec mots de passe nouveaux et uniques pour tous les comptes.
- Configuration de MFA matériel ou TOTP partout où possible (YubiKey si Catherine peut investir, sinon Aegis Authenticator sur le téléphone neuf).

## D.3 Mois 1-3 : stabilisation

**Audit physique du studio** :

- Vérification absence de caméras cachées (achetée pour 30 € sur Amazon, détecteur RF + lentille caméra). Aucune trouvée.
- Vérification absence d’écoute (microphones discrets) — généralement par scan RF et inspection visuelle.
- Serrure changée (responsabilité du bailleur, demandée explicitement).

**Audit numérique continu** :

- Connexions inhabituelles sur comptes ? Catherine surveille hebdomadaire les sessions actives.
- Alertes de tentative de connexion ? Activées sur tous les comptes principaux.
- Email principal en monitoring HaveIBeenPwned (notification de nouvelle fuite — particulièrement utile si Marc tenterait de la doxxer).

**Communications avec les enfants** :

- Les enfants utilisent leurs propres téléphones (avec accord parental). Catherine et eux communiquent via Signal avec disappearing messages 30 jours pour les conversations non essentielles. Pas de discussion juridique avec les enfants par messages.
- En garde partagée, Catherine n’écrit pas aux enfants sur des sujets sensibles via canaux que Marc pourrait surveiller.

**Soutien externe** :

- Association locale (CIDFF en France, équivalents locaux) pour soutien juridique et psychologique.
- Avocate spécialisée violences conjugales.
- Psychologue spécialisée trauma post-séparation.
- Réseau de soutien (deux amies, une sœur) — un seul cercle de confiance restreint, choisi soigneusement (les autres « amis » communs avec Marc ne sont pas mis dans le secret).
- Coalition Against Stalkerware ressources internationales.

## D.4 Incident à M+4 — tentative d’accès au compte Gmail

Catherine reçoit une notification : « Une tentative de connexion à votre compte Google a été refusée. Emplacement : [ville de Marc]. Heure : 22h17 ». Plus tard, deuxième notification similaire. Marc tente d’accéder. La MFA matérielle (YubiKey configurée) bloque.

Réponse :

- Catherine vérifie qu’aucune session n’est active.
- Changement préventif du mot de passe.
- Documentation de l’incident : capture des notifications, ajout au dossier juridique.
- Signalement à l’avocate qui transmet à l’instruction.

## D.5 Incident à M+8 — tentative de doxxing

Marc, dans le contexte de la procédure de divorce conflictuel et de garde, publie sur un blog familial accessible au cercle élargi des informations privées de Catherine : sa nouvelle adresse, son nom d’employeur, des éléments de sa vie privée. Tentative manifeste d’intimidation.

Réponse :

- Capture immédiate (preuve), avec horodatage notarié si possible.
- Signalement à la plateforme.
- Dépôt de plainte additionnelle (atteinte à la vie privée, art. 226-1 ; et possiblement harcèlement).
- Demande de droit à l’effacement au blog hébergeur.
- Communication contrôlée avec l’employeur (Catherine prévient son N+1 de la situation pour qu’il sache à quoi s’attendre, sans détails).

Effet : le blog est retiré sous 72h après signalement à l’hébergeur. La plainte avance, le dossier de violences conjugales se renforce.

## D.6 Mois 12+ : nouvelle normalité

Un an après la séparation, Catherine a :

- Une stack cyber complètement renouvelée, indépendante de Marc.
- Une procédure judiciaire qui avance (Marc condamné pour les violences initiales, garde partagée modifiée en sa défaveur).
- Une posture de monitoring qui devient routine sans plus être anxiogène.
- Un soutien externe pérenne.

Elle peut commencer à relâcher progressivement la vigilance (sans baisser la garde sur l’hygiène cyber de base), à reconstruire sa vie sociale et professionnelle.

## D.7 Leçons

1. **L’adversaire de proximité est sous-évalué**. Marc avait des capacités modérées techniquement mais une connaissance préalable totale qui compensait largement.
1. **La rupture cyber doit accompagner la rupture sentimentale**. Sans cela, l’ex-conjoint conserve un accès massif.
1. **La détection de stalkerware** doit être une étape précoce, pas une découverte tardive. Coalition Against Stalkerware fournit ressources et outils.
1. **Les preuves comptent** : ne pas effacer trop vite les éléments compromis qui constituent des preuves utiles à la procédure pénale.
1. **Le soutien collectif** : associations, avocate, psychologue, réseau de proches choisis. Ne pas s’isoler. La défense individuelle pure ne suffit pas.
1. **Patience et durée** : la stabilisation prend des mois, pas des semaines. La posture doit être soutenable sur la durée.

-----
