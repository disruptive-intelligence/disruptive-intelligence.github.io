---
title: Réponses flash
source: IT/03_Networking/AppSec.md
note: AppSec
up:
- - AppSec
  - index.md
---

- **Injection SQL** → Input interprété comme code. Fix = prepared statements / ORM. Jamais de concaténation.
- **IDOR** → Changement d'ID → accès non autorisé. Fix = vérification d'autorisation côté serveur sur chaque endpoint.
- **XSS** → JS injecté dans la page. Fix = output encoding, HttpOnly, CSP avec nonces.
- **DevSecOps** → Sécurité dans le CI/CD : SAST (code), SCA (dépendances), DAST (scan dynamique), secrets detection.
- **Supply chain** → Dépendances compromises. Fix = lockfiles, registre privé, SCA, SBOM, signature.
- **Threat modeling** → STRIDE, DFD, trust boundaries. Atelier en amont du développement.
- **LLM security** → Prompt injection, insecure output, excessive agency. Traiter la sortie LLM comme source non fiable.

---

> **Note de clôture**
>
> Ce cours a été conçu pour enseigner la sécurité applicative comme une discipline complète — du code à la production, de l'attaque à la défense, de la vulnérabilité individuelle au programme d'entreprise.
>
> SecureHealth illustre une transformation que toute organisation peut réaliser : en 12 mois, une équipe sans référent sécurité est passée de 3 vulnérabilités critiques à un score SAMM de 2.0/3, un pipeline DevSecOps complet, des Security Champions formés, un bug bounty actif, et la capacité de détecter et contenir un incident supply chain en 48 heures. Le coût : 50-150K€/an. Le coût de ne rien faire : 4-10M€ par breach.
>
> Le cours assume trois convictions. Première : l'AppSec ne s'arrête pas au secure coding — elle couvre la prévention, la vérification, la détection et la gouvernance. Un code parfaitement sécurisé déployé dans un environnement mal configuré, sans logging, et sans processus de gestion des vulnérabilités est un incident en attente. Deuxième : les surfaces d'attaque évoluent — la supply chain logicielle, les applications intégrant de l'IA, et les environnements cloud-native sont les terrains de 2025-2026, et ce cours les couvre. Troisième : la défense en profondeur fonctionne — chaque couche (code, tests, WAF, monitoring, IR) est contournable individuellement, mais les empiler force l'attaquant à dépenser plus de temps et à générer plus de signaux.
>
> *Comprendre la vulnérabilité • Écrire le code qui la prévient • Détecter l'attaque qui l'exploite • Construire le programme qui pérennise la sécurité.*
