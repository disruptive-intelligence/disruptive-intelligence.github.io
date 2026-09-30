---
title: Cas C — Olivier Mercier
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - index.md
---

dirigeant de PME tech, cible d’espionnage économique

## C.1 Contexte

Olivier Mercier, 47 ans, dirigeant d’une PME française de 80 salariés, secteur chiffrement matériel (HSM, modules pour le secteur bancaire et défense). Capital majoritairement détenu par lui et deux cofondateurs. Carnet de commandes croissant, partenariats avec deux grands groupes français du secteur défense. Récemment, intérêt commercial de la part d’acteurs étrangers (chinois, américain), avec offres de rachat non sollicitées.

Adversaires plausibles :

- **Concurrents internationaux** : capacité d’espionnage économique élevée (services étatiques chinois APT documentés visant la cybersécurité européenne, hacking commercial américain également).
- **Services russes** : capacité très élevée, motivation modérée à élevée (le secteur intéresse).
- **Concurrents européens directs** : capacité moyenne.
- **Criminalité financière** : capacité moyenne, motivation forte si visibilité Olivier (médias spécialisés ont publié son nom).
- **Insiders mécontents** : capacité variable, motivation possible (en cas de conflit interne, peu probable actuellement).

Hors périmètre :

- Espionnage industriel par voie commerciale légitime (intelligence économique standard).
- Diligence raisonnable d’acheteurs potentiels (avec accords NDA).

## C.2 Posture initiale et audit

À T0, posture standard de PME française : Microsoft 365 entreprise, Windows 11 sur la plupart des postes, quelques Mac chez l’équipe créa/dev. Compte O365 admin global tenu par le DSI. Pas de MFA matériel généralisé. Pas de procédure formelle anti-BEC. Backups Veeam dans le DC local. Pas de Pegasus Test (jamais évoqué).

Audit par RSSI externe à T0+2 mois (Olivier a sollicité après les premières offres de rachat) :

- Vulnérabilités identifiées : MFA SMS sur certains comptes, exposition VPN historique, partage de mots de passe entre dirigeants, comptes Apple ID familiaux mélangés.
- Hygiène réseau : VLAN absent, IoT corporate (impression, salle de réunion) sur même VLAN que postes admin.
- Manque de procédures : pas de processus anti-BEC, pas de Threat Modeling formalisé.
- Surface email externe : Olivier accessible via 4 emails publics, signatures professionnelles riches en information (téléphone direct, fonctions, organigramme implicite).

Plan d’action à 6 mois validé en CODIR.

## C.3 Architecture cible déployée

**Niveau dirigeants (Olivier + 2 cofondateurs)** :

- iPhones 15 Pro avec Lockdown Mode activé. ADP iCloud. Contact Key Verification entre dirigeants et exec team.
- MacBooks Pro avec FileVault, Lockdown Mode en voyage. Mises à jour disciplinées via Apple Business Manager.
- 1Password Famille + Business (partage de credentials sensibles avec audit). YubiKey 5C NFC (chacun avec 2 clés).
- Signal entre dirigeants (vérification Safety Numbers en présentiel). iMessage en backup.
- Email pro avec MFA matériel obligatoire.
- Travel kit : MacBook Air burner pour voyages sensibles (Chine, US sensibles), GrapheneOS sur Pixel burner.

**Niveau exec team (12 personnes)** :

- Même stack mais sans MacBook burner systématique.
- Formation BEC obligatoire trimestrielle.
- Procédure : tout virement > 10 k€ doit être validé par appel téléphonique sur ligne connue, jamais sur la seule base d’un email.

**Niveau salariés** :

- MFA via Microsoft Authenticator (push) sur tous les comptes O365.
- Politique de chiffrement disque automatique (BitLocker via Intune).
- Filtre email Microsoft Defender + sandbox pour pièces jointes.
- Formation phishing trimestrielle.

**Niveau infrastructure** :

- Segmentation VLAN : production / corporate / IoT / invités.
- Pare-feu sortant restrictif depuis le segment R&D.
- Bastion pour accès admin, journalisation.
- EDR (Microsoft Defender for Endpoint) déployé.
- SOC managé externalisé pour monitoring nuit/weekend.
- Backup 3-2-1 avec immutabilité + tests trimestriels.

**Politique BYOD** : pas de BYOD pour l’accès aux données sensibles. Mobile management via Intune sur les téléphones pro.

## C.4 Incident à T+8 mois — tentative de BEC sophistiquée

Olivier est en déplacement à Tokyo pour un partenariat. Pendant son absence, la directrice financière (Sophie L.) reçoit un email d’Olivier. L’adresse semble correcte. Le sujet : « URGENT - virement Kazakhstan partenaire confidentiel ». Le message demande un virement de 380 000 € sur un IBAN kazakh, sous prétexte d’un acompte sur partenariat strictement confidentiel à conclure ce jour-là. Le ton est cohérent avec celui d’Olivier. Le mail est suivi 30 minutes plus tard d’un appel téléphonique sur ligne fixe de Sophie, prétendument d’Olivier, voix très similaire (deepfake vocal), insistant : « C’est confidentiel, ne dis rien aux autres, exécute. »

Sophie applique la procédure interne : tout virement > 10 k€ doit être validé par appel sur ligne *connue*. Sophie raccroche, appelle Olivier sur son numéro habituel — pas de réponse (Olivier est en réunion). Sophie attend. Olivier rappelle 2 heures plus tard sur sa ligne habituelle. Confirmation : il n’a rien demandé.

Investigation :

- Email envoyé depuis un domaine sosie (`mercieretassocies-fr.com` au lieu de `mercieretassocies.fr`). DKIM signé sur le domaine sosie.
- Appel téléphonique : numéro spoofé, voix probablement clonée (le SOC retrouve plus tard que la voix d’Olivier est disponible dans plusieurs interviews de presse sectorielle, suffisamment pour un voice clone qualité).
- Reconnaissance préalable : LinkedIn de Sophie L. comme DAF, mention publique du partenariat Tokyo prévu (Olivier l’avait évoqué en conférence 2 mois plus tôt), nom et numéro de Sophie public sur le site corporate.

Effet : pas de perte financière. Investigation par le SOC en lien avec ANSSI (PME stratégique secteur sécurité). Plainte déposée. Identification partielle : infrastructure compromise dans un pays tiers, attribution incertaine.

Réponse :

- Suppression du téléphone direct de Sophie du site corporate.
- Procédure renforcée : tout virement > 50 k€ exige double validation (Sophie + Olivier ou cofondateurs) avec hot-pin vocal convenu en présentiel, à renouveler trimestriellement.
- Communication interne : tous les collaborateurs sont informés du modus operandi. Formation spécifique BEC avec exemples concrets.
- Coordination avec ANSSI sur le partage d’IOCs (l’attaque cible peut être réutilisée sur d’autres entreprises du secteur).

## C.5 Incident à T+11 mois — voyage Chine

Olivier doit se rendre à Shenzhen pour rencontrer un partenaire potentiel. Préparation :

- MacBook burner installé spécifiquement pour ce voyage, OS frais, aucun document d’entreprise, accès cloud E2EE (Proton Drive) à la demande.
- Pixel burner avec GrapheneOS, profil voyage. Aucun mail pro, aucun compte personnel. Signal username connu de 3 personnes (sa femme, son DSI, son associé).
- Pas de YubiKey emportée (laissée chez le DSI en France).
- Documents physiques minimaux. Notes professionnelles sur papier, à brûler à l’aéroport au retour.
- Avant départ : Olivier informe son DSI et son associé. Plan de communication : un check-in quotidien sur Signal à heure fixe. Si pas de check-in, escalade après 24h.

Pendant le voyage :

- À l’hôtel à Shenzhen, le MacBook burner reste en chambre uniquement quand il est dans le coffre de la chambre (modéré sécurisé, mais pas zero risque). Olivier le porte avec lui le plus souvent.
- Constatation au matin J+2 : la pochette de transport du MacBook a été manipulée (le pli systématique qu’Olivier fait sur la fermeture est défait). Pas de marquage évident sur le laptop lui-même.
- Olivier suspend l’usage du MacBook. Ne l’utilise plus pour les réunions sensibles ce jour. Bascule sur prise de notes papier.

Au retour en France :

- Le MacBook est livré directement à l’analyste forensique externe.
- Investigation : analyse du firmware, du SSD, des logs. Trace d’une connexion physique externe en heures non opérables (3h du matin local), pas de modification système identifiable (ou modification trop fine pour outils d’analyse standard).
- Décision conservative : le MacBook est physiquement détruit. Reset matériel impossible à garantir.
- Coût total du voyage en pertes matérielles : ~3 500 €. Coût en information sensible exfiltrée : zéro (le MacBook ne contenait aucun document sensible).

## C.6 Posture à T+18 mois

L’entreprise a maintenant :

- Une posture cyber sérieuse, auditée annuellement.
- Une culture interne où la BEC est connue de tous, l’OPSEC voyage est partagée.
- Une relation établie avec l’ANSSI (programme DI/DCI pour entreprises stratégiques).
- Un budget annuel sécurité représentant 4-5 % du CA, contre 1 % à T0.

Les offres de rachat continuent. Olivier les évalue. Aucune compromission documentée. L’entreprise valorise sa posture cyber comme un actif (les acheteurs potentiels du secteur défense font des due diligences cyber poussées ; une bonne posture augmente la valorisation).

## C.7 Leçons

1. **BEC > APT** comme threat principal pour PME, statistiquement et par retour d’expérience.
1. **Procédures de virement** : code anti-BEC, double validation par canal séparé. Non négociable.
1. **Voyage hostile = burner device**. Le coût d’un burner est inférieur au coût d’une compromission.
1. **Formation continue** des collaborateurs : sans la directrice financière disciplinée, l’entreprise aurait perdu 380 k€.
1. **Relation institutionnelle** : ANSSI pour la France, équivalents nationaux ailleurs. Une PME stratégique a accès à du conseil gratuit.
1. **Trade-off sécurité-business** : le sur-durcissement détruit l’agilité commerciale. La posture doit être proportionnée et soutenable.

-----
