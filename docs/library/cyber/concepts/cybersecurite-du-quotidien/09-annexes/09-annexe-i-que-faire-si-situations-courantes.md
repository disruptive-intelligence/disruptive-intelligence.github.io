---
title: Annexe I — Que faire si... (situations courantes)
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Annexes
  - index.md
---

*Format ultra court : situation → gravité → actions immédiates. À consulter en cas d'incident, sans relire tout le cours.*

## J'ai cliqué sur un lien suspect mais je n'ai rien saisi
**Gravité : faible.** Un simple clic sur un lien malveillant est rarement suffisant pour compromettre un appareil moderne à jour. **Actions** : fermer l'onglet, ne pas saisir d'identifiant, ne pas télécharger ce qui est proposé. Vérifier l'URL exacte (capture d'écran si signalement). Lancer une analyse antimalware par sécurité. Si vous étiez sur un site bancaire, vérifier les sessions actives et changer le mot de passe par précaution.

## J'ai saisi mon mot de passe sur un site suspect
**Gravité : élevée.** Le mot de passe est probablement compromis. **Actions immédiates** : (1) changer ce mot de passe sur le vrai site, (2) si ce mot de passe était réutilisé ailleurs, le changer partout, (3) activer le MFA si pas déjà fait, (4) vérifier les sessions actives et déconnecter tout, (5) vérifier les paramètres du compte (email de récupération, transferts, filtres ajoutés). Surveiller les jours suivants.

## J'ai donné un code SMS à quelqu'un qui m'appelait
**Gravité : critique.** L'attaquant a très probablement validé une opération frauduleuse à votre place. **Actions immédiates** : (1) appeler la banque sur le vrai numéro pour faire opposition et bloquer toute opération en cours, (2) faire opposition sur la carte, (3) consulter l'historique des opérations et lister les anomalies, (4) déposer plainte (THESEE ou commissariat), (5) contester par écrit auprès de la banque dans les 13 mois (article L133-18 CMF). Conserver tous les éléments.

## J'ai envoyé une photo de ma CNI / passeport
**Gravité : élevée à critique** selon le destinataire. **Actions** : (1) si le destinataire est suspect, déposer plainte pour usurpation d'identité potentielle (THESEE), (2) demander une nouvelle CNI (le numéro change), (3) interroger la Banque de France pour vérifier qu'aucun crédit n'a été souscrit (FICP), (4) surveiller les courriers reçus dans les semaines suivantes (notifications de comptes inconnus, relances), (5) garder une copie de la plainte — elle sera demandée par chaque organisme victime d'usurpation.

## J'ai perdu mon téléphone
**Gravité : élevée si non préparé, faible si préparé.** **Actions immédiates** : (1) bloquer la SIM (numéro opérateur, à noter à l'avance hors du téléphone), (2) localiser et verrouiller/effacer via Find My / Find My Device depuis un autre appareil, (3) changer le mot de passe de l'email maître, (4) révoquer les sessions actives sur les comptes critiques, (5) prévenir la banque, (6) déposer plainte (récépissé pour assurance). Voir Ch.42.

## Je reçois une menace de sextorsion
**Gravité : élevée psychologiquement, faible si on ne paie pas.** **Actions** : (1) ne pas répondre, ne pas payer (les arnaqueurs disparaissent quand ils n'obtiennent rien — payer entraîne plus de demandes), (2) bloquer le contact, (3) conserver toutes les preuves (captures avec URL/identifiant), (4) signaler sur Pharos, (5) plainte au commissariat ou via THESEE, (6) si mineur ou jeune adulte : 3018 (gratuit, anonyme, 7j/7 9h-23h). Si la menace concerne une diffusion, un signalement aux plateformes peut être appuyé par les autorités.

## Une opération bancaire inconnue apparaît sur mon compte
**Gravité : élevée.** **Actions immédiates** : (1) faire opposition sur la carte si carte concernée (numéro au dos de la carte ou app bancaire), (2) contester l'opération par écrit auprès de la banque (délai 13 mois, 70 jours hors EEE), (3) demander un remboursement (article L133-18 CMF), (4) déposer plainte (THESEE), (5) si la banque refuse au motif de « négligence grave », saisir le médiateur bancaire, puis association de consommateurs (UFC-Que Choisir, CLCV).

## Je pense être surveillé(e) par un proche
**Gravité : variable, parfois critique.** **NE PAS AGIR SEULE** si le contexte est violent ou conflictuel — une suppression brutale d'un stalkerware peut déclencher une escalade. **Actions** : (1) si situation de violence : 3919 (Violences Femmes Info, gratuit, anonyme, 24/7 — écoute et orientation, **pas un numéro d'urgence : danger immédiat → 17 ou 112**) ou France Victimes (116 006) pour un protocole de mise en sécurité, (2) sinon, suivre les étapes du Ch.38 (vérifier partages de localisation, sessions actives, profils MDM, trackers Bluetooth), (3) ne pas confronter directement avant d'avoir mis l'essentiel en sécurité.

## J'ai mis un fichier pro / sensible dans une IA publique (ChatGPT, Gemini, etc.)
**Gravité : variable.** Le contenu est potentiellement sorti du périmètre maîtrisé. **Actions** : (1) supprimer la conversation dans l'historique de l'outil (cela ne garantit pas la suppression complète mais limite la visibilité), (2) si l'option « ne pas utiliser pour entraîner les modèles » existe, l'activer pour le compte, (3) signaler à la DSI / RSSI si pertinent (obligation potentielle si données client, données de santé, données régulées), (4) évaluer la nature du contenu — si données très sensibles, considérer l'incident comme une fuite et appliquer la procédure de l'organisation. Voir Ch.27.

## J'ai reçu une notification MFA que je n'ai pas déclenchée
**Gravité : critique.** Quelqu'un essaie d'accéder à votre compte. **Actions immédiates** : (1) **refuser** la notification, (2) changer immédiatement le mot de passe du compte concerné, (3) vérifier les sessions actives, (4) vérifier que le MFA est bien actif, (5) chercher d'où vient la fuite (mot de passe réutilisé compromis ? — vérifier sur Have I Been Pwned).

## Mon SIM ne capte plus subitement et je reçois des SMS de mon opérateur
**Gravité : critique** — possible SIM swap en cours. **Actions immédiates** : (1) appeler l'opérateur depuis un autre téléphone pour bloquer la SIM frauduleuse, (2) prévenir la banque (les comptes liés au numéro sont en danger immédiat), (3) changer les mots de passe critiques depuis un appareil sûr, (4) déposer plainte. Le SIM swap permet à l'attaquant de recevoir vos SMS, donc vos codes MFA SMS — ne plus se reposer dessus.

---

<a id="annexe-j"></a>
