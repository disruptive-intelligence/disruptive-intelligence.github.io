---
title: Chapitre 41 — Réagir à une compromission de compte
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - 'Partie VIII — Quand ça tourne mal : réagir et se reconstruire'
  - index.md
---

L'ordre des actions : (1) **changer immédiatement le mot de passe** du compte compromis (si l'accès est encore possible — si l'attaquant a changé le mot de passe, utiliser la procédure de récupération), (2) **changer le mot de passe de l'email maître** (si le même mot de passe était utilisé — si le compte compromis et l'email ont le même mot de passe, l'email est potentiellement compromis aussi, et l'email contrôle la réinitialisation de tous les autres comptes), (3) **activer le MFA** sur le compte compromis et sur l'email maître (si ce n'est pas déjà fait), (4) **révoquer toutes les sessions actives** (la plupart des services permettent de « déconnecter tous les appareils » dans les paramètres de sécurité — l'attaquant qui a volé un cookie de session perd l'accès), (5) **vérifier les paramètres du compte** (l'attaquant peut avoir ajouté une adresse email de récupération, un numéro de téléphone, ou une règle de transfert automatique d'email → les supprimer ; vérifier aussi les filtres email qui pourraient masquer les notifications de sécurité de l'attaquant), (6) **changer le mot de passe sur tous les comptes qui utilisaient le même mot de passe**, (7) **documenter** ce qui s'est passé (captures d'écran, emails reçus, dates, actions effectuées — pour la plainte ou le signalement), et (8) **informer les contacts** si le compte a pu être utilisé pour les contacter (faux messages envoyés au nom de la victime).

Le cas particulier de l'**email maître compromis** : c'est le pire scénario parce que l'email contrôle la réinitialisation de mot de passe de tous les autres comptes. Si l'attaquant a accès à votre Gmail, il peut demander la réinitialisation de votre banque, de votre cloud, de vos réseaux sociaux. Reprendre l'email d'abord, puis tous les comptes liés. Si vous ne pouvez pas reprendre l'email (mot de passe et MFA changés par l'attaquant), passer immédiatement par la procédure de récupération du fournisseur — ces procédures existent et fonctionnent, mais peuvent prendre plusieurs jours.

Les erreurs à ne PAS faire : paniquer et tout changer en même temps sans ordre (→ risque de perdre l'accès à tout, et de se déconnecter du seul appareil qui a encore une session valide), supprimer le compte compromis (→ perte de l'historique et des données, et l'attaquant peut recréer le compte), ou ignorer l'incident en espérant qu'il n'y aura pas de conséquences (→ l'attaquant revient et exploite l'accès).

---

<a id="chapitre-42"></a>
