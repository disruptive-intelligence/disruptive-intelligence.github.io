---
title: Annexe B — Modèle de cartographie vierge
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Annexes
  - index.md
---

## Types d'entités (nœuds)

| Catégorie | Couleur | Exemples | Attributs standard |
|-----------|---------|----------|-------------------|
| Personne / Pseudo | Bleu | Pseudo, alias, identité réelle | Pseudo principal, plateformes, fuseau horaire, confiance |
| Organisation | Vert | Groupe RaaS, société écran, forum | Nom, type, pays, statut (actif/inactif) |
| Infrastructure technique | Orange | Domaine, IP, serveur, C2, certificat | Identifiant, hébergeur, ASN, dates |
| Objet financier | Jaune | Wallet, cluster, exchange, mixer | Adresse, blockchain, volume, attribution |
| Espace relationnel | Violet | Forum, canal Telegram, leak site | Nom, plateforme, nb membres, accès |

## Types de relations (arêtes)

| Type | Style visuel | Exemples |
|------|-------------|----------|
| Technique | Trait orange | Même IP, même certificat, même builder |
| Financier | Trait jaune, directionnel | Transfert de crypto, paiement de service |
| Identitaire | Trait bleu | Même email, même clé PGP, même pseudo |
| Social | Trait vert | Conversation, vouching, recommandation |
| Temporel | Trait gris pointillé | Séquence d'événements, corrélation temporelle |
| Narratif | Trait violet | Même narratif, même campagne d'influence |

## Qualification des liens

| Axe | Valeurs | Signification |
|-----|---------|---------------|
| Direction | Direct / Indirect | Avec ou sans intermédiaire |
| Force | Fort / Modéré / Faible | Spécificité de l'indice |
| Nature | Contextuel / Structurel | Ponctuel ou durable |
| Confiance | A1 à F6 | Cotation source × information |

---
