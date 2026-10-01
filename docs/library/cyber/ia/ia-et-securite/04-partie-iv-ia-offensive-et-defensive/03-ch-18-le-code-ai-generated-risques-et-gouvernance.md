---
title: 'Ch.18 — Le code AI-generated : risques et gouvernance'
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie IV — IA offensive et défensive
  - index.md
---

## 18.1 L’état des lieux

Les assistants de code IA (GitHub Copilot, Cursor, Claude Code, ChatGPT) sont massivement adoptés par les développeurs. Les gains de productivité sont réels et documentés. Mais le code généré par IA contient fréquemment des vulnérabilités classiques car les modèles reproduisent les patterns du code d’entraînement — y compris les mauvaises pratiques.

Les vulnérabilités les plus courantes dans le code AI-generated incluent les injections (SQL, XSS, commande) par absence de sanitization des entrées, les IDOR (Insecure Direct Object References) par absence de vérification d’autorisation, les secrets en dur (API keys, mots de passe, tokens dans le code source), la cryptographie faible (algorithmes obsolètes, gestion incorrecte des clés, IV statiques), et la gestion incorrecte des erreurs (exceptions silencieuses, messages d’erreur exposant des détails internes).

L’étude conjointe ANSSI-BSI d’octobre 2024 sur les assistants de programmation basés sur l’IA détaille ces risques et formule des recommandations spécifiques. Le document souligne le risque de faux sentiment de sécurité : « l’IA l’a généré donc c’est correct » pousse les développeurs à réduire leur vigilance sur le code qu’ils n’ont pas écrit eux-mêmes.

## 18.2 Risques spécifiques

Au-delà des vulnérabilités dans le code généré, plusieurs risques spécifiques méritent attention.

**L’injection indirecte via les assistants de code.** Un attaquant peut insérer des instructions malveillantes dans la documentation d’un package ou dans un fichier du dépôt. L’assistant de code, qui ingère le contexte du projet (fichiers ouverts, documentation, dépendances), peut exécuter ces instructions en suggérant du code malveillant ou en exfiltrant des informations via les suggestions de code.

**La fuite de code propriétaire.** L’envoi de code source propriétaire à un LLM cloud (Copilot, ChatGPT) pour obtenir des suggestions expose le code au fournisseur. Les conditions d’utilisation varient (certains fournisseurs garantissent de ne pas utiliser le code pour l’entraînement, d’autres non). En production, la politique doit définir clairement quels assistants de code sont autorisés et quelles données peuvent leur être envoyées.

**Le slopsquatting.** Quand un LLM hallucine un nom de package dans ses suggestions de code, un attaquant peut créer un package malveillant portant ce nom. Le développeur qui installe les dépendances suggérées par l’IA installe alors le malware. Ce vecteur a été identifié comme une nouvelle classe d’attaque de supply chain en 2025.

## 18.3 Provenance des snippets, licences et contamination de dépôt

Un risque souvent négligé du code AI-generated est la provenance des fragments suggérés. Le LLM a été entraîné sur du code sous des licences variées (MIT, GPL, Apache, propriétaire) et peut régurgiter des fragments substantiels de code sous licence copyleft (GPL) dans un projet propriétaire, créant un risque juridique de contamination de licence. Le développeur qui accepte une suggestion Copilot ne sait pas si le fragment provient d’un projet GPL — et le fournisseur ne donne généralement pas cette information.

La contamination de dépôt est un risque connexe : un assistant de code qui a accès au contexte du projet (fichiers ouverts, historique git) peut suggérer du code basé sur des fichiers sensibles du dépôt (fichiers de configuration, secrets, code propriétaire critique) et exposer ces informations au fournisseur cloud. Inversement, un attaquant qui contrôle un fichier dans le dépôt (via une pull request malveillante, un package compromis, ou une modification de documentation) peut injecter des instructions qui influenceront les suggestions de l’assistant.

La confiance excessive des développeurs dans les suggestions IA est bien documentée par l’étude conjointe ANSSI-BSI d’octobre 2024. Les développeurs utilisant des assistants IA ont tendance à produire du code avec davantage de vulnérabilités s’ils ne vérifient pas systématiquement, précisément parce que le code suggéré semble correct et professionnel. Le faux sentiment de sécurité — « l’IA l’a généré, donc c’est correct » — est le risque humain principal associé à ces outils.

## 18.4 Gouvernance du code AI-generated

Le code AI-generated doit passer par les mêmes contrôles que le code humain — et éventuellement des contrôles supplémentaires. La politique doit couvrir quand l’utilisation d’un assistant de code est autorisée (pas sur des projets classifiés ou à haute sensibilité si l’assistant est cloud), quelles vérifications sont obligatoires (revue de code systématique, SAST, SCA, tests de sécurité), quelles données peuvent être envoyées au LLM de code (jamais de code propriétaire critique dans un LLM cloud non contractualisé), et la traçabilité (identifier dans le commit quand du code a été généré par IA, pour cibler les revues de sécurité).

-----
