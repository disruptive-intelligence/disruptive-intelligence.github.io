---
title: Réponses flash
source: IT/03_Networking/Infrastructure_IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

- **Architecture réseau** → Internet → FW → DMZ → FW → LAN (serveurs, AD) + réseau management séparé.
- **Segmentation** → VLANs + filtrage inter-zones. Sans ça = flat network = blast radius maximal.
- **SPF/DKIM/DMARC** → SPF = serveurs autorisés. DKIM = signature. DMARC = politique. Les trois ensemble.
- **Sauvegardes** → 3-2-1. Immuable (WORM). Hors domaine AD. Tester la restauration.
- **Zero Trust** → Aucune confiance par défaut, vérification continue, MFA, moindre privilège, micro-segmentation.
- **NGFW** → Stateful + inspection applicative, filtrage URL, IPS, inspection TLS.
- **Management plane** → iLO/iDRAC/vCenter = contrôle total. Réseau dédié, jamais sur le LAN utilisateur.

---

> **Note de clôture**
>
> Ce cours a été conçu comme le socle technique de la bibliothèque — la cartographie du terrain sur lequel les analystes SOC détectent, les incident responders interviennent, les pentesters attaquent, et les architectes construisent.
>
> L'opération BACKBONE illustre une vérité opérationnelle : la majorité des compromissions n'exploitent pas des vulnérabilités exotiques — elles exploitent des fondamentaux négligés. Un mot de passe par défaut sur le vCenter. Un flat network sans segmentation. Un NAS de sauvegarde joint au domaine. Un NTP désynchronisé qui rend les logs inutilisables. Un iLO accessible depuis le réseau utilisateur. Un VPN non patché. Ce sont ces « détails » d'infrastructure qui font la différence entre une organisation résiliente et une organisation qui paye une rançon.
>
> Le cours assume une conviction : comprendre l'infrastructure est la compétence la plus fondamentale en cybersécurité. Avant de détecter, il faut savoir ce qui génère les logs. Avant de répondre, il faut savoir sur quoi on intervient. Avant d'auditer, il faut savoir ce qu'on regarde. Et avant de protéger, il faut savoir ce qu'on défend.
>
> *Comprendre le terrain • Cartographier les surfaces • Durcir les fondations — parce que la sécurité commence par l'infrastructure.*
