---
title: Questions essentielles
source: IT/03_Networking/Infrastructure_IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - index.md
---

- **Question :** Décrivez l'architecture réseau type d'une entreprise.
  - **Réponse type :** On a généralement un firewall externe côté Internet, puis une DMZ qui héberge les services exposés (reverse proxy, bastion, VPN), un firewall interne, et le LAN avec les serveurs, l'AD, les bases de données. Les postes utilisateurs sont dans un réseau séparé. On ajoute un réseau de management isolé pour l'administration des équipements. L'idée c'est la défense en profondeur avec des zones de confiance décroissante.

- **Question :** Pourquoi la segmentation réseau est-elle fondamentale ?
  - **Réponse type :** Sans segmentation, un attaquant qui compromet un poste utilisateur peut atteindre directement le contrôleur de domaine, le vCenter, les sauvegardes — le blast radius est maximal. La segmentation via VLANs et firewalls inter-zones limite le mouvement latéral. C'est la mesure la plus efficace contre la propagation d'un ransomware ou d'un attaquant dans le réseau.

- **Question :** Quels sont les mécanismes anti-phishing côté infrastructure email ?
  - **Réponse type :** Il y a trois enregistrements DNS complémentaires : SPF qui liste les serveurs autorisés à envoyer pour le domaine, DKIM qui signe les mails cryptographiquement, et DMARC qui définit la politique si SPF ou DKIM échoue — none, quarantine ou reject. Les trois sont indispensables et complémentaires. En plus, on met une email gateway qui analyse les URLs, sandboxe les pièces jointes, et réécrit les liens.

- **Question :** Expliquez la règle 3-2-1 des sauvegardes et les erreurs courantes.
  - **Réponse type :** 3 copies des données, sur 2 supports différents, dont 1 hors site. L'erreur la plus critique, c'est le NAS de sauvegarde joint au domaine AD — en cas de ransomware, les sauvegardes sont chiffrées avec le reste. Autres erreurs : pas de test de restauration, même compte admin partout, pas de sauvegardes immuables (WORM). Les sauvegardes doivent être isolées du réseau standard et régulièrement testées.

- **Question :** C'est quoi le Zero Trust et en quoi ça diffère du modèle traditionnel ?
  - **Réponse type :** Le modèle traditionnel fait confiance au réseau interne — une fois à l'intérieur du périmètre, on accède à tout. Le Zero Trust part du principe que personne n'est de confiance par défaut, même en interne. Chaque accès est vérifié : identité forte (MFA), état du poste (conformité), moindre privilège, micro-segmentation. Le VPN est remplacé par des solutions d'accès conditionnel. C'est particulièrement pertinent avec le télétravail et le cloud.


## Questions complémentaires

- **Question :** Quelle est la différence entre un firewall stateful et un NGFW ?
  - **Réponse type :** Le firewall stateful suit les connexions et filtre sur IP/port — il sait si un paquet fait partie d'une connexion initiée depuis l'intérieur. Le NGFW ajoute l'inspection applicative : il peut identifier les applications même sur des ports non standards, faire du filtrage URL, de l'IPS intégré, de l'inspection TLS, et du sandboxing. C'est le standard en entreprise aujourd'hui.

- **Question :** Pourquoi le management plane est-il critique et souvent négligé ?
  - **Réponse type :** Les interfaces d'administration — iLO, iDRAC, vCenter — permettent un contrôle total sur l'infrastructure physique, même si l'OS est éteint. Le problème c'est qu'elles sont souvent sur le même réseau que les utilisateurs, avec des mots de passe par défaut. Un attaquant qui y accède peut tout contrôler. La solution c'est un réseau de management dédié, accessible uniquement via le bastion.

- **Question :** Quelles différences entre OAuth, SAML et OIDC ?
  - **Réponse type :** SAML est le plus ancien, basé sur XML, utilisé pour le SSO d'entreprise vers des applications web. OAuth 2.0 est un protocole d'autorisation (pas d'authentification) — il délivre des tokens d'accès. OIDC est une couche d'authentification construite sur OAuth 2.0, basée sur JSON/JWT — c'est le standard moderne pour le SSO, utilisé par Google, Microsoft, etc.


## Questions les plus probables en entretien

1. Architecture réseau type d'entreprise ?
2. Pourquoi segmenter le réseau ?
3. SPF, DKIM, DMARC — à quoi ça sert ?
4. Règle 3-2-1 et erreurs de sauvegarde ?
5. C'est quoi le Zero Trust ?
6. Firewall stateful vs NGFW ?
