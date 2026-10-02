---
title: Partie IV — Administration active directory
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
---

> **🏗️ À ce stade, on entre dans l'administration d'infrastructure Windows.** Les parties précédentes s'appliquaient à un poste isolé. Active Directory est l'annuaire central d'un **réseau d'entreprise**. Pour pratiquer cette partie, il te faut l'environnement de lab décrit en début de cours : une **VM Windows Server** promue contrôleur de domaine, ou un poste avec **RSAT** connecté à un domaine.
>
> **⚠️ Pratique sur un lab, JAMAIS en production.** À partir d'ici, les exemples **créent, modifient, désactivent et suppriment** de vrais objets d'annuaire (comptes, groupes, OU). Une erreur sur un domaine de production peut désactiver des utilisateurs réels ou casser des accès. Tous les exercices et mini-projets de cette partie sont à réaliser exclusivement sur **ton domaine de lab** (`lab.local`), sur des objets de test. Applique systématiquement la discipline du cours : `Get`/`Test` avant d'agir, `-WhatIf` avant toute opération de masse.
>
> **Ce cours reste un cours PowerShell.** On apprend ici à *piloter* AD avec PowerShell — pas à concevoir une forêt, gérer la réplication, les niveaux fonctionnels ou les approbations. Pour ça, réfère-toi à un cours Active Directory dédié. Ici, AD est le **terrain** sur lequel on applique tout ce qu'on a appris : objets, pipeline, filtrage, boucles, CSV.

---

## Dans cette partie

- [Chapitre 19 — Comprendre Active Directory](01-chapitre-19-comprendre-active-directory.md)
- [Chapitre 20 — Utilisateurs AD](02-chapitre-20-utilisateurs-ad.md)
- [Chapitre 21 — Groupes AD](03-chapitre-21-groupes-ad.md)
- [Chapitre 22 — Ordinateurs et unités d'organisation](04-chapitre-22-ordinateurs-et-unites-d-organisation.md)
- [Chapitre 23 — Recherche et filtrage AD](05-chapitre-23-recherche-et-filtrage-ad.md)
- [Chapitre 24 — Administration en masse avec CSV](06-chapitre-24-administration-en-masse-avec-csv.md)
