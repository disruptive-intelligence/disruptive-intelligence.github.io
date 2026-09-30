---
title: Chapitre 18 — La chaîne de valeur cybercriminelle
source: Cyber/01_CTI/Cartographie_Ecosystemes_Cybercriminels.md
note: Cartographie des écosystèmes cybercriminels
up:
- - Cartographie des écosystèmes cybercriminels
  - ../index.md
- - Partie IV — Comprendre L'économie cybercriminelle
  - index.md
---

## 18.1 De la conception à la conversion

La chaîne de valeur complète d'une opération ransomware typique comprend les étapes suivantes, chacune créant et captant de la valeur : développement de l'outil (ransomware, builder, panel), mise à disposition de la plateforme (recrutement d'affiliés, fourniture du builder), acquisition d'accès initial (campagne de phishing/infostealer, exploitation de vulnérabilité, ou achat auprès d'un IAB), compromission du réseau (élévation de privilèges, mouvement latéral, identification des actifs critiques), exfiltration de données (pour la double extorsion), déploiement du ransomware (chiffrement des systèmes), demande de rançon et négociation, paiement en cryptomonnaie, blanchiment (mixing, conversion, peeling chains), cash-out (exchange, OTC, mules), et réinvestissement (dans l'infrastructure, les outils, et les opérations suivantes).

## 18.2 Points de concentration et points de fragilité

La chaîne de valeur révèle les points où beaucoup de valeur transite par peu d'acteurs. En 2025-2026, les principaux points de concentration sont les plateformes RaaS elles-mêmes (quelques dizaines d'opérateurs servent des centaines d'affiliés), les hébergeurs bulletproof dominants (une poignée de fournisseurs héberge une proportion significative de l'infrastructure malveillante mondiale), les services de mixing majeurs (quelques services traitent la majorité des flux de blanchiment crypto criminels), et les exchanges à KYC laxiste (quelques plateformes sont disproportionnellement utilisées pour le cash-out).

Ces points de concentration sont aussi les points de fragilité : si un hébergeur bulletproof majeur est déconnecté, des dizaines d'opérations sont simultanément impactées. Si un mixer est saisi (comme Chipmixer en 2023 ou Sinbad fin 2023), les acteurs doivent trouver des alternatives, ce qui prend du temps et expose les flux à davantage de traçabilité pendant la transition.

## 18.3 Fil rouge — NEXUS : la chaîne de valeur reconstituée

> **🔍 NEXUS — Épisode 17**
>
> Samira reconstitue la chaîne de valeur complète de l'attaque contre Énergis.
>
> 1. **Développement :** PhantomCrypt (opérateur RaaS) → builder v3.2
> 2. **Acquisition d'accès :** ghost_access déploie Lumma via phishing → vol de credentials → vente d'accès domain admin à kr0n0s_ops pour 12 000 $
> 3. **Compromission :** kr0n0s_ops utilise l'accès pour se déplacer latéralement vers le réseau OT
> 4. **Exfiltration :** données techniques et documents internes exfiltrés avant détection
> 5. **Déploiement :** tentative de chiffrement bloquée par l'EDR
> 6. **Extorsion :** publication sur le leak site malgré l'échec du chiffrement (les données exfiltrées suffisent pour la pression)
> 7. **Amplification :** blog de façade + canaux Telegram
>
> Le point de concentration identifié : l'hébergeur moldave héberge non seulement le C2 de cette attaque mais aussi le panel PhantomCrypt, le blog de façade, et selon les rapports CTI, 15+ autres domaines liés à des opérations RaaS distinctes. C'est un facilitateur critique dont la disruption impacterait l'ensemble de l'écosystème.

---
