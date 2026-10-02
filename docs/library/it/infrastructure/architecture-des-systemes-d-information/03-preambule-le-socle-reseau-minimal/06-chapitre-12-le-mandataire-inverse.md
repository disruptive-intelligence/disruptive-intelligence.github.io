---
title: Chapitre 12 — Le mandataire inverse
source: IT/06 Infrastructure & architecture/Infrastructure & SI/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - Préambule — Le socle réseau minimal
  - index.md
---

> **Le composant que ce cours voit le plus souvent mal compris**, et celui dont le nom trompe le plus.

## 12.1 À quoi ça sert

Recevoir les demandes venues de l'extérieur **à la place** des serveurs internes, et les relayer. L'extérieur ne parle jamais au serveur : il parle au mandataire.

🖼 **SCHÉMA 12.1 — Ce que le mandataire inverse change**

```
  SANS                Internet ──────────────► [ serveur web ]
                      Le serveur est joignable directement.
                      Son adresse est publique. Sa version est visible.
                      Une faille du serveur est directement exploitable.

  AVEC                Internet ──► [ mandataire ] ──► [ serveur web ]
                      Le serveur n'est joignable que par le mandataire.
                      L'extérieur ne connaît que l'adresse du mandataire.
                      Une faille du serveur exige d'abord de passer le mandataire.
```


## 12.2 Les quatre fonctions qu'il assure réellement

**On croit qu'il en a une. Il en a quatre, et elles s'ajoutent progressivement dans une architecture.**

| # | Fonction | Ce qu'elle apporte | Quand elle apparaît |
|---|---|---|---|
| **1** | **Masquer** | Le serveur n'est pas exposé directement | Dès qu'un service est publié |
| **2** | **Terminer le chiffrement** | Un seul point où gérer les certificats | Dès qu'il y a plus d'un serveur |
| **3** | **Authentifier** | On prouve son identité **avant** d'atteindre l'application | **Souvent sa vraie raison d'être** |
| **4** | **Router selon le contenu** | Un même point d'entrée pour plusieurs applications | Quand les applications se multiplient |

⚠️ **La fonction 3 est celle qu'on oublie et qui compte le plus.** Placer l'authentification devant l'application signifie qu'une faille de l'application **n'est pas atteignable par un anonyme**. C'est un changement de nature, pas un raffinement.

## 12.3 Ce qu'il fait à la donnée

Cela dépend du mode de terminaison retenu. **Dans le modèle employé dans ce cours, le mandataire termine le chiffrement** : il lit le contenu, parfois le modifie — en-têtes, cache, compression — et le rechiffre ou non vers le serveur. **C'est alors un point où le contenu est en clair**, donc un point d'observation et un point de risque.

⚠️ **Ce n'est pas une propriété obligatoire d'un mandataire inverse.** Un mandataire peut relayer un flux chiffré sans le terminer ; il ne voit alors que les extrémités.

🖼 **SCHÉMA 12.2 — Les trois modes de terminaison du chiffrement**

```
  A — TERMINAISON AU SERVEUR  (« passthrough »)
      client ══chiffré══════════════════════════► serveur
      Le mandataire relaie sans ouvrir.
      → aucune inspection possible · aucun contrôle applicatif
      → aucune authentification préalable possible
      → le certificat est géré sur chaque serveur

  B — TERMINAISON AU MANDATAIRE, PUIS CLAIR
      client ══chiffré══► [ mandataire ] ──clair──► serveur
      → inspection et authentification possibles
      → le trafic interne circule en clair
      → un seul certificat à gérer

  C — TERMINAISON PUIS RECHIFFREMENT
      client ══chiffré══► [ mandataire ] ══chiffré══► serveur
      → inspection ET trafic interne protégé
      → deux jeux de certificats à gérer
      → charge de chiffrement doublée
```


| Mode | Voit le contenu | Trafic interne protégé | Authentification possible | Coût |
|---|---|---|---|---|
| **A** | ❌ | ✅ | ❌ | Certificats sur chaque serveur |
| **B** | ✅ | ❌ | ✅ | Le plus simple, et le plus courant |
| **C** | ✅ | ✅ | ✅ | Deux gestions de certificats, charge doublée |

**Ce que le mode change en lecture** : la question *« qui voit le contenu en clair ? »* n'a pas la même réponse selon les trois — et **aucun schéma ne le dit**. C'est une question à poser.

⚠️ **La conséquence en sécurité, souvent mal comprise** : en mode B, le trafic entre le mandataire et le serveur est en clair **sur votre réseau interne**. Ce n'est un problème que si ce réseau n'est pas maîtrisé — c'est un arbitrage, pas une faute.

🔭 **À RECONNAÎTRE — WAF**

**① Qu'est-ce que c'est.** Un dispositif qui **analyse et filtre le trafic web applicatif** selon des règles de sécurité — contenu des requêtes, paramètres, en-têtes.

**② Quel problème il résout.** Un pare-feu réseau décide si un flux passe ; il ne regarde pas *ce que la requête demande*. Un mandataire inverse relaie ; il ne juge pas le contenu. **Le WAF comble cet écart.**

**③ Les trois se distinguent, et se confondent en pratique** :

| | **Pare-feu** | **Mandataire inverse** | **WAF** |
|---|---|---|---|
| Décide selon | Adresses, ports, état | Le chemin, le nom demandé | **Le contenu applicatif de la requête** |
| Question posée | *Ce flux a-t-il le droit de passer ?* | *Quel serveur doit répondre ?* | *Cette requête est-elle légitime ?* |
| Voit le contenu | Selon la génération | Si le chiffrement y est terminé | **Nécessairement** |

⚠️ **Les trois peuvent être trois équipements, un seul équipement, ou un service en ligne.** Sur un schéma, une même boîte peut porter les trois — et rien ne le dit.

**④ Ce que cela change.** Le WAF **doit voir le contenu en clair**, donc il impose le mode B ou C du §12.3. Il devient un point où tout le trafic web est lisible.

**⑤ Le coût.** Des faux blocages qui cassent des usages légitimes · un réglage long, souvent en mode observation pendant des semaines · une latence · **un composant de plus sur le chemin critique**.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On a un WAF devant » | **En mode blocage ou en mode observation ?** Beaucoup restent en observation des années |
| « Le WAF bloque » | Une règle a été déclenchée. Légitime ou faux positif ? |
| « C'est protégé, il y a un firewall » | **Un pare-feu réseau ne juge pas le contenu d'une requête web** |

---

🔭 **À RECONNAÎTRE — CDN**

**① Qu'est-ce que c'est.** Un réseau de serveurs répartis qui **servent des contenus au plus près de l'utilisateur**, en s'intercalant devant votre serveur d'origine.

**② Quel problème il résout.** La latence, la charge, et l'absorption des pointes — y compris malveillantes.

**③ Ce que cela change au dessin naïf.**

```
   SANS          Utilisateur ──────────────► serveur d'origine

   AVEC          Utilisateur ──► [ CDN ] ──► serveur d'origine
                                    │
                              répond directement
                              si le contenu est en cache
```


**④ Les cinq questions que le CDN impose**, et ce sont elles qui font sa valeur pédagogique :

| Question | Pourquoi elle compte |
|---|---|
| **Où le chiffrement est-il terminé ?** | Chez le fournisseur du CDN — **il voit le contenu en clair** |
| **Qu'est-ce qui est mis en cache ?** | Une page personnalisée mise en cache par erreur est servie à un autre utilisateur |
| **Quelle adresse voit l'origine ?** | Celle du CDN, pas celle de l'utilisateur — §P.4, §34.2 |
| **Que se passe-t-il si le CDN tombe ?** | Selon la configuration : plus rien, ou un repli vers l'origine qui ne tiendra pas la charge |
| **Où placer le WAF ?** | Souvent chez le fournisseur du CDN, puisque c'est là que le contenu est lisible |

⚠️ **La deuxième ligne produit des incidents réels et embarrassants** : un contenu personnalisé — un panier, un nom, une page authentifiée — mis en cache et servi à d'autres. **La règle de cache est une décision de sécurité, pas un réglage de performance.**

**⑤ Le coût.** Une dépendance à un tiers pour la disponibilité de votre site · un point où le contenu est en clair hors de chez vous · **une origine qui doit rester protégée** — sinon on la contourne en s'adressant directement à elle.

**⑥ En réunion**

| Ce que vous entendrez | À vérifier |
|---|---|
| « On est derrière un CDN » | **L'origine est-elle joignable directement ?** Si oui, le CDN se contourne |
| « Le CDN gère le TLS » | Il voit tout en clair. **Rechiffre-t-il vers l'origine ?** |
| « On a purgé le cache » | Un contenu obsolète était servi. **Combien de temps l'a-t-il été ?** |

## 12.4 Mandataire inverse ou répartiteur de charge ?

**Une confusion fréquente, après celle avec le pare-feu**, et la distinction est utile.

| | **Mandataire inverse** | **Répartiteur de charge** |
|---|---|---|
| Sa raison d'être | **Masquer et contrôler** | **Distribuer et absorber les pannes** |
| Décide selon | Le contenu de la demande — chemin, nom demandé | La disponibilité et la charge des membres |
| Nombre de cibles | Une ou plusieurs | **Plusieurs, par définition** |
| Authentifie | Souvent | Rarement |

⚠️ **En pratique, un même équipement fait souvent les deux** — et c'est pourquoi les deux termes sont employés indifféremment en réunion. **La question qui tranche** : *cet équipement existe-t-il pour cacher le serveur, ou pour en avoir plusieurs ?* La réponse dit à quoi on renoncerait en le supprimant.

## 12.5 La confusion avec le pare-feu

Celle d'Amélie au §1.8, et elle est universelle.

| | Pare-feu | Mandataire inverse |
|---|---|---|
| Décide | Si le flux passe | Ce qui est servi, et par quel serveur |
| Voit | Les extrémités, parfois le contenu | Le contenu **si le chiffrement y est terminé** — modes B et C |
| Termine la connexion | Non | **Oui en modes B et C**, non en mode A |
| Peut authentifier | Rarement | **Oui, et c'est souvent sa vraie raison d'être** |
| S'il tombe | Selon la configuration | **Les accès externes seuls** |

## 12.6 S'il disparaît

Tout ce qui est publié devient injoignable de l'extérieur — **et reste joignable de l'intérieur**.

🔥 **SCÉNARIO — le mandataire fonctionne, le service ne répond plus**

| Question | Réponse |
|---|---|
| Symptôme | Les clients externes obtiennent une erreur. Le mandataire répond, sa supervision est verte |
| Hypothèse naïve | « Le mandataire est en panne » |
| Dépendance réelle | **Le serveur derrière lui**. Le mandataire va bien : il n'a plus personne à qui parler |
| Ce que le schéma aurait dû montrer | Les contrôles de santé entre le mandataire et ses cibles |
| Comment vérifier | Le journal du mandataire : il enregistre l'échec de connexion vers l'arrière |

⚠️ **Ce scénario illustre une règle générale** : un composant intermédiaire en bonne santé ne dit rien de la santé du service. **La supervision d'un mandataire doit porter sur ce qu'il obtient de ses cibles, pas sur son propre état.**

## 12.7 Sur un schéma

En zone démilitarisée, entre la bordure et l'interne. **Reconnaissable à sa position** : tout ce qui vient de l'extérieur y converge.

🗣 **VOCABULAIRE DE RÉUNION**

| Ce que vous entendrez | Ce que la personne veut dire | À vérifier |
|---|---|---|
| « C'est derrière le reverse » | Le service n'est pas exposé directement | **Quel mode de terminaison ?** Y a-t-il un chemin direct depuis l'interne ? |
| « Le frontal termine le TLS » | Mode B ou C | Rechiffre-t-il vers l'arrière, ou le trafic interne est-il en clair ? |
| « C'est une VIP » | Une adresse virtuelle portée par le mandataire ou le répartiteur | Combien de cibles derrière ? Une seule ? |
| « Il faut publier l'appli » | La rendre joignable depuis l'extérieur | Par où ? Avec quelle authentification en amont ? |

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Ne pas exposer directement les serveurs | Un composant de plus à exploiter et corriger |
| Concentrer le chiffrement et les certificats | Une gestion de certificats · **un point où tout est en clair, en modes B et C** |
| Authentifier avant d'atteindre l'application | **Une dépendance forte à l'annuaire** |
| Router selon le contenu | Une configuration qui devient vite complexe |
| Servir de point d'entrée unique | **Un point de rupture pour tous les accès externes** |

🏭 **TROIS TAILLES** — Atelier Martin : **aucun**. Elle ne publie aucun service : la contrainte n'existe pas. HELIOMED : un couple redondé, parce qu'elle publie une plateforme de télésuivi accessible à ses clients. Novaris : une ferme par région, parce que la latence et la réglementation imposent une terminaison locale.

---
