---
title: Chapitre 1 — Pourquoi raisonner en écosystème
source: Cyber/01 CTI & renseignement/Menace cyber/Cartographie des écosystèmes cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - 'Partie I — Fondations : penser en écosystème'
  - index.md
---

## 1.1 Les limites de la vision « un hacker fait tout »

La représentation dominante de la cybermenace dans les médias, dans les présentations de direction générale, et même dans certains rapports de sécurité, reste celle du hacker isolé : un individu techniquement brillant qui, seul devant son écran, compromet un système, vole des données, et disparaît. Cette image est obsolète depuis au moins quinze ans, et elle est activement nuisible à la compréhension de la menace contemporaine.

La persistance de cette représentation s'explique par trois facteurs. Premièrement, le narratif individuel est cognitivement satisfaisant : il est plus facile de concevoir un adversaire unique qu'un réseau de prestataires interconnectés. Deuxièmement, les affaires judiciaires se concluent souvent par l'arrestation d'un individu ou d'un petit groupe, ce qui renforce l'illusion d'un acteur monolithique même quand l'enquête a révélé un écosystème complet. Troisièmement, une partie de l'industrie de la cybersécurité a intérêt à simplifier la menace pour vendre des solutions « clé en main » — si le problème est un hacker, la solution est un produit.

Le problème opérationnel de cette vision est qu'elle conduit à des réponses inadaptées. Si l'analyste pense affronter un individu, il cherche à l'identifier et à le bloquer. Si l'analyste comprend qu'il affronte un écosystème, il cherche à cartographier les dépendances et à identifier les points de fragilité. La première approche est tactique et éphémère ; la seconde est stratégique et structurelle.

> **Implication pour le praticien :** Un rapport d'incident qui conclut par « le groupe X nous a attaqués » sans cartographier la chaîne d'approvisionnement (qui a fourni l'accès initial, qui a fourni le malware, qui héberge l'infrastructure, qui blanchit l'argent) est un rapport incomplet. Il répond au « qui » superficiel mais pas au « comment » structurel — et c'est le « comment » structurel qui permet d'anticiper et de prévenir.

## 1.2 D'un acteur isolé à un marché structuré

la fragmentation des rôles

La cybercriminalité contemporaine fonctionne comme une économie de services spécialisés. Celui qui développe le ransomware ne le déploie généralement pas lui-même. Celui qui compromet le réseau de la victime n'a souvent pas écrit une ligne du malware qu'il utilise. Celui qui négocie la rançon avec la victime n'a souvent jamais touché à un clavier technique. Celui qui blanchit les cryptomonnaies n'a souvent aucune compétence en intrusion informatique.

Cette fragmentation n'est pas un accident — c'est le résultat d'une logique économique de spécialisation. Chaque rôle exige des compétences distinctes, comporte des risques différents, et génère une rémunération propre. Un développeur de ransomware peut toucher un salaire mensuel de 5 000 à 15 000 dollars sans jamais interagir avec une victime. Un affilié (celui qui déploie le ransomware) prend un risque opérationnel plus élevé mais capte 70 à 80 % de la rançon. Un Initial Access Broker (IAB) vend des accès compromis pour quelques centaines à quelques dizaines de milliers de dollars, avec un risque modéré car il n'est pas directement impliqué dans l'extorsion.

La conséquence analytique est fondamentale : « l'attaquant » n'est presque jamais une entité unique. C'est un assemblage temporaire de prestataires spécialisés qui coopèrent le temps d'une opération, chacun apportant sa compétence et facturant son service.

Le détail des rôles spécialisés (développeurs, opérateurs, affiliés, IAB, crypter services, hébergeurs, blanchisseurs, mules, négociateurs, modérateurs) est traité au Ch.17.

## 1.3 La notion d'écosystème

Un écosystème cybercriminel n'est pas simplement un « groupe » au sens classique du terme. C'est un ensemble d'acteurs en interaction — certains stables, d'autres éphémères — qui forment un système fonctionnel plus vaste que la somme de ses parties.

Les composantes d'un écosystème typique incluent un noyau opérateur (les acteurs qui contrôlent les opérations et les décisions stratégiques), des intermédiaires (brokers d'accès, facilitateurs de communication, négociateurs), des sous-traitants techniques (développeurs de malware, fournisseurs de crypters, hébergeurs), des facilitateurs financiers (services de mixing, sociétés écrans, mules), des relais médiatiques et informationnels (leak sites, canaux Telegram, blogs de façade), des clients (les affiliés qui utilisent le service, les acheteurs de données), parfois des sponsors étatiques ou para-étatiques (voir Ch.21), et des communautés périphériques (forums, canaux de discussion, espaces de recrutement).

La propriété fondamentale d'un écosystème est qu'il possède des caractéristiques émergentes que ses composants individuels n'ont pas. Un affilié seul est vulnérable ; un écosystème RaaS complet est résilient. Un forum seul est une liste de messages ; un réseau de forums interconnectés est un marché avec gouvernance, réputation et mécanismes de confiance. C'est cette émergence qui rend l'approche systémique nécessaire.

> **Alerte / Piège fréquent :** La tentation de l'analyste est de traiter un écosystème comme un organigramme figé. C'est une erreur. Les écosystèmes cybercriminels sont dynamiques : les acteurs entrent et sortent, les alliances se forment et se défont, les services disparaissent et sont remplacés. La cartographie d'un écosystème est toujours un instantané daté, pas une structure permanente.

## 1.4 La chaîne de valeur criminelle

Emprunté à l'économie industrielle (le concept de Michael Porter), la notion de chaîne de valeur appliquée à la cybercriminalité décrit la séquence d'activités par lesquelles une menace se transforme en profit. De la conception de l'outil d'attaque à la conversion en argent propre, chaque étape crée et capte de la valeur économique.

Une chaîne de valeur ransomware typique en 2025-2026 se décompose ainsi : le développement de l'outil (le ransomware, son builder, son panel de contrôle), puis l'acquisition d'un accès initial (achat auprès d'un IAB, exploitation d'une vulnérabilité, phishing), puis la compromission du réseau (élévation de privilèges, mouvement latéral, désactivation des défenses), puis l'exfiltration des données (pour la double extorsion), puis le chiffrement et la demande de rançon, puis la négociation avec la victime, puis le paiement en cryptomonnaie, puis le blanchiment (mixing, conversion, cash-out), et enfin le réinvestissement dans l'infrastructure et les opérations suivantes.

L'intérêt analytique de cette vision est double. Premièrement, elle permet d'identifier les points de concentration — les étapes où beaucoup de valeur transite par peu d'acteurs. Les services de mixing, les hébergeurs bulletproof dominants, et les quelques exchanges non coopératifs sont des points de concentration parce que de nombreux écosystèmes dépendent des mêmes prestataires à ces étapes. Deuxièmement, elle permet d'identifier les points de fragilité — les étapes où la disruption serait la plus efficace. La chaîne de valeur complète est détaillée au Ch.18.

## 1.5 Convergence entre technique, finance, logistique, réputation et influence

Un écosystème cybercriminel n'est pas un phénomène purement technique. Il repose sur au moins cinq dimensions qui interagissent.

La **dimension technique** couvre les outils (malware, infrastructure C2, exploits), les compétences (développement, intrusion, administration système), et les plateformes (hébergement, DNS, CDN). La **dimension financière** couvre les flux de valeur (paiements de rançon, rémunérations des prestataires, blanchiment), les instruments (cryptomonnaies, sociétés écrans, mules bancaires), et les mécanismes de transaction (escrow, arbitrage). La **dimension logistique** couvre l'approvisionnement en ressources (acquisition d'accès, recrutement de mules, location d'infrastructure), la coordination opérationnelle (communication entre acteurs, gestion des affiliés), et la continuité des opérations (backup d'infrastructure, migration après disruption). La **dimension réputationnelle** couvre la confiance entre acteurs (réputation sur les forums, vouching, historique de transactions), la crédibilité de la marque (un opérateur RaaS dont les affiliés sont satisfaits attire plus d'affiliés), et la dissuasion (la réputation d'un groupe comme fiable dans le paiement de la rançon encourage les victimes futures à payer). La **dimension informationnelle et d'influence** couvre la pression médiatique sur les victimes (leak sites, menaces de publication), l'amplification via les réseaux sociaux et les médias de façade, et parfois la manipulation narrative à des fins géopolitiques.

L'analyste qui ne regarde que la dimension technique manque les trois quarts de l'écosystème. La cartographie doit intégrer ces cinq dimensions pour être complète.

## 1.6 Fil rouge — Opération NEXUS : le point de départ

> **🔍 NEXUS — Épisode 1**
>
> Le SOC d'Énergis remonte l'alerte à 14h37. Le fichier détecté est un exécutable PE32 de 847 Ko, obfusqué, qui a tenté de résoudre le domaine `update-srv-infra[.]xyz` avant d'être bloqué par l'EDR.
>
> Le réflexe classique de la direction serait de demander : « Qui nous a attaqués ? » La réponse initiale du CERT est : « Un variant de la famille de ransomware PhantomCrypt, associée à une plateforme RaaS active. » Cette réponse est correcte mais radicalement insuffisante. Elle identifie l'outil, pas l'écosystème.
>
> Samira reformule la question : « Quel est l'écosystème derrière ce sample ? Qui l'a développé, qui l'a déployé, qui a fourni l'accès initial, qui héberge l'infrastructure, qui blanchira les fonds si une rançon est payée, et pourquoi cette cible ? » Ce sont ces questions qui guideront les 27 chapitres suivants.

---
