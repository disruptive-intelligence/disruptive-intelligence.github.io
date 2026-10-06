---
title: "Journaux réseau"
cours:
  - library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/index.md
  - library/cyber/detection/analyste-soc/index.md
besoin: "Retrouver une attaque dans les journaux réseau (pare-feu, VPN, proxy, DNS, IDS, WAF, web)"
---
# Journaux réseau

Les journaux des équipements réseau, lus en ligne de commande sur un export ou un serveur de logs : pare-feu, NetFlow, VPN, proxy, DNS, IDS / IPS, WAF et serveurs web. Chaque source répond à une question différente ; aucune ne suffit seule.

Les incontournables : `grep` · `sed -n 's/…/…/p'` · `awk` · `sort | uniq -c | sort -rn` · `zeek-cut` · `nfdump`
{ .kw-cs-top }

## Sous-rubriques

| Sous-rubrique | Ce qu'on y trouve |
|---|---|
| [**Pare-feu, NetFlow et VPN**](pare-feu-vpn.md) | Filtrer par IP, port, action ; scans ; volumes sortants ; plus gros flux ; connexions VPN d'un utilisateur |
| [**Proxy et DNS**](proxy-dns.md) | Requêtes bloquées, gros envois ; domaines interrogés, tunneling DNS, DGA, modifications sur un serveur DNS Windows |
| [**IDS / IPS et WAF**](ids-waf.md) | Alertes par signature et par source ; attaques web par type ; ce que le WAF a laissé passer |
| [**Logs web**](web.md) | IP les plus actives, URL, codes, User-Agents ; injections et traversées ; brute force sur une page de connexion |

## Vue d'ensemble : quelle source pour quelle question

| Question | Source | Sous-rubrique |
|---|---|---|
| Qui a parlé à qui, sur quel port, avec quel volume ? | Pare-feu, NetFlow | [Pare-feu, NetFlow et VPN](pare-feu-vpn.md) |
| Qui s'est connecté à distance, et depuis où ? | VPN (`remip`, `tunnelip`, `user`) | [Pare-feu, NetFlow et VPN](pare-feu-vpn.md) |
| Quelle URL, quel utilisateur, autorisé ou bloqué ? | Proxy | [Proxy et DNS](proxy-dns.md) |
| Quel poste a voulu joindre quel domaine ? | DNS | [Proxy et DNS](proxy-dns.md) |
| Quelle attaque a été tentée, et a-t-elle été bloquée ? | IDS / IPS, WAF | [IDS / IPS et WAF](ids-waf.md) |
| Qu'a reçu et renvoyé le serveur web ? | Logs web | [Logs web](web.md) |

Les journaux du poste lui-même (pare-feu Windows, Defender, PowerShell…) sont dans la fiche Windows [Journaux et événements](../../../windows/fondamentaux/logs/index.md).

Pour comprendre : [Analyse des journaux réseau (Network Log Analysis)](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/index.md) · [Synthèse : quelle source pour quelle question](../../../../library/it/reseau/analyse-des-journaux-reseau-network-log-analysis/09-synthese-quelle-source-pour-quelle-question.md)
{ .kw-cs-meta }
