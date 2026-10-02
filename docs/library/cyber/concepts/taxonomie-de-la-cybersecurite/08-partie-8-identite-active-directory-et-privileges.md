---
title: Partie 8 — Identité, Active Directory et privilèges
source: Cyber/11 Concepts/Cartes & familles/Taxonomie de la cybersécurité.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - index.md
---

### Vue d'ensemble taxonomique

Les attaques d'identité suivent une logique de progression :

- **Obtenir des identifiants** : deviner (spraying, brute force, stuffing), arracher (kerberoasting, AS-REP roasting), voler en mémoire (credential dumping).
- **Réutiliser sans casser** : pass-the-hash/ticket, overpass-the-hash — l'authentification par « preuve » sans connaître le mot de passe.
- **Forger des accès** : golden/silver ticket, shadow credentials, AD CS abuse — fabriquer ses propres preuves d'identité.
- **Abuser des relations de confiance** : délégation, RBCD, ACL/GPO abuse — exploiter la configuration de l'annuaire.
- **Atteindre le cœur** : DCSync/DCShadow — se faire passer pour un contrôleur de domaine.
- **Se déplacer** : lateral movement Windows vers le contrôle total.

🧭 **Taxonomie** — Ces techniques correspondent aux tactiques ATT&CK *Credential Access, Lateral Movement, Privilege Escalation, Persistence*. La défense de fond : tiering, PAM/bastion, durcissement, surveillance comportementale.

---


### Chapitre 155 — L'identité comme nouveau périmètre

**Définition.** Constat structurant : dans un SI moderne (cloud, SaaS, télétravail), ce n'est plus le réseau qui délimite la confiance, mais l'*identité*. Voler une identité, c'est obtenir ses accès où qu'ils soient.

**Principe.** Le « château fort » périmétrique s'efface : les ressources sont dispersées, accessibles de partout. L'authentification et l'autorisation deviennent le vrai point de contrôle. D'où la centralité de l'IAM, du MFA, du Zero Trust et de la protection de l'annuaire.

🔧 **Exemple concret** — Un identifiant volé par phishing donne accès à la messagerie cloud, au SaaS et au VPN — sans jamais « entrer » physiquement dans un réseau.

🧭 **Taxonomie** — Cadre directeur de toute la partie ; relie AD on-prem, identité cloud (Partie 10) et Zero Trust (chapitre 17).

🎯 **À retenir** — Protéger l'identité est devenu *la* priorité défensive : c'est elle, plus que le réseau, qui détient les clés.


### Chapitre 156 — Annuaire, domaine, forêt, OU, GPO

**Définition.** Les briques structurelles d'Active Directory.

- **Annuaire** : base centralisée des objets (utilisateurs, machines, groupes).
- **Domaine** : unité d'administration et de sécurité regroupant ces objets.
- **Forêt** : ensemble de domaines partageant un schéma et des relations de confiance ; *frontière de sécurité ultime* d'AD.
- **OU (unité d'organisation)** : conteneur pour organiser et déléguer l'administration.
- **GPO (stratégie de groupe)** : mécanisme de configuration/sécurité appliqué massivement aux objets.

**Principe.** Cette structure détermine *qui administre quoi* et *comment les politiques se propagent*. Sa complexité crée des chemins d'attaque souvent invisibles (relations de confiance, délégations, héritage de GPO).

🧭 **Taxonomie** — La **forêt** est la vraie frontière de sécurité : compromettre un domaine peut, via les relations de confiance, menacer toute la forêt.

🎯 **À retenir** — Comprendre la structure AD (forêt > domaine > OU, + GPO) est indispensable : c'est la carte du terrain que l'attaquant cherche à cartographier.


### Chapitre 157 — Kerberos

**Définition.** Protocole d'authentification d'AD fondé sur des *tickets* délivrés par un centre de distribution de clés (KDC, porté par le contrôleur de domaine).

**Principe.** Après authentification, l'utilisateur reçoit un ticket initial (TGT) lui permettant d'obtenir des tickets de service (TGS) pour accéder aux ressources, sans renvoyer son mot de passe. La sécurité repose sur des secrets cryptographiques (dont celui du compte *krbtgt*, clé de voûte du domaine).

🧭 **Taxonomie** — De nombreuses attaques d'identité ciblent Kerberos : kerberoasting (TGS), AS-REP roasting (pré-auth), pass-the-ticket, golden ticket (forge de TGT via krbtgt), silver ticket (forge de TGS).

⚠️ **Erreur fréquente** — Ignorer la sensibilité extrême du compte *krbtgt* : sa compromission permet de forger des accès quasi indétectables (golden ticket).

🎯 **À retenir** — Kerberos évite de transmettre les mots de passe mais introduit des tickets et des secrets (krbtgt) dont l'abus est au cœur des attaques AD.


### Chapitre 158 — NTLM

**Définition.** Protocole d'authentification Windows plus ancien, par défi-réponse, encore présent pour compatibilité.

**Principe.** NTLM authentifie via un condensat (hash) du mot de passe plutôt que le mot de passe en clair. Cette mécanique rend possible la *réutilisation du hash* (pass-the-hash) et le *relais* (NTLM relay), car « prouver qu'on a le hash » suffit.

🧭 **Taxonomie** — Racine du pass-the-hash (chapitre 168) et du NTLM relay (lié à SMB — chapitre 139).

⚠️ **Erreur fréquente** — Laisser NTLM (surtout ses versions anciennes) activé partout « pour compatibilité », au lieu de le restreindre et de privilégier Kerberos.

🎯 **À retenir** — NTLM, par sa mécanique de hash réutilisable, est un facilitateur majeur d'attaques d'identité : le restreindre et activer la signature/EPA est important.


### Chapitre 159 — LDAP

**Définition.** Protocole d'interrogation et de modification de l'annuaire (lecture/écriture des objets AD).

**Principe.** LDAP permet de *lire la structure* (énumération d'utilisateurs, groupes, ACL, délégations) et parfois de *modifier* des objets. C'est l'outil de reconnaissance interne d'AD par excellence, et un vecteur si les écritures sont mal contrôlées.

🧭 **Taxonomie** — Support de l'énumération AD (chapitre 128) et de l'analyse des chemins d'attaque (relations, ACL). Lié à l'injection LDAP côté applicatif (chapitre 101).

🎯 **À retenir** — LDAP est la « vue » de l'annuaire : un attaquant l'utilise pour cartographier les chemins vers les privilèges ; sa surveillance révèle la reconnaissance interne.


### Chapitre 160 — Comptes utilisateurs, machines et services

**Définition.** Les trois grands types de comptes dans AD.

- **Comptes utilisateurs** : personnes physiques.
- **Comptes machines** : ordinateurs joints au domaine (avec leur propre secret).
- **Comptes de service** : identités non humaines exécutant des applications/services, souvent à privilèges élevés et mots de passe rarement changés.

**Principe.** Les comptes de service sont une cible privilégiée : puissants, persistants, parfois avec un SPN exposé (cible du kerberoasting) et des mots de passe faibles/anciens.

🧭 **Taxonomie** — Les comptes de service relient kerberoasting (chapitre 163), permissions excessives (chapitre 76) et persistance.

🎯 **À retenir** — Les comptes de service, puissants et négligés, sont un maillon faible classique : mots de passe forts, gMSA, moindre privilège et rotation.


### Chapitre 161 — Groupes privilégiés

**Définition.** Groupes conférant des droits étendus (administrateurs du domaine, de l'entreprise, opérateurs divers).

**Principe.** L'appartenance à ces groupes est la « clé du royaume ». Les attaquants cherchent à y accéder directement ou *indirectement* (via une chaîne d'ACL/délégations menant à un membre). Leur surveillance et leur minimisation sont prioritaires.

🧭 **Taxonomie** — Cible finale des chemins d'attaque AD ; lié au tiering (chapitre 162) et à l'abus d'ACL (chapitre 178).

⚠️ **Erreur fréquente** — Comptes nominatifs accumulés dans les groupes d'administration, jamais revus (privilege creep).

🎯 **À retenir** — Minimiser et surveiller l'appartenance aux groupes privilégiés est l'un des contrôles AD les plus rentables.


### Chapitre 162 — Tier 0, Tier 1, Tier 2

**Définition.** Modèle de cloisonnement des privilèges d'administration (rappel du chapitre 19, appliqué à AD).

- **Tier 0** : ce qui contrôle l'identité (contrôleurs de domaine, comptes d'admin du domaine, krbtgt, AD CS).
- **Tier 1** : serveurs et applications.
- **Tier 2** : postes de travail.

**Principe.** Étanchéité entre tiers : un identifiant d'un tier ne doit jamais s'exposer sur un tier inférieur. Casser cette règle (un admin du domaine se connectant à un poste) offre à l'attaquant un chemin direct vers le Tier 0.

🧭 **Taxonomie** — Contre-mesure structurante du pass-the-hash, du lateral movement et de l'élévation vers le domaine.

🎯 **À retenir** — Le tiering empêche qu'un poste banal compromis ne mène au contrôle du domaine. C'est l'ossature défensive d'AD.


### Chapitre 163 — Kerberoasting

1. **Définition.** Technique visant à obtenir, puis à casser hors ligne, le secret de *comptes de service* via leurs tickets Kerberos.
2. **Famille.** Credential Access (ATT&CK T1558.003).
3. **Principe.** Tout utilisateur authentifié peut demander un ticket de service pour un compte doté d'un SPN ; ce ticket est chiffré avec une clé dérivée du mot de passe du compte de service. Si ce mot de passe est faible, il peut être retrouvé hors ligne, sans alerter le système.
4. **Sous-types.** Selon l'algorithme de chiffrement et la robustesse du mot de passe ciblé.
5. **Exemple conceptuel.** Un compte de service au mot de passe faible voit son ticket récupéré, puis son secret deviné hors ligne, donnant à l'attaquant ses privilèges.
6. **Impacts.** Compromission de comptes de service (souvent privilégiés), élévation, persistance.
7. **Détection.** Demandes anormales de tickets de service (volume, comptes ciblés), chiffrement faible demandé, surveillance Kerberos.
8. **Prévention.** Mots de passe **longs et aléatoires** pour les comptes de service (idéalement **gMSA** à rotation automatique), moindre privilège, suppression des SPN inutiles, chiffrement fort, surveillance.
9. ⚠️ **Erreur fréquente.** Comptes de service à mot de passe faible et privilèges élevés, jamais changés.
10. 🎯 **À retenir.** Le kerberoasting transforme un compte de service à mot de passe faible en porte d'entrée silencieuse : gMSA et mots de passe forts le neutralisent.


### Chapitre 164 — AS-REP roasting

1. **Définition.** Technique exploitant les comptes dont la *pré-authentification Kerberos est désactivée* pour récupérer un élément cassable hors ligne.
2. **Famille.** Credential Access (ATT&CK T1558.004).
3. **Principe.** Quand la pré-authentification est désactivée pour un compte, on peut obtenir une réponse chiffrée avec une clé dérivée de son mot de passe, puis tenter de retrouver ce dernier hors ligne.
4. **Sous-types.** Selon la robustesse du mot de passe et le compte ciblé.
5. **Exemple conceptuel.** Un compte sans pré-authentification permet de récupérer un matériel chiffré servant à deviner son mot de passe hors ligne.
6. **Impacts.** Compromission de comptes, élévation, persistance.
7. **Détection.** Comptes sans pré-authentification (audit), demandes anormales, surveillance Kerberos.
8. **Prévention.** **Activer la pré-authentification** pour tous les comptes, mots de passe forts, audit régulier de cette propriété, surveillance.
9. ⚠️ **Erreur fréquente.** Laisser des comptes hérités avec pré-authentification désactivée.
10. 🎯 **À retenir.** Désactiver la pré-authentification crée une faiblesse cassable hors ligne : auditer et réactiver la pré-auth partout.


### Chapitre 165 — Password spraying

1. **Définition.** Tester *quelques* mots de passe courants contre *de nombreux* comptes, pour éviter les verrouillages.
2. **Famille.** Credential Access (ATT&CK T1110.003).
3. **Principe.** Au lieu d'essayer beaucoup de mots de passe sur un compte (brute force, qui verrouille), on essaie un mot de passe probable sur tous les comptes, puis on recommence lentement — discret et efficace contre les politiques faibles.
4. **Sous-types.** Spraying lent/distribué, ciblé sur des services exposés (VPN, messagerie cloud, RDP).
5. **Exemple conceptuel.** Un mot de passe saisonnier courant est testé une fois sur l'ensemble des comptes de l'organisation.
6. **Impacts.** Compromission de comptes faibles, accès initial, point de départ d'une intrusion.
7. **Détection.** Nombreux comptes avec un échec quasi simultané, schémas distribués, pics d'authentification, surveillance.
8. **Prévention.** **MFA** (parade principale), mots de passe robustes/bannissement des mots de passe courants, détection de spraying, verrouillage intelligent, surveillance des services exposés.
9. ⚠️ **Erreur fréquente.** Se fier au seul verrouillage de compte (contourné par le spraying) sans MFA ni détection.
10. 🎯 **À retenir.** Le spraying contourne les verrouillages classiques ; le MFA et la détection des schémas distribués sont les vraies parades.


### Chapitre 166 — Brute force

1. **Définition.** Essayer systématiquement de nombreuses combinaisons pour deviner un secret (mot de passe, clé, PIN).
2. **Famille.** Credential Access (ATT&CK T1110).
3. **Principe.** Par essais répétés (en ligne ou hors ligne sur des condensats volés), on finit par trouver un secret faible. La robustesse du secret et la limitation des essais déterminent la faisabilité.
4. **Sous-types.** Brute force en ligne (contre un service), hors ligne (sur des hash volés), par dictionnaire, ciblé.
5. **Exemple conceptuel.** Un service sans limitation d'essais permet de tester un très grand nombre de mots de passe jusqu'à succès.
6. **Impacts.** Compromission de comptes, accès non autorisé.
7. **Détection.** Pics d'échecs d'authentification, essais répétés, surveillance, alertes de verrouillage.
8. **Prévention.** **Limitation/verrouillage**, MFA, mots de passe forts, hachage lent et salé (contre le hors ligne), CAPTCHA ciblé, surveillance.
9. ⚠️ **Erreur fréquente.** Hacher les mots de passe avec un algorithme rapide (facilite le brute force hors ligne) au lieu d'un algorithme lent dédié.
10. 🎯 **À retenir.** Le brute force réussit contre les secrets faibles et les services non limités : robustesse + limitation + MFA + hachage lent.


### Chapitre 167 — Credential stuffing

1. **Définition.** Réutiliser des identifiants volés ailleurs (fuites) pour se connecter, en pariant sur la *réutilisation de mots de passe*.
2. **Famille.** Credential Access (ATT&CK T1110.004).
3. **Principe.** D'immenses listes d'identifiants issus de fuites sont testées automatiquement ; les utilisateurs réutilisant leurs mots de passe sont compromis sans aucun « cassage ».
4. **Sous-types.** Stuffing distribué, ciblé sur des services grand public, combiné à la rotation d'IP (contre la limitation).
5. **Exemple conceptuel.** Des couples identifiant/mot de passe d'une fuite tierce sont essayés massivement contre un service.
6. **Impacts.** Prise de comptes en masse, fraude, accès initial.
7. **Détection.** Pics de connexions avec taux d'échec élevé, sources distribuées, identifiants connus comme compromis, surveillance.
8. **Prévention.** **MFA**, détection des identifiants compromis (bannissement), limitation, unicité des mots de passe (gestionnaires), surveillance comportementale.
9. ⚠️ **Erreur fréquente.** Compter sur la « complexité » des mots de passe alors que le problème est leur *réutilisation*.
10. 🎯 **À retenir.** Le stuffing exploite la réutilisation : MFA et détection des identifiants déjà fuités sont déterminants.


### Chapitre 168 — Pass-the-hash

1. **Définition.** S'authentifier en réutilisant le *condensat (hash)* du mot de passe, sans connaître le mot de passe en clair.
2. **Famille.** Lateral Movement / Credential Access (ATT&CK T1550.002).
3. **Principe.** Avec NTLM (chapitre 158), prouver qu'on détient le hash suffit. Un hash volé en mémoire sur une machine permet de s'authentifier ailleurs comme l'utilisateur, sans cassage.
4. **Sous-types.** Selon le compte et la portée (local vs domaine).
5. **Exemple conceptuel.** Un hash récupéré sur un poste est réutilisé pour s'authentifier sur d'autres machines acceptant NTLM.
6. **Impacts.** Mouvement latéral, élévation si le hash est privilégié, propagation.
7. **Détection.** Authentifications NTLM anormales, usage d'un même compte sur de nombreuses machines, EDR, surveillance.
8. **Prévention.** **Tiering** (ne pas exposer de hash privilégiés sur des machines basses), **LAPS** (mots de passe locaux uniques), restriction de NTLM, protection des secrets (Credential Guard), moindre privilège, détection.
9. ⚠️ **Erreur fréquente.** Mots de passe d'administrateur local identiques partout : un hash volé ouvre tout le parc.
10. 🎯 **À retenir.** Pass-the-hash réutilise une preuve sans casser le secret : tiering, LAPS et protection mémoire des secrets sont les parades clés.


### Chapitre 169 — Pass-the-ticket

1. **Définition.** Réutiliser un *ticket Kerberos* volé pour accéder à des ressources sans connaître le mot de passe.
2. **Famille.** Lateral Movement / Credential Access (ATT&CK T1550.003).
3. **Principe.** Un ticket Kerberos (TGT ou TGS) extrait de la mémoire d'une machine peut être réinjecté pour se faire passer pour l'utilisateur jusqu'à son expiration.
4. **Sous-types.** Réutilisation de TGT (accès large) ou de TGS (accès à un service précis).
5. **Exemple conceptuel.** Un ticket récupéré en mémoire est réutilisé pour accéder aux ressources du titulaire.
6. **Impacts.** Mouvement latéral, accès aux ressources, élévation selon le ticket.
7. **Détection.** Usage de tickets depuis des emplacements anormaux, anomalies Kerberos, EDR.
8. **Prévention.** Protection des secrets en mémoire (Credential Guard), tiering, durée de vie des tickets maîtrisée, moindre privilège, détection comportementale.
9. ⚠️ **Erreur fréquente.** Négliger la protection de la mémoire des contrôleurs/serveurs où des tickets précieux résident.
10. 🎯 **À retenir.** Pass-the-ticket réutilise des tickets volés : protéger la mémoire et appliquer le tiering limite le vol et la portée.


### Chapitre 170 — Overpass-the-hash

1. **Définition.** Utiliser un hash NTLM pour obtenir un *ticket Kerberos* légitime, combinant les deux mondes (aussi appelé « pass-the-key »).
2. **Famille.** Credential Access / Lateral Movement (ATT&CK T1550).
3. **Principe.** À partir d'un hash volé, l'attaquant demande un TGT Kerberos valide, obtenant ainsi une authentification Kerberos « propre » sans le mot de passe en clair — plus discret que le NTLM pur.
4. **Sous-types.** Selon la clé utilisée et la portée obtenue.
5. **Exemple conceptuel.** Un hash sert à obtenir un ticket Kerberos, utilisé ensuite comme une authentification normale.
6. **Impacts.** Mouvement latéral plus furtif, accès aux ressources Kerberos.
7. **Détection.** Incohérences entre type d'authentification et contexte, anomalies Kerberos, EDR.
8. **Prévention.** Identiques au pass-the-hash/ticket : tiering, protection mémoire (Credential Guard), LAPS, restriction NTLM, détection.
9. ⚠️ **Erreur fréquente.** Croire que « passer à Kerberos » suffit si les hash restent volables en mémoire.
10. 🎯 **À retenir.** Overpass-the-hash transforme un hash en ticket Kerberos : la protection des secrets en mémoire et le tiering restent les parades.


### Chapitre 171 — Golden ticket

1. **Définition.** Forge d'un *TGT arbitraire* à partir du secret du compte *krbtgt*, donnant un accès quasi total et persistant au domaine.
2. **Famille.** Persistence / Privilege Escalation (ATT&CK T1558.001).
3. **Principe.** Le compte krbtgt signe les TGT ; quiconque détient son secret peut forger des tickets pour n'importe quel utilisateur (y compris administrateur), valides et difficiles à révoquer sans réinitialiser krbtgt (deux fois).
4. **Sous-types.** Selon la portée et la durée forgées.
5. **Exemple conceptuel.** Avec le secret krbtgt, l'attaquant fabrique un ticket d'administrateur du domaine valide longtemps.
6. **Impacts.** Contrôle total et persistant du domaine, persistance majeure, très difficile à éradiquer.
7. **Détection.** Tickets aux propriétés anormales (durées, chiffrement), incohérences, surveillance avancée.
8. **Prévention.** **Protéger krbtgt absolument** (Tier 0), rotation (double) de krbtgt en cas de suspicion, durcissement et surveillance des contrôleurs, limiter l'accès au Tier 0.
9. ⚠️ **Erreur fréquente.** Sous-estimer la criticité de krbtgt et ne jamais prévoir sa rotation après incident.
10. 🎯 **À retenir.** Le golden ticket signifie un domaine entièrement compromis et persistant : la protection de krbtgt et sa rotation post-incident sont vitales.


### Chapitre 172 — Silver ticket

1. **Définition.** Forge d'un *ticket de service (TGS)* pour un service précis, à partir du secret de ce service, sans passer par le KDC.
2. **Famille.** Persistence / Lateral Movement (ATT&CK T1558.002).
3. **Principe.** Plus ciblé que le golden ticket : avec le secret d'un compte de service, l'attaquant forge des accès à *ce* service, plus furtivement (le contrôleur n'est pas sollicité).
4. **Sous-types.** Selon le service ciblé.
5. **Exemple conceptuel.** Le secret d'un service permet de forger un accès direct à ce service, sans interaction avec le contrôleur de domaine.
6. **Impacts.** Accès persistant et furtif à un service, mouvement latéral ciblé.
7. **Détection.** Plus difficile (pas de trace côté KDC) ; surveillance des accès de service incohérents, anomalies.
8. **Prévention.** Mots de passe forts/gMSA pour les comptes de service, rotation, moindre privilège, surveillance des services, durcissement.
9. ⚠️ **Erreur fréquente.** Comptes de service à secret faible/statique, permettant la forge silencieuse de tickets.
10. 🎯 **À retenir.** Le silver ticket forge des accès furtifs à un service : protéger et faire tourner les secrets de service (gMSA) est la parade.


### Chapitre 173 — DCSync

1. **Définition.** Abus consistant à se faire passer pour un contrôleur de domaine afin de *demander la réplication* des secrets de l'annuaire (dont les condensats des comptes).
2. **Famille.** Credential Access (ATT&CK T1003.006).
3. **Principe.** Un compte disposant de droits de réplication peut demander à un contrôleur de lui « répliquer » des secrets, comme le ferait un autre contrôleur — extrayant ainsi des hash sensibles (y compris krbtgt).
4. **Sous-types.** Selon les comptes/secrets ciblés.
5. **Exemple conceptuel.** Un compte aux droits de réplication récupère les condensats de comptes privilégiés via le mécanisme de réplication.
6. **Impacts.** Vol des secrets du domaine, préparation de golden ticket, compromission totale.
7. **Détection.** Demandes de réplication provenant d'hôtes non-contrôleurs, surveillance des droits de réplication et des événements associés.
8. **Prévention.** **Restreindre strictement les droits de réplication** (Tier 0), surveiller leur attribution, durcissement des contrôleurs, détection des réplications anormales.
9. ⚠️ **Erreur fréquente.** Droits de réplication accordés trop largement ou non surveillés.
10. 🎯 **À retenir.** DCSync extrait les secrets du domaine en imitant un contrôleur : verrouiller et surveiller les droits de réplication est essentiel.


### Chapitre 174 — DCShadow

1. **Définition.** Abus enregistrant un *faux contrôleur de domaine* pour injecter des modifications dans l'annuaire de façon furtive.
2. **Famille.** Persistence / Defense Evasion (ATT&CK T1207).
3. **Principe.** En se faisant passer pour un contrôleur légitime, l'attaquant pousse des modifications (ajout de droits, portes dérobées) via la réplication, contournant une partie de la journalisation classique.
4. **Sous-types.** Selon les modifications injectées (persistance, élévation).
5. **Exemple conceptuel.** Une modification malveillante de l'annuaire est introduite via un mécanisme de réplication, en imitant un contrôleur.
6. **Impacts.** Persistance furtive, élévation, altération de l'annuaire difficile à repérer.
7. **Détection.** Apparition d'objets contrôleurs inattendus, réplications anormales, surveillance avancée d'AD.
8. **Prévention.** Restreindre qui peut enregistrer/agir comme contrôleur (Tier 0), surveillance fine de la réplication et du schéma, durcissement, détection spécialisée.
9. ⚠️ **Erreur fréquente.** Ne surveiller que les journaux classiques, que DCShadow contourne partiellement.
10. 🎯 **À retenir.** DCShadow injecte des changements en imitant un contrôleur : seule une surveillance avancée de la réplication le détecte.


### Chapitre 175 — Delegation abuse (délégation Kerberos)

1. **Définition.** Abus des mécanismes de *délégation Kerberos*, qui permettent à un service d'agir au nom d'un utilisateur.
2. **Famille.** Privilege Escalation / Lateral Movement.
3. **Principe.** La délégation autorise un service à réutiliser l'identité d'un utilisateur pour accéder à d'autres ressources. Mal configurée (surtout la délégation *non contrainte*), elle permet à un attaquant contrôlant ce service d'usurper des utilisateurs privilégiés.
4. **Sous-types.** Délégation non contrainte (la plus dangereuse), contrainte, et RBCD (chapitre 176).
5. **Exemple conceptuel.** Un service avec délégation non contrainte capte des tickets d'utilisateurs privilégiés s'y connectant, permettant leur usurpation.
6. **Impacts.** Usurpation d'identités privilégiées, élévation, mouvement latéral.
7. **Détection.** Audit des configurations de délégation, comptes à délégation non contrainte, anomalies Kerberos.
8. **Prévention.** **Supprimer la délégation non contrainte**, préférer la délégation contrainte/RBCD maîtrisée, marquer les comptes sensibles comme non délégables, audit régulier, Tier 0.
9. ⚠️ **Erreur fréquente.** Laisser des serveurs en délégation non contrainte (configuration historique très risquée).
10. 🎯 **À retenir.** La délégation non contrainte est une bombe à retardement : l'éliminer et protéger les comptes sensibles de la délégation est prioritaire.


### Chapitre 176 — RBCD (Resource-Based Constrained Delegation abuse)

1. **Définition.** Abus de la *délégation contrainte basée sur les ressources*, où la configuration de délégation est portée par l'objet ressource.
2. **Famille.** Privilege Escalation / Lateral Movement.
3. **Principe.** Si un attaquant peut modifier l'attribut de délégation d'un objet (via un droit d'écriture mal maîtrisé), il peut se configurer pour usurper des utilisateurs sur cette ressource, élevant ses privilèges.
4. **Sous-types.** Selon l'objet et les droits d'écriture exploités.
5. **Exemple conceptuel.** Un droit d'écriture sur un objet machine est exploité pour configurer une délégation autorisant l'usurpation d'un compte privilégié sur cette machine.
6. **Impacts.** Élévation de privilèges, usurpation, prise de contrôle de ressources.
7. **Détection.** Modifications anormales des attributs de délégation, surveillance des ACL et des écritures sur objets, anomalies Kerberos.
8. **Prévention.** Contrôler strictement les **droits d'écriture** sur les objets (ACL), surveiller les attributs de délégation, durcissement, moindre privilège, Tier 0.
9. ⚠️ **Erreur fréquente.** Droits d'écriture sur des objets machine/compte accordés trop largement.
10. 🎯 **À retenir.** RBCD transforme un droit d'écriture mal placé en élévation : la maîtrise des ACL et la surveillance des attributs de délégation sont clés.


### Chapitre 177 — GPO abuse

1. **Définition.** Abus des *stratégies de groupe* (GPO) pour déployer des configurations/actions malveillantes à grande échelle.
2. **Famille.** Privilege Escalation / Lateral Movement / Persistence.
3. **Principe.** Les GPO s'appliquent massivement aux objets liés. Un attaquant pouvant *modifier* une GPO (ou la lier à une OU) peut pousser des actions malveillantes (tâches, scripts, paramètres) sur de nombreuses machines/utilisateurs.
4. **Sous-types.** Modification de GPO existante, liaison d'une GPO à une OU, abus de droits sur les GPO.
5. **Exemple conceptuel.** Une GPO modifiable est détournée pour déployer une configuration affaiblissant la sécurité sur tout un périmètre.
6. **Impacts.** Compromission massive, élévation, persistance, désactivation de défenses.
7. **Détection.** Modifications de GPO inattendues, changements de liaison, surveillance des droits sur les GPO et des journaux.
8. **Prévention.** Restreindre et **surveiller les droits de modification des GPO**, contrôle de version/validation des changements, moindre privilège, Tier 0, audit.
9. ⚠️ **Erreur fréquente.** Droits de modification de GPO accordés trop largement, sans surveillance.
10. 🎯 **À retenir.** Une GPO est un levier de déploiement de masse : qui peut la modifier peut compromettre largement. Restreindre et surveiller ces droits.


### Chapitre 178 — ACL abuse

1. **Définition.** Exploitation de *droits d'accès mal configurés* sur les objets de l'annuaire pour élever ses privilèges via des chaînes de permissions.
2. **Famille.** Privilege Escalation (cœur des « chemins d'attaque » AD).
3. **Principe.** AD est un graphe de permissions ; certains droits (réinitialiser un mot de passe, modifier l'appartenance d'un groupe, écrire un attribut) permettent de prendre le contrôle d'autres objets. En enchaînant ces droits, un attaquant trace un *chemin* d'un compte peu privilégié vers l'administration du domaine.
4. **Sous-types.** Droits de réinitialisation de mot de passe, d'écriture d'appartenance de groupe, de propriété d'objet, d'écriture d'attributs sensibles.
5. **Exemple conceptuel.** Un compte a le droit de modifier l'appartenance d'un groupe qui, lui-même, mène par étapes à un groupe privilégié — l'attaquant remonte la chaîne.
6. **Impacts.** Élévation jusqu'au contrôle du domaine, souvent par des chemins invisibles à l'œil nu.
7. **Détection.** Analyse des chemins d'attaque (graphes d'ACL), modifications anormales d'appartenance/d'attributs, surveillance.
8. **Prévention.** **Audit et nettoyage des ACL**, cartographie des chemins d'attaque (outils de graphe), moindre privilège, Tier 0, surveillance des modifications sensibles.
9. ⚠️ **Erreur fréquente.** Délégations d'administration historiques jamais revues, créant des chemins d'élévation cachés.
10. 🎯 **À retenir.** AD est un graphe de droits : l'abus d'ACL relie un compte banal à l'admin du domaine. Cartographier et nettoyer ces chemins est une défense majeure.


### Chapitre 179 — Shadow credentials

1. **Définition.** Technique ajoutant des *informations d'authentification alternatives* (par clé/certificat) à un compte pour s'authentifier comme lui.
2. **Famille.** Credential Access / Persistence.
3. **Principe.** En écrivant sur un attribut d'authentification d'un compte (via un droit mal maîtrisé), l'attaquant y associe une clé qu'il contrôle, lui permettant ensuite de s'authentifier comme ce compte sans son mot de passe.
4. **Sous-types.** Selon le droit d'écriture exploité et le compte ciblé.
5. **Exemple conceptuel.** Une information d'authentification alternative est ajoutée à un compte privilégié, donnant un accès durable à l'attaquant.
6. **Impacts.** Usurpation et persistance, élévation, contournement du changement de mot de passe.
7. **Détection.** Modifications de l'attribut d'authentification, surveillance des écritures sensibles, anomalies.
8. **Prévention.** Restreindre les **droits d'écriture** sur les attributs d'authentification, surveiller ces modifications, durcissement de l'infrastructure de certificats, Tier 0.
9. ⚠️ **Erreur fréquente.** Ne pas surveiller les écritures sur les attributs liés à l'authentification par clé.
10. 🎯 **À retenir.** Les shadow credentials ajoutent une clé d'accès cachée à un compte : surveiller les écritures sur les attributs d'authentification est la parade.


### Chapitre 180 — AD CS abuse

1. **Définition.** Abus des *services de certificats d'Active Directory* (PKI interne) pour obtenir des certificats permettant l'usurpation ou l'élévation.
2. **Famille.** Privilege Escalation / Persistence / Credential Access.
3. **Principe.** Une autorité de certification interne mal configurée (modèles de certificats trop permissifs, droits d'inscription larges) peut être amenée à délivrer des certificats permettant de s'authentifier comme un autre utilisateur, y compris privilégié.
4. **Sous-types.** Modèles de certificats vulnérables, droits d'inscription/gestion abusés, persistance via certificats à longue durée.
5. **Exemple conceptuel.** Un modèle de certificat permissif permet d'obtenir un certificat au nom d'un compte privilégié, utilisé ensuite pour s'authentifier comme lui.
6. **Impacts.** Élévation jusqu'au domaine, persistance durable (certificats peu révoqués), usurpation.
7. **Détection.** Inscriptions de certificats anormales, audit des modèles et des droits, surveillance de la CA.
8. **Prévention.** **Durcir les modèles de certificats** et les droits d'inscription, traiter l'AD CS comme du **Tier 0**, audit régulier, surveillance, révocation/rotation.
9. ⚠️ **Erreur fréquente.** Modèles de certificats permissifs et CA non considérée comme un actif Tier 0.
10. 🎯 **À retenir.** L'AD CS mal configuré offre des chemins d'élévation et de persistance puissants : durcir les modèles et protéger la CA comme un joyau (Tier 0).


### Chapitre 181 — Credential dumping

1. **Définition.** Extraction d'identifiants (hash, tickets, mots de passe en mémoire, secrets stockés) depuis un système compromis.
2. **Famille.** Credential Access (ATT&CK T1003) — alimente la plupart des techniques précédentes.
3. **Principe.** Sur une machine contrôlée, l'attaquant récupère les secrets présents en mémoire, dans les bases de comptes locales, ou dans des stockages applicatifs, pour alimenter pass-the-hash/ticket, lateral movement et élévation.
4. **Sous-types.** Extraction mémoire de secrets, extraction de la base de comptes locale, vol de tickets, secrets d'applications/navigateurs.
5. **Exemple conceptuel.** Sur un poste compromis, des secrets résidant en mémoire sont récupérés pour rebondir vers d'autres systèmes.
6. **Impacts.** Carburant du mouvement latéral et de l'élévation ; souvent l'étape pivot d'une intrusion.
7. **Détection.** Accès anormaux aux processus/mémoire sensibles, alertes EDR, comportements de collecte d'identifiants.
8. **Prévention.** **Protection des secrets en mémoire** (Credential Guard), EDR, moindre privilège (pas d'admin local), tiering (limiter les secrets exposés), LAPS, durcissement, surveillance.
9. ⚠️ **Erreur fréquente.** Laisser des secrets privilégiés résider sur des machines peu protégées (violation du tiering).
10. 🎯 **À retenir.** Le credential dumping alimente presque toutes les attaques AD : protéger la mémoire, appliquer le tiering et l'EDR coupe le carburant.


### Chapitre 182 — Lateral movement en environnement Windows

1. **Définition.** Application concrète du mouvement latéral (chapitre 144) dans un parc Windows/AD, combinant les techniques précédentes.
2. **Famille.** Lateral Movement (ATT&CK).
3. **Principe.** Après l'accès initial, l'attaquant enchaîne credential dumping → réutilisation (pass-the-hash/ticket) → abus de services d'administration (SMB/RDP/WinRM) → progression vers le Tier 0, jusqu'au contrôle du domaine.
4. **Sous-types.** Via partages/SMB, via RDP, via exécution distante (WinRM/tâches), via outils d'administration légitimes (living-off-the-land).
5. **Exemple conceptuel.** Des identifiants récupérés sur un poste permettent d'atteindre un serveur, d'y récupérer d'autres secrets, puis de viser un contrôleur de domaine.
6. **Impacts.** Compromission progressive jusqu'au domaine, préalable au ransomware et à l'exfiltration.
7. **Détection.** Connexions inter-machines anormales, usage atypique de comptes d'administration et d'outils légitimes, corrélation SIEM, EDR/NDR.
8. **Prévention.** **Tiering**, segmentation, LAPS, moindre privilège, MFA pour l'administration, bastion/PAM, durcissement, détection comportementale.
9. ⚠️ **Erreur fréquente.** Réutilisation de comptes d'administration sur tous les tiers, mots de passe locaux identiques, absence de segmentation.
10. 🎯 **À retenir.** Le lateral movement Windows est la « colonne vertébrale » des intrusions AD : tiering + LAPS + segmentation + détection le rendent lent et bruyant.


### Chapitre 183 — PAM, bastion et modèle tiering (synthèse défensive AD)

**Définition.** Récapitulatif des défenses structurantes de l'identité : gestion des accès privilégiés (PAM), bastion d'administration, et tiering.

**Principe.** Ces trois éléments, combinés, brisent les chemins d'attaque AD :

- le **tiering** empêche l'exposition de secrets privilégiés sur des machines peu fiables ;
- le **bastion** canalise et journalise tous les accès d'administration via un point durci ;
- le **PAM** supprime les secrets permanents (coffre-fort, accès just-in-time, rotation, enregistrement de session).

À cela s'ajoutent LAPS (mots de passe locaux uniques), MFA pour l'administration, Credential Guard (protection mémoire), audit des ACL/délégations/GPO, et surveillance comportementale.

🧭 **Taxonomie** — Ce chapitre relie toutes les attaques de la Partie 8 à leur antidote commun : casser la *réutilisation* et l'*exposition* des secrets privilégiés.

⚠️ **Erreur fréquente** — Déployer des outils PAM tout en laissant subsister des accès directs « de secours » non contrôlés qui contournent le dispositif.

🎯 **À retenir** — La défense de l'identité tient en une idée : *empêcher l'exposition et la réutilisation des secrets privilégiés*. Tiering + bastion + PAM + LAPS + MFA + surveillance forment le socle.

---

> **Fin du Volume 5/8.**
>
> Vous disposez d'une taxonomie des attaques d'identité (obtenir → réutiliser → forger → abuser des relations → atteindre le cœur → se déplacer) et de leur antidote commun (tiering, PAM/bastion, LAPS, protection mémoire, audit des ACL/délégations/GPO, surveillance).
>
> **Suite — Volume 6 : Partie 9, Malware, phishing et attaques client-side** (classification des malwares : virus, ver, trojan, ransomware, wiper, spyware, infostealer, RAT, backdoor, loader/dropper/downloader, rootkit/bootkit, fileless, macro, LOLBins ; et l'ingénierie sociale : phishing, spear phishing, whaling, smishing, vishing, quishing, BEC, malspam, drive-by, malvertising, SEO poisoning, watering hole, MFA fatigue, consent phishing).


---


## Taxonomie de la cybersécurité — Volume 6/8

> Partie 9 : Malware, phishing et attaques client-side
>
> Cette partie classe deux grandes familles : les **logiciels malveillants** (par fonction et par comportement) et l'**ingénierie sociale** (par canal et par cible). Le point commun : l'humain et le poste (chapitres 40, 59) sont les portes d'entrée. Format en 10 points pour les attaques majeures, format compact pour les variantes.
>
> **Posture** : on décrit la *fonction*, les *impacts*, la *détection* et la *défense* — jamais comment créer un malware ni conduire une campagne offensive.

---
