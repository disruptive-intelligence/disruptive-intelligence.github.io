---
title: 5) DNS / VPN / Protocoles
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

---

- **Question : Quels sont les différents mécanismes autour du DNS : DNSSEC, DoH, DoT ?**
  **Réponse type :** DNSSEC (DNS Security Extensions) ajoute de la signature cryptographique aux réponses DNS — ça garantit l'authenticité et l'intégrité de la réponse (pas de spoofing), mais ça ne chiffre PAS la requête. DoT (DNS over TLS, port 853) chiffre les requêtes DNS dans un tunnel TLS — le contenu est confidentiel, mais le FAI voit qu'on utilise le port 853. DoH (DNS over HTTPS, port 443) encapsule les requêtes DNS dans du HTTPS — le trafic se mélange avec le trafic web normal, impossible à distinguer et à bloquer. En résumé : DNSSEC = intégrité, DoT/DoH = confidentialité. Ils sont complémentaires.

- **Question : Quelle différence entre un VPN IPsec et un VPN SSL ?**
  **Réponse type :** IPsec fonctionne au niveau réseau (couche 3) — il crée un tunnel entre deux réseaux et donne accès à tout le réseau distant comme si on était branché localement. C'est utilisé pour le site-to-site et le remote access d'entreprise. Le VPN SSL/TLS fonctionne au niveau applicatif (couche 7) — il donne accès à des applications spécifiques via le navigateur ou un client léger. C'est plus simple à déployer (passe les firewalls car c'est du HTTPS sur le port 443) mais moins flexible. IPsec offre un accès réseau complet, SSL/TLS offre un accès granulaire par application.

- **Question : Comment fonctionne un VPN IPsec dans les grandes lignes ?**
  **Réponse type :** En deux phases. Phase 1 (IKE SA) : les deux extrémités négocient les paramètres de sécurité (algorithmes, authentification), s'authentifient mutuellement (clé pré-partagée ou certificat), et établissent un canal sécurisé pour la négociation. Phase 2 (IPsec SA) : dans ce canal sécurisé, elles négocient les paramètres du tunnel de données (algorithmes de chiffrement et d'intégrité, durée de vie). Ensuite le tunnel est établi et le trafic est chiffré — soit en mode tunnel (tout le paquet IP est encapsulé — utilisé pour le site-to-site), soit en mode transport (seul le payload est chiffré — utilisé entre deux hôtes).

- **Question : Comment fonctionne un VPN SSL/TLS dans les grandes lignes ?**
  **Réponse type :** Il établit un tunnel chiffré au-dessus de TLS, comme un site HTTPS. Le client se connecte au concentrateur VPN sur le port 443, le handshake TLS s'effectue (certificat serveur, échange de clés ECDHE, clé de session). Une fois le tunnel établi, le trafic est chiffré en AES-GCM. Deux modes : le portail web (accès à des applications via le navigateur, sans client) ou le tunnel complet (avec un client comme OpenVPN ou AnyConnect, qui route tout le trafic ou une partie via le tunnel). L'avantage c'est que le port 443 est rarement bloqué par les firewalls.

---
