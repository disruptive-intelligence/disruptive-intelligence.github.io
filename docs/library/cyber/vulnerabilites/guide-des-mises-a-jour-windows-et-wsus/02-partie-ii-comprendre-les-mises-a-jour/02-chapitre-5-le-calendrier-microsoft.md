---
title: Chapitre 5 — Le calendrier Microsoft
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie II — Comprendre les mises à jour
  - index.md
---

> 🧱 **Les bases**
>
> - **Redmond** (État de Washington) est le siège de Microsoft. L'heure de référence est celle du Pacifique (PT), en général **9 heures de moins qu'à Paris**.
> - Un **calendrier prévisible** permet aux équipes de planifier tests, fenêtres de maintenance et effectifs.

## 5.1 Les rendez-vous

| Moment | Événement | En entreprise |
|---|---|---|
| **2e mardi du mois**, 10 h à Redmond = **~19 h à Paris** | **Patch Tuesday** (« B release ») : cumulatives Windows, .NET, Office, serveurs… | **le** déploiement mensuel |
| le lendemain | ***Exploit Wednesday*** : analyse des correctifs (*patch diffing*), apparition d'exploits pour les failles corrigées | ne pas traîner sur les failles critiques |
| 4e semaine | **préversion non sécurité** (*optional non-security preview*, anciennement « D release ») : contenu non sécurité de la B suivante | tester sur quelques machines, **jamais en production** |
| n'importe quand | **hors calendrier** (*out-of-band*, OOB) : faille exploitée, régression grave | procédure accélérée |
| chaque semaine ou presque | **Edge** (correctifs Chromium) | cycle Edge (Ch.13) |
| plusieurs fois par jour | définitions **Defender** | automatique |
| septembre-octobre | nouvelle **version annuelle** de Windows 11 | projet annuel |

**Le Patch Tuesday (B).** Le 2e mardi du mois, vers 19 h à Paris (18 h en mars, pendant les semaines où les États-Unis sont déjà passés à l'heure d'été et pas l'Europe). En pratique, une équipe française **découvre les correctifs le mardi soir et travaille dessus le mercredi**. Le soir même, le **CERT-FR** publie un avis « Multiples vulnérabilités dans les produits Microsoft ».

**La préversion (D).** En juillet 2026, Microsoft a clarifié son vocabulaire : les anciennes « C » et « D releases » s'appellent désormais *optional non-security preview updates*. Elles sortent généralement la **4e semaine**, sont cumulatives, ne contiennent **aucun correctif de sécurité nouveau**, et préfigurent la B du mois suivant. Leur intérêt pour l'entreprise : **un mois d'avance** pour détecter une régression sur un petit groupe IT. Sur les machines gérées, elles ne s'installent que si la politique le permet ; dans WSUS, elles n'arrivent que si on les synchronise et approuve.

**Le hors calendrier (OOB).** Publié quand on ne peut pas attendre : faille exploitée activement, ou régression grave introduite par la B. Certains OOB ne sont publiés que dans le **catalogue Microsoft Update** (à importer manuellement dans WSUS), d'autres aussi sur Windows Update et WSUS. **Lire la page KB pour savoir par où il passe.**

> 💡 **Exemple — Des OOB réels**
>
> - 23 octobre 2025 : OOB pour CVE-2025-59287 (WSUS), sur toutes les versions de Windows Server supportées.
> - Fin mars 2026 : la préversion de mars a été **remplacée** par un OOB (KB5086672) pour Windows 11 24H2 et 25H2.
> - Janvier 2026 : OOB corrigeant des problèmes de connexion RDP introduits par la B de janvier.

## 5.2 Le calendrier 2026-2027

| Mois | Patch Tuesday | Particularité hotpatch |
|---|---|---|
| novembre 2026 | **mardi 10** | hotpatch ; dernière mise à jour de 23H2 Entreprise |
| décembre 2026 | mardi 8 | hotpatch |
| janvier 2027 | mardi 12 | base (redémarrage) ; **fin de Windows Server 2016** le même jour |
| février 2027 | mardi 9 | hotpatch |
| mars 2027 | mardi 9 | hotpatch ; publication à ~18 h à Paris |
| avril 2027 | mardi 13 | base (redémarrage) |

## 5.3 Le piège du « Nième mercredi »

Beaucoup d'équipes expriment leur cycle en « 2e mercredi », « 3e mercredi »… C'est **faux une partie de l'année** : quand un mois commence un mercredi, le 2e mercredi tombe **avant** le Patch Tuesday.

> 💡 **Exemple — Avril et juillet 2026**
>
> - **Avril 2026** : le 1er avril est un mercredi. 2e mercredi = **8 avril** ; Patch Tuesday = **14 avril**. Un cycle « on récupère les mises à jour le 2e mercredi » récupère… celles de mars.
> - **Juillet 2026** : même situation (1er juillet = mercredi ; 2e mercredi = 8 juillet ; Patch Tuesday = 14 juillet).

✅ **Bonne pratique** — Exprimer tout le cycle en **J+n**, où **J = le Patch Tuesday** : J+1 (le mercredi qui suit), J+8, J+15, J+22. Attention aussi : selon les mois, le Patch Tuesday suivant tombe à J+28 ou à **J+35**. Le cycle complet est détaillé au Ch.12.

## 5.4 Ce que le calendrier implique pour l'équipe

- **Mardi soir** : synchronisation WSUS (planifiée après 19 h 30), première lecture des notes et des avis.
- **Mercredi (J+1)** : qualification (Ch.6), approbation sur le groupe pilote.
- **Les jours suivants** : surveillance des retours (régressions signalées par la communauté, *known issues* de Microsoft).
- **Quatrième semaine** : préversion sur un petit groupe IT, nettoyage WSUS, préparation du mois suivant.
- **À tout moment** : capacité à traiter un OOB en quelques heures.

> 🧵 **Fil rouge — Avril 2026**
>
> En reprenant les procédures, Inès remarque que la consigne écrite dit « 2e mercredi du mois : approbation des applicatifs en pilote ». Elle vérifie le calendrier d'avril : le 2e mercredi est le 8, le Patch Tuesday le 14. Karim se souvient qu'en octobre 2025 (le 1er octobre était aussi un mercredi), l'équipe avait approuvé le pilote… avec les mises à jour du mois précédent, sans s'en rendre compte. La procédure est réécrite en J+n et validée au CAB.

> 📌 **À retenir**
>
> - Patch Tuesday = 2e mardi, ~19 h à Paris. Préversion non sécurité = 4e semaine. OOB = n'importe quand.
> - Raisonner en **J+n après le Patch Tuesday**, jamais en « Nième mercredi ».
> - Sur le hotpatch : bases en janvier, avril, juillet, octobre, plus des bases imprévues.

---
