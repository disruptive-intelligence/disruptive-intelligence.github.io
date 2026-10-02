---
title: MFA
source: Cyber/12 Fiches notions/MFA.md
format: fiche
revue: '2026-10-02'
terms:
  MFA: Authentification multi-facteur — exiger au moins deux familles de facteurs (ce que je sais, ce que je possède, ce que je suis).
---

> Fiche notion assemblée à partir de mes notes (sources en fin de fiche).

## En bref

**Facteurs d'authentification** (à connaître) : ce que je *sais* (mot de passe), ce que je *possède* (téléphone, clé), ce que je *suis* (biométrie). Combiner au moins deux familles = MFA.[^1]

**Définition.** Authentification multi-facteur (rappel du chapitre 6).
**Contre quoi.** Vol/devinette d'identifiants (phishing, spraying, stuffing, brute force).
**Principe.** Exiger ≥2 familles de facteurs ; privilégier le **MFA résistant au phishing** (FIDO2/passkeys, number matching) contre le phishing et la MFA fatigue.[^2]

## MFA résistant au phishing

**MFA résistant au phishing.** Le déploiement de FIDO2/WebAuthn (clés de sécurité physiques ou passkeys) élimine les risques de phishing en temps réel (Evilginx) parce que l'authentification est liée au domaine — la clé ne s'active que sur le domaine légitime. C'est la mesure technique la plus efficace contre le credential harvesting par phishing. En 2025, le déploiement de FIDO2 est en forte accélération mais reste minoritaire dans les entreprises.[^3]

## Au quotidien

Les **codes de récupération** : à chaque activation de MFA, le service fournit des codes de secours. Ces codes doivent être imprimés ou stockés dans un lieu sûr — PAS dans le téléphone (c'est le téléphone qu'on perd). Sans ces codes, la perte du téléphone = la perte de l'accès aux comptes. La **fatigue MFA** : les attaquants envoient des dizaines de notifications push MFA jusqu'à ce que la victime accepte par épuisement → ne JAMAIS accepter une notification MFA qu'on n'a pas déclenchée soi-même.[^4]

## Limites

⚠️ **Erreur fréquente** — MFA par simple push (vulnérable à la fatigue) ; pas de protection contre le vol de jeton de session.[^2]

10. 🎯 **À retenir.** L'infostealer vole vite et peut contourner le MFA via les jetons de session : protéger/expirer les sessions et détecter les réutilisations anormales est crucial.[^5]

## À retenir

🎯 **À retenir** — Le MFA est la parade reine au vol d'identifiants ; la version résistante au phishing est désormais la cible.[^2]

## Voir aussi

[Zero Trust](zero-trust.md) · [Défense en profondeur](defense-en-profondeur.md) · [SPF, DKIM, DMARC](spf-dkim-dmarc.md)

## Sources

[^1]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 6.
[^2]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), chapitre 282.
[^3]: [HUMINT & social engineering](../osint/humint-social-engineering/index.md).
[^4]: [Cybersécurité du quotidien](../concepts/cybersecurite-du-quotidien/index.md).
[^5]: [Taxonomie cyber](../concepts/taxonomie-de-la-cybersecurite/index.md), infostealer.
