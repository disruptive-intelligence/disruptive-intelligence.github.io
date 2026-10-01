---
title: 'Annexe B — Lire un message SWIFT : MT103, MT202, MT940'
source: Cyber/02 OSINT/FININT — investigation financière.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Annexes
  - index.md
---

*Lecture annotée des trois types de messages SWIFT les plus rencontrés en FININT.*

## MT103 — Single Customer Credit Transfer

*(paiement client à client international)*

Structure simplifiée :

```
{1: Basic header}
{2: Application header}
{4:
:20:REF1234567890         <- Référence unique du message
:23B:CRED                 <- Type de transaction
:32A:240315EUR12500,00    <- Date valeur + devise + montant
:50K:/FR7612345678901234567890123  <- Donneur d'ordre (IBAN + nom)
NEXUS TRADING SAS
12 RUE Y PARIS 9E
:52A:BNPAFRPP              <- Banque du donneur d'ordre (BIC)
:57A:CHASUS33              <- Banque correspondante intermédiaire (US ici)
:59:/CY01234567890123      <- Bénéficiaire (compte + nom)
NEXUS HOLDINGS LTD
NICOSIA CYPRUS
:70:TRADE PAYMENT INVOICE 0234  <- Libellé / référence
:71A:SHA                   <- Frais (SHA = partagés, OUR = donneur, BEN = bénéficiaire)
-}
{5: Trailer}
```


**Lecture FININT** :

- :20 référence unique du message.
- :32A donne **date + devise + montant** sur une seule ligne (format YYMMDD).
- :50 = donneur d’ordre. K = nom + adresse en clair. A = BIC.
- :52 = banque du donneur.
- :57 = banque correspondante (peut révéler un transit US si USD).
- :59 = bénéficiaire (IBAN + nom + adresse).
- :70 = libellé.
- :71 = qui paie les frais.

Signaux à surveiller : libellés vagues, banques correspondantes inattendues, donneur ou bénéficiaire dans juridictions à risque, références non vérifiables.

## MT202 — General Financial Institution Transfer (transfert interbancaire)

Structure simplifiée :

```
:20:REF0987654321
:21:RELATED20240314
:32A:240315USD2500000,00
:52A:BSUICHGG            <- Banque émettrice
:57A:DEUTDEFF            <- Banque correspondante
:58A:CYNICY2N            <- Banque bénéficiaire
:72:/BNF/Pour client final NEXUS HOLDINGS
```


**Lecture FININT** :

- Transfert entre **banques** (pas entre clients).
- Volume typique : élevé.
- :72 peut contenir des informations sur le client final ; souvent succinctes.
- Utilisé par les banques pour leurs transferts ou pour le compte de clients de grande taille.

Le MT202 est plus opaque pour la traçabilité client. Combiné avec MT202COV (cover payment), il a été un canal historique du **stripping** (suppression de mentions de juridictions sanctionnées) — pratique sanctionnée massivement par OFAC (Standard Chartered, HSBC, BNP Paribas dans les années 2010).

## MT940 — Customer Statement (relevé de compte)

Structure simplifiée :

```
:20:STATEMENT240315
:25:FR7612345678901234567890123      <- Compte concerné
:28C:00086/001                       <- Numéro de séquence
:60F:C240314EUR12345,67              <- Solde d'ouverture (C = créditeur)
:61:240315D12500,00NTRFREF...        <- Mouvement : date / D-C / montant / code type
:86:VIR EMIS NEXUS HOLDINGS LTD CY
:61:240315C85000,00NTRFREF...
:86:VIR REC ATLAS TECHNICAL TURKEY
:62F:C240315EUR84845,67              <- Solde de fermeture
```


**Lecture FININT** :

- Format standardisé des relevés interbancaires (transmission B2B).
- :60 et :62 = soldes d’ouverture et de fermeture.
- :61 = un mouvement (date, débit/crédit, montant, type de transaction).
- :86 = libellé associé.

Utile pour l’analyse de séries de mouvements. Les exports vers Excel ou pandas se font directement depuis MT940 (parsers disponibles).

-----
