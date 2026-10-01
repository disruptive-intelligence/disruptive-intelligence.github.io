---
title: Chapitre 31 — CSP, en-têtes et défenses navigateur
source: IT/07 Scripting & programmation/JavaScript.md
note: JavaScript
up:
- - JavaScript
  - ../index.md
- - 'Partie 7 — Sécurité web côté client : synthèse défensive'
  - index.md
---

## Le minimum à savoir

Le navigateur offre des **défenses configurables**, posées par le **serveur** via des **en-têtes HTTP**. Tu ne les écris pas en JavaScript, mais tu dois les **comprendre** : ce sont elles qui encadrent ce que ton JavaScript (et celui d'un attaquant) a le droit de faire.

### CSP (Content Security Policy)

La **CSP** est un en-tête qui **limite ce qu'une page a le droit de charger et d'exécuter**. C'est une défense majeure contre le XSS : même si une injection passe, la CSP peut **empêcher l'exécution** du script injecté.

```text
Content-Security-Policy: default-src 'self'; script-src 'self'
```


Cet exemple dit : « ne charge scripts, styles, images, etc. que depuis **ma propre origine** ; refuse les scripts inline et les scripts d'autres domaines ». Un `<script>` injecté par un attaquant, ou un `onerror=...` inline, est alors **bloqué** par le navigateur.

### Autres en-têtes de sécurité utiles

| En-tête | Rôle |
| --- | --- |
| **`Content-Security-Policy`** | limite sources de scripts/styles/etc. ; anti-XSS. |
| **`Strict-Transport-Security`** (HSTS) | force HTTPS pour les futures visites. |
| **`X-Content-Type-Options: nosniff`** | empêche le navigateur de « deviner » le type d'un fichier. |
| **`X-Frame-Options`** / `frame-ancestors` | empêche l'inclusion de la page dans une iframe (anti-clickjacking). |
| **`Referrer-Policy`** | limite les infos de provenance envoyées. |

### Rappel : les attributs de cookies (chapitre 19)

Les défenses cookies font partie du même arsenal d'en-têtes serveur :

```text
Set-Cookie: session=...; HttpOnly; Secure; SameSite=Strict
```


- **`HttpOnly`** : cookie invisible à JavaScript → protège contre le vol par XSS.
- **`Secure`** : envoyé seulement en HTTPS.
- **`SameSite`** : limite l'envoi cross-site → atténue le CSRF.

### Rappel : CORS (chapitre 24)

CORS est lui aussi un mécanisme d'en-têtes (`Access-Control-Allow-Origin`), appliqué par le **navigateur**, qui encadre les lectures cross-origin. Rappel essentiel : **CORS protège l'utilisateur, pas le serveur**.

## Très utile en pratique

> ### 🛡️ Réflexe sécurité : lire les en-têtes d'une réponse
> Dans les DevTools, onglet **Réseau** → sélectionne une requête → **En-têtes de réponse**. Tu peux y vérifier la présence de `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, et les attributs `Set-Cookie`. **Leur absence est une faiblesse** souvent relevée dans les audits de sécurité web.

## Exemple simple

Ce que tu observes, tu ne l'écris pas en JS — tu le **lis** :

```text
# En-têtes d'une réponse bien configurée (vue dans DevTools → Réseau)
Content-Security-Policy: default-src 'self'
Strict-Transport-Security: max-age=63072000
X-Content-Type-Options: nosniff
Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Strict
```


## Application IT / cyber / OSINT

L'analyse des en-têtes de sécurité est un geste **quotidien** en sécurité web défensive et en audit. Des outils et des scanners vérifient automatiquement la présence et la qualité de la CSP, de HSTS, des attributs de cookies. Savoir lire ces en-têtes dans les DevTools, comprendre ce que chacun protège, et repérer les manques, est une compétence d'analyste directement opérationnelle. Tu approfondiras cela dans la suite « Web Security ».

> ### 🔍 Lecture de code inconnu
> Une CSP stricte sur une page **réduit la surface** d'un éventuel XSS. Quand tu analyses une page, vérifier la CSP t'indique à quel point un script injecté pourrait (ou non) s'exécuter.

## ❌ Erreur classique

```text
# ❌ Croire que la CSP s'écrit en JavaScript
# → non : c'est un en-tête HTTP, posé par le serveur (ou un <meta http-equiv>).

# ❌ Croire qu'une CSP rend le code invulnérable
# → c'est une défense EN PROFONDEUR : elle réduit l'impact, ne remplace pas
#   le bon usage de textContent et l'évitement d'eval.

# ❌ Confondre les rôles : CORS ≠ CSP
# → CORS encadre les LECTURES cross-origin ; CSP limite ce que la page EXÉCUTE/charge.
```


> **Réflexe diagnostic :** un script légitime est « bloqué » sans erreur JavaScript classique, avec un message mentionnant `Content Security Policy` dans la console ? C'est la **CSP** qui l'empêche de s'exécuter (script inline ou source non autorisée).

## Exercices

**Guidé**

1. Ouvre une grande application web, DevTools → Réseau → la requête principale.
2. Repère, dans les en-têtes de réponse, `Content-Security-Policy` et `Strict-Transport-Security` (si présents).
3. Note ce que la CSP autorise (`script-src`, `default-src`).

**Autonome**
Sur trois sites différents, compare la présence/absence des en-têtes de sécurité (CSP, HSTS, nosniff) et des attributs de cookies. Lequel semble le mieux configuré ? Justifie en deux phrases.

**Défi**
Rédige un mini-mémo « checklist en-têtes de sécurité » : pour chaque en-tête (CSP, HSTS, X-Content-Type-Options, X-Frame-Options) et chaque attribut de cookie (HttpOnly, Secure, SameSite), une ligne expliquant ce qu'il protège. Ce mémo te servira en audit.

## ✅ Tu sais maintenant…

- expliquer ce qu'est une CSP et en quoi elle limite le XSS ;
- citer les en-têtes de sécurité principaux et leur rôle ;
- relier cookies (`HttpOnly`/`Secure`/`SameSite`) et CORS à cet arsenal ;
- lire les en-têtes de réponse dans les DevTools ;
- distinguer les rôles de CORS et de CSP.

-----
