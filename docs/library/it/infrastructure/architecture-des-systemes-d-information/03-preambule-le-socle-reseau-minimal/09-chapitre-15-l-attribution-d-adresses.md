---
title: Chapitre 15 — L'attribution d'adresses
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

## 15.1 À quoi ça sert

Donner automatiquement à une machine qui démarre son adresse, son masque, sa passerelle et l'adresse de son résolveur.

**Pourquoi ça existe.** Configurer six cents postes à la main est impossible ; et un plan d'adressage qui change imposerait de tous les reprendre. L'attribution automatique rend le poste **indifférent au réseau sur lequel il est branché**.

## 15.2 La séquence, et ce qu'elle distribue

```
   ①  La machine démarre. Elle n'a pas d'adresse.
   ②  Elle demande, en diffusion : « quelqu'un peut-il me configurer ? »
   ③  Le serveur répond, et propose :
         · une adresse, pour une DURÉE limitée (le bail)
         · un masque de sous-réseau
         · une passerelle par défaut
         · l'adresse d'un ou plusieurs résolveurs
         · parfois : un domaine, un serveur de temps, un mandataire
   ④  La machine accepte, et renouvelle avant expiration du bail
```


⚠️ **Ce qu'il faut retenir de l'étape ③** : ce composant ne distribue pas seulement une adresse. **Il distribue la configuration réseau complète.** Une erreur dans l'adresse du résolveur distribuée, et six cents postes perdent la résolution de noms — §14.

## 15.3 Le bail, et pourquoi la panne est différée

```
   Bail de 8 jours, renouvelé à mi-parcours.

   Jour 0    Le serveur tombe.
   Jour 0    RIEN ne se passe. Toutes les machines ont une adresse valide.
   Jour 4    Les premiers renouvellements échouent → les machines gardent
             leur adresse et réessaient
   Jour 8    Les premiers baux expirent → les premières machines
             perdent leur adresse
   Jour 8-16 Les machines tombent une par une, dans un ordre
             qui paraît aléatoire
```


⚠️ **C'est la panne différée par excellence**, et la plus difficile à relier à sa cause : **plusieurs jours peuvent séparer l'incident de ses premiers effets**, et les effets arrivent progressivement.

🔥 **SCÉNARIO — des postes tombent au hasard depuis trois jours**

| Question | Réponse |
|---|---|
| Symptôme | Chaque jour, quelques postes n'ont plus de réseau. Aucun point commun apparent |
| Hypothèse naïve | « Un problème matériel sur les postes » ou « le commutateur » |
| Dépendance réelle | Le serveur d'attribution, arrêté **il y a plusieurs jours** |
| Ce que le schéma aurait dû montrer | Ce composant — il n'y figure jamais |
| Comment le reconnaître | **Les postes touchés sont ceux qui ont redémarré ou dont le bail a expiré** — pas un groupe géographique |

## 15.4 Ce qu'il fait à la donnée

Rien. Mais il sait **quelle machine est apparue, quand, et avec quelle identité matérielle** — une source précieuse pour l'inventaire, et presque jamais exploitée. C'est le chapitre 11 du volume Asset Management.

## 15.5 Sur un schéma

Jamais. Flux de dépendance.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « Il est en DHCP » | La machine reçoit sa configuration automatiquement | **Son adresse change-t-elle ?** Cela affecte les règles de filtrage par adresse |
| « On lui a mis une IP fixe » | Adresse configurée en dur, ou réservée | En dur sur la machine, ou réservée sur le serveur ? Ce n'est pas la même chose |
| « Un poste a pris une mauvaise IP » | Conflit ou serveur non autorisé | **Un serveur d'attribution non déclaré sur le réseau est un incident de sécurité** |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne pas configurer chaque machine à la main | **Une machine peut apparaître sans être déclarée nulle part** |
| Changer un plan d'adressage sans toucher aux postes | Une dépendance de plus au démarrage |
| Distribuer toute la configuration réseau | **Une erreur se propage à l'ensemble du parc** |

⚠️ **La ligne du milieu à droite** est l'origine d'un problème traité dans deux autres volumes : une machine branchée obtient une adresse et fonctionne, **sans avoir été inventoriée, autorisée ni supervisée**.

---
