---
title: Annexe 6 — Templates opérationnels
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Annexes
  - index.md
---

## 6.1 Template — Threat model personnel

```
[DATE] — [VERSION X.Y]
À RELIRE À : [DATE + 3 MOIS]

QUI JE SUIS (CONTEXTE) :
- Profession :
- Contexte spécifique (enquête, engagement, mission, situation) :
- Profil HVT-ness honnête (oui / non / partiel) :

ACTIFS PRIORITAIRES (top 5) :
1.
2.
3.
4.
5.

ADVERSAIRES PLAUSIBLES (top 5, par probabilité × capacité × motivation) :
1. [Nom] | Capacité : | Motivation : | Méthodes typiques :
2.
3.
4.
5.

HORS PÉRIMÈTRE EXPLICITE :
- 
- 
- 

MESURES PRIORITAIRES ACTUELLES :
1.
2.
3.
4.
5.

POINTS D'ATTENTION (à surveiller) :
- 
- 

SIGNATURE :
```


## 6.2 Template — Brief manifestation

```
[DATE] — [LIEU] — [HEURE DE DÉBUT]

CONTEXTE :
- Nature de la manifestation :
- Risques anticipés (interpellations, gaz, charges, présence drones) :
- Présence de presse :

ÉQUIPE (présents au brief) :
-
-
-

RÉFÉRENT :
- Personne désignée hors manif :
- Procédure d'alerte si silence > X heures :

HOTLINE JURIDIQUE :
- Numéro :
- Avocat de garde :

CHECKLIST PERSONNELLE :
[ ] Téléphone manif chargé, BFU, faraday bag
[ ] Téléphone perso laissé éteint chez soi
[ ] Papier avec numéros essentiels
[ ] Cash + CB prépayée
[ ] Vêtements anonymes
[ ] Lunettes / protection
[ ] Pas de document compromettant

CHECKLIST RETOUR :
[ ] Compter les présents
[ ] Communication référent OK
[ ] Téléphone non saisi
[ ] Si saisie : protocole brûlure
[ ] Audit appareils (si perquisition possible)
```


## 6.3 Template — Plan IR personnel

```
PROCÉDURE D'INCIDENT — VERSION [X.Y] — [DATE]

CONTACTS D'URGENCE :
- Avocat : [nom, téléphone]
- Référent technique (si applicable) : 
- Famille de confiance :
- Association de soutien :
- Hotline crisis : Access Now Digital Security Helpline +1 888 414 0100

EN CAS DE TÉLÉPHONE PERDU / VOLÉ :
1. Localisation à distance via [iCloud / Google] : [étapes]
2. Effacement à distance si nécessaire
3. Opérateur : [numéro support pour bloquer SIM]
4. Comptes à révoquer en priorité : Apple / Google / Microsoft / banques / messageries
5. Plainte police (numéro IMEI fourni à l'opérateur — noté dans 1Password sous "Matériel")

EN CAS DE COMPTE COMPROMIS :
1. Mot de passe changé depuis [appareil sain — préciser lequel]
2. Sessions actives révoquées
3. Audit modifications (mail récup, MFA, filtres)
4. Comptes liés vérifiés
5. Communication aux contacts si nécessaire

EN CAS DE SPYWARE SUSPECTÉ :
1. Mode avion + faraday
2. NE PAS REDÉMARRER
3. Access Now Helpline
4. MVT / Citizen Lab

EN CAS DE DOXXING :
1. Captures + horodatages
2. Signalement plateformes
3. Évaluation menace physique
4. Avocat + plainte
5. Soutien : [association locale]

CODES DE RÉCUPÉRATION :
- Stockés : [coffre — où exactement]
- Apple ID : ____
- Google : ____
- Bitwarden : ____
- 2FA backup codes : ____
```


## 6.4 Template — Audit trimestriel

```
TRIMESTRE [TX] — [DATE]

OSINT DÉFENSIF :
[ ] Recherche nom complet sur Google / Bing / DDG
[ ] HaveIBeenPwned sur emails principaux
[ ] Reverse image sur photo de profil
[ ] WhatsMyName sur pseudonymes
[ ] Data brokers nouveaux apparus

SÉCURITÉ COMPTES :
[ ] Audit sessions Google / Apple / Microsoft
[ ] Audit MFA sur 20 comptes critiques
[ ] Revue gestionnaire de mots de passe (doublons, faibles)
[ ] Codes de récupération à jour

APPAREILS :
[ ] Mises à jour OS et firmware
[ ] Intégrité physique des appareils (vis, photos comparatives)
[ ] Permissions mobiles auditées
[ ] Reboot complet

SAUVEGARDES :
[ ] Test de restauration mini (un fichier)
[ ] Cloud E2EE fonctionnel
[ ] Disque externe en lieu sûr OK
[ ] Sauvegarde immuable mensuelle OK

THREAT MODEL :
[ ] Toujours pertinent ?
[ ] Évolutions à acter ?

NOTES :
```


## 6.5 Template — Page « comment me joindre confidentiellement »

```
COMMENT ME JOINDRE CONFIDENTIELLEMENT

Je travaille sur des dossiers parfois sensibles. Si vous souhaitez 
me contacter de manière sécurisée, voici les canaux que je vérifie :

1. SECUREDROP : [lien .onion]
   À utiliser via Tor Browser (https://torproject.org).
   Anonyme. Préféré pour transmission de documents.

2. SIGNAL : @username (pas de numéro de téléphone)
   Pour discussion préalable et coordination.
   Vérification : Safety Numbers à comparer.

3. EMAIL CHIFFRÉ : email@domain.org
   Clé PGP : [fingerprint] — disponible sur Keys.OpenPGP.org
   Pour échanges techniques.

4. SIMPLEX : Sur demande, je peux fournir un lien d'invitation.

Avant tout envoi de documents sensibles, contactez-moi d'abord 
pour que nous choisissions ensemble le canal adapté.

Précautions à prendre de votre côté :
- Ne pas utiliser un appareil professionnel pour me contacter.
- Considérer Tor Browser sur Tails pour confidentialité maximale.
- Ne jamais transmettre depuis un réseau de votre employeur.

Cette page est à jour au [date].
```


-----
