---
title: Chapitre 29 — Validation d'éradication et surveillance post-nettoyage
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie VI — Éradication, reconstruction et reprise
  - index.md
---

## 29.1 Comment savoir qu'on a vraiment éradiqué

L'éradication n'est pas un acte ponctuel (« on a supprimé le malware, c'est fini ») mais un processus qui se valide dans la durée. La question « l'attaquant est-il vraiment parti ? » ne peut jamais recevoir une réponse avec certitude absolue — mais la confiance se construit par accumulation de vérifications positives et absence de réapparition.

## 29.2 Checklist de validation technique

Après l'éradication, une checklist de contrôle est exécutée sur l'ensemble du parc. Aucun processus malveillant actif (scan EDR complet — tous les endpoints, pas un échantillon). Aucune tâche planifiée non légitime (script de vérification exécuté via Velociraptor sur tout le parc). Aucun service Windows non répertorié. Aucun compte non autorisé dans les groupes privilégiés (audit AD complet). Aucune GPO non légitime (revue de toutes les GPO). Aucune règle de forwarding email non légitime (audit de toutes les boîtes mail M365). Aucun flux réseau vers les destinations C2 identifiées (monitoring continu proxy + pare-feu). Intégrité vérifiée des fichiers système critiques.

## 29.3 Hunts post-nettoyage

Pendant 2 à 4 semaines après l'éradication, un threat hunting ciblé est mené en continu. Les hypothèses de hunting sont dérivées directement de l'attaque observée. « L'attaquant utilisait des scheduled tasks pour la persistence → chercher toute nouvelle scheduled task créée depuis le jour J. » « L'attaquant utilisait rclone pour l'exfiltration → chercher tout processus rclone ou tout flux vers S3/Blob/Cloud storage. » « L'attaquant avait un Golden Ticket → monitorer les anomalies Kerberos (TGT avec lifetime anormal, authentifications sans pré-authentification). »

Si le hunting révèle des traces, l'éradication est incomplète et le cycle recommence (investigation complémentaire → éradication complémentaire → validation).

## 29.4 Seuil de confiance

Après 3 à 4 semaines de surveillance renforcée sans détection de réapparition, l'éradication est déclarée réussie avec un niveau de confiance « élevé — risque résiduel faible ». Ce seuil est documenté : il ne signifie pas « certitude absolue » mais « confiance suffisante pour un retour à la normale, avec un monitoring standard ». Le risque résiduel (un mécanisme de persistance non détecté, une porte d'entrée secondaire non identifiée) est accepté explicitement et géré par la surveillance continue.

## 29.5 Fil rouge — BLACKTIDE : la validation

> **🔍 BLACKTIDE — Épisode 29**
>
> 3 semaines de surveillance renforcée post-éradication. Hunting quotidien sur les IoC PhantomCrypt (hash, domaines C2, patterns de beaconing). Monitoring continu des flux réseau vers les IP/domaines identifiés. Audit AD hebdomadaire via PingCastle (score passé de D à B après le durcissement). Scan EDR approfondi de tout le parc (100 % — y compris les 8 % auparavant non couverts, sur lesquels l'EDR a été déployé en urgence pendant l'incident).
>
> Résultat : aucun indicateur de réapparition après 3 semaines. Marc (RSSI) déclare l'éradication réussie avec un niveau de confiance « élevé ».

---
