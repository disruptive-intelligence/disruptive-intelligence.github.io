---
title: Chapitre 34 — Métadonnées, contexte et fuite involontaire
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie VI — VIE privée, images, documents ET surexposition
  - index.md
---

*Ce que le fichier dit de vous sans que vous le sachiez.*

Les **EXIF** des photos : coordonnées GPS (l'endroit exact où la photo a été prise — latitude/longitude au mètre près), date et heure, modèle de l'appareil, parfois le nom du propriétaire. La plupart des réseaux sociaux suppriment les EXIF au upload (Facebook, Instagram, Twitter) — mais l'envoi par email, par messagerie en mode « document » (WhatsApp permet d'envoyer des photos en pièce jointe/document, ce qui conserve les EXIF), ou par partage de fichier (Google Drive, WeTransfer) les conserve.

Les **métadonnées des documents** : un fichier Word contient le nom de l'auteur, l'organisation, la date de création, l'historique des modifications, et parfois les commentaires et les révisions « supprimées » (qui sont en réalité masquées mais toujours présentes dans le fichier). Un PDF peut contenir l'historique des annotations, le nom du logiciel qui l'a créé, et des calques masqués. Un document envoyé à un tiers peut contenir des informations non visibles dans le texte mais lisibles dans les propriétés du fichier ou en retirant le masquage.

Les **données de contexte** : une photo d'intérieur révèle le niveau de vie, les habitudes, les équipements. Une capture d'écran révèle les applications installées, l'heure, le réseau Wi-Fi, le niveau de batterie, et les notifications (un SMS bancaire, un message WhatsApp, un rappel de rendez-vous). Un document mal anonymisé révèle les noms sous le « caviardage » si celui-ci est fait en superposition (un rectangle noir sur le texte) plutôt qu'en suppression réelle (le texte sous le rectangle est toujours là et peut être copié-collé ou extrait).

Le nettoyage : avant d'envoyer un fichier sensible, supprimer les métadonnées (Windows : clic droit > Propriétés > Détails > Supprimer les propriétés et informations personnelles ; macOS : Aperçu > Outils > Inspecteur). Pour les photos : les repartager via un réseau social qui supprime les EXIF, ou utiliser un outil de suppression. Pour les PDF : vérifier que le caviardage est un vrai masquage — le texte a été supprimé, pas juste recouvert.

---

> ### 🟦 Réflexes — Fin de Partie VI
>
> **À configurer** :
> - Profils réseaux sociaux en privé par défaut, géolocalisation désactivée
> - Comptes des fournisseurs d'identité utilisés via FranceConnect (Ameli, impots, La Poste, etc.) sécurisés avec mot de passe unique et authentification renforcée quand disponible
> - France Identité activé si CNI électronique
> - Mon espace santé vérifié et sécurisé
> - Notifications de remboursement Ameli activées (détection d'usurpation médicale)
>
> **À éviter** :
> - Photo de CNI / passeport / permis envoyée par email ou messagerie non chiffrée
> - Boarding pass, badge, RIB, ordonnance visibles sur une photo postée en ligne
> - Caviardage en superposition (rectangle noir) sur PDF — c'est lisible
> - Cliquer sur les liens des emails/SMS « impôts/Ameli/CAF/ANTS »
> - Coller des analyses ou ordonnances dans une IA grand public
>
> **À vérifier** :
> - Connexions récentes sur FranceConnect (page dédiée sur franceconnect.gouv.fr)
> - Liste des soins/remboursements sur Ameli (toutes les semaines)
> - Métadonnées avant envoi d'un document sensible (Propriétés > Supprimer)
>
> **Si quelque chose arrive** :
> - Soin/médicament inconnu sur Ameli → signaler à l'Assurance Maladie + plainte
> - Suspicion d'usurpation d'identité → THESEE + renouvellement CNI + Banque de France (FICP)
> - Phishing administratif → Signal Spam / 33700, ne JAMAIS répondre

---
