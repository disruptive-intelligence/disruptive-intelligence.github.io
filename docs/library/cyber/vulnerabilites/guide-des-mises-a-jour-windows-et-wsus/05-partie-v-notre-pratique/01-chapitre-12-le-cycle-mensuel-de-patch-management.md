---
title: Chapitre 12 — Le cycle mensuel de patch management
source: Cyber/07 Vulnérabilités & MCS/Maintenir dans la durée/Guide des mises à jour Windows et WSUS.md
note: Guide des mises à jour Windows et WSUS
up:
- - Guide des mises à jour Windows et WSUS
  - ../index.md
- - Partie V — Notre pratique
  - index.md
---

> 🧱 **Les bases**
>
> - Le **patch management** est le processus complet qui va de la connaissance d'un correctif à la **preuve** qu'il est actif sur toutes les machines concernées.
> - Un **anneau** (*ring*) est un groupe de machines qui reçoit les mises à jour à une étape donnée : d'abord un petit groupe, puis de plus en plus large. Dans WSUS, un anneau = un **groupe d'ordinateurs**.
> - Une **dérogation** est une exception écrite, datée et validée, à la règle de mise à jour.

## 12.1 Le processus de bout en bout

```
Inventaire ─► Veille ─► Qualification ─► Test (pilote) ─► Déploiement ─► Vérification ─► Rapport ─► Amélioration
    ▲                                                                                                    │
    └────────────────────────────────────────────────────────────────────────────────────────────────────┘
```


| Étape | Question | Chapitre |
|---|---|---|
| Inventaire | Qu'avons-nous (produits, versions, éditions, rôles) ? | Ch.2, 3 |
| Veille | Qu'est-ce qui a été publié, qu'est-ce qui casse ? | Ch.5, 6 |
| Qualification | Quelle urgence pour nous ? | Ch.6 |
| Test | Est-ce que ça casse chez nous ? | §12.5 |
| Déploiement | Comment, quand, pour qui ? | §12.2 à 12.4, Ch.10 |
| Vérification | Est-ce réellement actif ? | §12.7 |
| Rapport | Comment le prouver ? | §12.7 |
| Amélioration | Qu'apprend-on de ce mois ? | post-mortem |

## 12.2 Les anneaux

| Anneau | Contenu | Rôle |
|---|---|---|
| **Pilote IT** | 1 à 2 % : machines de l'équipe informatique, volontaires | détecter les problèmes évidents (démarrage, connexion, VPN) |
| **Pilote métier** | 5 à 10 % : au moins une machine par **modèle matériel**, par **application critique**, par **site**, des **nomades** | détecter les problèmes propres à l'organisation |
| **Production** | le reste, éventuellement en plusieurs vagues | généraliser |
| **Critiques / exceptions** | machines sensibles (direction, postes de contrôle, applications fragiles) | traitement dédié, souvent en dernier, avec fenêtre convenue |

> ✅ **Bonne pratique — Un pilote représentatif**
>
> Un pilote composé uniquement des postes de l'équipe IT ne teste rien de l'application de tiers payant, du logiciel de numérisation ou de l'imprimante de l'agence. Construire le pilote **à partir de l'inventaire** : chaque modèle de poste, chaque application critique et chaque site doit y être représenté, avec un **référent** qui sait signaler un problème.

## 12.3 Le cycle mensuel en J+n

J = le Patch Tuesday (2e mardi, ~19 h à Paris). Le cycle ci-dessous est celui de l'équipe, réécrit en J+n (Ch.5) :

| Jour | Applicatifs (Office MSI, .NET, composants tiers…) | Système (cumulatives Windows) | Autres |
|---|---|---|---|
| **J** (mardi soir) | — | — | synchronisation WSUS après 19 h 30, première lecture (gravités, *Exploited*) |
| **J+1** (mercredi) | **pilote** | qualification ; voie d'urgence si P0 | fiche de veille, avis CERT-FR |
| **J+8** (mercredi) | **production** | **pilote** | lecture des retours communautaires et *known issues* |
| **J+15** (mercredi) | — | **production** (postes, puis serveurs par vagues) | — |
| **J+22** (mercredi) | — | — | **nettoyage WSUS**, rapport de conformité, préversion non sécurité sur le pilote IT |
| **J+28 ou J+35** | — | — | Patch Tuesday suivant |

**Pourquoi séparer applicatifs et système ?** Si une régression apparaît, on sait d'où elle vient. Et les deux familles n'ont pas le même risque : une cumulative Windows touche tout le système et exige un redémarrage.

> 💡 **Exemple — Les vraies dates de fin 2026**
>
> - **Novembre 2026** : J = mardi 10. **J+1 = mercredi 11 novembre, jour férié** (Armistice). La qualification et le pilote applicatif glissent au jeudi 12 : à prévoir dans le planning d'astreinte. J+8 = 18 ; J+15 = 25 ; J+22 = 2 décembre. Patch Tuesday suivant : 8 décembre (J+28).
> - **Décembre 2026** : J = mardi 8 ; J+15 = **mercredi 23 décembre**, veille de Noël, effectifs réduits. Décision à prendre en CAB dès novembre : avancer la production système à J+14, ou la décaler au 5 janvier avec une analyse de risque écrite.

**Forces et limites de ce cycle**

| Forces | Limites | Réponse |
|---|---|---|
| progressif, séparation applicatifs/système | les failles système exploitées attendent **15 jours** | **voie d'urgence** (§12.4) |
| nettoyage planifié, donc réellement fait | formulation en « Nième mercredi » piégeuse | J+n |
| rythme connu de tous (CAB, utilisateurs) | jours fériés et congés (novembre, décembre, mai, août) | calendrier annuel publié en janvier |
| | serveurs et postes au même jour | vagues serveurs avec fenêtres dédiées (§12.8) |
| | la préversion de la 4e semaine n'est pas exploitée | l'installer sur le pilote IT à J+22 : un mois d'avance sur les régressions |

## 12.4 La voie d'urgence

Déclenchée par une qualification **P0** (Ch.6) : faille exploitée sur un actif exposé ou critique, OOB de sécurité, alerte CERT-FR.

| Étape | Délai indicatif | Qui |
|---|---|---|
| Détection et qualification écrite | H+0 à H+4 | MCS (veille) |
| Décision d'urgence | H+4 | RSSI (le CAB est informé, pas réuni) |
| Import si nécessaire (OOB publié seulement au catalogue), approbation pilote IT | H+4 à H+8 | MCS |
| Pilote raccourci (quelques heures, tests de fumée) | H+8 à H+24 | MCS + référents |
| Déploiement large avec **échéance courte** et redémarrage forcé | H+24 à H+72 | MCS, exploitation |
| Mesures temporaires si le correctif ne peut pas être déployé (désactiver un rôle, bloquer un port, isoler) | en parallèle | RSSI, réseau |
| Vérification (UBR, état WSUS, scanner) et compte rendu | H+72 | MCS |

## 12.5 Tests, suspension et retour arrière

**Que tester sur le pilote** (tests de fumée, en quelques minutes par poste) : démarrage et ouverture de session, VPN, impression, applications métier critiques, accès aux partages, lecture de documents, visioconférence, périphériques spécifiques (numériseurs, lecteurs de cartes).

**Signaux de régression** : tickets au support corrélés au groupe pilote, échecs d'installation en série dans WSUS, *known issue* ajouté par Microsoft, plusieurs témoignages indépendants dans la communauté.

**Suspendre** : retirer l'approbation pour les groupes non encore servis (les machines qui l'ont déjà ne sont pas affectées). **Refuser** la mise à jour ne désinstalle rien.

**Revenir en arrière**, par ordre de préférence :

1. **KIR** (si Microsoft en publie un) : GPO, sans retirer le correctif de sécurité.
2. **Contournement** documenté dans la KB.
3. **Désinstallation** ciblée de la cumulative (`DISM /Remove-Package`, ou approbation pour suppression), en sachant que la machine redevient vulnérable : **dérogation obligatoire**.

> ⚠️ **Piège** — Retirer une cumulative, c'est retirer **tous** les correctifs de sécurité du mois. Ce n'est jamais une décision technique seule : c'est une décision de risque, prise avec la RSSI, limitée dans le temps.

## 12.6 Dérogations

Une dérogation contient au minimum : machines concernées, correctif(s) non installé(s), raison, **mesures compensatoires** (isolement réseau, désactivation d'un service, surveillance renforcée), **date de fin**, validation RSSI. Elle est revue à chaque cycle. Une dérogation sans date de fin n'est pas une dérogation, c'est un oubli organisé. Modèle en Annexe C.

## 12.7 Vérifier et prouver

**Trois sources qui ne disent pas la même chose :**

| Source | Ce qu'elle mesure | Limite |
|---|---|---|
| **WSUS** | ce que les clients ont **déclaré** à leur dernier rapport | une machine silencieuse garde un état ancien ; hors support = « conforme » |
| **UBR** (registre, inventaire) | le niveau de cumulative **réellement installé et actif** | ne couvre pas .NET, Office, Edge |
| **Scanner de vulnérabilités** | les failles détectables depuis le réseau ou un agent | faux positifs (KB remplacée, redémarrage en attente, détection par version de fichier) |

Une conformité sérieuse **croise** les trois et traite les écarts.

**Indicateurs utiles** (rapport mensuel à la RSSI) :

- taux de machines au **niveau du mois** (UBR attendu) à J+15 et J+30, par population (postes, serveurs, critiques) ;
- délai moyen entre publication et installation, **pour les failles exploitées** en particulier ;
- machines **silencieuses** (pas de rapport depuis 14 jours) ;
- machines en **version hors support** ;
- machines en **redémarrage en attente** depuis plus de 3 jours ;
- dérogations actives et leur échéance.

**Le cadre** : le guide d'hygiène informatique de l'ANSSI demande une politique de mises à jour définie et appliquée ; l'ISO/IEC 27001:2022 en fait une mesure (A.8.8, gestion des vulnérabilités techniques) ; la directive **NIS2** inclut la gestion des vulnérabilités parmi les mesures exigées des entités concernées (suivre l'état de la transposition française sur le site de l'ANSSI) ; pour le secteur financier, **DORA** et son règlement délégué sur la gestion des risques TIC (2024/1774) consacrent des exigences explicites à la gestion des vulnérabilités et des correctifs. Dans tous les cas, l'auditeur demandera : **la politique, les délais, la preuve, les exceptions**.

## 12.8 Encart : les serveurs

- **Ordre** : serveurs de test, puis non critiques, puis critiques ; **le serveur WSUS et les serveurs exposés tôt** dans la séquence.
- **Contrôleurs de domaine** : un par un, en vérifiant la réplication entre chaque ; jamais tous la même nuit.
- **Clusters** : *Cluster-Aware Updating* (CAU) bascule les rôles d'un nœud à l'autre pendant la mise à jour.
- **Avant** : sauvegarde ou instantané (*snapshot*) vérifié pour les serveurs critiques, fenêtre de maintenance convenue avec le métier, plan de retour arrière.
- **Windows Server 2016** : approuver la SSU **et** la cumulative (Ch.4) ; fin de support le **12 janvier 2027**.
- **Hotpatch** sur Server 2025 : possible via Azure Arc (abonnement payant), hors WSUS (Ch.14).

Approfondissement : version complète, Ch.19 à 23.

> 🧵 **Fil rouge — Mardi 10 novembre 2026 (et après)**
>
> 19 h 40 : synchronisation terminée. Inès lit les gravités : une faille exploitée touche un composant présent sur tous les postes, mais seulement en élévation de privilèges locale. Grille : **P1**. Elle propose pilote système dès le jeudi 12 (le 11 est férié), production à J+8 au lieu de J+15. Pour les 40 postes 23H2 de Lille sous dérogation, c'est la **dernière** cumulative : leur dérogation expire le 10 décembre. Le 2 décembre (J+22), le rapport montre 97,8 % des postes au bon UBR, 31 machines silencieuses (dont 22 portables jamais rallumés depuis les congés) et 0 serveur en retard. Le rapport part chez Claire avec la liste nominative.

> 📌 **À retenir**
>
> - Le cycle se pense en **J+n** ; applicatifs et système séparés ; nettoyage à date fixe.
> - Une **voie d'urgence** écrite, avec qui décide et en combien de temps.
> - Pilote représentatif ; suspendre = retirer l'approbation ; désinstaller = décision de risque + dérogation.
> - Prouver = croiser WSUS, UBR et scanner ; suivre les silencieux, les hors-support, les redémarrages en attente.

---
