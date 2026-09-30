---
title: Chapitre 32 — Suivre une donnée
source: IT/Architecture_SI.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE V — Les flux
  - index.md
---

> **Principe 6 : le système d'information n'existe que pour traiter de la donnée.** Ce chapitre suit un enregistrement de sa création à sa destruction.

## 32.1 Le cycle complet

🖼 **SCHÉMA 32.1 — Une donnée, de la saisie à l'oubli**

```
  ①  SAISIE          poste utilisateur
  ②  TRANSIT         mandataire · web · applicatif
  ③  STOCKAGE        base de données
  ④  RÉPLICATION     base secondaire, éventuellement autre site
  ⑤  SAUVEGARDE      support de sauvegarde, souvent hors ligne
  ⑥  COPIE           export, tableur, rapport, environnement de recette
  ⑦  DIFFUSION       courriel, partage de fichiers, service en ligne
  ⑧  ARCHIVAGE       stockage long terme
  ⑨  SUPPRESSION     de la base — mais pas des copies
```


⚠️ **L'étape ⑨ ne supprime que ⑨.** Une donnée effacée de la base subsiste dans les sauvegardes, les réplicas, les exports, les courriels et les environnements de recette. **C'est le principal écart entre la suppression déclarée et la suppression réelle.**

## 32.2 Les copies qu'on ne voit jamais

| Copie | Où elle naît | Pourquoi elle échappe |
|---|---|---|
| **L'environnement de recette** | Copie de production pour tester | **Contient de vraies données, avec des protections moindres** |
| **L'export tableur** | Un utilisateur qui extrait | Part sur un poste, un partage, un courriel |
| **La sauvegarde** | Automatique | Souvent conservée bien au-delà du besoin |
| **Le cache** | Intermédiaires techniques | Invisible et temporaire — mais réel |
| **Le rapport** | Outil décisionnel | Une seconde base, avec ses propres droits |
| **Le journal applicatif** | La journalisation elle-même | **Il peut contenir la donnée** — §31.4 |
| **La messagerie** | Un fichier envoyé une fois | Conservé indéfiniment, chez l'expéditeur et le destinataire |

**La première ligne est la plus significative en sécurité** : un environnement de recette contient les données de production avec des protections inférieures, et il est **presque toujours hors du périmètre des schémas et des inventaires**.

⚠️ **La sixième mérite d'être signalée** : une application qui journalise le contenu de ses requêtes pour faciliter le diagnostic **duplique la donnée dans un système dont la rétention et les droits sont différents**. C'est une copie que personne n'a décidée.

## 32.3 Ce qui multiplie les copies sans qu'on le décide

| Mécanisme | Combien de copies il crée |
|---|---|
| Une réplication de base | +1, en permanence |
| Une sauvegarde quotidienne conservée 30 jours | **+30** |
| Un environnement de recette rafraîchi mensuellement | +1, à jour d'un mois |
| Un outil décisionnel | +1, avec ses propres droits |
| Un export mensuel envoyé par courriel | **+N, indéfiniment** |

⚠️ **Le calcul est instructif.** Une base unique, sauvegardée quotidiennement sur trente jours, répliquée, copiée en recette et alimentant un outil décisionnel, **existe en trente-quatre exemplaires** — dont trente-trois ne sont sur aucun schéma.

## 32.4 Le chemin de la sauvegarde, et pourquoi il compte

**Un flux d'exploitation qui n'apparaît nulle part, et qui est le plus transverse de l'architecture.**

```
   [ base ] ◄──── [ serveur de sauvegarde ] ────► [ support ]
       ▲                    │                        │
       │                    │  il atteint AUSSI :    │
       │                    ├──► serveurs de fichiers │
       │                    ├──► machines virtuelles  │
       │                    └──► annuaire             │
       │                                              │
   Trois questions :
      ① Qui initie ? (§3.6 — la sauvegarde, presque toujours)
      ② Avec quel compte ? (il atteint tout, donc il peut tout lire)
      ③ Le support est-il atteignable depuis le réseau ?
```


⚠️ **La troisième question décide de la gravité d'un rançongiciel.** Une sauvegarde atteignable en écriture depuis un compte compromis est chiffrée avec le reste. **C'est le scénario du §21.4**, et c'est ce qui distingue un incident d'une catastrophe.

🔥 **SCÉNARIO — la donnée effacée réapparaît**

| Question | Réponse |
|---|---|
| Symptôme | Une donnée supprimée sur demande réapparaît trois mois plus tard |
| Hypothèse naïve | « Une erreur de manipulation » |
| Dépendance réelle | **Une restauration partielle depuis une sauvegarde antérieure à la suppression** |
| Ce que le schéma aurait dû montrer | Le cycle complet, et les points où la donnée persiste |
| Concevoir différemment | Traiter la suppression comme un **processus sur toutes les copies**, pas comme une action sur la base |

🎯 **QUELLE ERREUR ÇA ÉVITE ?**
*Vous devez évaluer l'impact d'une compromission de la base de production. Où cherchez-vous ?*
**Pas seulement dans la base.** Vous listez les neuf étapes : où sont les réplicas, les sauvegardes, la recette, les exports, les rapports, les journaux. Dans la majorité des cas, **la donnée existe en plusieurs endroits**, dont plusieurs ne sont sur aucun schéma. La mauvaise décision évitée : **déclarer un périmètre d'impact qui ne couvre qu'une fraction des copies**, et devoir le corriger publiquement quelques jours plus tard.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « La donnée a été supprimée » | Effacée de la base | **Et les sauvegardes ? La recette ? Les exports ?** |
| « La recette est une copie de prod » | Données réelles hors production | **Avec quelles protections ? Qui y a accès ?** |
| « On sauvegarde tout » | Un dispositif existe | **Le support est-il atteignable depuis le réseau ?** |
| « On a extrait un fichier » | Un export a été fait | **Où est-il maintenant ?** C'est une copie de plus |

---
