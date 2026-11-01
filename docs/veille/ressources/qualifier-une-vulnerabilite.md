---
title: Qualifier et prioriser une vulnérabilité
description: De l'alerte à la décision — applicabilité, exploitation, exposition, impact, puis une décision tracée et vérifiée.
hide:
  - footer
---

<span class="kw-muted">[🚨 Veille vulnérabilités](vulnerabilites.md) · méthode</span>

# 📐 Qualifier et prioriser une vulnérabilité

!!! abstract "En bref"
    Quatre questions, dans cet ordre, avant de décider :

    1. **Suis-je concerné ?** Produit, version, configuration.
    2. **Est-elle exploitée ?** Catalogue KEV, alerte CERT, code public, EPSS.
    3. **Qui peut l'atteindre ?** Internet, réseau interne, accès local.
    4. **Que perd-on ?** Vecteur CVSS et valeur de l'actif touché.

    Puis une décision (corriger, contourner, accepter le risque, non concerné) avec une échéance, tracée et vérifiée.

## 1. Applicabilité : suis-je concerné ?

- **Le produit est-il présent ?** Inventaire du parc, outil de gestion des configurations, résultats du scanner de vulnérabilités.
- **La version est-elle dans la plage vulnérable ?** Les versions corrigées indiquées dans l'avis de l'éditeur font référence : elles sont plus précises que la fiche CVE.
- **La fonction vulnérable est-elle active ?** Beaucoup d'avis ne concernent qu'un module, un service ou une option (portail VPN, interface d'administration exposée…).
- **Le composant est-il embarqué ailleurs ?** Une bibliothèque (OpenSSL, Log4j…) peut se trouver dans une appliance ou un logiciel tiers : avis de l'éditeur du produit, inventaire des composants (SBOM).
- **Conclusion écrite :** concerné, non concerné (avec la preuve) ou à confirmer (avec la question posée, et à qui).

## 2. Exploitation : est-elle utilisée ?

- **Exploitation constatée** : catalogue KEV de la CISA, alerte CERT-FR, mention « exploited » dans l'avis de l'éditeur, liste des vulnérabilités exploitées de l'EUVD. C'est le critère qui pèse le plus.
- **Code d'exploitation public** (Exploit-DB, dépôts GitHub, publications de chercheurs) : une exploitation de masse peut suivre en quelques jours.
- **EPSS** : probabilité d'une activité d'exploitation dans les 30 jours, recalculée chaque jour.[^epss] Plus utile pour départager deux vulnérabilités que comme seuil absolu ; le percentile situe la CVE par rapport à toutes les autres.
- **Usage par des rançongiciels** : signalé dans le catalogue KEV (« Known »).[^kev]

## 3. Exposition : qui peut l'atteindre ?

- **Exposée sur Internet** : passerelle VPN, pare-feu, messagerie, portail web, service d'accès distant. Les équipements de bordure reviennent sans cesse dans le catalogue KEV (Ivanti, Fortinet, Citrix, Cisco, Palo Alto…).
- **Accessible depuis le réseau interne** : un attaquant déjà entré, ou un poste compromis, peut s'en servir pour se déplacer.
- **Accès local ou authentifié requis** : moins urgent, sauf sur des systèmes partagés ou en chaîne avec une autre faille (élévation de privilèges).
- **Mesures déjà en place** : filtrage, segmentation, authentification forte devant le service, règle IPS ou WAF. Elles réduisent l'exposition sans remplacer le correctif.

## 4. Impact : que perd-on ?

- **Lire le vecteur CVSS, pas seulement le score.** Le score de base mesure la gravité technique de la faille, pas le risque pour une organisation donnée.[^cvss]

| Métrique | Question | Pire cas |
|---|---|---|
| AV — vecteur d'attaque | D'où part l'attaque ? | `N` : par le réseau |
| AC (et AT en v4) — complexité, prérequis | Faut-il des conditions particulières ? | `L` / `N` : aucune |
| PR — privilèges requis | Faut-il un compte ? | `N` : aucun |
| UI — interaction utilisateur | Faut-il qu'un utilisateur agisse ? | `N` : non |
| C, I, A (VC, VI, VA en v4) | Confidentialité, intégrité, disponibilité | `H` : perte totale |

- **Valeur de l'actif** : contrôleur de domaine, hyperviseur, sauvegardes, messagerie ou équipement de bordure pèsent plus qu'un poste isolé, car leur compromission ouvre le reste du système.
- **Score ajusté** : les métriques environnementales du CVSS recalculent la gravité dans son contexte ([calculateur du FIRST](https://www.first.org/cvss/calculator/4.0)).

## 5. Décider et fixer l'échéance

Exemple de grille, à aligner sur la politique de sécurité de l'organisation :

| Situation | Priorité | Échéance indicative |
|---|---|---|
| Exploitée **et** exposée sur Internet | P0 | Contournement immédiat, correctif sous 72 h |
| Exploitée, ou critique et exposée | P1 | Sous 7 jours |
| Critique ou élevée, non exploitée, interne | P2 | Sous 30 jours |
| Autres | P3 | Cycle normal de mise à jour |

- **Repère public** : la directive BOD 22-01 de la CISA, qui a créé le catalogue KEV, laissait en général deux semaines aux agences fédérales américaines pour corriger une vulnérabilité exploitée.[^bod]
- **Autre approche** : l'arbre de décision SSVC de la CISA aboutit à quatre réponses (Track, Track\*, Attend, Act) à partir de l'état d'exploitation, de l'impact technique, de la possibilité d'automatiser l'attaque et de l'importance de l'actif.[^ssvc]

Quatre décisions possibles :

- **Corriger** : appliquer le correctif ou passer à la version corrigée.
- **Contourner** : mesure temporaire en attendant le correctif (désactiver la fonction, filtrer l'accès, isoler). À suivre, et à retirer une fois le correctif posé.
- **Accepter le risque** : par écrit, avec la justification, les mesures compensatoires, la personne qui décide et une date de réexamen.
- **Non concerné** : avec la preuve (produit absent, version non vulnérable, fonction inactive).

## 6. Tracer et vérifier

- **Une fiche par vulnérabilité retenue** : le bouton « 📋 Fiche » de la [veille vulnérabilités](vulnerabilites.md) prépare ce qui est connu et les cases à remplir.
- **Vérifier après correction** : nouveau passage du scanner ou contrôle de la version installée. Un correctif posé sur un service qui n'a pas redémarré peut laisser l'ancienne version active.
- **Clore** : date, preuve, contournement retiré.
- **Réexaminer** les acceptations de risque à la date prévue.
- **Suivre quelques indicateurs** : délai moyen de correction, vulnérabilités ouvertes au-delà de leur échéance, part des systèmes encore supportés.[^nist]

## Pièges fréquents

- **Trier au seul score CVSS** : un 9,8 sur un service interne non exploité passe souvent après un 7,5 exposé et exploité.
- **« Pas de CVE, pas de problème »** : certains avis d'éditeurs ou de CERT n'en citent pas, ou pas encore.
- **Oublier les appliances et les composants embarqués** : ils échappent aux outils de mise à jour habituels.
- **Laisser vivre un contournement** : sans suivi, la mesure temporaire devient permanente et le correctif n'arrive jamais.
- **Oublier la fin de support** : une version qui n'est plus supportée ne recevra pas de correctif (bloc [Fin de support](vulnerabilites.md#fin-de-support)).

Pour aller plus loin : les référentiels (guide d'hygiène de l'ANSSI, NIST SP 800-40, CIS Controls, ISO 27002) sont rangés dans [Ressources · Référentiels & gouvernance](cyber/referentiels-gouvernance.md).

## Sources

[^epss]: FIRST, [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/).
[^kev]: CISA, [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).
[^cvss]: FIRST, [CVSS v4.0 Specification Document](https://www.first.org/cvss/v4.0/specification-document).
[^bod]: CISA, [BOD 22-01 — Reducing the Significant Risk of Known Exploited Vulnerabilities](https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities).
[^ssvc]: CISA, [Stakeholder-Specific Vulnerability Categorization (SSVC)](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc).
[^nist]: NIST, [SP 800-40 Rev. 4 — Guide to Enterprise Patch Management Planning](https://csrc.nist.gov/pubs/sp/800/40/r4/final).
