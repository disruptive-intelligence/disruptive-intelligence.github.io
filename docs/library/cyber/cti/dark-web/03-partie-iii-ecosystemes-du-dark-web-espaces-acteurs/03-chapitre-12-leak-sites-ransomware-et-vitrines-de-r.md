---
title: Chapitre 12 — Leak sites ransomware et vitrines de revendication
source: Cyber/01_CTI/Dark_Web_vFULL.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie III — Écosystèmes du DARK WEB : espaces, acteurs et culture'
  - index.md
---

Les **leak sites** sont les vitrines publiques des groupes ransomware. C'est là que les groupes revendiquent les victimes, publient des échantillons de données volées, et menacent de publier l'intégralité si la rançon n'est pas payée. Depuis l'avènement du modèle « double extorsion » (chiffrement + menace de publication), les leak sites sont devenus un des objets d'investigation CTI les plus riches.

## 12.1 Le modèle de la double extorsion

Historiquement, un ransomware chiffrait les données et demandait une rançon pour la clé de déchiffrement. La victime avait deux options : payer, ou restaurer depuis des backups. Si les backups existaient et étaient intacts, la victime pouvait refuser de payer.

Le modèle **double extorsion** (popularisé par Maze en 2019-2020) ajoute une couche. L'attaquant **exfiltre les données avant de les chiffrer**, puis menace de les publier publiquement si la rançon n'est pas payée — même si la victime a des backups et peut restaurer. L'intérêt criminel : augmente la pression (risque réputationnel, légal, contractuel de la publication), élargit le levier (même les victimes avec backups sont touchées).

Le **leak site** est l'outil de cette menace. Plateforme publique où le groupe **revendique** la victime (nom, secteur, pays), **publie des échantillons** de données volées (documents sensibles, financiers, RH), **affiche un countdown** jusqu'à publication intégrale, et **publie intégralement** si non-paiement.

L'effet psychologique est considérable. Une victime qui voit son nom publié sur un leak site majeur est dans une position extrêmement inconfortable — ses clients, partenaires, journalistes, autorités voient le post. La pression au paiement est forte.

## 12.2 Anatomie d'un post de leak site

Un post typique contient :

- **Nom de la victime** : raison sociale, parfois logo.
- **Secteur d'activité** : aerospace, healthcare, manufacturing, etc.
- **Pays / région** : juridiction.
- **Taille** : chiffre d'affaires approximatif, nombre d'employés.
- **Description** : quelques paragraphes sur ce que le groupe a exfiltré, type de données, volumétrie.
- **Countdown** : temps restant avant publication intégrale (typiquement 1-4 semaines).
- **Échantillons** : 10-100 fichiers publiés comme preuve de compromission. Choisis pour maximiser l'impact réputationnel (docs financiers, contrats, emails de dirigeants, données RH).
- **Contact** : méthode pour initier la négociation (souvent un onion avec un chat ou un formulaire).

Certains leak sites permettent des **interactions** : vote de la communauté pour pousser à la publication, mise en vente des données à la pièce, achats « first-come first-served » pour les autres criminels intéressés.

## 12.3 Les principaux groupes et leurs leak sites en 2024-2026

*Liste non exhaustive et évolutive — plusieurs groupes disparaissent ou rebrandent.*

**LockBit** — historiquement le plus prolifique. Leak site très actif, interface sombre, countdown flashy. **Operation Cronos (février 2024)** a saisi l'infrastructure, identifié Dmitry Khoroshev comme LockBitSupp, rendu publiques des clés de déchiffrement. LockBit a tenté un relaunch mais sa crédibilité est entamée.

**ALPHV / BlackCat** — malware sophistiqué écrit en Rust. Disparition en mars 2024 suite à ce qui semble être un exit scam post-paiement Change Healthcare (~22 M USD présumés).

**Cl0p** — spécialisé dans l'exploitation de vulnérabilités d'edge devices (MOVEit 2023, Fortra GoAnywhere, Oracle EBS 2025). Leak site moins visuel que LockBit mais attaques techniquement sophistiquées.

**Black Basta** — actif depuis 2022, ciblage enterprise. Leak data massives en 2024-2025.

**Play / PlayCrypt** — actif depuis 2022, ciblage varié.

**Akira** — émergent fin 2023, croissance rapide.

**RansomHub** — émergent mi-2024, semble absorber des affiliés d'ALPHV post-disparition.

**Qilin** — anglophone malgré son nom, actif.

**BianLian** — historiquement hybrid chiffrement + exfiltration, en 2023 s'est tourné vers extorsion seule (sans chiffrement).

**8Base, Hunters International, Inc Ransom, Dragonforce, Medusa** — autres groupes actifs à surveiller.

La scène change **mensuellement** — des groupes disparaissent, rebrandent, émergent. Les outils de monitoring (Ransomfeed, Ransomwatch) suivent ces évolutions en temps réel.

## 12.4 La lecture analytique d'un leak site

Pour un analyste CTI, chaque revendication de leak site est une source de renseignement.

**Vérification de la compromission réelle**. Tous les posts ne correspondent pas à de vraies victimes.

- **True positives** : la victime confirme (rarement publiquement, souvent via comms privées).
- **False claims** : groupe re-publie des données d'un breach antérieur sous son nom (pattern récurrent), ou revendique une compromission inexistante pour gonfler sa réputation.
- **Doubles claims** : la même victime revendiquée par deux groupes (conflit d'affiliés, rachat d'accès).

**Signaux sur l'activité du groupe**. Volume de revendications par mois, secteurs ciblés, géographies, évolution du rythme. Un groupe qui passe de 5 à 50 revendications/mois signale une croissance significative ou un recrutement d'affiliés.

**Patterns de targeting**. Les secteurs / pays ciblés donnent des indications sur les priorités et les compétences du groupe. Un groupe avec beaucoup de santé US est différent d'un groupe avec beaucoup de manufacturing EU.

**TTP implicites**. Les leak sites ne publient pas les TTPs (pour protéger leurs accès), mais des patterns peuvent se déduire — affinité pour certaines tailles de victimes, certains vecteurs d'entrée inférables par crosscheck avec cas connus.

**Indicateurs de disruption**. Un leak site qui disparaît brutalement, dont le countdown se fige, dont les affiliés migrent vers un concurrent — signaux d'une operation law enforcement en cours ou d'un conflit interne.

## 12.5 Le monitoring automatisé

**Ransomfeed.it** (site public, gratuit) agrège les revendications de dizaines de leak sites en temps réel. Outils open source type **Ransomwatch** fournissent des archives.

**Vendors CTI** (Recorded Future, Mandiant, CrowdStrike, Flashpoint, SOCRadar, Flare) intègrent le monitoring dans leurs plateformes avec alerting sur marques, secteurs, géographies.

**Limites** : leak sites modernes implémentent protections anti-scraping (CAPTCHA, rate limiting, proof-of-work) ; leak sites « tiered » avec partie publique + partie accessible uniquement après interaction ; échantillons publiés pas toujours téléchargés / analysés.

## 12.6 Le paiement de rançon : angle d'investigation

Les paiements de rançon, quand ils surviennent, laissent des traces **on-chain** exploitables.

**Mécanisme** : le groupe fournit une adresse Bitcoin / Monero / autre dans un portail de négociation. La victime paie. Les fonds transitent vers le groupe, puis sont blanchis (mixers, Monero swaps, OTC).

**Pour l'investigation** : si l'adresse est connue, le paiement confirme une compromission ; les mouvements on-chain peuvent révéler des connexions à d'autres opérations du même groupe ; les tentatives d'off-ramp peuvent révéler des identités si passage par exchange KYC.

**Saisies de paiements** : le FBI a récupéré des portions de rançons dans plusieurs cas emblématiques — Colonial Pipeline (~2,3 M USD récupérés en juin 2021), autres cas plus récents. Nécessite coopération internationale et vitesse d'exécution (avant blanchiment complet).

**Sanctions OFAC** : payer un groupe sanctionné (certains groupes sont sur listes OFAC) peut exposer l'organisation payeuse à des sanctions américaines. Considération réglementaire importante, qui pèse dans les décisions de paiement.

## 12.7 Le débat sur le paiement

Question récurrente : faut-il payer une rançon ?

**Arguments contre le paiement** : finance l'activité criminelle ; ne garantit pas la non-publication (plusieurs cas de groupes publiant après paiement) ; ne garantit pas l'intégrité des données exfiltrées ; crée un précédent — organisation qui paie devient cible récurrente ; expose à sanctions (groupes OFAC).

**Arguments pour le paiement** : urgence opérationnelle (vie humaine en cause dans certains cas — hôpitaux) ; coût moindre que la perte business prolongée ; clé de déchiffrement peut accélérer la reprise.

**Positions officielles** : la plupart des agences nationales (FBI, ANSSI, NCSC) recommandent de **ne pas payer** comme principe, tout en acceptant pragmatiquement que la décision incombe à la victime.

**Les faits statistiques** (rapports Coveware, Chainalysis) : la proportion de victimes qui paient a **baissé** sur la décennie (de ~70% en 2018-2019 à ~25-30% en 2024). Le paiement moyen a augmenté (quelques millions de dollars par cas en moyenne sur les grandes victimes). La dynamique a changé : moins de payeurs, payeurs plus gros.

---
