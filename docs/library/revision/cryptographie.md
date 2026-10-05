---
title: Révision — Cryptographie
revision: cyber/cryptographie
domaine: Cyber
sources:
- Révision/Cryptographie — questions de révision.md
---

## Questions essentielles

- **Question :** Quelle est la différence entre encodage, chiffrement et hachage ?
    - **Réponse type :** L'encodage transforme le format sans sécurité — Base64 est réversible sans clé, c'est du transport. Le chiffrement protège la confidentialité — c'est réversible uniquement avec la clé (AES, RSA). Le hachage produit une empreinte irréversible — on ne peut pas retrouver l'entrée à partir du hash (SHA-256, bcrypt). En entretien, ne jamais dire que Base64 est du chiffrement, et ne jamais dire qu'il faut "chiffrer" les mots de passe — il faut les hasher.

- **Question :** Expliquez le mécanisme hybride asymétrique + symétrique.
    - **Réponse type :** L'asymétrique est lent mais résout le problème de l'échange de clés. Le symétrique est rapide mais nécessite une clé partagée. En pratique, on combine les deux : l'asymétrique (ou Diffie-Hellman) sert uniquement à échanger une clé symétrique éphémère, puis le symétrique fait le gros du travail pour chiffrer le trafic. C'est le modèle de TLS, SSH, et GPG.

- **Question :** C'est quoi la Forward Secrecy et pourquoi c'est important ?
    - **Réponse type :** Avec ECDHE, les clés d'échange sont éphémères — générées pour chaque session et détruites après. Même si la clé privée du serveur est compromise dans le futur, les sessions passées restent protégées car la clé de session n'a jamais été transmise, elle a été calculée indépendamment de chaque côté. Sans Forward Secrecy (ancien RSA key exchange), un attaquant qui enregistre le trafic et vole la clé privée plus tard peut tout déchiffrer rétroactivement.

- **Question :** Comment doit-on stocker des mots de passe ?
    - **Réponse type :** Avec un algorithme de hachage conçu pour les mots de passe : Argon2id en priorité, sinon bcrypt ou scrypt. Chaque mot de passe a un salt unique — une valeur aléatoire ajoutée avant le hachage pour empêcher les rainbow tables. Le salt est stocké en clair à côté du hash, ce n'est pas un secret. En complément, un pepper (secret serveur stocké séparément de la base) ajoute une couche supplémentaire. Jamais de MD5 ou SHA-256 brut pour les mots de passe — ils sont trop rapides et vulnérables au brute force GPU.

- **Question :** Expliquez la chaîne de confiance TLS.
    - **Réponse type :** Le certificat du site est signé par une CA intermédiaire, elle-même signée par une CA racine. La CA racine est préinstallée dans le trust store du navigateur ou de l'OS. Le navigateur vérifie la chaîne : le certificat est-il valide, non expiré, le domaine correspond-il au SAN, la CA est-elle de confiance. Si la chaîne est brisée ou le certificat invalide, le navigateur affiche un avertissement — un possible MITM.

## Questions complémentaires

- **Question :** Pourquoi ECB est-il dangereux et quel mode utiliser ?
    - **Réponse type :** ECB chiffre chaque bloc indépendamment — deux blocs identiques en clair donnent deux blocs identiques en chiffré, donc les patterns sont visibles (l'exemple classique c'est le pingouin). Le mode recommandé c'est AES-GCM : c'est un mode AEAD qui fournit confidentialité, intégrité et authenticité en une seule opération, et c'est le standard de TLS 1.3.

- **Question :** C'est quoi un HMAC et quelle est la différence avec un hash simple ?
    - **Réponse type :** Un hash simple vérifie l'intégrité — le fichier n'a pas été modifié. Mais n'importe qui peut calculer un hash. Un HMAC (Hash-based Message Authentication Code) utilise une clé secrète : seul celui qui a la clé peut produire et vérifier un HMAC valide. Ça ajoute l'authenticité à l'intégrité — on sait non seulement que le message n'a pas été modifié, mais aussi qu'il vient de quelqu'un qui possède la clé.

## Questions les plus probables en entretien

1. Encodage vs chiffrement vs hachage ?
2. Mécanisme hybride (asymétrique + symétrique) ?
3. Forward Secrecy : c'est quoi, pourquoi ?
4. Comment stocker les mots de passe ?
5. Chaîne de confiance TLS ?
6. AES-GCM vs AES-CBC ?

## Réponses flash

- **Triade** → Encodage (réversible sans clé, pas de sécurité). Chiffrement (réversible avec clé). Hachage (irréversible).
- **Hybride** → Asymétrique = échange de clé. Symétrique = chiffrement du trafic. Modèle TLS/SSH/GPG.
- **Forward Secrecy** → ECDHE, clés éphémères, calculées pas transmises. Compromise future ≠ déchiffrement du passé.
- **Mots de passe** → Argon2id/bcrypt + salt unique. Jamais MD5/SHA brut. Pepper en complément.
- **TLS** → Certificat → CA intermédiaire → CA racine (trust store). Vérifier validité, domaine, chaîne.
- **GCM vs CBC** → GCM = AEAD (confidentialité + intégrité + authenticité). CBC = confidentialité seule, vulnérable aux padding oracle.
- **HMAC vs hash** → Hash = intégrité seule. HMAC = intégrité + authenticité (clé secrète).

---
