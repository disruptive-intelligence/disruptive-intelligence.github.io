---
title: Chapitre 18 — L'ingénierie sociale dans la fraude et la criminalité organisée
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - 'Partie IV — L''attaquant : perspectives offensives'
  - index.md
---

## 18.1 La fraude au président : modèle opérationnel

La fraude au président est une industrie criminelle structurée. Les groupes opèrent à partir de « call centers » organisés (principalement en Afrique de l'Ouest, Europe de l'Est, Asie du Sud-Est) avec une répartition des rôles : les « researchers » collectent l'OSINT sur les cibles, les « callers » exécutent les appels de vishing, les « email operators » gèrent les communications email, et les « money mules » blanchissent les fonds via des chaînes de comptes bancaires.

Le modèle opérationnel suit une séquence : reconnaissance OSINT (identification de la cible et du circuit de validation financière) → approche initiale (email et/ou appel) → manipulation (urgence, confidentialité, autorité) → exfiltration des fonds (virement vers un compte contrôlé) → blanchiment (transfert rapide vers d'autres comptes, conversion en crypto-monnaie). La chaîne complète peut se dérouler en quelques heures — la vitesse est critique pour devancer les mécanismes de rappel de virement.

## 18.2 Les romance scams et le pig butchering

Les romance scams (arnaques sentimentales) ont évolué vers un modèle industriel appelé « pig butchering » (sha zhu pan) : la victime est « engraissée » (cultivée pendant des semaines ou des mois) avant d'être « abattue » (escroquée de sommes importantes, souvent en investissements crypto frauduleux).

Le modèle repose sur des « compound » en Asie du Sud-Est (Cambodge, Myanmar, Laos) où des victimes de traite humaine sont forcées d'opérer comme scammers. Les conversations sont gérées via des scripts et, de plus en plus, assistées par des chatbots IA qui maintiennent des conversations cohérentes sur la durée. Les pertes individuelles sont typiquement de 5 000 à 500 000 € et les pertes globales se chiffrent en milliards.

## 18.3 Le SIM swapping

Le SIM swapping est une technique de social engineering ciblant les opérateurs télécom. L'attaquant contacte l'opérateur mobile de la victime (par téléphone ou en boutique) et, en utilisant des informations personnelles collectées par OSINT (nom, adresse, date de naissance, dernier montant facturé), convainc l'opérateur de transférer le numéro de téléphone vers une nouvelle carte SIM contrôlée par l'attaquant.

L'objectif est de prendre le contrôle du numéro de téléphone pour intercepter les codes MFA envoyés par SMS. Une fois le numéro transféré, l'attaquant peut reset les mots de passe de tous les comptes liés au numéro (email, banque, réseaux sociaux, crypto). Les pertes financières peuvent être considérables, en particulier dans le monde des crypto-monnaies.

**Défense** : ne pas utiliser le SMS comme second facteur pour les comptes critiques (préférer une app d'authentification ou une clé FIDO2), activer les protections anti-SIM swap de l'opérateur (code PIN, alerte sur les changements de SIM), utiliser un numéro de téléphone dédié et non public pour le MFA.

## 18.4 L'évolution avec l'IA

L'IA transforme l'industrie du social engineering criminel de trois manières convergentes.

**La personnalisation à l'échelle.** Les LLM permettent de générer des emails de phishing personnalisés pour chaque cible à partir de données OSINT, dans n'importe quelle langue, avec une qualité linguistique native. Ce qui nécessitait auparavant un opérateur humain qualifié est maintenant automatisable.

**Le deepfake vocal et vidéo.** Le clonage vocal en temps réel permet des vishings d'un réalisme sans précédent. La vidéo deepfake en temps réel permet des visioconférences frauduleuses (cas de Hong Kong). Le coût de ces technologies diminue rapidement et leur accessibilité augmente.

**Les chatbots de social engineering.** Des agents conversationnels autonomes capables de maintenir des conversations d'élicitation ou de romance scam sur des jours ou des semaines, avec une cohérence et une adaptabilité que les scripts manuels ne permettaient pas. C'est le passage à l'échelle de l'ingénierie sociale relationnelle.

---
