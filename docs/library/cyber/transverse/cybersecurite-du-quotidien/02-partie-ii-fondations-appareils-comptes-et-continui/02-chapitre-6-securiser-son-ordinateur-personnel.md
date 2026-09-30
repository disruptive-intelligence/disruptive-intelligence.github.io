---
title: Chapitre 6 — Sécuriser son ordinateur personnel
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie II — Fondations : appareils, comptes ET continuité'
  - index.md
---

Le **compte utilisateur** : utiliser un compte standard au quotidien, pas un compte administrateur. Un malware exécuté en admin a le contrôle total de la machine — il peut installer des logiciels, modifier la configuration, accéder à tous les fichiers. En compte standard, ses actions sont limitées. L'administrateur ne sert que pour les installations et les modifications système.

Les **mises à jour** : OS + navigateur + applications. Les mises à jour de l'OS seules ne suffisent pas — le navigateur est l'une des principales surfaces d'attaque (c'est par lui que passent les sites malveillants, les téléchargements, les extensions), et les applications tierces (lecteur PDF, suite bureautique, logiciel de visioconférence) ont aussi des vulnérabilités.

La **protection locale** : Windows Defender (intégré à Windows) est suffisant pour un usage personnel — pas besoin d'acheter une suite de sécurité payante. Sur macOS, Gatekeeper (vérifie la signature des applications) et XProtect (antimalware intégré) couvrent les bases. L'antivirus est un filet de sécurité, pas une protection absolue — il ne bloque pas tout et ne remplace pas les bons réflexes.

Le **chiffrement du disque** : BitLocker sur Windows Pro, FileVault sur macOS. Si l'ordinateur est volé, les données sont illisibles sans le mot de passe de session. Sans chiffrement, un attaquant peut accéder à tous les fichiers en démarrant depuis une clé USB. Le **verrouillage de session** : Win+L sur Windows, Ctrl+Cmd+Q sur macOS — le verrouiller à CHAQUE départ, même pour 2 minutes. Une session ouverte dans un café, une bibliothèque, ou un bureau partagé est une session compromise.

Les **téléchargements** : ne télécharger que depuis les sources officielles ou les stores. Les cracks, les logiciels piratés, et les « versions gratuites » de logiciels payants restent un vecteur majeur d'infection sur PC — le logiciel fonctionne, mais il contient parfois un malware en bonus (keylogger, stealer, ransomware). Les **macros Office** : ne JAMAIS « activer le contenu » dans un document reçu par email, sauf si l'on sait exactement pourquoi et que l'on fait confiance à l'expéditeur. Les macros malveillantes dans les documents Office sont un vecteur d'attaque classique. Les **extensions de navigateur** : chaque extension a accès à tout ce que le navigateur voit — y compris les pages bancaires. Installer le minimum strict, vérifier les permissions, et supprimer celles qu'on n'utilise plus.

---

<a id="chapitre-7"></a>
