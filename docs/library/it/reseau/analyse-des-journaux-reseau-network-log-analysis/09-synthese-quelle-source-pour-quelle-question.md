---
title: 'Synthèse : quelle source pour quelle question'
source: IT/04 Réseau/Journaux & investigation/Analyse des journaux réseau (Network Log Analysis).md
note: Analyse des journaux réseau (Network Log Analysis)
up:
- - Analyse des journaux réseau (Network Log Analysis)
  - index.md
---

## Ce que chaque source permet de voir

| Source | Répond surtout à | Ne montre pas | À corréler avec |
|---|---|---|---|
| **NetFlow** | Qui a parlé à qui, quand, sur quel port, avec quel volume | Contenu, URL, fichier, utilisateur | DNS, pare-feu, proxy, EDR |
| **Pare-feu** | Connexion autorisée ou refusée, règle (Policy ID), NAT, volume | Contenu applicatif (sauf NGFW) | NetFlow, IPS, EDR |
| **VPN** | Qui s’est connecté à distance, depuis quelle IP (`remip`), avec quelle IP interne (`tunnelip`) | Ce que l’utilisateur a fait ensuite | Pare-feu (activité depuis la `tunnelip`), authentification, MFA |
| **Proxy** | Quelle URL, quelle catégorie, quel utilisateur, autorisé ou bloqué | Contenu HTTPS sans inspection TLS | DNS, EDR / XDR, pare-feu |
| **IDS / IPS** | Quelle signature d’attaque, quelle cible, détectée ou bloquée | Si l’exploitation a réussi | Pare-feu, EDR, état du service ciblé |
| **WAF** | Attaque applicative contre un site (SQLi, XSS, traversal…), action prise | Ce que l’application a réellement exécuté | Logs web, réputation de l’IP source |
| **Logs web** | Méthode, URI, code de statut, taille, User-Agent de chaque requête | Corps des POST / PUT (non journalisé par défaut) | WAF, IDS, logs applicatifs |
| **DNS** | Quel poste a résolu quel domaine, tunneling, DGA, NXDOMAIN | Si une connexion a suivi la résolution | Proxy, NetFlow, pare-feu, EDR |

## Quelle source pour quel scénario

| Scénario | Sources à consulter en premier |
|---|---|
| Scan de ports | NetFlow, pare-feu, IDS / IPS |
| Mouvement latéral | NetFlow et pare-feu (flux est-ouest), VPN si accès distant |
| C2 / beaconing | NetFlow (périodicité), DNS, proxy, pare-feu |
| Exfiltration | NetFlow et pare-feu (volume sortant), proxy (POST, cloud), DNS (tunneling) |
| Accès distant suspect | VPN, puis pare-feu depuis la `tunnelip` |
| Attaque d’un site web | WAF, logs web, IDS / IPS |
| Poste infecté | Proxy (URL bloquées), DNS (domaines malveillants, NXDOMAIN), EDR |

Le point commun de tous ces journaux : **aucune source ne suffit seule**. Une adresse IP relie le pare-feu, NetFlow et le VPN ; un domaine relie le DNS et le proxy ; une requête relie le WAF et les logs web ; l’EDR rattache le tout à un processus et à un utilisateur.
