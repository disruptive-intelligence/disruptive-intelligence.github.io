---
title: Chapitre 8 — Navigateur, sessions et hygiène web
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie II — Fondations : appareils, comptes et continuité'
  - index.md
---

Les **sessions actives** : chaque onglet de connexion est une session ouverte. Si quelqu'un accède au navigateur, il accède à tous les comptes connectés. Le réflexe : se déconnecter des comptes sensibles après utilisation (banque, email), surtout sur un ordinateur partagé. Les **cookies** de session maintiennent la connexion — le vol de cookie (par un malware ou une extension malveillante) permet à un attaquant d'accéder au compte sans connaître le mot de passe.

L'**auto-remplissage** : le navigateur propose de sauvegarder les mots de passe. C'est mieux que rien, mais moins sécurisé qu'un gestionnaire dédié — les mots de passe du navigateur sont accessibles à quiconque a accès à la session OS. Les **extensions** : chaque extension a accès à TOUT ce que le navigateur voit — les pages bancaires, les emails, les formulaires de connexion. Installer le minimum strict. Vérifier les permissions (une extension qui demande « lire et modifier toutes les données sur tous les sites » a un accès total). Supprimer les extensions inutilisées.

Les **notifications push** abusives : les sites qui demandent « Autoriser les notifications ? » — refuser systématiquement sauf pour les services essentiels. Les notifications push sont utilisées par des sites malveillants pour afficher du spam et du phishing directement sur le bureau ou l'écran du téléphone. Les **faux onglets de connexion** : un site malveillant affiche un faux formulaire de connexion Google/Microsoft/Facebook dans un popup qui imite parfaitement la page d'authentification légitime. Le réflexe : toujours vérifier l'URL dans la barre d'adresse — un vrai login Google est sur accounts.google.com, pas sur google-login-secure.com.

L'**hygiène par séparation** : utiliser un navigateur ou un profil pour les usages sensibles (banque, email principal, gestionnaire de mots de passe) et un autre pour la navigation courante (recherches, articles, réseaux sociaux). Les sessions, les cookies, et les extensions sont séparés — une compromission de la navigation courante n'affecte pas les sessions sensibles.

---

<a id="chapitre-9"></a>
