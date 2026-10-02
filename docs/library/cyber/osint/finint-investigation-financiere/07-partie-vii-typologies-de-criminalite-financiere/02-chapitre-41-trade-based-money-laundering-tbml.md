---
title: Chapitre 41 — Trade-Based Money Laundering (TBML)
source: Cyber/02 OSINT/Finance & cryptoactifs/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies de criminalité financière
  - index.md
---

## Objectif du chapitre

Comprendre le **blanchiment par le commerce international (TBML)** — l’une des typologies les plus utilisées et les plus difficiles à détecter, car elle s’appuie sur des flux commerciaux qui paraissent légitimes.

## Le concept

Le **TBML** est le blanchiment via des opérations commerciales internationales : import-export, achats-ventes de marchandises, prestations de service. La dissimulation passe par le **décalage entre valeur déclarée et valeur réelle** de la marchandise, ou par la **fictivité totale** de l’opération.

## Mécanismes courants

**Sur-facturation** : la marchandise est vendue à un prix supérieur à sa valeur réelle. Le payeur transfère ainsi un montant supérieur, l’excédent étant un canal de valeur déguisé.

**Sous-facturation** : la marchandise est vendue à un prix inférieur. Permet de minimiser les droits de douane à l’import, ou de transférer de la valeur via revente à valeur réelle.

**Facturation multiple** : la même marchandise est facturée plusieurs fois à des entités liées.

**Marchandise fictive** : facture sans contrepartie physique.

**Documents falsifiés** : certificats d’origine, bills of lading, CMR, certificats douaniers — donnent une apparence légitime à des flux fictifs.

**Transit par juridictions complaisantes** : la marchandise passe (ou semble passer) par des free zones (Dubai, Singapour) pour brouiller la traçabilité.

**Triangulation** : achat dans un pays A, vente dans un pays C, transit par un pays B intermédiaire — opportunité de surcouches.

## L’utilité opérationnelle

Le TBML est particulièrement difficile à détecter parce qu’il imite des opérations commerciales légitimes. La détection repose sur l’analyse fine de la cohérence économique (chapitre 38).

## Méthode — signaux de TBML

- Marges sur-prix marché significatives.
- Décalages valeur facture / valeur de marché (Eurostat Comext, UN Comtrade, indices sectoriels).
- Contreparties commerciales sans activité réelle vérifiable.
- Pays de transit sans rationale économique.
- Documents douaniers incohérents (ports d’embarquement, dates).
- Paiements en avance disproportionnée par rapport aux pratiques sectorielles.
- Flux financiers déconnectés des flux physiques observables.

## Mini-walkthrough — schéma TBML simplifié

Une société A en France importe « 200 tonnes d’huile de palme » depuis une société B au Bénin, payée 850 K€. La société B est facturée par une société C en Côte d’Ivoire pour 350 K€.

- Si la marchandise existe : marge B = 500 K€ — atypique pour le marché.
- Vérification douanière française : aucune trace d’import enregistré pour A à ces volumes.
- Vérification logistique : aucun transport identifié.

Hypothèse forte : opération **fictive ou sur-facturée**, le flux de 850 K€ ayant une finalité de transfert de valeur déguisée. Probable TBML.

## Erreurs fréquentes

- **Confondre marge atypique et TBML.** Certains secteurs (luxe, technologies de pointe) ont des marges très élevées légitimement.
- **Conclure sans vérification physique** : la vérification douanière (existence du transport) est souvent la clé.
- **Sous-estimer le rôle des free zones** : la traçabilité y est moindre.

## Limites

La détection fine du TBML exige souvent une coopération douanière internationale (OMD, douanes nationales). En CRF, cette coopération est mobilisable mais lente.

## Lien avec le fil rouge

> **CLEARFLOW — TBML hypothèse centrale**
> 
> Dans le dossier Haddad, plusieurs éléments convergent vers une hypothèse TBML *probable* : sur-facturation apparente sur le marché ivoirien (×2), incohérences entre flux financiers et flux physiques pour les imports déclarés français depuis le Bénin, transit Bénin → France sans rationale logistique. La qualification précise exigerait coopération douanière française et ivoirienne, prévue dans les recommandations.

## Points clés à retenir

- TBML = blanchiment via flux commerciaux internationaux.
- Mécanismes : sur/sous-facturation, facturation multiple, marchandise fictive, documents falsifiés.
- Détection : cohérence valeur, contreparties, logistique.
- Coopération douanière internationale souvent nécessaire.

-----
