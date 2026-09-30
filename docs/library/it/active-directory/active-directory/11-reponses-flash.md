---
title: Réponses flash
source: IT/04_Active-Directory/Active_Directory.md
note: Active Directory
up:
- - Active Directory
  - index.md
---

- **AD** → Annuaire centralisé Microsoft, SSO, 90 % des entreprises, cible n°1 (accès total si compromis).
- **Kerberos** → Client → TGT (via krbtgt) → TGS (via SPN) → accès service. Secret = hash krbtgt.
- **Kerberoasting** → Demande TGS pour SPN → crack offline. Défense = gMSA, mots de passe 25+ chars, AES.
- **Tiering** → Tier 0 (DC/DA), Tier 1 (serveurs), Tier 2 (postes). Jamais de connexion cross-tier.
- **Hardening quick wins** → Audit Policy, LAPS, séparation comptes, SMB signing, désactiver LLMNR.
- **DCSync** → Fausse réplication pour extraire hashes. Détection = 4662 depuis non-DC.
- **Golden Ticket** → TGT forgé avec hash krbtgt. Remédiation = double rotation krbtgt espacée de 10-12h.
- **BloodHound** → Graphe AD, chemins vers DA, nœuds de convergence. Offensif ET défensif.

---

> **Note de clôture**
>
> Ce cours a été conçu comme LA référence Active Directory de la bibliothèque — la ressource complète pour comprendre, attaquer, défendre et répondre à incident sur AD.
>
> L'opération KERBEROS illustre une réalité que tout professionnel cyber constate sur le terrain : la majorité des compromissions AD exploitent des fondamentaux négligés. Un compte de service avec un SPN et un mot de passe de 5 ans. Un template AD CS avec le SAN libre. Un Domain Admin qui a une session active sur un serveur Tier 1. Un krbtgt jamais roté depuis la création du domaine. Un RODC avec une PRP trop large. Un LLMNR actif. Ce ne sont pas des vulnérabilités exotiques — ce sont des configurations par défaut que personne n'a durcies.
>
> Le cours assume deux convictions. Première : comprendre l'attaque est le prérequis pour défendre efficacement — chaque technique offensive est présentée avec son mécanisme, ses outils, ses preuves, ET sa détection et sa remédiation. Deuxième : aucune mesure seule ne suffit — c'est la défense en profondeur (hardening + détection + deception + IR) qui protège AD. Un Golden Ticket est forgeable, mais si le krbtgt est roté régulièrement, les sessions sont monitorées, et les honey accounts sont en place, l'attaquant est détecté avant d'atteindre son objectif.
>
> *Comprendre le mécanisme • Exploiter la faiblesse • Détecter le signal • Durcir la configuration • Répondre à l'incident — avec méthode et profondeur.*
