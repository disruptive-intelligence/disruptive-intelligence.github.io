---
title: Chapitre 3 — Pourquoi le dark web existe
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - 'Partie I — Fondations : COMPRENDRE le DARK WEB'
  - index.md
---

Le dark web n'est pas une accumulation fortuite d'infrastructures. Il existe parce qu'il répond à des besoins réels, et il persiste parce que ces besoins persistent. Ce chapitre articule les raisons légitimes, les usages détournés, et la tension fondamentale qui structure le débat public.

## 3.1 L'anonymat comme besoin fondamental

**Résistance à la censure**. Dans les régimes autoritaires (République populaire de Chine, Iran, Russie depuis 2022, Biélorussie, Myanmar, Érythrée, Corée du Nord dans une certaine mesure, Turkménistan), l'accès à des contenus jugés subversifs par l'État est filtré, surveillé, parfois criminalisé. Tor permet, dans beaucoup de ces contextes, d'accéder à Wikipedia, à des médias indépendants (Voice of America, BBC Persian, Deutsche Welle), à des réseaux sociaux bloqués (Twitter/X bloqué en Chine, Facebook en Iran). **Reporters Sans Frontières** opère des miroirs .onion de médias dissidents. Le **Tor Project** développe des techniques dédiées (bridges, pluggable transports comme obfs4, meek, snowflake) pour contourner le Deep Packet Inspection des censeurs.

La mesure n'est pas théorique. Pendant les manifestations en Iran (2022-2023, mouvement Woman Life Freedom), l'usage de Tor a bondi. Après l'invasion russe de l'Ukraine (février 2022) et le durcissement du régime russe vis-à-vis des médias (blocage de Facebook, Twitter, de nombreux médias indépendants), les connexions russes à Tor ont augmenté. Ces périodes de pic confirment que Tor est un **outil opérationnel de résistance informationnelle**.

**Protection des sources journalistiques**. La protection des sources est un pilier de la liberté de la presse, reconnu dans les législations démocratiques (article 10 CEDH, jurisprudence Goodwin c. Royaume-Uni 1996, First Amendment américain, loi française sur la liberté de la presse). Le dark web offre des canaux techniques pour que les sources communiquent avec les journalistes sans risque d'identification.

**SecureDrop** (développée initialement par Aaron Swartz et James Dolan, maintenue par la Freedom of the Press Foundation) est la plateforme de référence. Déployée par : le New York Times, le Guardian, le Washington Post, Le Monde, Der Spiegel, ProPublica, The Intercept, la BBC, et des dizaines d'autres médias. L'affaire **Panama Papers** (2016) et l'affaire **LuxLeaks** (2014) n'auraient pas été techniquement possibles sans des canaux de transmission anonymes.

**AfriLeaks** pour les lanceurs d'alerte africains, **GlobaLeaks** comme plateforme open source généraliste, **Hermes Center** pour le soutien technique à ces déploiements — un écosystème s'est structuré autour de cet usage.

**Vie privée comme droit fondamental**. Article 8 de la CEDH (respect de la vie privée et familiale), article 12 de la Déclaration universelle des droits de l'homme, article 7 de la Charte des droits fondamentaux de l'UE. L'anonymat en ligne est un **instrument** de ces droits. Dans un contexte de surveillance massive (activités commerciales de profilage, surveillance étatique légale ou illégale, collecte par des États hostiles), l'anonymat permet des choix informationnels libres.

**Communications sensibles légitimes**. Défenseurs des droits humains en zones hostiles, avocats consultant des cas sensibles, médecins communiquant sur des patients en zones de conflit, chercheurs en sécurité testant des infrastructures, employés lanceurs d'alerte envers leur propre employeur. L'anonymat technique protège des usages légitimes qui, sans anonymat, seraient impossibles ou dangereux.

## 3.2 L'anonymat comme facilitateur criminel

Le dark web offre aux acteurs malveillants un espace où :

- **L'identification est difficile** : l'IP source est masquée, les pseudonymes sont jetables, les artefacts de compilation et les conventions linguistiques peuvent être contrôlés.
- **Les transactions sont pseudonymes ou anonymes** : Bitcoin pseudonyme avec traçabilité croissante, Monero anonyme par construction.
- **L'infrastructure est résistante aux saisies** : un site .onion ne dépend d'aucun registre centralisé ; la saisie nécessite soit la compromission du serveur physique, soit l'identification de l'opérateur.

Les usages criminels documentés couvrent un spectre large : marchés de drogues (de loin le volume dominant historiquement, en baisse relative depuis 2020), données volées et credentials, armes (volume marginal, beaucoup de scams), documents contrefaits, services de hacking, CSAM (priorité 1 des forces de l'ordre), blanchiment, forums de fraude, infrastructures de communication pour cybercriminels sophistiqués.

La diversité de ces usages, du trafiquant solo au groupe ransomware étatique, montre que le dark web n'est **ni un repaire de super-criminels ni un simple outil de liberté** — l'anonymat est moralement neutre, c'est **l'usage** qui est qualifiable.

## 3.3 La tension fondamentale et ses régulations

La tension n'a pas de résolution simple : **l'anonymat technique qui protège les dissidents protège aussi les criminels**. Supprimer Tor (si c'était techniquement faisable, ce qui est contesté) ne supprimerait pas le besoin d'anonymat des dissidents — il les priverait d'un outil essentiel. Surveiller massivement Tor (comme certaines juridictions autoritaires tentent de le faire) compromet structurellement les usages légitimes.

Les régulations contemporaines tentent de naviguer cette tension par plusieurs approches.

**Lutte ciblée contre les usages criminels spécifiques**. Approche occidentale dominante : ne pas interdire Tor, mais poursuivre les opérateurs de plateformes criminelles (Ulbricht, Cazes, Khoroshev/LockBitSupp), les utilisateurs de CSAM identifiables, les infrastructures de paiement du crime. Les investigations combinent OSINT, analyse blockchain, erreurs OPSEC, infiltration, coopération internationale.

**Régulation des cryptomonnaies**. Parce que l'anonymat financier est le **maillon faible** de la cybercriminalité (à un moment, l'argent doit être converti en fiat utilisable), les régulateurs durcissent les exchanges (KYC renforcé, déclaration de transactions, sanctions ciblées type Tornado Cash en août 2022). Voir Ch.8 et Ch.31.

**Coopération internationale**. Convention de Budapest sur la cybercriminalité (2001), élargie par un deuxième protocole additionnel en 2022 sur la coopération renforcée et la divulgation électronique de preuves. Europol, Interpol, J-CAT, FBI Legal Attaché en poste dans les ambassades. Un écosystème d'échanges de renseignement et de coordination d'opérations.

**Approches contestées dans les démocraties**. Certaines juridictions explorent des pistes qui posent des questions de libertés publiques : lois sur la « responsabilité des plateformes » (Royaume-Uni Online Safety Act, UE Digital Services Act), tentatives de contrer le chiffrement de bout en bout pour permettre l'accès des autorités (projets récurrents type EARN IT aux US, Chat Control en UE — encore débattu), extension des pouvoirs d'interception (projets de mise à jour des législations nationales). Ces approches divisent, parce qu'elles pèsent sur l'équilibre vie privée / sécurité publique.

**Approches criminelles dans les régimes autoritaires**. Blocage pur et simple de Tor (Chine, Iran périodiquement), criminalisation de son usage (Russie depuis 2021 sous certaines formes), surveillance agressive des utilisateurs identifiés. Ces approches s'alignent sur des objectifs de contrôle politique plus que de lutte contre la criminalité.

L'équilibre exact entre anonymat et responsabilité reste un débat politique et sociétal vivant, sans résolution consensuelle à l'horizon.

---
