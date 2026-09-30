---
title: 34. Mini quiz
source: IT/Culture/Fiche_WebApp.md
note: Applications web
up:
- - Applications web
  - index.md
---

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
