---
title: Chapitre 9 — Sauvegardes, récupération et comptes de secours
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie II — Fondations : appareils, comptes ET continuité'
  - index.md
---

La **règle 3-2-1 adaptée** au grand public : 3 copies des données critiques, sur 2 supports différents (cloud + disque externe), dont 1 hors ligne (un disque externe débranché de l'ordinateur et du réseau). Les données critiques du particulier : photos irremplaçables (les photos de famille ne se recréent pas), documents d'identité numérisés (CNI, passeport — pour faciliter les démarches en cas de perte ou de vol des originaux), documents administratifs et fiscaux (avis d'imposition, contrats, bulletins de salaire), et la sauvegarde du gestionnaire de mots de passe et des codes de récupération MFA.

Les **codes de récupération** : à chaque activation de MFA, les imprimer ou les noter sur papier, et les stocker dans un lieu sûr (un tiroir à la maison, un coffre, chez un proche de confiance). Ne PAS les stocker uniquement dans le téléphone — c'est le téléphone qu'on perd. Ne PAS les stocker uniquement dans le cloud — c'est le cloud qui est inaccessible si le MFA bloque.

L'**email maître** : l'email principal est le compte le plus critique — c'est lui qui reçoit les réinitialisations de mot de passe de tous les autres comptes. Il doit avoir le mot de passe le plus fort (unique, long, stocké dans le gestionnaire), le MFA le plus robuste (application TOTP ou clé physique, PAS SMS), et un email de récupération secondaire qui n'est PAS le même email (un second email sur un fournisseur différent — si Gmail est compromis, l'email de récupération chez ProtonMail ou Outlook permet de reprendre le contrôle).

L'**appareil de secours** : avoir un second appareil (un vieux téléphone, une tablette) avec l'app du gestionnaire de mots de passe et les apps d'authentification MFA configurées. En cas de perte du téléphone principal, la reprise est immédiate — pas besoin d'attendre une nouvelle SIM ou de retrouver des codes de récupération.

---

<a id="chapitre-10"></a>
