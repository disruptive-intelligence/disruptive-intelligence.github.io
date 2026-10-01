---
title: Chapitre 36 — Automatisation, orchestration et limites
source: Cyber/07 Vulnérabilités & MCS/Maintien en condition de sécurité (MCS).md
note: Maintien en condition de sécurité (MCS)
up:
- - Maintien en condition de sécurité (MCS)
  - ../index.md
- - PARTIE VI — Fin de vie, industrialisation et soutenabilité
  - index.md
---

## 36.1 Que faut-il automatiser en premier

L'ordre importe, et l'intuition conduit généralement au mauvais.

| Rang | Objet | Pourquoi cet ordre |
|---|---|---|
| **1** | **La collecte** — inventaire, versions, états | Sans donnée fiable, tout le reste est faux (§10.1) |
| **2** | **La corrélation** — rapprocher avis et inventaire | Supprime le travail manuel le plus ingrat, sans risque |
| **3** | **La vérification** — contrôler que l'état a changé | Automatiser la preuve libère du temps et améliore l'audit |
| **4** | **Le déploiement** — appliquer les correctifs | Efficace, mais requiert anneaux et critères d'arrêt |
| **5** | **La décision** — prioriser automatiquement | En dernier, et jamais totalement |

**Pourquoi la décision arrive en dernier.** La priorisation dépend de l'exposition et de la criticité métier (§16.2), c'est-à-dire d'informations contextuelles que l'automatisme n'établit pas seul. Un arbre de décision peut être outillé — il l'est utilement — mais ses entrées doivent être fiables, ce qui suppose que les rangs 1 et 2 soient déjà solides.

⚠️ **L'erreur de séquencement la plus fréquente** consiste à automatiser le déploiement en premier, parce que c'est le plus visible. On obtient alors un mécanisme efficace appliqué à un périmètre inconnu — les tableaux de bord verts du §1.4.

## 36.2 Automatiser la remédiation

| Élément | Exigence |
|---|---|
| **Condition de déclenchement** | Écrite, précise, testée : quel type de constat, sur quelle classe d'actif |
| **Périmètre** | Explicitement borné, avec liste d'exclusions |
| **Déploiement témoin** | Obligatoire, même en automatique |
| **Critères d'arrêt** | Chiffrés, évalués automatiquement (§18.4) |
| **Journal** | Chaque action automatique tracée comme une action humaine |
| **Interruption manuelle** | Un moyen d'arrêter immédiatement, connu de l'astreinte |

**Le principe directeur** : l'automatisation ne doit pas retirer de garde-fou. Elle exécute plus vite ce qu'un humain ferait, avec les mêmes protections — anneaux, critères d'arrêt, retour arrière, preuve.

## 36.3 Auto-remédiation : où c'est raisonnable, où c'est dangereux

| Périmètre | Automatisation | Raison |
|---|---|---|
| Postes de travail, correctifs courants | **Raisonnable** | Volume élevé, impact unitaire faible, retour arrière par redéploiement |
| Images et modèles | **Raisonnable** | Corrige la source, effet démultiplié (§28.5) |
| Serveurs C3 non critiques | Raisonnable avec anneaux | Impact limité |
| Serveurs C1 et actifs de niveau 0 | **Déconseillé** | Un incident affecte tout le reste |
| Bases de données | **Déconseillé** | Point de non-retour (§6.7) |
| Équipements réseau | **Déconseillé** | Une erreur coupe l'accès au moyen de la corriger |
| Systèmes industriels | **Proscrit** | Validation constructeur obligatoire (ch. 29) |

**Le critère unique qui résume ce tableau** : automatisez là où **le retour arrière est simple et testé**. Partout ailleurs, l'automatisation transfère un risque humain vers un risque systémique.

## 36.4 La chaîne outillée type

```
Inventaire (source d'autorité, §17.11)
   ↓ enrichi de criticité, exposition, propriétaires
Veille automatisée (§14.6)
   ↓ corrélation, archivage de ce qui est écarté
Constats candidats
   ↓ arbre de décision outillé (§16.3)
Tickets et campagnes (§17.6)
   ↓ affectation automatique par propriétaire d'actif
Déploiement (§18.4)
   ↓ anneaux, critères d'arrêt automatiques
Vérification (§18.9)
   ↓ contrôle de l'état constaté
Preuve archivée (§2.9)
   ↓
Indicateurs (ch. 38)
```


**Les deux points de rupture** les plus fréquents dans cette chaîne : entre l'inventaire et les outils, faute d'identifiant pivot commun (§15.7) ; et entre le déploiement et la vérification, quand la clôture se fait sur déclaration plutôt que sur preuve (§17.8).

## 36.5 L'assistance par intelligence artificielle

**Les usages réellement utiles aujourd'hui**, dans le périmètre de ce cours :

| Usage | Valeur | Précaution |
|---|---|---|
| Résumer un avis technique long | Gain de temps réel | Vérifier les versions affectées à la source |
| Reformuler un constat technique en termes métier | Utile pour les dérogations (§20.10) | Relecture obligatoire |
| Aider à rédiger une règle de détection ou un script | Accélération | Tester avant déploiement |
| Explorer un jeu de données de constats | Aide à l'analyse | Ne pas fonder une décision sur la seule sortie |
| Préparer une communication de crise | Gain de temps sous pression | Validation par le pilote |

**Le risque spécifique** : une sortie plausible mais fausse est plus dangereuse qu'une absence de réponse, parce qu'elle ne déclenche aucune vérification. Une version affectée inexacte, un identifiant inventé, une conclusion sur l'exploitabilité non fondée peuvent orienter une décision entière.

✅ **BONNE PRATIQUE (P0)** — Toute information issue d'une assistance automatisée et destinée à fonder une décision engageante doit être **vérifiée à la source**, et le statut du §14.7 s'applique : ce qui n'est pas vérifié reste une hypothèse.

## 36.6 ⏱ Tendance : volumétrie et vitesse

*Bloc daté, vérifié le 30/07/2026.*

La découverte de vulnérabilités s'accélère, notamment sous l'effet de méthodes de recherche assistées. Trois conséquences pour le dimensionnement des processus, sans dramatisation :

1. **La pression porte sur la vitesse de remédiation**, pas sur la qualité du triage. Une organisation capable de décider vite mais lente à déployer sera limitée par le déploiement.
2. **Le regroupement devient plus rentable que le traitement unitaire** (§16.7) : la montée de version et la reconstruction d'image absorbent le volume, le traitement constat par constat ne le peut pas.
3. **L'exposition redevient le levier principal** : réduire la surface protège indépendamment du volume de vulnérabilités publiées (§11.8).

**Ce qui ne change pas** : l'inventaire, la propriété, les fenêtres, la preuve et le financement. Une organisation qui n'a pas ces cinq bases ne sera pas sauvée par l'automatisation — elle produira simplement plus vite des chiffres faux.

## 36.7 ⚠️ Le risque systémique de l'automatisation

Une mise à jour défectueuse, déployée manuellement, touche quelques machines avant qu'on ne l'arrête. Déployée automatiquement sans garde-fou, elle touche l'ensemble du parc en quelques minutes.

**Les quatre garde-fous non négociables** :

| Garde-fou | Rôle |
|---|---|
| **Déploiement progressif** | Un incident touche un anneau, pas le parc |
| **Critères d'arrêt automatiques** | La campagne s'interrompt sans attendre une décision humaine |
| **Retour arrière testé** | Chronométré, connu de l'astreinte (§18.8) |
| **Interruption manuelle** | Un moyen d'arrêter immédiatement, documenté et connu |

**La règle qui les résume** : *plus le déploiement est rapide, plus les garde-fous doivent être stricts.* L'automatisation sans anneaux n'est pas une accélération, c'est une amplification.

## 36.8 📌 Limites de l'automatisation

- **La dette d'outillage** : chaque automatisme est un actif à maintenir — scripts, connecteurs, règles. Une chaîne outillée non maintenue casse silencieusement.
- **La fragilité des connecteurs** : un changement d'interface côté fournisseur interrompt une intégration, souvent sans alerte.
- **L'effet « tableau de bord vert »** : un automatisme qui échoue silencieusement produit une absence de signal interprétée comme une absence de problème (§15.8).
- **L'automatisation ne crée pas de capacité de décision** : les arbitrages métier, les fenêtres et les dérogations restent humains.
- **Le coût d'intégration** est souvent supérieur au coût de la licence.

✅ **BONNE PRATIQUE (P1)** — Surveillez vos automatismes eux-mêmes : date de dernière exécution réussie, taux d'échec, volume traité. Un automatisme qui ne s'exécute plus est plus dangereux qu'un processus manuel qu'on sait manuel.

→ **Chapitre 37 — Économie du MCS, charge de travail et facteur humain** : financer le dispositif et le rendre soutenable.

## Synthèse mentale du chapitre 36

L'ordre d'automatisation compte, et l'intuition conduit au mauvais : collecte, corrélation, vérification, déploiement, décision — automatiser le déploiement en premier produit un mécanisme efficace appliqué à un périmètre inconnu. L'automatisation ne doit retirer aucun garde-fou : elle exécute plus vite ce qu'un humain ferait, avec les mêmes anneaux, critères d'arrêt et preuves. Le critère qui décide où automatiser est unique : là où le retour arrière est simple et testé. L'assistance automatisée est utile pour résumer, reformuler et explorer, mais une sortie plausible et fausse est plus dangereuse qu'une absence de réponse, car elle ne déclenche aucune vérification. Face à l'accélération de la volumétrie, le regroupement et la réduction d'exposition sont les seuls leviers qui passent à l'échelle. Enfin, un automatisme qui échoue silencieusement transforme une absence de signal en fausse assurance : surveillez vos automatismes comme vous surveillez vos actifs.

**Trois questions de vérification**

1. Votre direction veut automatiser le déploiement des correctifs avant tout le reste. Quel est le problème, et par quoi proposez-vous de commencer ?
2. Sur quel critère unique décidez-vous qu'un périmètre peut recevoir de l'auto-remédiation ?
3. Pourquoi une chaîne d'automatisation non surveillée est-elle plus dangereuse qu'un processus manuel équivalent ?

---
