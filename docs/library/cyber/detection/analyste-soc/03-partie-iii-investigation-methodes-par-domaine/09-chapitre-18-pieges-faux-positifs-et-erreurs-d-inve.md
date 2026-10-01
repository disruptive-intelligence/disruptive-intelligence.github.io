---
title: Chapitre 18 — Pièges, faux positifs et erreurs d'investigation
source: Cyber/06 Détection & réponse/Analyste SOC.md
note: Analyste SOC
up:
- - Analyste SOC
  - ../index.md
- - 'Partie III — Investigation : méthodes par domaine'
  - index.md
---

Les erreurs les plus fréquentes et comment les éviter, illustrées par des cas concrets. Timezones (le piège n°1 — un log proxy en heure locale Paris et un log firewall en UTC créent un décalage fantôme de 1-2h). NAT/proxy/VPN (l'IP source dans les logs firewall peut être le proxy, pas le poste — toujours croiser avec les logs d'authentification pour identifier la machine réelle). Comptes de service (bruit massif, logons réseau en continu, horaires atypiques — les baseliner mais surveiller tout changement : un compte de service qui fait du Kerberoasting, c'est anormal). DHCP et rotation d'IP (l'IP 10.0.5.112 était-elle attribuée à WKS-PROD-112 au moment de l'alerte ? vérifier les baux DHCP). Multi-sessions RDP (sur un serveur RDS, plusieurs utilisateurs partagent la même IP — le session ID est nécessaire pour identifier l'auteur). Scanners de vulnérabilité (Nessus, Qualys — exclure les IP sources dans les règles IDS/IPS, documenter l'exclusion). Le biais de confirmation (l'analyste qui pense « phishing » arrête de chercher des alternatives — peut-être que le document était légitime et l'alerte est un FP sur une macro inoffensive). Et le benign true positive (l'admin IT qui utilise PsExec légitime — la détection est correcte, l'action est bénigne, c'est un BTP pas un FP).

---
