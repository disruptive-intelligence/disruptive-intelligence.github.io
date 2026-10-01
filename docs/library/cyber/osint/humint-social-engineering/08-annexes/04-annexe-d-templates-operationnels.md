---
title: Annexe D — Templates opérationnels
source: Cyber/02 OSINT/HUMINT & social engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Annexes
  - index.md
---

## D.1 Structure de lettre de mission red team SE

1. Identification des parties (commanditaire, prestataire, testeurs nommés)
2. Objet de la mission
3. Scope géographique (sites concernés)
4. Scope humain (employés concernés — tous ou profils spécifiques)
5. Vecteurs autorisés (phishing, vishing, smishing, intrusion physique, élicitation)
6. Techniques exclues (chantage, exploitation de vulnérabilités personnelles, etc.)
7. Durée de la mission (dates de début et de fin)
8. Objectifs mesurables
9. Protocole d'urgence (safe word, contact de référence joignable 24/7)
10. Confidentialité des résultats individuels
11. Livrables attendus (rapport, restitution)
12. Conditions financières
13. Signatures (commanditaire habilité, prestataire)

## D.2 Fiche de signalement d'un incident de social engineering

- Date et heure de l'incident / de la tentative
- Vecteur (email, téléphone, physique, messagerie, autre)
- Description de l'incident (qui, quoi, quand, comment)
- Actions effectuées par l'employé (a cliqué, a transmis des informations, a donné un accès)
- Informations sur l'attaquant (nom affiché, numéro de téléphone, adresse email, description physique)
- Impact potentiel (credentials compromis, information divulguée, accès accordé)
- Actions correctives immédiates prises
- Signalement transmis à (SOC, RSSI, manager)

## D.3 Checklist de protection en salon professionnel

**Avant le départ :**

- [ ] Brief avec le RSSI : messages autorisés, informations interdites
- [ ] Identification des interlocuteurs à risque (pays, secteurs, profils)
- [ ] Dispositifs numériques sécurisés (téléphone dédié si risque élevé, VPN, chiffrement)
- [ ] Cartes de visite avec informations limitées (pas de numéro personnel)

**Pendant le salon :**

- [ ] Ne jamais laisser un dispositif sans surveillance
- [ ] Ne pas discuter de projets sensibles en public
- [ ] Appliquer les techniques de contre-élicitation si nécessaire (pont, déviation, réponse vague)
- [ ] Noter les contacts inhabituels (nom, entreprise, questions posées)

**Au retour :**

- [ ] Debriefing avec le RSSI
- [ ] Signalement des contacts suspects
- [ ] Vérification des dispositifs numériques (pas de malware, pas de modification)

## D.4 Grille de formation par profil de risque

| Profil | Menaces prioritaires | Contenu de formation | Fréquence | Format |
|---|---|---|---|---|
| Tous employés | Phishing, tailgating | Sensibilisation générale, signalement | Annuelle | E-learning + simulation |
| DAF / Comptabilité | BEC, fraude fournisseur | Processus de vérification, callback | Semestrielle | Atelier + simulation |
| Helpdesk | Pretexting, MFA manipulation | Vérification d'identité renforcée | Trimestrielle | Exercice vishing |
| Ingénieurs R&D | Élicitation, faux recruteurs | Contre-élicitation, protection en salon | Annuelle | Atelier interactif |
| Réception / Sécurité | Intrusion physique, impersonation | Vérification visiteurs, refus poli | Semestrielle | Exercice pratique |
| Dirigeants | Ciblage personnel, deepfake, spear-phishing | Surface d'exposition, sécurité des communications | Annuelle | Briefing individuel |

---
