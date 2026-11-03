---
title: Chapitre 1 — Pourquoi on met à jour
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie I — Les bases
  - index.md
---

> 🧱 **Les bases**
>
> - Un **système d'exploitation** (Windows) est un logiciel de plusieurs dizaines de millions de lignes de code. Il contient forcément des erreurs.
> - Un **correctif** (*patch*, *update*) est une modification publiée par l'éditeur pour remplacer des fichiers ou des réglages défectueux.
> - Le **MCO** (maintien en condition opérationnelle) vise à ce que le système *fonctionne*. Le **MCS** (maintien en condition de sécurité) vise à ce qu'il reste *sûr* dans le temps : correctifs, configuration, suivi des vulnérabilités. Les deux se recoupent : une mise à jour est à la fois un acte de sécurité et un changement qui peut casser la production.

## 1.1 Du bug à la vulnérabilité

Un **bug** est un comportement non prévu du logiciel. Il devient une **vulnérabilité** quand quelqu'un peut l'exploiter pour obtenir quelque chose qu'il ne devrait pas avoir : exécuter du code, lire des données, obtenir des droits plus élevés, arrêter un service.

On classe généralement les vulnérabilités Windows par **effet** :

| Effet | Sigle anglais | Ce que l'attaquant obtient | Exemple d'usage |
|---|---|---|---|
| Exécution de code à distance | RCE | lancer son programme sur la machine, sans y avoir accès | entrée initiale dans le réseau |
| Élévation de privilèges | EoP | passer d'un compte utilisateur à SYSTEM ou administrateur | après une première intrusion |
| Divulgation d'information | — | lire de la mémoire, des fichiers, des secrets | préparer une autre attaque |
| Contournement de sécurité | — | désactiver une protection (SmartScreen, Secure Boot…) | rendre une attaque possible |
| Déni de service | DoS | planter un service ou la machine | interruption |
| Usurpation | — | se faire passer pour un autre (fichier, site, utilisateur) | hameçonnage, relais |

Un correctif modifie des fichiers (DLL, pilotes, exécutables), parfois des clés de registre ou des valeurs par défaut. C'est pour cela que **la protection n'est effective qu'une fois le fichier corrigé chargé en mémoire**, donc souvent après redémarrage (Ch.7).

## 1.2 Le cycle de vie d'une vulnérabilité

```
Découverte ──► Signalement à Microsoft (MSRC) ──► Correctif développé en secret
                                                        │
                                                        ▼
         Patch Tuesday : publication du correctif ET de l'avis (CVE)
                                                        │
                                                        ▼
   Analyse du correctif par les attaquants (« patch diffing ») ──► Exploit
                                                        │
                                                        ▼
                Organisations qui n'ont pas installé = cibles
```


- **Divulgation coordonnée** : le chercheur prévient Microsoft, qui publie le correctif et l'avis en même temps. C'est le cas normal.
- **0-day** (*zero-day*) : la faille est exploitée **avant** que le correctif existe. Microsoft l'indique par la mention *Exploitation Detected* dans son avis.
- **n-day** : la faille est connue et corrigée, mais encore exploitable sur les machines non mises à jour. **La grande majorité des attaques réelles utilisent des n-days** : c'est exactement le terrain du MCS.
- **Patch diffing** : en comparant les fichiers avant et après le correctif, un attaquant voit ce qui a changé et en déduit la faille. Plus le délai est long entre publication et installation, plus le risque monte (Ch.5, *Exploit Wednesday*).

La **fenêtre d'exposition** est la durée entre la publication du correctif et le moment où il est **actif** sur la machine. Réduire cette fenêtre, sans casser la production, est tout l'objet du métier.

> 💡 **Exemple — Deux cas réels qui fondent la discipline**
>
> - **MS17-010 / WannaCry** : Microsoft corrige une faille du protocole SMBv1 le 14 mars 2017. Le rançongiciel WannaCry l'exploite à grande échelle le 12 mai 2017, soit **deux mois** plus tard. Les organisations touchées n'avaient pas installé un correctif disponible depuis huit semaines.
> - **CVE-2025-59287 (WSUS)** : faille critique dans WSUS lui-même, publiée au Patch Tuesday du 14 octobre 2025 avec un correctif **incomplet**. Un code d'exploitation devient public, Microsoft publie un correctif hors calendrier le **23 octobre 2025**, et des exploitations sont observées dans les heures qui suivent. Le serveur qui distribue les correctifs était lui-même la cible (Ch.11).

## 1.3 Le dilemme sécurité / stabilité

Mettre à jour vite réduit le risque d'attaque. Mais une mise à jour est aussi un **changement** non maîtrisé : Microsoft teste sur des millions de machines, pas sur *vos* applications métier, *vos* imprimantes, *vos* pilotes.

> 💡 **Exemple — Régressions réelles**
>
> - **KB5034441** (janvier 2024) : mise à jour de l'environnement de récupération (WinRE) qui échouait avec l'erreur **0x80070643** sur les machines dont la partition de récupération était trop petite. Des milliers de postes en échec « rouge » dans les rapports, pour un problème de partitionnement.
> - Les correctifs de **PrintNightmare** (2021) ont durci le spouleur d'impression et cassé l'installation de pilotes d'imprimante pour les utilisateurs non administrateurs dans beaucoup d'entreprises.

D'où la méthode de toute équipe MCS : **tester sur un petit groupe représentatif, puis élargir** (les « anneaux », Ch.12), avec une **voie rapide** pour les failles exploitées.

> 🧵 **Fil rouge — Lundi 5 janvier 2026**
>
> Premier jour d'Inès. Karim lui montre le tableau de bord WSUS : 96 % de conformité. « Ce chiffre ne veut rien dire tout seul, lui dit-il. Il faut savoir *96 % de quoi*, *depuis quand*, et *quelles machines manquent*. Le jour où on se fait attaquer, ce sera par les 4 %. » Le premier Patch Tuesday d'Inès tombe le **mardi 13 janvier**.

> 📌 **À retenir**
>
> - Une vulnérabilité est un bug exploitable ; un correctif ne protège qu'une fois installé **et actif** (souvent après redémarrage).
> - Les attaques réelles exploitent surtout des failles **déjà corrigées** mais pas déployées.
> - Le métier MCS consiste à réduire la fenêtre d'exposition sans casser la production : tests progressifs + voie d'urgence.

---
