---
title: Chapitre 4 — Sécurité du Wi-Fi et des accès distants
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Infrastructure IT.md
note: Infrastructure IT
up:
- - Infrastructure IT
  - ../index.md
- - Partie I — Réseau, protocoles et services fondamentaux
  - index.md
---

**Wi-Fi :** WPA2-Personal (clé partagée — acceptable pour le domicile, pas pour l'entreprise), WPA2-Enterprise (802.1X/RADIUS — chaque utilisateur s'authentifie avec ses credentials AD, le seul mode acceptable en entreprise), WPA3 (SAE — résistant au brute force offline, adoption en cours). Les attaques (rogue AP — faux point d'accès, evil twin — copie du SSID légitime pour capturer les credentials). La segmentation du Wi-Fi guest (réseau isolé sans accès au LAN, uniquement Internet).

**Accès distants :** le VPN (split tunneling — seul le trafic vers l'entreprise passe par le VPN vs full tunneling — tout le trafic passe par le VPN, plus sécurisé ; MFA obligatoire sur le VPN ; le VPN comme surface d'attaque APT majeure — Ivanti, Fortinet, Pulse Secure exploités systématiquement — cf. cours APT Ch.3). Le RDP (Remote Desktop Protocol — port 3389, risques : BlueKeep CVE-2019-0708, brute force, exposition directe sur Internet = compromission quasi certaine ; bonnes pratiques : NLA — Network Level Authentication, restriction des sources, accès via bastion uniquement, jamais directement exposé). Le SSH (clés vs mots de passe — les clés sont plus sécurisées, PasswordAuthentication no dans sshd_config ; port non standard pour réduire le bruit ; fail2ban pour bloquer le brute force).

---
