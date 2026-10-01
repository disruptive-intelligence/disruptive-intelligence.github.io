---
title: Chapitre 11 — Du signal faible à l'incident confirmé
source: Cyber/06 Détection & réponse/Réponse à incident.md
note: Réponse à incident
up:
- - Réponse à incident
  - ../index.md
- - Partie III — Détection, qualification et triage
  - index.md
---

## 11.1 Sources de détection et leurs biais

Chaque source de détection a un périmètre de visibilité et des angles morts. L'**EDR/XDR** détecte les comportements suspects sur les endpoints (exécution de binaires, modifications système, connexions réseau des processus) mais ne voit pas le trafic réseau entre les machines ni les activités cloud. Le **SIEM** voit les logs qui y sont envoyés — ce qui signifie que tout ce qui n'est pas journalisé est invisible (si le PowerShell script block logging n'est pas activé, le SIEM ne verra jamais les commandes PowerShell de l'attaquant). Le **NDR** voit le trafic réseau en temps réel mais ne voit pas le contenu du trafic chiffré (et en 2025-2026, la quasi-totalité du trafic C2 est chiffrée en HTTPS). Les **alertes antivirus** sont souvent noyées dans le bruit des faux positifs et des détections de PUA (Potentially Unwanted Applications). Le **signalement utilisateur** est parfois le premier signal (« j'ai cliqué sur un lien bizarre ») mais il est souvent tardif (l'utilisateur n'ose pas signaler, ou ne se rend pas compte). La **notification externe** (CERT-FR, partenaire, threat intel feed, notification par l'attaquant via une note de rançon) indique que la compromission est déjà connue en dehors de l'organisation — et souvent que le temps de séjour est déjà long.

La conséquence pour l'investigateur est qu'aucune source seule ne donne la vision complète. La corrélation multi-sources (endpoint + réseau + AD + cloud) est la seule méthode fiable pour établir l'étendue réelle de la compromission.

## 11.2 Le temps de séjour (dwell time)

Le dwell time — la durée entre la compromission initiale et la détection — est la métrique qui détermine la profondeur de l'investigation. Selon le M-Trends 2025 de Mandiant, la médiane mondiale est d'environ 10 à 13 jours, avec une amélioration progressive grâce à la généralisation des EDR. Mais cette médiane masque une distribution très dispersée : les ransomwares sont souvent détectés en quelques jours (l'attaquant accélère pour chiffrer), tandis que les opérations d'espionnage peuvent durer des mois, voire des années.

Le dwell time détermine la fenêtre temporelle de l'investigation : si l'attaquant est dans le réseau depuis 5 semaines, il faut investiguer 5 semaines de logs, d'artefacts, et de flux réseau. Si les logs ne couvrent que 30 jours, les premières actions de l'attaquant sont perdues.

## 11.3 Les signaux faibles pré-incident

Avant l'alerte majeure qui déclenche l'IR, des signaux faibles ont souvent été générés — et ignorés ou sous-priorisés. Les connexions à des heures inhabituelles (un compte de service qui s'authentifie à 3h du matin un dimanche), les alertes Kerberos en masse (erreurs de pré-authentification répétées sur de nombreux comptes = possible password spraying ou Kerberoasting), les modifications de GPO non documentées, les exécutions de binaires depuis des répertoires temporaires, les requêtes DNS vers des domaines générés algorithmiquement (DGA), et les petits pics d'exfiltration (quelques Go par jour, en dessous du seuil d'alerte mais visibles en tendance).

La difficulté est que ces signaux sont noyés dans le bruit de fonctionnement normal d'un SI de 12 000 utilisateurs. L'amélioration de la détection des signaux faibles passe par le tuning des règles de détection (réduction des faux positifs pour rendre les vrais positifs visibles), la détection comportementale (baseline de normalité par utilisateur et par machine, alertes sur les écarts), et la corrélation multi-sources (un signal faible sur l'endpoint + un signal faible sur le réseau + un signal faible sur l'AD = un signal fort).

## 11.4 Fil rouge — BLACKTIDE : les signaux manqués

> **🔍 BLACKTIDE — Épisode 11**
>
> L'investigation post-incident révélera que 3 alertes avaient été générées et classées faux positifs ou basse priorité. À J-30 : alerte antivirus sur un script PowerShell encodé détecté sur le poste du DRH du sous-traitant GestPaie, qui se connectait via VPN au réseau Arvantis. L'alerte a été classée « PUA — faux positif probable » par le SOC N1. En réalité, c'était l'infostealer Lumma en phase d'installation. À J-22 : pic anormal de requêtes Kerberos TGS (Event ID 4769) avec encryption type RC4 (0x17) sur DC01 — signature classique de Kerberoasting. L'alerte SIEM a été classée « activité suspecte — priorité basse » parce que le volume ne dépassait pas le seuil d'alerte automatique. À J-15 : seconde alerte antivirus, cette fois sur DC01, pour un script PowerShell obfusqué dans `C:\Windows\Temp\`. Classée faux positif parce que « les admins utilisent parfois PowerShell sur les DC ».
>
> Trois occasions manquées de détecter l'intrusion 2 à 4 semaines plus tôt — quand le confinement aurait été beaucoup plus simple.

---
