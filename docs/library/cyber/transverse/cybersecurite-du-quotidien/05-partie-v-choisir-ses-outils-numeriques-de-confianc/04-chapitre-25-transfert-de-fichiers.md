---
title: Chapitre 25 — Transfert de fichiers
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie V — Choisir ses outils numériques DE confiance
  - index.md
---

éviter les liens publics permanents

*Un lien « toute personne ayant le lien » n'est pas un partage privé. C'est une porte ouverte dont la clé peut être copiée à l'infini.*

## 25.1 Les pièges du transfert facile

WeTransfer, le lien Google Drive « toute personne ayant le lien », l'OneDrive partagé sans expiration, le lien Dropbox copié dans un email — ce sont les outils les plus pratiques et aussi les moins maîtrisés. Le lien fuite (forwardé, intercepté, indexé par un moteur de recherche public, capté dans un journal de proxy), et le contenu reste accessible à toute personne qui a la chaîne.

| Besoin | Mauvais réflexe | Meilleur réflexe |
|--------|-----------------|------------------|
| Envoyer un gros fichier banal à un proche | Lien public sans expiration | Lien temporaire (7-15 jours), mot de passe si possible |
| Envoyer CNI / RIB / document sensible | Pièce jointe email non chiffrée, lien public | Lien nominatif (le destinataire s'authentifie), mot de passe transmis par un autre canal, durée limitée |
| Envoyer un fichier professionnel | Drive perso, WeTransfer perso | Outil de partage de l'entreprise (avec DLP, audit, contrôle d'accès) |
| Agent public, fichier volumineux | Outil externe non validé | **France Transfert** (solution de l'administration) si disponible |

**Note souveraineté** : pour les fichiers volumineux (jusqu'à 20 Go), **France Transfert** permet aux agents de l'État d'envoyer des fichiers, y compris à des destinataires extérieurs, avec mot de passe optionnel et durée de conservation paramétrable. C'est l'alternative institutionnelle aux outils grand public type WeTransfer pour les contextes publics.

**Mais attention à ne pas confondre canal et protection du contenu** : France Transfert est conçu comme un **canal de transport** souverain pour des fichiers volumineux non sensibles. Il ne se substitue pas au chiffrement du contenu lui-même. Pour un fichier sensible, France Transfert seul n'est pas suffisant — le bon réflexe est de **chiffrer d'abord le fichier (par exemple avec Zed!)**, puis de l'envoyer via France Transfert (cf. Ch.25.3). Le canal transporte, le conteneur protège.

## 25.2 Les bons réflexes du partage

- **Lien nominatif** plutôt que « toute personne ayant le lien » (le destinataire doit s'authentifier).
- **Durée d'expiration** courte (7 jours par défaut, prolongeable au besoin).
- **Mot de passe** sur le lien, transmis via un canal différent (le lien par email, le mot de passe par SMS ou en personne).
- **Révocation** possible — connaître la procédure pour désactiver le lien si nécessaire.
- **Ne pas conserver d'historique de partages oubliés** — réviser semestriellement les partages actifs sur le cloud.

## 25.3 Chiffrer avant d'envoyer

Zed!, conteneurs chiffrés et alternatives

*Le canal transporte. Le conteneur protège.* Quand le contenu est sensible et que le canal de transport ne donne pas suffisamment de garanties (ou simplement parce qu'on veut une couche supplémentaire indépendante du canal), la bonne pratique est de **chiffrer le fichier avant l'envoi** dans un conteneur dédié. Le destinataire ouvre le conteneur avec une clé, et le canal — email, France Transfert, clé USB, dépôt cloud — n'a jamais accès au contenu en clair.

**Zed!** est une solution française développée par PRIM'X qui permet de créer des **conteneurs chiffrés `.zed`**. Concrètement, on glisse des fichiers ou des dossiers dans un conteneur, on définit les destinataires (par certificat ou par mot de passe partagé), et on envoie le conteneur via le canal de son choix. Zed! a fait l'objet de **certifications de l'ANSSI** sur des versions et configurations précises ; cette information vaut **selon la version, la configuration et le périmètre évalué** — c'est un gage de sérieux, pas une garantie absolue, et l'usage doit respecter la politique de l'organisation.

Une nuance importante : **Zed! est une « valise chiffrée de transport », pas un coffre-fort numérique probant d'archivage**. Sa vocation est de protéger un envoi (du dépôt jusqu'à l'ouverture par le destinataire), pas de remplacer un coffre-fort numérique au sens du Code civil avec valeur probante d'archivage long terme.

Le **couple Zed! + France Transfert** est particulièrement pertinent dans le secteur public ou pour des échanges sensibles entre organisations : Zed! chiffre le contenu, France Transfert assure le transport. Si l'un fuite, l'autre tient.

| Besoin | Solution |
|--------|----------|
| Envoyer un fichier sensible à un destinataire identifié, contexte pro/institutionnel | **Zed!** (conteneur chiffré) — éventuellement transporté via France Transfert, email, ou clé USB |
| Coffre chiffré synchronisé dans un cloud personnel (iCloud, Google Drive…) | **Cryptomator** (open source, gratuit) |
| Conteneur ou volume chiffré local plus avancé | **VeraCrypt** (open source, plus technique) |
| Protection ponctuelle simple d'un fichier | Archive **ZIP avec mot de passe AES-256** (compatible partout, mais moins professionnel) |

**Note méthodologique** : transmettre la clé/le mot de passe par un canal différent du conteneur. Si vous envoyez le `.zed` par email, le mot de passe se transmet par SMS, par téléphone, ou en personne. Le double canal divise drastiquement le risque.

---

<a id="chapitre-26"></a>
