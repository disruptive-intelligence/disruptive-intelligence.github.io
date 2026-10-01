---
title: 'Chapitre 97 — Cas pratique : société opaque'
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE XII — Production, transmission et cas pratiques
  - index.md
---

## 97.1 Présentation du cas

Une banque mandate l'analyste pour due diligence sur un nouveau client : une société immatriculée à Limassol (Chypre), dont l'UBO déclaré semble peu transparent. Avant d'ouvrir le compte, due diligence approfondie.

## 97.2 Étape 1 — Identification

**Société.** « Apollo Trading Ltd ». Companies Registry CY : immatriculée 09/2024, capital 1000 €, activité « general trading and consulting », adresse Limassol.

**Director.** « Andreas Antoniou », résidence Limassol.

**UBO déclaré.** « Petros Sokratis », résidence à Limassol (selon registre UBO CY accessible).

## 97.3 Étape 2 — Profilage du UBO

**Recherche « Petros Sokratis » Chypre.**

- Aucun profil LinkedIn vérifiable.
- Aucune mention presse.
- Aucune autre société immatriculée à son nom.

**Photo / identité.** Aucune photo trouvable.

**Conclusion préliminaire.** Profil suspectment minimaliste. Possible identité nominee.

## 97.4 Étape 3 — Profilage du director

**Recherche « Andreas Antoniou » Chypre.**

- Plusieurs profils correspondant (homonymie).
- Filtrage : un certain Andreas Antoniou est administrateur de 247 sociétés selon OpenCorporates.

**Conclusion.** Director est probablement un nominee professionnel.

## 97.5 Étape 4 — Adresse de domiciliation

**24 Athinon Street, Limassol.** OpenCorporates : 312 autres sociétés enregistrées à cette adresse.

**Conclusion.** Registered agent typique. Anonymisation.

## 97.6 Étape 5 — Search dans ICIJ leaks

**Cyprus Confidential.** Recherche : « Apollo Trading » → pas de hit. « Petros Sokratis » → pas de hit. « Andreas Antoniou » → trop de hits (homonymie).

**Pas de leak révélateur.**

## 97.7 Étape 6 — OpenCorporates cross-search

**Cross-recherche.** Le director « Andreas Antoniou » à 24 Athinon Street est administrateur de 247 sociétés.

**Analyse de ces 247.** Filtres par activité similaire (trading, consulting) → 84 sociétés.

**Sociétés liées plausibles.** 12 d'entre elles ont des noms semblables à Apollo Trading (Apollo Marketing, Apollo Logistics, Apollo Properties, etc.).

**Hypothèse.** Cluster de sociétés liées sous structure nominee commune. UBO réel peut être unique acteur derrière 12 sociétés.

## 97.8 Étape 7 — Réseau et empreinte

**Recherche du nom « Apollo Trading » dans presse internationale.**

- Pas de mention récente.
- Une mention dans un site russe d'analyse économique : Apollo Trading aurait été partenaire commercial d'une entreprise russe sanctionnée.

**Cross-recherche.** Cette entreprise russe est-elle sanctionnée ? OpenSanctions : oui, depuis 2023, sanctions UE pour contournement.

**Conclusion partielle.** Lien probable Apollo → entreprise sanctionnée. Risque sérieux pour la banque.

## 97.9 Étape 8 — Synthèse

**Conclusion globale.**

> **BLUF.** Apollo Trading Ltd présente un profil hautement opaque (capital symbolique, director nominee, UBO superficiel, adresse registered agent partagée, cluster de 12 sociétés liées). Une mention publique partielle suggère un lien commercial avec une entreprise russe sanctionnée. **Recommandation : refus d'ouverture de compte ou KYC renforcé avec demande de pièces complémentaires** (justificatifs UBO, audit indépendant). Niveau de risque : élevé.

**Cotation.** B2 globale (faisceau d'indices convergents).

## 97.10 Pédagogie

Ce cas illustre :

- Investigation corporate avec sources publiques (Pappers, OpenCorporates, ICIJ).
- Détection de nominee professionnels.
- Cross-recherche par adresse de domiciliation pour cluster.
- Importance du screening sanctions sur **partenaires** commerciaux.
- Recommandation actionnable proportionnée.

## 97.11 Variantes du cas

**Variante 1 — Holding luxembourgeoise.** Société dont la structure de détention passe par holding luxembourgeoise. Plus accessible que BVI (registre UBO partiel post-CJUE) mais structure profonde possible. Approfondir avec : RCS Luxembourg + LBR.lu + leaks ICIJ.

**Variante 2 — Trust irrévocable.** Société dont UBO formel est trustee d'un trust. Le bénéficiaire effectif est masqué par trust. ICIJ Pandora Papers riche en trusts. Pour OSINT, identifier le settlor, les trustees, les beneficiaries (souvent partiellement révélés dans leaks).

**Variante 3 — Cluster de sociétés liées.** Plusieurs sociétés apparemment indépendantes mais liées par : même registered agent, même director nominee, même infrastructure web (sites partageant trackers), même adresse de domiciliation. Investigation par cross-recherche OpenCorporates et Aleph.

**Variante 4 — Société de façade pour pays sanctionné.** Société européenne servant d'intermédiaire pour entreprise iranienne / russe sanctionnée. Détectable par : analyse des partenaires commerciaux mentionnés en presse, signaux de contournement (changements fréquents de dirigeants, structures multi-couches).

## 97.12 Niveaux de risque corporate

Pour standardiser l'évaluation, **échelle de risque** structurée :

| Niveau | Indicateurs typiques | Recommandation |
|---|---|---|
| Très faible | Société transparente, dirigeants identifiés, comptes publiés cohérents, sanctions clean, adverse media absent | Onboarding standard |
| Faible | Quelques zones d'ombre (filiale offshore raisonnable, dirigeant peu public mais identifiable) | Onboarding avec questions complémentaires |
| Modéré | Opacité partielle, nominee suspectée, juridiction grise | KYC renforcé, justificatifs UBO |
| Élevé | Multi-couches offshore, registered agents communs, signaux d'alerte multiples | KYB approfondi, audit indépendant |
| Très élevé | Lien probable sanctions, contentieux multiples, opacité totale | Refus d'engagement ou escalade conformité |

## 97.13 Workflow due diligence intégrée

Pour due diligence approfondie (au-delà du triage initial) :

1. **Identification formelle** : numéro entreprise unique, juridiction.
2. **Cartographie structurelle** : forme, capital, dates, dirigeants, UBO déclaré.
3. **Cross-références** : leaks ICIJ, registre national, OpenCorporates.
4. **Adverse media** : presse multi-langues sur 5 ans.
5. **Contentieux** : recherches juridictions principales.
6. **Sanctions / PEP** : entité + dirigeants + UBO + actionnaires.
7. **Réseau** : sociétés liées via dirigeants partagés.
8. **Activité réelle** : comparaison déclaration / observable (site web, presse, références clients).
9. **Indicateurs financiers** : comptes publiés, évolution.
10. **Infrastructure web** : domaine, hébergement, technologies.
11. **Risque géopolitique** : juridiction(s) impliquées, contexte.
12. **Synthèse cotée** : décision proportionnée.

-----
