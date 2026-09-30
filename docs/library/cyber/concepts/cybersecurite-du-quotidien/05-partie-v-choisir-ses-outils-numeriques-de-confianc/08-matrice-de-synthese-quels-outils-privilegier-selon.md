---
title: Matrice de synthèse — Quels outils privilégier selon le contexte
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie V — Choisir ses outils numériques DE confiance
  - index.md
---

*Ce tableau récapitule les options évoquées dans la Partie V. Il n'est pas exhaustif, ne prétend pas qualifier les outils dans l'absolu, et ne remplace pas la politique de votre organisation. Il sert de boussole : « pour ce besoin, dans ce contexte, vers quoi regarder ? ».*

| Besoin | Usage courant grand public | Sensible (particulier) | Pro / institutionnel sensible |
|--------|----------------------------|------------------------|-------------------------------|
| **Visioconférence** | Zoom, Meet, Teams, FaceTime | Outil grand public + bons réglages | **Visio de l'État / Webconférence de l'État** (DINUM) ; **Tixeo** pour le très sensible (solution certifiée CSPN ; offre TixeoPrivateCloud sur hébergement qualifié SecNumCloud) |
| **Messagerie instantanée** | iMessage, WhatsApp | **Signal**, **Olvid** | **Tchap** (agents publics), **Olvid** pour échanges très sensibles ou réduction des métadonnées |
| **Transfert de fichiers** | WeTransfer, lien Drive public | **Proton Drive**, **Tresorit**, ou Cryptomator + cloud | **France Transfert** + **Zed!** (chiffrer avant d'envoyer), **Oodrive**, **BlueFiles** selon contexte |
| **Conteneur chiffré** | ZIP avec mot de passe | **Cryptomator** (cloud personnel), **VeraCrypt** | **Zed!** (PRIM'X — certifié ANSSI sur versions/périmètres), **Cryptomator**, VeraCrypt |
| **Cloud / stockage** | iCloud, Google Drive, OneDrive perso | Cloud perso bien configuré + Cryptomator pour les documents très sensibles | Cloud d'entreprise ou solution **SecNumCloud** (Outscale, Oodrive, NumSpot, S3NS selon contexte) |
| **IA (résumer, traduire, reformuler)** | ChatGPT, Claude, Gemini grand public | IA locale (Mistral/Llama via Ollama), anonymisation forte, **Lumo** (Proton) pour cloud orienté vie privée | IA d'entreprise validée avec DPA et non-rétention ; côté État : **Albert** (Etalab) et IA de La Suite numérique quand disponibles |
| **Authentification forte** | Code SMS | Application TOTP (Aegis, 2FAS, Ente Auth, Proton Authenticator, Authy), passkeys | TOTP + clé physique (YubiKey, SoloKey) sur les comptes critiques |
| **Coffre-fort de mots de passe** | Gestionnaire intégré OS | Bitwarden, 1Password, KeePassXC | Gestionnaire validé par l'organisation, idéalement avec partages d'équipe contrôlés |

**Trois rappels pour bien lire ce tableau** :

1. *Le bon outil dépend du niveau de sensibilité.* Un même contenu peut basculer d'une catégorie à l'autre selon le contexte (un échange entre amis devient sensible si on partage un RIB).
2. *Le canal transporte. Le conteneur protège.* Combiner France Transfert (canal souverain) avec Zed! (conteneur chiffré) donne une défense en profondeur — si l'un fuite, l'autre tient.
3. *Une certification ANSSI (CSPN, qualification Élémentaire / Standard / Renforcée, qualification SecNumCloud) porte sur une version, une configuration et un périmètre précis.* C'est un signal fort de sérieux, mais ce n'est ni une garantie absolue ni une recommandation universelle. Toujours respecter la politique de l'organisation et vérifier que la version utilisée est bien celle qui est qualifiée.

---

> ### 🟦 Réflexes — Fin de Partie V
>
> **À configurer** :
> - Outil de visio adapté à chaque cadre (perso / pro / institutionnel) ; pour le très sensible : **Tixeo** ou solution équivalente certifiée, qualifiée ou validée par l'organisation selon le périmètre d'usage
> - **Signal** ou **Olvid** pour les conversations privées sensibles ; **Tchap** si agent public ; **Olvid** pour les échanges très sensibles ou nécessitant une réduction forte des métadonnées
> - Partages cloud nominatifs avec durée d'expiration, pas de lien public permanent
> - **Conteneur chiffré** pour envoyer des fichiers sensibles : **Zed!** côté pro/institutionnel, **Cryptomator** côté particulier
> - Gestionnaire de mots de passe en place avec mot de passe maître unique mémorisé
> - Codes de récupération MFA imprimés en lieu sûr
>
> **À éviter** :
> - Outil grand public par défaut quand un outil institutionnel ou validé existe
> - Lien « toute personne ayant le lien » pour des documents sensibles
> - Documents pro dans un cloud / une messagerie / une IA personnels
> - Données régulées dans une IA grand public
> - Stockage exclusif des codes de récupération dans le téléphone ou dans le seul cloud
>
> **À vérifier** :
> - Liste des partages cloud actifs (semestriel) — révoquer ce qui n'est plus utile
> - Outils utilisés au quotidien : sont-ils adaptés au niveau de sensibilité ?
> - Pour les agents publics : connaissance et activation des outils institutionnels disponibles
> - Présence d'au moins une clé physique de secours pour les comptes critiques (si cette voie est choisie)
>
> **Si quelque chose arrive** :
> - Document sensible déposé par erreur dans un outil public → supprimer la conversation, désactiver la rétention pour entraînement si possible, signaler à la DSI/RSSI si pertinent (cf. Annexe I)
> - Lien de partage qui a fuité → révoquer immédiatement, créer un nouveau lien nominatif si besoin
> - Perte de clé physique sans secours → utiliser les codes de récupération, recréer un MFA, racheter une nouvelle clé immédiatement

---
