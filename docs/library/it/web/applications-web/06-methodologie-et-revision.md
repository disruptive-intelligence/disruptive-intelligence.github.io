---
title: Méthodologie et révision
source: IT/05 Web & applications/Applications web/Applications web.md
note: Applications web
up:
- - Applications web
  - index.md
---

## 29. Méthodologie de lecture d'une application web

### À retenir
Une démarche reproductible pour cartographier puis tester une application, du visible vers le profond.

### Démarche

1. Identifier les **pages visibles**.
2. Observer le **trafic** (DevTools Network / Burp).
3. Lire le **code source** (View Source).
4. Identifier les **scripts JavaScript**.
5. Repérer les **endpoints / API**.
6. Identifier **stack et versions**.
7. Tester en **non authentifié**.
8. Tester en **authentifié**.
9. **Comparer les rôles** (user vs admin).
10. Tester les **entrées utilisateur**.
11. Vérifier l'**upload** de fichiers.
12. Vérifier le **contrôle d'accès**.
13. Examiner les **erreurs** 401 / 403 / 404 / 500.
14. **Documenter** proprement.

### Pourquoi c'est important en cyber
Une méthodologie évite les oublis (un rôle non testé, un endpoint JS ignoré) et rend l'audit reproductible et présentable au client.

### Point clé à mémoriser
Du visible vers le profond, du non authentifié vers l'authentifié, en comparant toujours les rôles.

---

## 30. Synthèse mentale

### Flux complet

```
Utilisateur → navigateur → front-end (HTML/CSS/JS)
           → requêtes HTTP/HTTPS
           → web server → application layer (validation / auth / droits)
           → database / services / API
           → réponse → rendu navigateur
```


### Synthèse sécurité

- Le **front-end est visible** (et modifiable, rejouable).
- Le **back-end décide** (c'est là qu'on impose auth, droits et validation).
- La **database contient la valeur**.
- L'**architecture** (segmentation, redondance) **limite ou amplifie** l'impact d'une compromission.

### Point clé à mémoriser
Front-end = ce qu'on voit. Back-end = ce qui décide. Database = ce qui vaut. Architecture = ce qui contient ou propage.

---

## 31. Commandes et réflexes utiles

### Ligne de commande

```bash
curl -I  https://cible        # en-têtes seuls (serveur, codes, redirections)
curl -v  https://cible        # détail complet requête/réponse
curl -s  https://cible        # mode silencieux (sortie propre)
curl -X OPTIONS -i https://cible/api/   # méthodes HTTP autorisées
curl -s https://cible/api/x | jq        # parser une réponse JSON
```


### Navigateur (DevTools)

- **View Source** (Ctrl+U) : commentaires, liens, scripts.
- **Network** : requêtes réelles, endpoints, en-têtes.
- **Sources** : fichiers JS, logique client.
- **Storage / Cookies** : cookies de session, tokens, flags (HttpOnly, SameSite).

### Réflexe

- `grep` les fichiers `.js` pour extraire les endpoints/API cachés.

### Point clé à mémoriser
curl pour le serveur, DevTools pour le client : deux angles d'observation complémentaires.

---

## 32. Erreurs fréquentes à éviter

- Faire **confiance au front-end** pour la sécurité.
- Stocker des **secrets dans le JS**.
- **Cacher** un bouton (CSS) au lieu de protéger la fonction côté serveur.
- Valider **uniquement côté client**.
- **Confondre authentification et autorisation**.
- **Exposer les versions** des composants.
- **Oublier de tester les rôles**.
- Accepter des **uploads sans contrôle** de type/contenu.
- **Concaténer** des entrées utilisateur dans une requête SQL.
- Croire qu'un **WAF remplace** du code sécurisé.
- Tester **uniquement sans compte** (ignorer le périmètre authentifié).
- **Ne pas lire les scripts JS**.

### Point clé à mémoriser
La plupart de ces erreurs reviennent à **faire confiance au client** ou à **confondre cacher et protéger**.

---

## 33. Résumé ultra-court (pour entretien)

> Une application web suit un modèle client/serveur : le **front-end** (HTML/CSS/JS) s'exécute dans le navigateur et est entièrement visible et modifiable, tandis que le **back-end** (web server, logique applicative, base de données) traite les requêtes HTTP et prend toutes les décisions de sécurité. La règle fondamentale est qu'on ne fait **jamais confiance au client** : authentification, autorisation et validation doivent être imposées côté serveur. Les vulnérabilités (XSS, SQLi, broken access control, IDOR, command injection…) ne sont pas des accidents isolés mais les **conséquences** d'une mauvaise décision dans une couche — entrée non filtrée, contrôle d'accès oublié, requête concaténée. L'**architecture** (segmentation, redondance) détermine ensuite si une compromission reste contenue ou se propage à tout le SI.

---

## 34. Mini quiz

1. **Quelle est la différence fondamentale entre front-end et back-end ?**
   Le front-end s'exécute dans le navigateur (visible et modifiable) ; le back-end s'exécute sur le serveur et prend les décisions de sécurité.

2. **Pourquoi ne faut-il jamais faire confiance au front-end ?**
   Tout ce qui est côté client est visible, modifiable et rejouable (JS désactivable, requêtes forgeables via curl/Burp).

3. **Que signifie « Web 2.0 » par rapport à « Web 1.0 » ?**
   Contenu dynamique et personnalisé (Web 2.0) vs pages statiques identiques pour tous (Web 1.0).

4. **Quelles sont les trois couches de la Three Tier Architecture ?**
   Presentation Layer, Application Layer, Data Layer.

5. **Quel modèle d'infrastructure est le plus risqué et pourquoi ?**
   « One Server » : tout sur un même serveur, donc une faille ou une panne compromet tout (œufs dans le même panier).

6. **Quel est l'intérêt sécurité de la segmentation (many servers / one database) ?**
   Un composant compromis n'expose pas directement les autres ; l'impact est contenu.

7. **Différence entre authentification et autorisation ?**
   Authentification = « qui es-tu ? » ; autorisation = « as-tu le droit ? ».

8. **Qu'est-ce qu'un IDOR ?**
   Manipuler un identifiant d'objet (ex. `/user/701` → `/user/702`) pour accéder aux ressources d'autrui faute de contrôle d'accès serveur.

9. **Différence entre HTML injection et XSS ?**
   HTML injection = injecter du HTML interprété ; XSS = injecter du JavaScript exécuté chez la victime.

10. **Cite les trois types de XSS.**
    Reflected, Stored, DOM.

11. **Comment fonctionne une attaque CSRF ?**
    Elle abuse de la session active : le navigateur joint automatiquement les cookies, exécutant une action non voulue au nom de la victime.

12. **Trois défenses contre le CSRF ?**
    Token anti-CSRF, attribut cookie SameSite, vérification Origin/Referer (et ressaisie du mot de passe pour actions sensibles).

13. **Différence entre validation, sanitization et output encoding ?**
    Validation = vérifier le format ; sanitization = nettoyer les caractères dangereux ; output encoding = afficher comme texte et non comme code.

14. **Quels ports écoutent typiquement les web servers ?**
    80 (HTTP) et 443 (HTTPS).

15. **Que signalent les codes HTTP 401 et 403 ?**
    401 = non authentifié ; 403 = authentifié mais accès interdit.

16. **Pourquoi IIS est-il un indice intéressant en pentest ?**
    Il tourne sur Windows Server et s'intègre à Active Directory, suggérant un environnement AD.

17. **Différence entre base SQL et NoSQL ?**
    SQL = tables/lignes/colonnes avec schéma et relations ; NoSQL = sans schéma fixe, flexible (clé-valeur, document, etc.).

18. **Pourquoi la concaténation d'entrée utilisateur dans une requête SQL est-elle dangereuse ?**
    Elle permet une SQL injection : l'attaquant modifie la logique de la requête.

19. **Que faut-il identifier en premier pour chercher un exploit public ?**
    La version du composant (web app, framework, plugin, serveur).

20. **Que mesure le score CVSS et sur quelle échelle ?**
    La sévérité d'une vulnérabilité, de 0 à 10 (Critical = 9.0–10.0 en v3).
