---
title: Partie 5 — HTTPS et TLS
source: IT/Culture/Fiche_How-The-Web-Works.md
note: 'Fonctionnement du web : URL, DNS, HTTPS'
up:
- - 'Fonctionnement du web : URL, DNS, HTTPS'
  - index.md
---

## 14. HTTPS : HTTP dans TLS

### À retenir
HTTPS = HTTP **encapsulé dans TLS**. Port **443**. Le contenu HTTP devient **illisible** sur le réseau.

### Comment ça fonctionne
Avant tout échange HTTP, un **handshake TLS** établit un tunnel chiffré (voir §16). Ensuite, les requêtes/réponses HTTP circulent **à l'intérieur** de ce tunnel. Dans Wireshark, on ne voit plus du HTTP mais du **« TLS Application Data »** (illisible sans la clé).

### Pourquoi c'est important en cyber
HTTPS apporte trois garanties : **confidentialité** (chiffré), **intégrité** (non altéré), **authentification du serveur** (certificat). Un site HTTP qui force HTTPS renvoie souvent une **redirection 301** vers le port 443, suivie du handshake.

### Commandes utiles

```bash
curl -k https://site.local   # désactive la validation du certificat TLS — LAB UNIQUEMENT
```

> `-k` désactive la **validation du certificat TLS** (la connexion reste chiffrée). À utiliser uniquement en lab ou environnement maîtrisé, **jamais en production**.

### Point clé à mémoriser
HTTPS = HTTP dans TLS, port 443. Sur le réseau, on ne voit que du « Application Data » chiffré.

---

## 15. TLS : certificats et chaîne de confiance

### À retenir
Un **certificat TLS** prouve que la **clé publique** appartient bien au domaine demandé.

### Comment ça fonctionne

- Le serveur possède une **clé privée** (secrète) et une **clé publique** (distribuée dans le certificat).
- Le certificat est au format **X.509**.
- Émission : l'admin génère une **CSR** (Certificate Signing Request) → la soumet à une **Autorité de Certification (CA)** → la CA vérifie et **signe** le certificat.
- Le navigateur fait confiance à un certificat si sa CA fait partie des **autorités de confiance** installées (chaîne de confiance).
- Un **certificat autosigné** chiffre, mais **ne prouve pas l'authenticité** (aucun tiers ne le valide) → le navigateur affiche une alerte.

### Pourquoi c'est important en cyber
La chaîne de confiance est ce qui empêche un attaquant de se faire passer pour la banque. Un certificat invalide = **problème d'authenticité**, signal d'un possible MiTM. Let's Encrypt fournit des certificats signés gratuits.

### Point clé à mémoriser
Le certificat lie une clé publique à un domaine, validé par une CA de confiance. Autosigné = chiffré mais non authentifié.

---

## 16. TLS handshake : le process simplifié

### À retenir
Le handshake établit la confiance et un **secret partagé**, puis bascule en chiffrement rapide.

### Comment ça fonctionne

1. **ClientHello** : le client annonce les versions TLS (1.2/1.3) et suites cryptographiques supportées.
2. **ServerHello** : le serveur choisit les paramètres.
3. Le serveur envoie son **certificat** (X.509).
4. Le client **vérifie** : domaine, date de validité, signature, CA de confiance.
5. **Échange de clés** : le client et le serveur établissent un **secret partagé** via un **échange de clés éphémère** (Diffie-Hellman / **ECDHE**), **sans transmettre directement** la clé de session sur le réseau. La clé publique du certificat sert surtout à **authentifier le serveur**.
6. Dérivation d'une **clé de session** symétrique commune à partir de ce secret.
7. **Passage au chiffrement symétrique** (rapide).
8. Les requêtes HTTP circulent ensuite **dans le tunnel TLS**.

### Métaphore
L'**asymétrique** (lent) sert à **établir la confiance et à négocier le secret** ; le **symétrique** (rapide) chiffre ensuite toute la conversation. *Cette métaphore aide à comprendre l'idée générale, même si TLS moderne (notamment **TLS 1.3**) utilise des mécanismes d'échange de clés éphémères plus avancés que le simple « chiffrer une clé avec la clé publique ».*

### Pourquoi c'est important en cyber
Comprendre le handshake explique les attaques de **downgrade** (forcer une version faible) et l'intérêt de TLS 1.3. La vérification du certificat est l'étape qu'un MiTM cherche à contourner.

### Point clé à mémoriser
ClientHello → ServerHello → certificat → vérification → échange de clés → clé de session → symétrique.

---

## 16 bis. Déroulé complet d'une requête HTTPS

### Comment ça fonctionne — déroulé HTTPS

1. L'utilisateur tape une URL en `https://`.
2. Le navigateur extrait le host, le path et le **port implicite 443**.
3. Le système résout le nom de domaine en adresse IP via **DNS**.
4. Le client ouvre une **connexion TCP** vers le serveur sur le **port 443**.
5. Avant d'envoyer la requête HTTP, le client démarre un **handshake TLS**.
6. Le client envoie un **`ClientHello`** (versions TLS + suites cryptographiques supportées).
7. Le serveur répond par un **`ServerHello`** et choisit les paramètres TLS.
8. Le serveur envoie son **certificat TLS**.
9. Le navigateur **vérifie le certificat** : nom de domaine, date de validité, signature, autorité de certification.
10. Le client et le serveur établissent un **secret partagé / une clé de session** via l'échange de clés.
11. Une fois le **tunnel TLS** établi, le navigateur envoie la **requête HTTP à l'intérieur du tunnel chiffré**.
12. Le serveur traite la requête et renvoie une **réponse HTTP elle aussi chiffrée** dans TLS.
13. Le navigateur **déchiffre** la réponse, interprète HTML/CSS/JS et déclenche d'autres requêtes si nécessaire.

```text
URL HTTPS → DNS → TCP:443 → TLS handshake → tunnel chiffré → HTTP request → HTTP response → navigateur
```


À retenir :

- HTTPS **ne remplace pas** HTTP : il **encapsule** HTTP dans TLS.
- Le contenu HTTP est **chiffré** : path, headers, cookies, body, réponse.
- Certaines **métadonnées peuvent encore fuiter** : DNS, IP destination, parfois **SNI** selon la configuration.
- Un **certificat invalide** = l'**authenticité du serveur n'est pas garantie**.
- `curl -k` **chiffre toujours** la connexion, mais **désactive la vérification d'identité** du serveur → MiTM possible.

---

## 17. Chiffrement asymétrique vs symétrique

### À retenir
HTTPS **combine** les deux : asymétrique pour s'installer, symétrique pour travailler.

### Comment ça fonctionne

- **Asymétrique** : une **clé publique** et une **clé privée** liées mathématiquement. Selon l'algorithme, elles peuvent servir à **chiffrer/déchiffrer**, **signer/vérifier** ou **authentifier un échange de clés**. Sûr mais **lent**.
- **Symétrique** : **une même clé** chiffre et déchiffre. **Rapide**, mais il faut d'abord partager la clé en sécurité.

Mécanisme (métaphore historique du cadenas) :

1. Le serveur prouve son identité via son **certificat** (clé publique signée par une CA).
2. Le client et le serveur **négocient un secret partagé** via un échange de clés éphémère.
3. Les deux dérivent la **même clé symétrique** → toute la suite passe en symétrique (ex. AES).

*Cette image aide à saisir l'idée, mais TLS moderne (TLS 1.3) n'envoie pas une clé enfermée dans un cadenas : il établit le secret par **Diffie-Hellman éphémère (ECDHE)**, sans jamais transmettre la clé de session.*

### Pourquoi c'est important en cyber
L'asymétrique résout le **problème d'échange de clé** sur un réseau hostile. C'est exactement ce que fait HTTPS au début de chaque session.

### Point clé à mémoriser
Asymétrique = établir la session (lent, sûr). Symétrique = échanger les données (rapide). HTTPS fait les deux.

---

## 18. HTTPS et limites de sécurité

### À retenir
HTTPS chiffre le **contenu**, pas forcément toutes les **métadonnées**.

### Comment ça fonctionne

- Le **DNS** peut rester **visible** s'il n'est pas chiffré (DoH/DoT).
- Le **SNI** (Server Name Indication) du handshake peut exposer le domaine demandé selon la version/config TLS.
- Un **certificat invalide** = problème d'**authenticité**, même si un chiffrement existe.
- `curl -k https://site.local` **ignore la validation** du certificat (la connexion reste chiffrée) → ouvre la porte au **MiTM** (à réserver aux labs).
- **HSTS** (Strict-Transport-Security) force HTTPS et limite les **downgrade attacks**.

### Pourquoi c'est important en cyber
« HTTPS = tout est caché » est une **erreur courante**. Un analyste peut déduire les sites visités via DNS/SNI même sans déchiffrer le contenu.

### Point clé à mémoriser
HTTPS protège le contenu, pas toujours le domaine (DNS/SNI). `-k` = MiTM possible. HSTS = anti-downgrade.

---
