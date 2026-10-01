---
title: Chapitre 11 — Corrélation, raisonnement analytique et gestion des biais
source: Cyber/04 Forensic/Investigation numérique (forensic).md
note: Investigation numérique (forensic)
up:
- - Investigation numérique (forensic)
  - ../index.md
- - Partie III — Analyse fondamentale et raisonnement forensic
  - index.md
---

## 11.1 Le forensic n'est pas juste extraire des artefacts

La compétence technique — savoir parser une MFT, analyser un dump mémoire, interpréter un Event Log — est nécessaire mais pas suffisante. Ce qui distingue un analyste compétent d'un opérateur d'outils, c'est la capacité à raisonner sur les données : formuler des hypothèses, les tester, gérer l'incertitude, et distinguer ce que les données montrent de ce que l'analyste infère.

## 11.2 Raisonnement par hypothèse

L'investigateur forensic ne cherche pas « la vérité » — il formule des hypothèses et les teste contre les données disponibles. Pour chaque question investigative, au moins deux hypothèses doivent être formulées.

Exemple dans MUSIC BOX : le compte `svc-backup` a été utilisé pour supprimer des fichiers de recherche. Hypothèse 1 : le compte a été compromis par un attaquant externe et utilisé pour l'exfiltration et la destruction de données. Hypothèse 2 : le titulaire légitime du compte (un administrateur système) a supprimé les fichiers pour une raison légitime ou malveillante (insider threat). L'investigation doit collecter des données qui permettent de discriminer entre ces hypothèses : l'IP source des connexions (interne vs externe), la présence d'un malware sur la machine, les logs de keylogging ou de credential dumping, et le profil comportemental de l'administrateur.

## 11.3 Le biais de confirmation

Le biais de confirmation est le piège le plus dangereux de l'investigation forensic. Il consiste à chercher sélectivement les données qui confirment l'hypothèse initiale et à ignorer ou minimiser celles qui la contredisent. Ce biais est inconscient et universel — même les analystes expérimentés y sont vulnérables.

Exemple : l'analyste suspecte un insider (un employé sur le départ). Il trouve des fichiers copiés sur une clé USB. Il interprète immédiatement : « voilà la preuve du vol de données ». Mais il ne cherche pas si le malware présent sur la machine a pu copier les fichiers automatiquement vers la clé USB. Il ne vérifie pas si l'employé copiait régulièrement des fichiers sur USB dans le cadre de son travail normal. Le biais de confirmation l'a conduit à s'enfermer dans sa première hypothèse sans tester les alternatives.

Contremesure : pour chaque conclusion, l'analyste se pose la question « qu'est-ce qui pourrait contredire cette interprétation ? » et recherche activement ces données contradictoires. La discipline de l'hypothèse alternative (formuler au moins 2 hypothèses et les tester toutes) est le garde-fou principal.

## 11.4 Niveaux de confiance dans les conclusions

Chaque conclusion forensic doit être accompagnée d'un niveau de confiance explicite.

**Fait vérifié :** observable directement dans les données, reproductible. « Le fichier `rclone.exe` a été exécuté sur WKS-RD-047 le 2 mars 2026 à 14h32 UTC » (constaté dans le Prefetch ET l'Amcache ET les Event Logs — triple confirmation).

**Déduction logique :** conclusion tirée par raisonnement à partir de faits vérifiés. « L'exfiltration a été réalisée via rclone, car le SRUM montre que `rclone.exe` a transféré 180 Go de données réseau entre le 2 et le 7 mars, et les logs proxy confirment des flux HTTPS vers des endpoints S3 AWS depuis cette machine pendant la même période. » (déduction forte, basée sur la convergence de 3 sources indépendantes).

**Hypothèse plausible :** interprétation cohérente mais non confirmée de manière certaine. « L'attaquant est probablement d'origine russophone, car les metadata du document Word piégé contiennent un auteur avec un nom cyrillique et le RAT utilise un C2 dans un ASN associé à un hébergeur d'Asie du Sud-Est couramment utilisé par des groupes russophones » (indices convergents mais non conclusifs — l'attaquant pourrait avoir falsifié ces éléments).

**Inconnue :** ce que l'investigation n'a pas pu déterminer. « L'identité réelle de l'attaquant n'a pas pu être établie dans le cadre de cette investigation. » Documenter les inconnues est aussi important que documenter les conclusions.

## 11.5 Corrélation vs causalité

Deux événements proches dans le temps ne sont pas nécessairement liés. Un reboot de serveur à 03h00 et une connexion C2 à 03h02 ne sont pas forcément le même incident — le reboot peut être une maintenance planifiée, et la connexion C2 un beaconing régulier qui a coïncidé temporellement. La corrélation temporelle est un indice, pas une preuve de causalité. L'analyste doit chercher des liens causaux (le reboot a été déclenché par un script déposé par l'attaquant — vérifiable dans les Event Logs et le registre) et ne pas se contenter de la proximité temporelle.

## 11.6 Fil rouge — MUSIC BOX : les hypothèses concurrentes

> **🔬 MUSIC BOX — Épisode 10**
>
> Lundi. Claire formule ses hypothèses concurrentes pour la question investigative #1 (vecteur d'accès initial).
>
> **H1 :** Spearphishing avec document piégé envoyé au Dr. Mallet. Indices : le RAT est actif sur son poste, les emails suspects sont à vérifier.
> **H2 :** Compromission d'un accès VPN/RDP exposé sur Internet. Indices : vérifier les logs VPN pour des connexions anormales.
> **H3 :** Insider — le Dr. Mallet ou un collègue a intentionnellement installé le RAT. Indices : vérifier le comportement de l'utilisateur, les accès physiques, et les motivations.
>
> L'investigation des emails (export PST de la boîte du Dr. Mallet) révèle un email de spearphishing reçu le 6 janvier 2026 (J-60), prétendant provenir d'un partenaire de recherche (`novapharma-partners.com` — domaine imitant le domaine légitime `novapharma-partner.com`). Le document Word joint contient une macro VBA obfusquée (confirmé par olevba). **H1 est confirmée. H2 et H3 ne sont pas soutenues par les données** (pas de connexion VPN anormale, pas d'accès physique suspect). Mais H3 n'est pas formellement exclue — elle est documentée comme « non soutenue en l'état ».

---
