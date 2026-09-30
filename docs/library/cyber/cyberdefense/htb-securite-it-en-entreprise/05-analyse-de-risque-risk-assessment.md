---
title: Analyse de risque — Risk Assessment
source: Cyber/04_Hardening/HTB_Sécurité IT en entreprise.md
note: HTB — Sécurité IT en entreprise
up:
- - HTB — Sécurité IT en entreprise
  - index.md
---

- Les **Risk Assessments** servent à identifier et prioriser les risques afin d’allouer les ressources et investissements de sécurité là où ils sont les plus importants.
- Une analyse de risque prend généralement en compte :

```
Risk ≈ Likelihood × Impact
```

→ probabilité qu’un événement se produise + conséquences pour l’organisation.
## Retour en service — Recovery Priority

- L’entreprise doit déterminer **quels systèmes/services doivent être restaurés en priorité** après un incident.
- Cette analyse permet également d’évaluer :
    - l’impact d’une interruption ;
    - la durée maximale d’indisponibilité acceptable ;
    - les dépendances entre systèmes.
- Exemple :

```
Incident majeur
   ↓
1. Identity / AD
2. Network / DNS
3. ERP / applications critiques
4. Services secondaires
```

## Business Impact Analysis — BIA

- Cette démarche correspond notamment à une **BIA — Business Impact Analysis** :
	- identifier les processus critiques ;
	- mesurer l’impact de leur indisponibilité ;
	- déterminer leurs priorités de restauration.
- Elle permet notamment de définir :

|Concept|Signification|
|---|---|
|**RTO**|Temps maximal acceptable avant restauration du service|
|**RPO**|Quantité maximale de données que l’on accepte de perdre|

## Risques liés aux réseaux connectés

- Toute connexion à l’infrastructure crée une **relation de confiance** et donc une surface de risque supplémentaire.
- Cela concerne :
    - autres entités du groupe ;
    - partenaires ;
    - prestataires ;
    - fournisseurs ;
    - services cloud.

```
Company A ← VPN / API / Network Link → Partner B
                              ↓
                     risque transférable
```

- Une compromission du partenaire peut devenir un point d’entrée vers votre propre infrastructure.
## Third-Party Risk

- Il faut évaluer le niveau de sécurité des partenaires avant et pendant la relation.
- Points à vérifier :
	- rapidité d’application des correctifs ;
	- politique de gestion des vulnérabilités ;
	- configuration sécurisée des VPN ;
	- gestion des certificats ;
	- MFA et contrôle des accès ;
	- sécurité des services exposés ;
	- configuration des solutions cloud ;
	- journalisation et capacité de réponse aux incidents.

```
Votre sécurité
≠ seulement votre infrastructure

Votre sécurité
→ dépend aussi des tiers qui y ont accès
```

## VPN & certificats

- Les équipements VPN doivent être correctement configurés.
- Éviter les certificats/configurations par défaut pouvant :
    - affaiblir l’authentification ;
    - révéler une mauvaise configuration ;
    - faciliter certaines attaques selon le produit.

→ les certificats doivent être **propres à l’organisation**, valides et correctement gérés.
## Accès partenaires

- Le principe de **Least Privilege** s’applique également aux tiers.

```
Partner
→ uniquement les systèmes nécessaires
→ uniquement les ports/services nécessaires
→ uniquement pendant la durée nécessaire
```

- Mesures utiles :
	- segmentation réseau ;
	- comptes dédiés ;
	- MFA ;
	- accès temporaires si possible ;
	- monitoring renforcé ;
	- révocation immédiate lorsque l’accès n’est plus nécessaire.
## Réévaluation du risque

- Une analyse de risque n’est pas définitive.
- Elle doit être réévaluée notamment lors de :
	- nouvelle vulnérabilité critique ;
	- changement d’architecture ;
	- ajout d’un partenaire ;
	- nouvelle connexion réseau ;
	- migration cloud ;
	- incident de sécurité chez un fournisseur.
