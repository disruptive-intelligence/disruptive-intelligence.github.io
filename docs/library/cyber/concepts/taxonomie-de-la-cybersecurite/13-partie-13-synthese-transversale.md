---
title: Partie 13 — Synthèse transversale
source: Cyber/11 Concepts/Cartes & familles/Taxonomie de la cybersécurité.md
note: Taxonomie de la cybersécurité
up:
- - Taxonomie de la cybersécurité
  - index.md
---

## Chapitre 306 — Comment classer une attaque inconnue

**Méthode en 6 questions.** Face à une attaque jamais vue, ne pas chercher à la « connaître » mais à la *ranger* :

1. **Quelle surface ?** (Partie 4) — web, réseau, identité, cloud, humain… *Où* frappe-t-elle ?
2. **Quelle propriété CIA visée ?** (chapitre 5) — confidentialité, intégrité, disponibilité ?
3. **Quelle faiblesse exploitée ?** (Partie 5) — authentification, autorisation, injection, configuration, confiance… ?
4. **Quelle famille d'attaque ?** (Parties 6–10) — la faiblesse + la surface pointent vers une famille connue.
5. **Quelle tactique ATT&CK ?** — accès initial, exécution, élévation, mouvement latéral, exfiltration, impact ?
6. **Quel impact métier ?** (chapitre 10) — pour prioriser.

🔧 **Exemple concret** — « Une fonctionnalité d'import récupère une URL et atteint un service interne. » → surface : application/cloud ; faiblesse : confiance dans une entrée + accès non prévu ; famille : SSRF (chapitre 105). On hérite aussitôt des défenses SSRF.

🎯 **À retenir** — On ne mémorise pas les attaques, on les *classe*. Six questions suffisent à rattacher l'inconnu au connu.


## Chapitre 307 — Comment relier une attaque à une vulnérabilité

**Principe.** Toute attaque *exploite* une vulnérabilité (Partie 5). Remonter de l'attaque à sa faiblesse-racine, c'est comprendre *pourquoi* elle marche — et donc *quoi corriger*.

**Méthode.** Demander : « *Quelle faiblesse rend cette attaque possible ?* »

- XSS, SQLi → injection (interpréteur confond données et code).
- IDOR/BOLA → défaut d'autorisation.
- Bucket public → mauvaise configuration.
- Pass-the-hash → mécanique de réutilisation + permissions excessives.
- BEC → confiance humaine + absence de double validation.

🧭 **Taxonomie** — Une même vulnérabilité (ex. injection) génère plusieurs attaques (XSS, SQLi, command…). Corriger la *faiblesse* neutralise *toute la famille*.

🎯 **À retenir** — Remonter à la vulnérabilité-racine permet de corriger la cause, pas le symptôme — et souvent toute une famille d'attaques d'un coup.


## Chapitre 308 — Comment relier une vulnérabilité à un contrôle

**Principe.** À chaque vulnérabilité correspond un (ou des) contrôle(s) défensif(s) (Partie 12). C'est la logique D3FEND : faiblesse → contre-mesure.

**Méthode.** Demander : « *Quel contrôle supprime ou compense cette faiblesse ?* »

- Injection → requêtes paramétrées + encodage de sortie (+ WAF en profondeur).
- Défaut d'autorisation → contrôle d'accès serveur systématique, deny by default.
- Exposition de secrets → coffre-fort + secrets scanning + rotation.
- Vol d'identifiants → MFA résistant au phishing.
- Lateral movement → segmentation + tiering + LAPS.

🧭 **Taxonomie** — Un contrôle couvre souvent plusieurs vulnérabilités (le moindre privilège limite élévation *et* lateral movement *et* impact d'injection). On priorise les contrôles à *large couverture*.

🎯 **À retenir** — Relier faiblesse → contrôle transforme l'analyse en action. Privilégier les contrôles couvrant le plus de familles.


## Chapitre 309 — Comment relier une attaque à une détection

**Principe.** Toute attaque laisse (ou peut laisser) des *signaux* (Partie 11). Anticiper ces signaux, c'est concevoir la détection.

**Méthode.** Demander : « *Quelles traces cette attaque produit-elle, et dans quelle source ?* »

- Password spraying → pics d'échecs sur de nombreux comptes (journaux d'authentification).
- Exfiltration DNS → requêtes DNS anormales (logs DNS/NDR).
- Lateral movement → connexions inter-machines atypiques (EDR/NDR/SIEM).
- Ransomware → chiffrement massif + suppression de sauvegardes (EDR/SIEM).

🧭 **Taxonomie** — Viser le niveau **TTP** (chapitre 247) : détecter le *comportement* plutôt que l'artefact volatil. Cartographier les détections sur ATT&CK mesure la couverture.

🎯 **À retenir** — À chaque attaque, se demander *quelle trace, dans quelle source* : c'est ainsi qu'on construit des cas d'usage de détection.


## Chapitre 310 — Comment prioriser les risques

**Principe.** On ne traite jamais tout : on priorise (Partie 3). La priorité combine *vraisemblance* et *impact* (chapitre 3), pondérés par l'*exposition* réelle.

**Méthode.**

1. Identifier l'actif et son impact métier (chapitre 10).
2. Évaluer la vraisemblance : exposition (Internet ?), exploitabilité (EPSS/KEV ?), menace réaliste (ciblé vs opportuniste ?).
3. Croiser → niveau de risque.
4. Décider : réduire / transférer / éviter / accepter (chapitre 30).

⚠️ **Erreur fréquente** — Prioriser par le seul score technique (CVSS). Une « critique » non exposée pèse moins qu'une « moyenne » exposée et activement exploitée.

🎯 **À retenir** — Priorité = vraisemblance × impact × exposition. Le risque le plus « grave sur le papier » n'est pas toujours le plus urgent.


## Chapitre 311 — Carte mentale finale de la cybersécurité

**La structure complète, en un schéma mental :**

- **On protège des ACTIFS** (données, services, systèmes, identités, humains) — Partie 1.
- **Sur des SURFACES** (poste, réseau, AD, web, API, cloud, conteneurs, supply chain, humain…) — Partie 4.
- **Qui ont des VULNÉRABILITÉS** (authentification, autorisation, injection, configuration, confiance…) — Partie 5.
- **Exploitées par des ATTAQUES** classées par famille et par surface — Parties 6 à 10.
- **Menées selon des TACTIQUES** (ATT&CK : accès initial → … → impact).
- **Contrées par des PRINCIPES** (défense en profondeur, moindre privilège, Zero Trust, assume breach…) — Partie 2.
- **Mis en œuvre par des CONTRÔLES** (préventifs/détectifs/correctifs) — Partie 12.
- **Surveillés et traités** par la détection et la réponse — Partie 11.
- **Le tout GOUVERNÉ** par la GRC — Partie 3.

**Le fil rouge unique :** `actif → menace → vulnérabilité → risque → attaque → impact → détection → réponse → remédiation`.

🎯 **À retenir** — Toute notion cyber trouve sa place sur cette carte. Si vous savez où ranger une notion, vous savez la relier, la défendre et y répondre.


## Chapitre 312 — Les erreurs de raisonnement fréquentes

Pièges classiques qui faussent l'analyse :

1. **Confondre les niveaux** : vulnérabilité ≠ risque ; authentification ≠ autorisation ; alerte ≠ incident.
2. **Sécurité par l'obscurité** : croire que « caché » = « protégé » (UUID, endpoint non documenté).
3. **Tout-préventif** : négliger détection et réponse (oublier *assume breach*).
4. **Faire confiance au client / à la localisation réseau** : violer les frontières de confiance (chapitre 80).
5. **Prioriser par le score technique seul** : ignorer exposition et impact métier.
6. **Confondre le symptôme et la cause** : corriger une attaque sans traiter la vulnérabilité-racine.
7. **Croire un outil suffisant** : « j'ai un WAF/un SIEM/un MFA » sans configuration, sources ni réglage.
8. **Punir l'erreur humaine** : tuer la culture du signalement.
9. **Oublier la supply chain et l'identité** : se concentrer sur le périmètre.
10. **Sauvegardes non testées / non immuables** : faux sentiment de résilience.

🎯 **À retenir** — La plupart des échecs viennent moins d'une attaque sophistiquée que d'une *erreur de raisonnement* : confusion de niveaux, confiance implicite, ou dépendance à un seul contrôle.


## Chapitre 313 — Glossaire final (voir Annexe A)

Le glossaire complet est fourni en **Annexe A**. Il rassemble les termes clés du cours, à utiliser comme référence rapide. Conserver à l'esprit que *définir précisément* est déjà une compétence de sécurité : la plupart des confusions opérationnelles viennent d'un vocabulaire flou.

🎯 **À retenir** — Un vocabulaire précis est un outil de sécurité : il évite les malentendus coûteux en analyse, en réponse et en gouvernance.

---

---
