---
title: Chapitre 3 — Méthodologie forensic et posture d'enquêteur
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Partie I — Fondations
  - index.md
---

## 3.1 Le modèle en 5 phases

Toute investigation forensic suit un processus structuré en cinq phases séquentielles. Ce n'est pas un formalisme bureaucratique — c'est un cadre qui évite les erreurs fatales et qui structure la documentation.

**Phase 1 — Identification :** définir le périmètre de l'investigation, les systèmes concernés, les données volatiles (à acquérir en priorité), et les questions investigatives auxquelles l'investigation doit répondre. Output : liste des cibles, ordre d'acquisition, questions investigatives formulées. Piège principal : périmètre trop large (on se noie dans les données) ou trop étroit (on rate l'essentiel).

**Phase 2 — Préservation :** protéger les preuves contre toute altération. Ne pas éteindre une machine allumée (on perdrait la RAM). Ne pas allumer une machine éteinte (le boot modifie le disque). Isoler la machine du réseau (pour éviter que l'attaquant efface ses traces ou que des processus légitimes écrasent des preuves). Documenter l'état initial (photos de l'écran, des connexions, des équipements). Piège principal : modifier involontairement la preuve par une action bien intentionnée mais mal exécutée.

**Phase 3 — Acquisition :** copier les données de manière forensiquement valide. Image bit-à-bit du disque avec write blocker, dump de la mémoire vive, export des logs, capture réseau. Hash d'intégrité (MD5 + SHA-256) calculé sur le support source et sur l'image acquise — si les hash correspondent, l'intégrité est prouvée. Piège principal : oublier le write blocker, rater le dump RAM, ne pas hasher immédiatement. Détaillé en Partie II.

**Phase 4 — Analyse :** extraire les artefacts pertinents, construire une timeline chronologique, formuler des hypothèses, et les tester contre les évidences. C'est le cœur intellectuel du forensic. Piège principal : biais de confirmation, tunnel vision. Détaillé en Parties III et IV.

**Phase 5 — Présentation :** produire le rapport forensic et, le cas échéant, témoigner devant un tribunal ou une direction générale. Le rapport doit être compréhensible par un non-technicien tout en étant techniquement inattaquable. La distinction fait/déduction/hypothèse doit être explicite à chaque étape. Piège principal : rapport trop technique ou conclusions dépassant les constatations. Détaillé au Ch.26.

## 3.2 Scoping strategy : définir le périmètre d'enquête

Le scoping est l'une des compétences les plus sous-estimées en forensic. La difficulté n'est pas seulement d'analyser, c'est de délimiter : quelles machines investiguer, quelle période couvrir, quels utilisateurs examiner, quels logs collecter, quel niveau de profondeur, et quand s'arrêter.

Les **questions investigatives** structurent le périmètre. Avant de toucher un clavier, l'investigateur formule les questions auxquelles l'investigation doit répondre : comment l'attaquant a-t-il pénétré (vecteur d'accès initial) ? Quand l'intrusion a-t-elle commencé ? Quels systèmes ont été compromis (mouvement latéral) ? Quelles données ont été impactées (exfiltration, modification, destruction) ? L'attaquant est-il encore présent ? Qui est l'attaquant (attribution, si possible) ? Ces questions orientent chaque action d'investigation.

**Délimiter le périmètre** implique des choix concrets. Quelles machines : on commence par les machines directement concernées par l'alerte, puis on élargit en fonction des découvertes (mouvement latéral, même IoC trouvé sur d'autres machines). Quelle période : la fenêtre temporelle initiale est définie par l'alerte, mais l'investigation révèle souvent que l'intrusion remonte beaucoup plus loin (dans MUSIC BOX, l'alerte est à J, mais l'intrusion initiale est à J-60). Quels logs : dépend de la rétention réelle (pas la rétention théorique configurée, mais ce qui est effectivement disponible et exploitable).

Le **piège du scope creep** : chaque découverte ouvre de nouvelles pistes. Un bon investigateur distingue les pistes prioritaires (qui répondent aux questions investigatives) des pistes secondaires (intéressantes mais non essentielles). Il documente les pistes non suivies pour éventuelle investigation ultérieure (avec la mention « piste identifiée, non suivie dans le cadre du scoping actuel — recommandation : investiguer ultérieurement si nécessaire »).

**Quand s'arrêter :** l'investigation est terminée quand toutes les questions investigatives ont reçu une réponse (même si la réponse est « indéterminable avec les données disponibles »), que la couverture temporelle est suffisante, et que la timeline est cohérente. La tentation du perfectionnisme (« et si on regardait aussi ce serveur ? ») doit être résistée si elle ne répond à aucune question investigative ouverte.

**Triage vs investigation complète — arbre de décision :** le choix entre triage rapide (KAPE, Velociraptor — artefacts ciblés, résultats en heures) et investigation complète (image disque + dump RAM + capture réseau + timeline exhaustive — résultats en jours à semaines) dépend de la gravité confirmée, de la perspective judiciaire, de la sensibilité des données, et des moyens disponibles. La bascule du triage vers l'investigation complète se fait quand la gravité est confirmée (vol de données, compromission étendue, insider), quand des données réglementées sont concernées (RGPD, santé, défense), ou quand la direction souhaite judiciariser.

## 3.3 Posture intellectuelle de l'enquêteur

Le forensic exige une posture intellectuelle rigoureuse qui va au-delà de la maîtrise technique des outils.

Le **doute méthodique** : l'analyste ne prend rien pour acquis. Un timestamp peut être falsifié (timestomping). Un log peut être incomplet (rotation, effacement). Un artefact peut être un planted evidence (fausse preuve déposée par l'attaquant pour incriminer un tiers ou brouiller les pistes). Chaque constatation est vérifiée contre au moins une source indépendante quand c'est possible.

Les **hypothèses alternatives** : l'analyste formule plusieurs hypothèses et les teste toutes, pas seulement celle qui semble la plus probable. Si l'hypothèse initiale est « le salarié Julien Mallet a exfiltré les données », l'analyste doit aussi tester « le compte de Julien Mallet a été compromis par un attaquant externe ». Le biais de confirmation — la tendance à chercher les données qui confirment l'hypothèse préférée et à ignorer celles qui la contredisent — est le piège le plus dangereux du forensic (développé au Ch.11).

La **distinction fait / déduction / hypothèse** : l'analyste distingue rigoureusement ce qu'il constate (« le fichier X a été supprimé le 3 mars à 14h32 » — fait, observable dans la MFT), ce qu'il en déduit (« la suppression a été effectuée par le compte svc-backup, car c'est le seul compte actif sur la machine à cette heure selon les Event Logs » — déduction logique), et ce qu'il suppose (« cette suppression est intentionnelle et liée à la compromission » — hypothèse, qui nécessite des évidences supplémentaires pour être confirmée). Le rapport forensic doit rendre cette distinction explicite à chaque étape.

## 3.4 Documentation continue

La documentation est un livrable continu, pas un exercice de fin d'investigation. Le **journal d'investigation** (case log) enregistre chronologiquement chaque action de l'investigateur : heure, action, outil utilisé, résultat, décision. Le **formulaire de chaîne de custody** suit chaque pièce à conviction. Les **photos** documentent l'état physique des équipements (avant de débrancher un câble, on photographie). Les **captures d'écran horodatées** documentent les étapes de l'analyse. Sans documentation, l'investigation la plus brillante est irrecevable (en judiciaire) et irrépétable (en interne).

## 3.5 Les 10 erreurs fatales

Ces erreurs invalident une preuve ou égarent une investigation : (1) éteindre une machine allumée avant le dump RAM, (2) allumer une machine éteinte sans write blocker, (3) oublier de hasher avant ET après l'acquisition, (4) travailler sur l'original au lieu de la copie, (5) ne pas documenter ses actions en temps réel, (6) ignorer les fuseaux horaires lors de la corrélation de timestamps, (7) se fixer sur la première hypothèse sans en tester d'autres, (8) ignorer les sources de preuves volatiles (connexions réseau, processus en mémoire), (9) sous-estimer l'anti-forensics (l'attaquant a pu falsifier des timestamps, supprimer des logs, ou déposer de fausses preuves), et (10) produire un rapport dont les conclusions dépassent les constatations.

## 3.6 Fil rouge — MUSIC BOX : le scoping

> **🔬 MUSIC BOX — Épisode 3**
>
> Scoping initial chez NovaPharma. Claire formule 4 questions investigatives :
> 1. Comment l'attaquant a-t-il pénétré le SI ? (vecteur d'accès initial)
> 2. Quels systèmes sont compromis au-delà du poste WKS-RD-047 ? (mouvement latéral)
> 3. Des données ont-elles été exfiltrées, et si oui, lesquelles et quel volume ? (impact sur la propriété intellectuelle)
> 4. L'attaquant est-il encore présent dans le réseau ? (urgence de confinement)
>
> Machines prioritaires : WKS-RD-047 (poste compromis), SRV-RD-01 (serveur R&D Linux, données de recherche NP-427), DC01 (contrôleur de domaine — vérifier si l'AD est compromis).
>
> Fenêtre temporelle : J-90 à J (on prend large pour ne pas rater le début de l'intrusion — les logs du SIEM couvrent 12 mois, les logs proxy 6 mois).
>
> Décision : triage immédiat (dump RAM de WKS-RD-047 + collecte KAPE sur les 3 machines + export des logs AD) ce soir. Image disque complète de WKS-RD-047 et du serveur R&D samedi matin avec l'experte judiciaire. Perspective : probable judiciarisation si vol de données R&D confirmé.

---
