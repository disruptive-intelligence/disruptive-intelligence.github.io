---
title: Partie VI — Protection runtime et détection
source: Cyber/05 Hardening/Sécurité applicative (AppSec).md
note: Sécurité applicative (AppSec)
up:
- - Sécurité applicative (AppSec)
  - index.md
---

*Le code est en production. Cette partie couvre la protection runtime, la détection des attaques web en production, l'investigation d'incidents, et la sécurité des données. C'est ce qui connecte l'AppSec au SOC, au forensic, et à l'IR.*

---


## Chapitre 24 — WAF, RASP et défense en profondeur

Le WAF (Web Application Firewall — reverse proxy qui filtre les requêtes malveillantes ; ModSecurity CRS, AWS WAF, Cloudflare WAF). Ce que le WAF protège (injections basiques, XSS évidents, scanners automatisés, volumétrie) et ce qu'il ne protège PAS (IDOR — la requête est légitime en forme, failles de logique métier, auth failures, SSRF complexes, zero-days). Le WAF est un filet de sécurité, pas une solution — la fondation reste le code sécurisé.

Le RASP (Runtime Application Self-Protection — agent intégré dans l'application, observe le comportement de l'intérieur ; détecte ce que le WAF ne voit pas — injection dans un paramètre JSON imbriqué ; ajoute de la complexité et de la latence). Le bot management (CAPTCHAs, browser fingerprinting — TLS fingerprint, canvas, comportement souris —, rate limiting intelligent).

La stratégie de défense en profondeur : code sécurisé (fondation) → tests automatisés (vérification) → WAF (filet) → monitoring et alerting (détection) → incident response (réaction). Si une couche échoue, la suivante rattrape.

---


## Chapitre 25 — Logging applicatif et détection d'attaques web

**Quoi logger** : authentification (succès, échecs, lockouts, changements de mot de passe, MFA bypass attempts), autorisation (accès refusés, tentatives d'élévation), actions sensibles (CRUD sur données critiques, exports, partages), erreurs applicatives (500, exceptions, timeouts), événements de sécurité (violations CSP, rate limit hits, WAF blocks).

**Comment logger** : format structuré JSON, request_id unique pour corréler les logs distribués, session_id, user_id, IP source, user-agent, endpoint, méthode HTTP, status code, latence, champ événement. **Quoi NE PAS logger** : mots de passe (même hashés), tokens de session et JWT, clés API, données PII (numéro de sécu, carte bancaire), contenus de formulaires sensibles.

Les **patterns de détection** : brute force (volume de 401/403 depuis une même IP), credential stuffing (IPs multiples, même endpoint, mots de passe variés), scraping (volume de 200 sur les pages de données), injection (patterns SQL/XSS dans les paramètres — loggés par le WAF), IDOR (accès séquentiel à des IDs — `GET /patients/1`, `/patients/2`, `/patients/3`...), et exfiltration (volume de données anormalement élevé sur un endpoint).

L'intégration SIEM : les logs applicatifs alimentent le SOC — corrélation avec les logs infra, les alertes EDR, les événements réseau (renvoi cours SOC). Les règles de détection web sont complémentaires aux règles infra — un SOC sans logs applicatifs est aveugle sur la couche 7.

---


## Chapitre 26 — Forensic et incident response web

La méthodologie IR web en 6 étapes : (1) **Préservation des logs** (avant rotation ou écrasement — exporter les logs applicatifs, reverse proxy, WAF, cloud), (2) **Timeline** (corréler les logs pour reconstituer la chronologie), (3) **Identification du vecteur** (comment l'attaquant a pénétré : vulnérabilité applicative, credentials volés, supply chain), (4) **Évaluation de l'impact** (quelles données, quels comptes, quel périmètre), (5) **Containment** (bloquer IP/session, patcher la vulnérabilité, révoquer les credentials compromis), (6) **Éradication et durcissement** (corriger la vulnérabilité à la source, ajouter des règles de détection).

L'investigation d'un webshell (fichier récent dans le webroot, accès POST vers un fichier PHP/ASPX inhabituel, commandes système dans les logs). L'investigation d'une fuite de données via API (logs d'accès anormaux — volume, patterns séquentiels). L'articulation SOC/forensic infra (quand l'incident web dépasse la couche applicative — le webshell pivote vers l'OS → escalade vers le forensic infra et le cours IR).

> **🎯 SecureHealth — incident :** SSRF dans le microservice PDF. Détection via logging centralisé (Datadog alerte sur accès metadata AWS). Timeline reconstruite via logs applicatifs + CloudTrail. Containment : rotation credentials IAM en 45 min. Impact limité : rôle IAM minimal (leçon du premier incident). Retex : threat modeling de tout nouveau service, même les « petits » microservices.

---


## Chapitre 27 — Sécurité des données

chiffrement, minimisation et traçabilité

*Ce chapitre reste sur le terrain technique de l'implémentation — pas sur le terrain juridique de la conformité (couvert par le cours GRC).*

Le **chiffrement au repos** : AES-256 pour les données en base (chiffrement par colonne pour les champs sensibles — numéro de sécurité sociale, données médicales), chiffrement du disque (LUKS, BitLocker, EBS encryption), chiffrement des sauvegardes. Le **chiffrement en transit** : TLS 1.3 pour toutes les communications, mTLS entre les microservices (le service mesh le rend transparent). Le chiffrement **par champ** (field-level encryption — les données sensibles sont chiffrées individuellement, chaque champ avec sa clé ou sa politique — AWS DynamoDB encryption, MongoDB field-level encryption ; même si la base est compromise, les champs sensibles restent chiffrés).

La **minimisation technique** : ne collecter que les données strictement nécessaires à la fonctionnalité (un formulaire d'inscription n'a pas besoin de la date de naissance si l'application ne l'utilise pas). La **pseudonymisation** (remplacer les identifiants directs par des pseudonymes — le lien avec l'identité est conservé mais séparé ; la pseudonymisation est réversible). L'**anonymisation** (irréversible — aucun moyen de relier les données à l'individu). La **suppression effective** : le soft-delete (is_deleted=true) ne supprime pas les données — il les masque dans l'interface. La suppression effective nécessite un delete physique + purge des backups + purge des logs + purge des caches.

La **traçabilité des accès** : qui a accédé à quelle donnée, quand, depuis quelle IP, pour quelle action. Pour les données de santé (SecureHealth — HDS), la traçabilité est une obligation technique — chaque accès à un dossier patient doit être loggé et auditable. La **tokenisation** pour les données de paiement (PCI-DSS — ne pas stocker les données de carte → utiliser un PSP comme Stripe qui tokenise les cartes ; le token est inutile sans le PSP).

La **séparation des données** : les données de dev/test ne doivent pas contenir de données de production. Les dumps de base de données pour le développement doivent être anonymisés avant transfert.

---
