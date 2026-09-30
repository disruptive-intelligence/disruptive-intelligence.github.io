---
title: 'Chapitre 40 — Scénarios d''incident : atelier de synthèse'
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VIII — Post-incident, maturité ET capitalisation
  - index.md
---

*Ce chapitre est conçu comme un atelier de synthèse — une mise en pratique transversale de toute la méthodologie IR enseignée dans le cours. Chaque scénario applique le processus complet : détection → qualification → investigation → confinement → éradication → reprise → RETEX. L'objectif n'est pas d'ajouter de la matière théorique nouvelle, mais de démontrer la polyvalence de la méthode sur des types d'incidents aux dynamiques distinctes.*

---

## 40.1 Scénario 1 — Ransomware avec double extorsion (synthèse BLACKTIDE)

Synthèse intégrée du fil rouge, structurée comme un cas d'étude autonome avec les décisions clés à chaque étape. Focus sur les arbitrages spécifiques au ransomware : timing du confinement (course contre le chiffrement), gestion de la double extorsion (l'exfiltration est irréversible — payer ne la « dé-fait » pas), décision sur la rançon (tableau d'aide à la décision avec critères : sauvegardes disponibles ?, survie de l'entreprise en jeu ?, données irremplaçables ?, opérateur sanctionné ?), et reconstruction sans paiement (cercles de confiance, restauration depuis bandes).

## 40.2 Scénario 2 — Compromission de messagerie (BEC)

Un directeur financier d'une ETI française reçoit un email de son CEO demandant un virement urgent de 2,3 M€ vers un compte à Hong Kong. L'email provient du vrai compte M365 du CEO — compromis par un phishing 3 jours plus tôt. L'investigation via les Unified Audit Logs révèle : connexion depuis une IP nigériane, création d'une règle de forwarding (tous les emails du CFO redirigés vers une boîte externe), et envoi de 12 emails frauduleux à des partenaires bancaires. Confinement : désactivation du compte CEO, révocation de tous les tokens, suppression de la règle de forwarding, alerte aux banques. L'investigation montre que le phishing initial a exploité une absence de MFA (le CEO avait refusé le MFA pour « raisons de praticité »). Le virement a été bloqué par la banque (procédure de confirmation téléphonique pour les virements internationaux > 500 K€). RETEX : MFA obligatoire pour tous, sans exception, y compris la direction.

## 40.3 Scénario 3 — Exfiltration de données / espionnage

Une entreprise de biotechnologie française est alertée par un partenaire : des données de R&D confidentielles circulent sur un forum underground. L'investigation révèle un dwell time de 8 mois — un implant RAT installé via une clé USB trouvée dans le parking (social engineering physique). L'attaquant a exfiltré lentement (quelques centaines de Mo par semaine) via DNS tunneling, en dessous de tous les seuils d'alerte. L'AD n'est pas compromis (l'attaquant est resté avec des privilèges utilisateur standard sur un poste R&D). Confinement : isolation du poste, blocage du domaine de tunneling DNS. Le scénario illustre l'importance du NDR (le DNS tunneling aurait été détectable) et des règles DLP (l'accès massif aux fichiers R&D depuis un seul poste sur 8 mois aurait pu être alerté).

## 40.4 Scénario 4 — Compromission supply chain

Un éditeur de logiciel de supervision industrielle publie une mise à jour contenant un implant malveillant (à la SolarWinds). L'implant est découvert 3 semaines après la mise à jour, quand un CERT sectoriel publie un advisory. 200 clients sont potentiellement touchés. L'investigation dans chaque organisation cliente doit déterminer : la mise à jour a-t-elle été installée ?, l'implant a-t-il été activé (communication C2 observée) ou est-il dormant ?, si activé, quelles actions l'attaquant a-t-il menées ? Le scénario illustre la complexité de l'IR supply chain : le périmètre est vaste (centaines de clients), la coordination avec l'éditeur est critique, et chaque client doit mener sa propre investigation.

## 40.5 Scénario 5 — Insider threat

Un ingénieur R&D annonce sa démission pour rejoindre un concurrent. Après son départ, un audit DLP révèle : 50 Go de documentation technique copiée sur une clé USB dans les 2 semaines précédant le départ, et un upload de 15 Go vers un compte Google Drive personnel depuis le réseau d'entreprise. L'investigation forensic (analyse du poste, des logs DLP, des logs proxy) confirme les transferts. Le scénario illustre les spécificités de l'insider threat : les accès sont légitimes (pas de mouvement latéral classique), l'investigation est autant RH/juridique que technique, la gestion de la preuve doit être compatible avec une procédure disciplinaire ou pénale (vol de secrets de fabrication — article L.1227-1 du Code du travail et articles L.621-1 et suivants du Code de la propriété intellectuelle), et la communication interne est extrêmement sensible (pas de witch hunt, pas de rumeurs).

---
