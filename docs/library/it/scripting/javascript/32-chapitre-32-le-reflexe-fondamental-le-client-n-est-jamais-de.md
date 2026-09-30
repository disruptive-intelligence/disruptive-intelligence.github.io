---
title: 'Chapitre 32 — Le réflexe fondamental : le client n''est jamais de confiance'
source: IT/05_Scripting_Langage-Prog/JavaScript.md
note: JavaScript
chapter: 32
chapters: 35
---

## Le minimum à savoir

C'est **le principe de sécurité le plus important** de tout le cours, celui qui sous-tend la Boîte à risques. Une seule phrase à graver :

> **Tout ce qui s'exécute dans le navigateur est sous le contrôle total de l'utilisateur. Le frontend sert à l'expérience, jamais à la sécurité.**

### Pourquoi le client n'est pas fiable

Un utilisateur (ou un attaquant) peut, sur **ta** page, dans **son** navigateur :
- **lire tout ton code JavaScript** (il est livré en clair) ;
- **le modifier en direct** dans les DevTools ;
- **désactiver JavaScript** entièrement ;
- **changer n'importe quelle valeur** (variables, champs, cases cochées) ;
- **envoyer des requêtes directement au serveur**, en contournant totalement ta page (`curl`, Postman, scripts).

Conséquence : **aucune** garantie de sécurité ne peut reposer sur le code client.

### Reprise de la Boîte à risques sous cet angle

Presque tous les risques du cours découlent de ce principe :

| Risque (Boîte à risques) | Pourquoi le principe s'applique | Chapitre |
| --- | --- | --- |
| Validation client prise pour de la sécurité (n° 3) | L'utilisateur contourne la validation → **valider au serveur**. | 17 |
| Token en LocalStorage / exposé (n° 4, 5) | Tout JS lit le LocalStorage → **ne pas y mettre de secret**. | 18 |
| Bouton masqué = contrôle d'accès (n° 8) | Cacher ≠ interdire → **autoriser au serveur**. | 17, 32 |
| Logique sensible côté frontend (n° 17) | Le code client est lisible/modifiable → **logique sensible au serveur**. | 32 |
| CORS pris pour une sécurité serveur (n° 7) | CORS protège l'utilisateur, pas l'API → **authentifier au serveur**. | 24, 31 |

### Ce qui appartient au client vs au serveur

| Côté client (navigateur) | Côté serveur |
| --- | --- |
| Expérience utilisateur, affichage | **Sécurité, autorisation** |
| Validation de **confort** (retour immédiat) | **Validation qui fait foi** |
| Logique non sensible | **Logique sensible, secrets, clés** |
| Suggestions, ergonomie | **Décisions d'accès aux données** |

## Très utile en pratique

Quand tu conçois ou analyses une application, pose-toi systématiquement : **« cette protection repose-t-elle uniquement sur le client ? »** Si oui, elle est contournable. La vraie barrière est **toujours** au serveur. C'est le réflexe qui distingue une personne qui « écrit du JavaScript » d'une personne qui « pense sécurité web ».

## Exemple simple

```javascript
// ☠️ Anti-pattern : contrôle d'accès côté client
if (utilisateur.role === "admin") {
  afficherBoutonSupprimer();   // cacher le bouton n'empêche personne
}
// L'utilisateur peut appeler l'API de suppression directement.
// → Le SERVEUR doit vérifier le rôle à chaque requête sensible.

// ✅ Côté client : on AMÉLIORE l'expérience (cacher ce qui n'est pas utile),
//    mais on sait que la sécurité réelle est imposée par le serveur.
```

## Application IT / cyber / OSINT

Ce principe est le **socle mental** du pentest web et de l'analyse défensive. Un testeur d'intrusion commence souvent par : modifier les valeurs côté client, rejouer les requêtes en contournant l'interface, désactiver les validations JS — précisément parce qu'il sait que le client n'est pas fiable. Côté défense, concevoir en supposant un client hostile est la base d'une application robuste. Intérioriser ce réflexe te fait progresser plus vite que n'importe quelle astuce technique.

> ### 🔍 Lecture de code inconnu
> Quand tu analyses une application, repère les contrôles qui semblent **uniquement** côté client (validation, masquage de boutons, « rôle » stocké en JS). Ce sont des points où la sécurité réelle dépend entièrement de ce que fait — ou non — le serveur derrière.

## ❌ Erreur classique

```javascript
// ❌ Faire confiance à une valeur venue du client
// prix envoyé par le formulaire = 0.01 → le serveur l'accepte tel quel ☠️
// ✅ Le serveur recalcule/vérifie le prix à partir de SES données.

// ❌ Mettre une clé d'API secrète dans le JavaScript de la page
const API_KEY = "sk_live_secret...";   // ☠️ visible par tous → le secret reste au serveur

// ❌ Croire qu'obfusquer le JS protège la logique
// → l'obfuscation ralentit la lecture, ne protège rien.
```

> **Réflexe diagnostic :** tu t'apprêtes à faire reposer une décision de sécurité sur du code navigateur ? Arrête : déplace-la côté serveur. Le client ne décide jamais des autorisations.

## Exercices

**Guidé**
1. Reprends ton formulaire de validation (chapitre 17).
2. Dans les DevTools, modifie la valeur d'un champ après validation, ou supprime l'attribut qui bloque l'envoi.
3. Constate que la validation client se contourne trivialement. Conclus (commentaire) : la vraie validation est au serveur.

**Autonome**
Liste, pour une application que tu connais, trois protections qui **doivent** être au serveur (autorisation, validation de données, calcul de prix/score) et explique pourquoi le client ne suffit pas.

**Défi**
Rédige une courte note « principe du client non fiable » destinée à un développeur débutant : la phrase-clé, trois exemples de contournement, et la règle « client = expérience, serveur = sécurité ». Relie chaque point à un risque de la Boîte à risques.

## ✅ Tu sais maintenant…

- énoncer le principe : le client n'est jamais de confiance ;
- citer les façons dont un utilisateur contrôle le code client ;
- relier la majorité des risques du cours à ce principe ;
- répartir correctement responsabilités client (expérience) et serveur (sécurité) ;
- adopter le réflexe de conception/analyse « et si le client était hostile ? ».

-----
