---
title: Attaques basées sur les MDP
source: Cyber/99_Concepts/HTB_Comprendre les types d'attaques.md
note: HTB — Comprendre les types d'attaques
up:
- - HTB — Comprendre les types d'attaques
  - index.md
---

### Types d'attaques
#### Attaque par dictionnaire

- Teste des MDP provenant d'une wordlist : mots courants, password issus de leaks, variantes fréquentes...
  Rapide car l'attaquant ne génère pas toutes les combinaisons possibles.
- Efficace contre passwords faibles/prévisibles.
- Inefficace si le password n’est pas présent ou dérivable de la wordlist.
#### Attaque par force brute

- Teste toutes les combinaisons possibles selon un charset et une longueur donnés.
- Avantage : avec suffisamment de temps, les attaques par force brute peuvent finir par casser n'importe quel mot de passe.
- Inconvénient :  est le temps que cela prend. En raison du grand nombre de mots de passe possibles, il pourrait falloir des années pour casser un mot de passe avec cette méthode.
#### Attaque hybride

- Combine dictionnaire + brute force.
- Commence avec un fichier de dictionnaire, mais ensuite le logiciel de cassage de mot de passe modifie les mots du dictionnaire. 
- Exemple, il pourrait ajouter des chiffres à la fin d'un mot ou remplacer certains caractères par d'autres.

### Password Spraying

- Tester un même mot de passe (ou quelques-uns) contre beaucoup de comptes.
- But : éviter les mécanismes de lockout qui se déclencheraient en testant beaucoup de passwords sur un seul compte.
- Ex :
	- Password123 → alice
	- Password123 → bob
	- Password123 → admin
	- Password123 → john
### Credential Stuffing

- Réutiliser des couples email:password issus d'une fuite de données sur d'autres services.
- Exploite la réutilisation des mots de passe.

Leak site A
alice@email.com : Winter2025!

        ↓ testé sur

VPN / O365 / Gmail / Site B

- → Ce n’est pas du brute force : les credentials testés sont déjà connus.
### Rainbow tables

- Tables pré-calculées permettant d'accélérer la recherche d'un mot de passe correspondant à un hash.
- Evitent de recalculer les mêmes hashes à chaque attaque.
#### Défense : Sel

- Un salt aléatoire ajouté avant le hash rend les rainbow tables pré-calculées beaucoup moins utiles.
- Deux utilisateurs avec le même password obtiennent alors des hashes différents.

### Plaintext / Known-Plaintext Attack (KPA)

- En cryptanalyse, l'attaquant possède :
	- Une donnée en clair (plaintext/crib) ;
	- le ciphertext correspondant.
- Il tente d'en déduire des informations sur la clé ou le mécanisme de chiffrement.
### Cryptographic Attacks
#### Collision de hash / Birthday Attack

- Une collision apparaît lorsque deux entrées différentes produisent le même hash.

Input A ─┐
         ├→ même Hash
Input B ─┘
#### Downgrade Attack

- Forcer deux systèmes à utiliser un protocole/algorithme moins sécurisé que celui normalement disponible.
- Ex :
	- Ancienne version TLS ;
	- chiffrement plus faible ;
	- fallback vers protocole legacy.
#### Online vs Offline Attacks

- Online : Attaquant teste directement contre le service : Attacker -> SSH / VPN / Web Login / RDP. Risques pour l'attaquant :
	- Logs, détection, rate limiting, account lockout, blocage IP.
- Offline : Attaquant récupère les hashes puis travaille sur sa propre machine. Database / SAM / dump -> hashes récupérés -> Hashcat / John. Avantage :
	- pas de lockout, pas de trafic vers la victime, très grand nombre d'essais possibles, possibilité d'utiliser CPU/GPU puissants. 
### Outils de Password Cracking

|Outil|Usage|
|---|---|
|**John the Ripper**|Cracking offline : dictionary, brute-force, règles/hybride|
|**Hashcat**|Cracking offline très performant, notamment GPU, nombreux formats de hash|
|**Hydra**|Attaques **online** contre SSH, FTP, HTTP, RDP et autres services|
|**Cain & Abel**|Ancien outil Windows de cracking/sniffing ; surtout historique aujourd’hui|


## Recap - 4 grandes familles d’attaques

|Type|Principe|Exemples|
|---|---|---|
|**Social Engineering**|Manipuler une personne pour contourner la sécurité|Phishing, smishing, dumpster diving, tailgating|
|**Network-Based**|Exploiter/intercepter les communications ou services réseau|Sniffing, DoS/DDoS, MITM, ARP/DNS poisoning|
|**Password-Based**|Deviner, récupérer ou réutiliser des credentials|Dictionary, brute-force, spraying, hybrid|
|**Application-Based**|Exploiter des vulnérabilités présentes dans des logiciels/applications|Client-side exploit, vulnérabilité Web, logiciel non patché|
