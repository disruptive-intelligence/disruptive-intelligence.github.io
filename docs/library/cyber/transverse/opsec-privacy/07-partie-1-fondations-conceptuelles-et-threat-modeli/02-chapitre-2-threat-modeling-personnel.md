---
title: Chapitre 2 — Threat modeling personnel
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 1 — Fondations conceptuelles et threat modeling
  - index.md
---

## 2.1 Les cinq questions fondatrices

L’Electronic Frontier Foundation a formalisé un cadre minimal de threat modeling personnel en cinq questions. Elles sont simples, mais leur mise en œuvre rigoureuse change tout.

1. **Que veux-je protéger ?** (mes actifs)
1. **Contre qui ?** (mes adversaires)
1. **Quelle est la probabilité que je doive le protéger ?** (le risque)
1. **Quelles sont les conséquences si j’échoue ?** (l’impact)
1. **Combien de difficultés suis-je prêt(e) à accepter pour empêcher cela ?** (le coût acceptable)

La cinquième est la plus importante et la plus souvent oubliée. Elle ancre la réflexion dans le réel : sans elle, on dérive vers des architectures théoriquement parfaites mais inapplicables dans la vraie vie.

## 2.2 Inventaire des actifs

Un actif est une chose à laquelle tu tiens et que tu veux protéger. Pour un individu, ce sont généralement :

- **Identité** : nom, photo, voix, adresse, état civil, nationalités.
- **Comptes** : email principal (centre de gravité, cf. Ch 29), réseaux sociaux, comptes bancaires, comptes professionnels, comptes cloud, comptes administratifs (impôts, sécurité sociale).
- **Données** : fichiers personnels, photos, documents professionnels, dossiers médicaux, contrats, journaux, correspondance.
- **Appareils** : téléphone(s), ordinateur(s), tablettes, IoT, clés de sécurité, cartes SIM.
- **Relations** : carnet d’adresses, liens familiaux, sources journalistiques, contacts professionnels, réseaux d’engagement (associatif, politique, religieux).
- **Localisation** : domicile, lieux de travail, déplacements habituels, voyages.
- **Réputation** : image publique, dossiers passés, opinions exprimées, contenus produits.
- **Présence physique** : sécurité personnelle, intégrité corporelle, accès au domicile.

Liste tes actifs *avant* de penser aux outils. Pour chacun, note : où est-il stocké, qui y a accès, qu’est-ce qui empêche aujourd’hui un tiers d’y accéder. La plupart des gens découvrent à ce stade que l’« email principal » concentre les clés de tout le reste (récupération de mot de passe, MFA SMS, factures).

## 2.3 Identifier ses adversaires sans inflation ni déni

Deux travers symétriques empoisonnent l’exercice.

L’**inflation** consiste à se croire la cible de la NSA quand on est un militant climatique local. C’est flatteur, c’est anxiogène, c’est inefficace : on construit des architectures sur-dimensionnées qui détournent l’attention des vraies menaces (un employeur qui surveille les emails, un ex qui a gardé un mot de passe, un harceleur qui scrute les réseaux sociaux). On se prépare à Pegasus alors qu’on est vulnérable à un simple phishing.

Le **déni** est l’inverse : « je ne suis personne, qui voudrait m’attaquer ? ». Or beaucoup d’attaques sont *opportunistes* (phishing de masse, vol de crédentials, ransomware). Tu n’as pas besoin d’intéresser quelqu’un personnellement pour être ciblé statistiquement. Et certaines menaces sont *de proximité* (ex-partenaire, employeur intrusif) : il suffit d’une relation à problèmes pour avoir un adversaire réel.

Le bon réflexe : lister les adversaires *plausibles* compte tenu de qui tu es et de ce que tu fais. Un journaliste d’investigation a comme adversaires réalistes : États visés par ses enquêtes, sociétés visées, criminalité organisée si pertinent, harceleurs en ligne (notamment femmes journalistes), employeurs (sécurité industrielle des médias). Une activiste a : forces de l’ordre nationales, infiltrés, contre-mouvements organisés, harceleurs. Un dirigeant : concurrents (espionnage économique), fraudeurs ciblés, criminalité organisée si secteur exposé. Un particulier durci typique : criminalité de masse, employeur, ex-partenaire, plateformes elles-mêmes (capitalisme de surveillance).

## 2.4 Capacité × motivation × probabilité

Chaque adversaire doit être caractérisé par trois paramètres :

- **Capacité** : quelles ressources techniques, juridiques, humaines, financières ? Un service de renseignement étatique a accès à des zero-days, à de la coopération inter-services, à des contraintes judiciaires sur les opérateurs. Un harceleur isolé a accès à Google, des forums, peut-être un peu d’OSINT manuel. La capacité borne le *plafond* de la menace.
- **Motivation** : quel intérêt l’adversaire a-t-il à m’attaquer, *moi spécifiquement* ? Forte (une enquête qui le compromet) ou faible (statistique, sans personnalisation) ?
- **Probabilité** : sachant capacité et motivation, quelle est la probabilité d’occurrence ?

Une matrice utile :

|                      |Faible capacité   |Capacité moyenne|Forte capacité              |
|----------------------|------------------|----------------|----------------------------|
|**Faible motivation** |Risque négligeable|Risque faible   |Risque modéré (opportuniste)|
|**Motivation moyenne**|Risque faible     |Risque modéré   |Risque élevé                |
|**Forte motivation**  |Risque modéré     |Risque élevé    |Risque critique             |

Les défenses doivent être calibrées sur les cases à *risque modéré et plus*. Les cases à risque négligeable n’imposent rien de spécifique.

## 2.5 Coût acceptable de la défense

C’est l’arbitrage permanent. Trois dimensions :

- **Coût financier** : prix des appareils, abonnements (VPN, gestionnaire de mots de passe), clés matérielles.
- **Coût cognitif** : apprendre, mémoriser, configurer, maintenir.
- **Coût social et ergonomique** : friction au quotidien, perte de fonctionnalités, isolement par rapport aux usages dominants.

Une mesure trop coûteuse sur l’une des trois dimensions finit abandonnée. La vraie question n’est pas « quelle est la meilleure configuration ? » mais « quelle est la meilleure configuration que je suis capable de maintenir 18 mois sans relâcher ? ».

Un exemple : Qubes OS offre une compartimentation excellente, mais demande un matériel adapté, deux heures d’installation, une discipline opérationnelle, et une acceptation de friction quotidienne. Si la personne, après deux semaines, repasse à Windows par fatigue, le bénéfice net est négatif (elle a perdu du temps et n’a pas amélioré sa posture). Pour cette personne, un Linux durci + gestionnaire de mots de passe + clé FIDO2 est *meilleur* que Qubes, parce que c’est ce qu’elle tiendra.

## 2.6 Trois niveaux de posture : N1 / N2 / N3

Pour éviter le sur-dimensionnement (et le sous-dimensionnement) qui sont les deux travers symétriques du threat modeling individuel, ce cours propose trois niveaux de posture explicites. Chaque chapitre indiquera, quand pertinent, à quel niveau telle mesure se rapporte.

**Niveau 1 — Hygiène essentielle**

- *Pour qui* : tout adulte connecté, sans contexte de menace personnalisée. La grande majorité des lecteurs.
- *Objectif* : réduire significativement la surface d’exposition au capitalisme de surveillance, à la criminalité opportuniste, aux fuites de credentials, aux harcèlements de bas niveau.
- *Stack type* : gestionnaire de mots de passe (Bitwarden) + MFA matériel (YubiKey) ou TOTP pour comptes critiques + Signal pour communications + chiffrement disque (BitLocker / FileVault / LUKS) + mises à jour disciplinées + sauvegardes 3-2-1 + uBlock Origin + DNS chiffré + ADP iCloud si Apple.
- *Coût* : 50-200 € de matériel (YubiKey, abonnement gestionnaire éventuel), 2-3 h de configuration initiale, 15-30 min par mois de maintenance.
- *Ce que ce niveau fait* : élimine 90 % du risque statistique.

**Niveau 2 — Profil exposé**

- *Pour qui* : journaliste, militant identifié, dirigeant d’entreprise sensible, personnalité publique modérée, professionnel du droit ou de la santé manipulant des dossiers sensibles, personne ayant un adversaire de proximité connu et motivé.
- *Objectif* : ajouter une compartimentation forte et une résistance aux attaques ciblées de niveau intermédiaire.
- *Stack type* : N1 + GrapheneOS sur Pixel dédié *ou* iPhone avec Lockdown Mode + SimpleX pour canaux les plus sensibles + Tails sur USB pour sessions ponctuelles + Mullvad VPN permanent + Mullvad Browser quotidien + email Proton avec alias + procédures BEC si pro + reboot quotidien des appareils sensibles.
- *Coût* : 500-1500 € (Pixel, USB Tails, abonnements), 1-2 jours de configuration initiale + apprentissage continu, 1-2 h par mois de maintenance disciplinée.

**Niveau 3 — HVT / source / journaliste sensible / cible documentée**

- *Pour qui* : journaliste avec enquête en cours sur acteurs ressourcés, lanceur d’alerte avant divulgation, opposant politique en exil, dissident, avocat de la défense sur dossier sensible, personne ayant reçu une *Threat Notification* d’Apple/Google/Meta.
- *Objectif* : résister aux attaques par spyware mercenaire, à l’analyse forensique avancée, à la coercition juridique transfrontière.
- *Stack type* : N2 + Qubes OS sur laptop principal + Whonix dans Qubes + GrapheneOS avec profils multiples + air-gap pour secrets long terme + MVT mensuel + iVerify + audit forensique périodique + plan d’incident documenté + équipe juridique mobilisable + relation établie avec Access Now / Citizen Lab.
- *Coût* : 2000-5000 € (matériel adapté Qubes, multiples appareils), 2-4 semaines d’apprentissage initial, 4-8 h par mois de maintenance, discipline opérationnelle continue.

**Note critique** : un niveau plus élevé ne se substitue pas à un niveau plus bas. Le Niveau 3 *contient* le Niveau 1. Une posture Niveau 3 mal entretenue sur les fondamentaux N1 (mot de passe réutilisé sur un compte de récupération) est moins solide qu’une posture N1 disciplinée. **Aucun lecteur ne devrait viser directement le N3 sans avoir maîtrisé le N1.**

**Anti-pattern à éviter** : se dimensionner en N3 par fascination technique alors que le threat model réel est N1. La friction qui en résulte épuise et conduit à abandonner *en bloc*, sortant alors en N0 (rien). Mieux vaut un N1 tenu dix ans qu’un N3 abandonné en deux mois.

## 2.7 Matrice STRIDE/LINDDUN adaptée au particulier

Pour un audit plus structuré, deux taxonomies de menaces sont utiles.

**STRIDE** (Microsoft, focalisée sécurité) :

- **S**poofing — usurpation d’identité (compte piraté, SIM swap, faux mail au nom de…)
- **T**ampering — altération de données (modification de fichiers, faux documents)
- **R**epudiation — possibilité de nier une action (qui a fait quoi sur un appareil partagé ?)
- **I**nformation disclosure — fuite d’informations
- **D**enial of service — déni de service (compte bloqué, appareil rendu inutilisable)
- **E**levation of privilege — élévation de privilèges (admin sur ton appareil)

**LINDDUN** (focalisée privacy) :

- **L**inkability — possibilité de relier deux activités
- **I**dentifiability — possibilité d’identifier une personne derrière une activité
- **N**on-repudiation — impossibilité de nier une action (problème côté privacy)
- **D**etectability — possibilité de détecter qu’une activité a eu lieu
- **D**isclosure of information — divulgation d’information
- **U**nawareness — l’utilisateur ignore ce qui se passe avec ses données
- **N**oncompliance — non-conformité aux règles applicables

LINDDUN est particulièrement utile pour penser privacy plutôt que sécurité pure. *Linkability* notamment recoupe la surface de corrélation discutée au Ch 1.

## 2.8 L’erreur « threat model trop complexe »

Privacy Guides a identifié un anti-pattern récurrent : la personne qui construit un threat model d’opposant politique alors qu’elle fait du tricot. Trois symptômes :

- Empilement d’outils dont la combinaison crée de nouvelles surfaces d’attaque (un VPN qui fuit, branché derrière un Tor mal configuré, sur un OS compromis).
- Procédures qui exigent une discipline permanente impossible à tenir (rotation manuelle de comptes hebdomadaire).
- Adversaires fantasmés qui justifient des mesures, en ignorant les adversaires réels.

Le bon test : *« Si l’adversaire que je redoute me ciblait demain, que ferait-il en premier ? »* La réponse, dans 90 % des cas, n’est pas un zero-day Pegasus. C’est un phishing, une réutilisation de mot de passe, une question de récupération de compte mal protégée, une publication imprudente d’un proche. Commence par ça.

## 2.9 Définir ce qui est hors périmètre

Un threat model honnête liste explicitement ce qu’il *ne couvre pas* :

- « Je ne cherche pas à résister à une perquisition judiciaire en France. »
- « Je ne cherche pas à empêcher que ma banque sache combien j’ai sur mon compte. »
- « Je ne cherche pas l’anonymat sur LinkedIn, qui est mon outil professionnel. »
- « Je ne cherche pas à protéger contre un voleur qui aurait mon téléphone allumé et déverrouillé en main. »

Cette explicitation a deux vertus. D’abord, elle décharge la conscience : tu n’as pas à porter le poids de défenses contre tout. Ensuite, elle clarifie où placer les efforts.

## 2.10 *Fil rouge* — Léa construit son premier threat model en 90 minutes

Léa Martens, journaliste freelance à Bruxelles, démarre son enquête en consortium. Elle s’assied avec un carnet et trois colonnes : actifs, adversaires, mesures.

**Actifs critiques** :

- Identité de ses sources (priorité absolue — la révéler les met en danger physique).
- Documents reçus (priorité haute — base de l’enquête).
- Carnet d’adresses (priorité haute — révèle ses relations).
- Communications avec ses sources (contenu *et* métadonnées).
- Son matériel et son domicile (sécurité personnelle).

**Adversaires plausibles** :

- Le commissaire visé (capacité moyenne via cabinet, motivation forte si l’enquête sort).
- La société de surveillance privée (capacité technique élevée — c’est leur métier — motivation modérée à élevée selon avancement).
- L’oligarque (capacité élevée via services achetés, motivation élevée).
- Services russes (capacité très élevée, motivation modérée à élevée si l’enquête touche).
- Trolls et harceleurs en ligne (capacité faible, motivation possible si l’enquête sort).

**Hors périmètre explicite** :

- Résistance à une saisie judiciaire belge ou française légale (Léa s’engage à respecter la loi locale et fera appel à son avocat si besoin).
- Anonymat sur LinkedIn et auprès de sa rédaction.
- Protection contre criminalité opportuniste classique (couverte par hygiène standard, pas spécifique à l’enquête).

**Mesures prioritaires identifiées** (à creuser dans les chapitres suivants) :

- Compartimentation stricte : un appareil enquête séparé du quotidien.
- Canal source ne passant pas par Gmail/WhatsApp.
- Réduction d’empreinte publique sur les réseaux sociaux *pendant* l’enquête.
- Audit de son entourage proche pour ne pas créer de fuite indirecte.
- Préparation à un possible voyage en pays sensible.

Le document tient sur deux pages. Léa le date, le chiffre dans son gestionnaire de mots de passe (qu’elle vient de mettre en place — cf. Ch 29), et se promet de le réviser tous les trimestres.

> 🟦 **Exercice du chapitre**
> Produis ton propre threat model en une page : 3 actifs prioritaires, 3 adversaires plausibles, 3 mesures réalistes, 3 éléments explicitement hors périmètre. Date-le, range-le, prévois sa relecture à 3 mois.

-----
