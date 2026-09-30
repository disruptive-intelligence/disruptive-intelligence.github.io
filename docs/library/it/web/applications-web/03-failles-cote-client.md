---
title: Failles côté client
source: IT/Culture/Fiche_WebApp.md
note: Applications web
up:
- - Applications web
  - index.md
---

## 14. Exposition de données sensibles côté front-end

### À retenir
Le **Sensitive Data Exposure** désigne des données sensibles laissées en clair dans le code visible côté client.

### Comment ça fonctionne
Outils d'inspection : **View Source** (Ctrl+U), **DevTools** (onglets Network, Sources, Storage/Cookies), proxy **Burp Suite**.
On y trouve : commentaires HTML oubliés, scripts JS, endpoints cachés, **credentials de test**, **clés API**, liens internes.

### Pourquoi c'est important en cyber
C'est le premier réflexe d'audit : chercher les **« low-hanging fruits »**. Un commentaire oublié contenant des identifiants peut suffire à entrer.

### Exemple concret

```html
<!-- TODO: remove test credentials test:test -->
```

Un commentaire de développeur non supprimé pouvant exposer des identifiants encore valides.

### Prévention
Ne **jamais** mettre de secret côté client ; relire le code visible ; supprimer commentaires et liens inutiles ; minifier/obfusquer le JS pour limiter l'exposition.

### Point clé à mémoriser
Tout ce qui est dans le code client est public. Lire le source avant tout le reste.

---

## 15. HTML Injection

### À retenir
L'**HTML injection** survient quand une entrée utilisateur non filtrée est affichée comme du **HTML** plutôt que comme du texte.

### Comment ça fonctionne
Si l'application insère l'entrée directement dans la page (par ex. via `innerHTML`) sans nettoyage, le navigateur **interprète** le HTML soumis au lieu de l'afficher littéralement. La donnée peut venir directement du front-end ou être récupérée depuis la base (commentaire stocké).

### Pourquoi c'est important en cyber
Impacts : **défacement** de page, insertion de **faux formulaire** de connexion (phishing), modification visuelle trompeuse. C'est souvent la porte d'entrée vers le **XSS**.

### Exemple concret
Un champ « nom » réaffiché tel quel : soumettre une balise `<style>` modifiant l'arrière-plan suffit à prouver que l'entrée est interprétée comme HTML.

### Prévention
Validation, sanitization, **output encoding** (afficher comme texte), éviter `innerHTML` avec une entrée utilisateur.

### Point clé à mémoriser
Si une entrée s'affiche comme du code et non comme du texte, le contrôle d'affichage est cassé.

---

## 16. Cross-Site Scripting (XSS)

### À retenir
Le **XSS** injecte du **JavaScript** exécuté dans le navigateur de la victime. C'est une HTML injection poussée à l'exécution de code client.

### Comment ça fonctionne

| Type | Déclenchement |
|---|---|
| **Reflected** | L'entrée est renvoyée immédiatement (résultat de recherche, message d'erreur) |
| **Stored** | L'entrée est stockée en base puis réaffichée (post, commentaire) — touche plusieurs victimes |
| **DOM** | L'entrée est écrite directement dans un objet du DOM par du JS côté client |

### Pourquoi c'est important en cyber
Impacts : **vol de session** (cookies), actions effectuées au nom de la victime, et — si la victime est admin — compromission de comptes à privilèges pouvant mener au serveur.

### Exemple concret
Un payload affichant `document.cookie` dans une alerte prouve qu'on peut lire le cookie de session de la victime — première étape vers son vol.

### Prévention
**Output encoding**, sanitization, **CSP** (Content Security Policy), cookies **HttpOnly**, éviter les *DOM sinks* dangereux, validation côté serveur. Les navigateurs modernes bloquent une partie des exécutions automatiques, mais ce n'est pas suffisant.

### Point clé à mémoriser
HTML injection = injecter du HTML. XSS = injecter du JS exécuté chez la victime.

---

## 17. Cross-Site Request Forgery (CSRF)

### À retenir
Le **CSRF** abuse de la **session active** d'une victime pour exécuter une action **non voulue** en son nom.

### Comment ça fonctionne
Le navigateur joint **automatiquement** les cookies d'authentification à chaque requête vers le site. Si un attaquant force la victime authentifiée à envoyer une requête (via un lien, une image, ou un XSS), l'action s'exécute avec les droits de la victime.

### Pourquoi c'est important en cyber
Permet de modifier un mot de passe, d'effectuer une action sensible, ou — en visant un admin — d'obtenir des accès privilégiés. Le CSRF s'appuie souvent sur un XSS pour porter le payload.

### Exemple concret
Un commentaire piégé charge un script qui rejoue la procédure de changement de mot de passe de l'application. La victime, connectée, change son mot de passe à son insu vers une valeur connue de l'attaquant.

### Prévention
**Token anti-CSRF** unique par session/requête, attribut cookie **SameSite** (Strict/Lax), vérification **Origin/Referer**, et confirmation (ou ressaisie du mot de passe) pour les actions sensibles. Ces défenses sont des **couches**, pas des garanties absolues.

### Point clé à mémoriser
CSRF = faire agir le navigateur de la victime à son insu, en exploitant ses cookies automatiquement envoyés.

---

## 18. Validation, sanitization et output encoding

### À retenir
Trois contrôles complémentaires sur les entrées/sorties utilisateur :

- **Validation** : vérifier que l'entrée correspond au format attendu (un email ressemble à un email).
- **Sanitization** : supprimer/neutraliser les caractères dangereux avant stockage ou affichage.
- **Output encoding** : afficher la donnée comme **texte** et non comme du code.

### Comment ça fonctionne
Validation et sanitization s'appliquent à l'entrée ; l'output encoding s'applique à la sortie, au moment du rendu. Les trois ensemble bloquent HTML injection et XSS même si une couche est contournée.

### Pourquoi c'est important en cyber
Le contrôle **côté client** sert l'expérience utilisateur (UX) ; il se contourne trivialement. La sécurité réelle se joue **côté serveur**, et idéalement aussi à l'affichage.

### Point clé à mémoriser
Valider l'entrée, nettoyer la donnée, encoder la sortie — et toujours imposer la décision côté serveur.

---
