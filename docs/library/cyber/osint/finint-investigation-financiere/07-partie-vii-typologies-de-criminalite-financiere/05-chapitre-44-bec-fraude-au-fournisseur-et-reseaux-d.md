---
title: Chapitre 44 — BEC, fraude au fournisseur et réseaux de mules
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Partie VII — Typologies DE criminalité financière
  - index.md
---

## Objectif du chapitre

Comprendre les **fraudes au virement** modernes : Business Email Compromise (BEC), fraude au changement d’IBAN, fraude au président, et le rôle des **réseaux de mules** dans le cashout.

## Le concept

**BEC (Business Email Compromise)** : famille d’attaques où un attaquant prend le contrôle (réel ou simulé) d’une adresse email professionnelle pour détourner un paiement. Variantes principales :

- **Fraude au président (CEO fraud)** : un faux email d’un dirigeant demande un virement urgent et confidentiel à un collaborateur des finances.
- **Fraude au changement d’IBAN** : un fournisseur légitime semble écrire à son client pour signaler un changement d’IBAN. Le client paie sur le nouveau RIB — au fraudeur.
- **Fraude au faux client** : un faux client semble passer commande, demande livraison, puis disparaît sans payer (à la marge du BEC, mais souvent traité ensemble).
- **Fraude à l’avocat** : un faux avocat ou notaire demande un virement urgent dans le cadre d’une fausse transaction.
- **Vendor email compromise** : compromission réelle de la boîte email d’un fournisseur, exploitée pour rediriger les paiements.

**Réseau de mules.** Les fonds détournés transitent par des comptes de personnes physiques (mules) avant cashout. Les mules sont :

- **Recrutées** via fausses offres d’emploi (« assistant financier », « agent de transfert »), réseaux sociaux, applications de rencontre, sites de petites annonces.
- **Volontaires** (rémunérées) ou **involontaires** (manipulées par phishing ou romance scam).
- **Utilisées** pour recevoir un virement frauduleux, retirer en cash ou retransférer vers le réseau, en quelques heures.

## L’utilité opérationnelle

Le BEC est un volet majeur de la fraude moderne. Pour la victime (PME, ETI, grand groupe), les pertes sont fréquemment de 50 K€ à plusieurs millions. La récupération dépend de la rapidité du gel — typiquement quelques heures.

## Méthode — détection et réponse

**En prévention** (au-delà du périmètre FININT pur) : double signature obligatoire pour les virements significatifs, validation par téléphone d’un changement d’IBAN, formation des équipes finances, vérifications techniques (SPF, DKIM, DMARC sur les emails).

**En détection** :

- Virement vers IBAN nouveau, montant inhabituel, libellé urgent.
- Demandes en dehors des heures ouvrées.
- Discrépance entre nom du bénéficiaire affiché et titulaire réel du compte (la **Verification of Payee** — VOP — devient progressivement obligatoire dans l’UE avec le règlement sur les paiements instantanés ; pour les PSP de la zone euro, l’échéance opérationnelle majeure est **octobre 2025** ; pour les PSP hors zone euro, **juillet 2027**. Au moment où l’analyste travaille, le déploiement effectif varie selon les PSP).
- Activité immédiate de fractionnement et de cashout sur le compte bénéficiaire.

**En réaction** (essentielle, urgente) :

- **Contact immédiat** avec la banque émettrice pour gel (fenêtre quasi-nulle en SCT Inst).
- **Plainte** auprès des autorités (en France : Plate-forme PHAROS, plainte en ligne, ou commissariat).
- **Coopération internationale** via CRF (signalement urgent à TRACFIN qui peut activer FIU.NET pour les comptes destinataires européens).
- **Volet crypto** si conversion crypto : renvoi vers OSINT Crypto pour le traçage on-chain.

## Mini-walkthrough

Une PME française reçoit, le mardi 14h32, un email semblant venir de son fournisseur habituel, demandant le paiement d’une facture sur un nouvel IBAN espagnol. Le directeur financier paie 215 K€ via SCT Inst.

À 14h35-14h41 : le compte espagnol fractionne en 5 virements vers PT et LT.
À 16h12 : conversion USDT sur exchange.
À 18h45 : sortie vers wallet auto-géré.

La PME découvre la fraude le mercredi matin (le vrai fournisseur appelle pour réclamer le paiement). Délai : 18+ heures. Fenêtre de gel : pratiquement fermée pour la portion crypto. Pour les comptes PT et LT, gel possible si rapidité d’action de la CRF.

Bilan typique : récupération de 20 à 40 % du montant si action rapide ; recouvrement total très rare.

## Erreurs fréquentes

- **Sous-estimer la vitesse.** Les fraudeurs exploitent la non-réversibilité de SCT Inst.
- **Croire que la victime est forcément négligente.** Beaucoup de BEC sont sophistiqués (compromission réelle d’email, manipulation contextuelle).
- **Ignorer le réseau de mules** : sans elles, le cashout est plus difficile. Identifier la mule peut conduire au recruteur.

## Limites

Le BEC est rapide ; la coopération internationale est plus lente. La récupération totale est rare. Le travail FININT vise souvent à **identifier le réseau** (mules, recruteurs, organisateurs) pour démanteler, plus qu’à récupérer les fonds.

## Lien avec le fil rouge

> **CLEARFLOW — Branche BEC limitée**
> 
> Une des entrées du dossier Haddad inclut un BEC : 215 K€ détournés d’une PME française vers le compte d’une SAS du réseau Haddad. La piste mule semble présente — la SAS pouvait être utilisée comme étape de layering pour des fonds frauduleux d’origine externe au réseau lui-même. Cette branche est secondaire dans le dossier mais documente que le réseau a pu fonctionner comme **infrastructure de service** pour des fraudes externes.

## Points clés à retenir

- BEC = famille de fraudes au virement par compromission ou simulation d’email.
- SCT Inst rend le gel quasi impossible.
- Réseaux de mules : volontaires ou involontaires, recrutées en ligne.
- Réaction : rapidité critique, coopération CRF, renvoi crypto si pertinent.

-----
