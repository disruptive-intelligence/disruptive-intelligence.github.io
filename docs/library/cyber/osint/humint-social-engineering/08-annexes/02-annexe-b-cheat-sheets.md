---
title: Annexe B — Cheat sheets
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Annexes
  - index.md
---

## B.1 Pretextes classiques par vecteur

| Vecteur | Pretexte | Levier psychologique | Cible type |
|---|---|---|---|
| **Phishing** | Mise à jour portail RH | Obligation, urgence | Tous employés |
| **Phishing** | Invitation conférence | Curiosité, ego | Cadres, ingénieurs |
| **Phishing** | Facture / bon de commande | Routine, urgence | Comptabilité, achats |
| **Phishing** | Partage de document OneD/SharePoint | Normalité, confiance | Utilisateurs M365 |
| **Vishing** | Support IT — incident de sécurité | Autorité, peur, urgence | Tous employés |
| **Vishing** | Prestataire — intervention planifiée | Autorité, normalité | Helpdesk, réception |
| **Vishing** | Direction — demande urgente | Autorité, urgence, pression | DAF, assistants |
| **Vishing** | Recruteur — opportunité de carrière | Ego, cupidité | Ingénieurs, cadres |
| **Physique** | Technicien prestataire IT | Autorité, normalité | Gardien, réception |
| **Physique** | Inspecteur (incendie, qualité) | Autorité | Gardien, employés |
| **Physique** | Employé autre site | Normalité, sympathie | Employés, réception |
| **Élicitation** | Chercheur universitaire intéressé | Flatterie, réciprocité | Ingénieurs R&D |
| **Élicitation** | Consultant secteur / networking | Réciprocité, normalité | Cadres en salon |
| **Smishing** | Notification livraison | Curiosité, urgence | Tous |

## B.2 Signaux d'alerte par technique

| Technique | Signaux d'alerte |
|---|---|
| **Phishing** | Expéditeur externe avec display name interne, urgence excessive, URL raccourcie ou lookalike, demande de credentials, pièce jointe inattendue |
| **Vishing** | Appel non sollicité demandant des informations sensibles, urgence, impossibilité de rappeler sur un numéro vérifié, name-dropping non vérifiable |
| **BEC** | Demande de virement urgente par email, confidentialité exigée, changement d'IBAN, pression hiérarchique anormale |
| **Intrusion physique** | Personne inconnue sans badge visible, pretexte de prestataire non vérifié, tentative de tailgating, comportement hésitant |
| **Élicitation** | Questions inhabituellement spécifiques, flatterie excessive, réciprocité forcée, transition vers canal privé, profil difficile à vérifier |

## B.3 Checklist red team SE

- [ ] Lettre de mission signée par représentant habilité
- [ ] Rules of engagement documentées
- [ ] Scope (sites, employés, vecteurs, limites) défini
- [ ] Protocole d'urgence (safe word, contact de référence)
- [ ] Reconnaissance OSINT complétée
- [ ] Reconnaissance physique complétée
- [ ] Pretextes construits (principal + secours)
- [ ] Infrastructure technique déployée
- [ ] OPSEC praticien validé (légendes, compartimentation)
- [ ] Matériel préparé
- [ ] Documentation en temps réel planifiée
- [ ] Rapport final livré avec recommandations P0/P1/P2
- [ ] Debriefing commanditaire réalisé
- [ ] Implants physiques retirés
- [ ] Données de test détruites après livraison

---
