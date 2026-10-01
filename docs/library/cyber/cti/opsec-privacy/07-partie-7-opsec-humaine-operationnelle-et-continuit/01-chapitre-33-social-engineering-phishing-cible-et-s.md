---
title: Chapitre 33 — Social engineering, phishing ciblé et spyware mercenaire
source: Cyber/01 CTI & renseignement/OPSEC/OPSEC & privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 7 — OPSEC humaine, opérationnelle et continuité
  - index.md
---

> **Niveau de posture (cf. Ch 2.6)** : la vigilance phishing concerne **tous les niveaux** (le phishing est l’attaque la plus statistiquement probable, indépendamment du profil). Lockdown Mode iOS, GrapheneOS et reboot quotidien relèvent du **Niveau 2** quand un indicateur de ciblage existe (publication sensible, contexte politique, threat notification reçue). MVT et iVerify systématiques, audit forensique périodique, plan de réponse spyware = **Niveau 3** réservé aux cibles documentées (journalistes investigation actuelle, opposants politiques, défenseurs droits humains exposés).

> **Note critique** : ne pas se dimensionner au Niveau 3 par fascination ou anxiété. Recevoir une vraie *Threat Notification* d’Apple, Google ou Meta est rare et conservateur. Les notifications de ce type sont envoyées à des cibles confirmées. Si tu n’en as jamais reçu et que ton profil ne correspond pas aux cibles documentées par Citizen Lab et Amnesty Security Lab, ton temps est mieux investi sur N1 et N2.

## 33.1 Pourquoi l’humain reste le maillon faible

La cryptographie moderne tient. Les protocoles aussi. Ce qui se casse, c’est l’humain : il clique sur le lien, il fait confiance à la voix au téléphone, il branche la clé USB trouvée au sol, il déverrouille son téléphone parce qu’il a peur de manquer un appel important. Les attaquants sérieux investissent dans l’ingénierie sociale parce qu’elle est *plus rentable* que les exploits techniques.

## 33.2 Phishing : taxonomie

- **Phishing de masse** : email générique envoyé à des millions. Faible taux de succès individuel mais volume.
- **Spear phishing** : message ciblé, personnalisé avec OSINT préalable (nom du destinataire, contexte professionnel, vocabulaire interne). Beaucoup plus efficace.
- **Whaling** : spear phishing visant un cadre supérieur ou une personne haut placée. Effets de levier importants (autorisation de virement, ouverture d’accès).
- **Smishing** : phishing par SMS. En croissance avec faux livreurs, fausses banques, faux opérateurs.
- **Vishing** : phishing vocal. Le téléphone légitime l’autorité ressentie.
- **Quishing** : phishing par QR code. Affichage en lieu public d’un QR qui pointe vers site malveillant.

## 33.3 BEC : Business Email Compromise

Variante professionnelle. Un attaquant compromet (ou usurpe) le compte d’un dirigeant. Envoie au comptable une demande de virement urgent, plausible, semblant venir du DG. Le comptable exécute. Pertes annuelles mondiales : milliards.

Mitigation : procédures internes exigent confirmation par canal séparé (téléphone interne, en personne) pour tout virement au-dessus d’un seuil. Formation systématique. Vérification des en-têtes email (SPF, DKIM, DMARC).

## 33.4 Reconnaissance préalable et OSINT offensif

Avant un spear phishing sérieux, l’attaquant a typiquement passé heures voire jours sur ta présence publique : LinkedIn, X, articles, slides de conférences, contributions GitHub, mentions dans la presse. Il connaît tes collègues, ton vocabulaire, tes projets en cours.

Conséquence : ta réduction d’empreinte publique (Ch 5-8) est *aussi* une mesure anti-phishing structurelle.

## 33.5 Indicateurs et détection

À l’œil :

- **Domaine légèrement modifié** : `proton-mail.com` au lieu de `proton.me`, `microsoft0nline.com` au lieu de `microsoft.com`. Survoler les liens, lire l’URL réelle.
- **Sense d’urgence artificielle** : « action immédiate requise », « votre compte sera suspendu dans 24h ».
- **Émotion stimulée** : peur (« sécurité compromise »), curiosité (« document confidentiel pour vous »), cupidité (« vous avez gagné »), serviabilité (« j’ai besoin d’aide »).
- **Demande inhabituelle** : action que tu ne ferais normalement pas dans ce contexte.
- **Discordance signal/canal** : ton patron ne t’envoie jamais des emails à 22h pour des virements urgents.

Au-delà :

- **Vérification du sender** : analyser les en-têtes complets (Received, Authentication-Results).
- **Vérification du domaine** : `whois` du domaine, ancienneté (un domaine créé hier est suspect).
- **Bac à sable** pour pièces jointes (Ch 16).

## 33.6 Spyware mercenaire : Pegasus, Predator, Graphite

**Pegasus (NSO Group)** : spyware iOS/Android le plus documenté. Capacités révélées par Citizen Lab, Amnesty Security Lab : exfiltration complète (messages, photos, contacts, localisation), activation du micro et de la caméra, contournement du chiffrement E2EE (lecture après déchiffrement local).

Vecteurs documentés :

- **Zero-click iMessage** (FORCEDENTRY, 2021) : exploit envoyé en iMessage qui s’exécute sans interaction. Patch Apple ultérieur.
- **Zero-click WhatsApp** (2019) : appel WhatsApp qui infecte même sans décrocher.
- **One-click via lien** : SMS contenant un lien qui exploite WebKit.
- **Réseau** : injection via opérateur cellulaire compromis.

**Predator (Intellexa / Cytrox)** : concurrent grec, capacités similaires, déploiement documenté en Grèce, Égypte, Vietnam, Madagascar, Soudan.

**Graphite (Paragon Solutions)** : plus récent (2024-2025), capacités équivalentes, déploiement contesté (révélations Citizen Lab fin 2024, WhatsApp a notifié des journalistes et activistes en janvier 2025).

**QuaDream, Candiru** : autres acteurs, plus en retrait.

**Cibles documentées 2020-2025** : journalistes (dont Jamal Khashoggi avant son assassinat — un des proches était sous Pegasus), activistes (Forbidden Stories Pegasus Project), avocats, opposants politiques, proches de cibles. Cas confirmés sur 6 continents.

## 33.7 Lockdown Mode, GrapheneOS, durcissement

**Lockdown Mode iOS** (cf. Ch 15) désactive des fonctionnalités spécifiquement exploitées par les spyware mercenaires. Études de cas Citizen Lab montrent qu’il aurait bloqué plusieurs exploits documentés. Pour HVT : activation systématique.

**GrapheneOS** : durcissement kernel, sandboxing renforcé, attestation. N’élimine pas le risque mais relève la barre.

**Reboot quotidien** : la plupart des spyware modernes ne persistent pas au redémarrage. Cinq secondes par jour de discipline = grandes leçons d’élévation du coût pour l’attaquant.

## 33.8 Détection : MVT, iVerify, notifications plateformes

- **MVT (Mobile Verification Toolkit)** : développé et maintenu par *Amnesty Security Lab*, open source (https://github.com/mvt-project/mvt). Analyse les sauvegardes iPhone (iTunes/iCloud-style local backups, *pas* iCloud chiffré) et les *full filesystem dumps* Android pour détecter des indicateurs de compromission (IOCs) Pegasus, Predator, Graphite, QuaDream et d’autres familles documentées. Plus efficace en post-mortem (sur un appareil suspecté) qu’en temps réel. Les IOCs sont publiés et mis à jour par Amnesty et Citizen Lab à mesure de leurs investigations.
  
  *Limites* : MVT détecte les IOCs *connus*. Une variante neuve d’un spyware mercenaire peut ne pas être détectée. L’absence de détection ne prouve pas l’absence d’infection. C’est néanmoins un outil de référence — la majorité des cas Pegasus publiquement confirmés l’ont été après analyse MVT par Amnesty ou Citizen Lab.
  
  *Workflow typique* : sauvegarde locale iTunes du iPhone (cryptée, mais MVT peut traiter), import dans MVT, scan automatique contre les IOCs, génération d’un rapport. Pour Android, plus complexe (full image dump requis, possibilité de root requis).

- **iVerify** : outil commercial développé par *Trail of Bits* puis par une équipe dédiée. Application iOS / Android. Heuristiques pour détecter spywares connus, audit de la posture de sécurité de l’appareil (versions à jour, Lockdown Mode actif, services à risque), alertes en cas d’anomalie. Pratique au quotidien pour profils HVT — c’est un complément de MVT, pas un substitut. Modèle freemium, plans pro pour journalistes/ONG accessibles via partenariats avec Access Now.
- **Notifications plateformes** :
  - **Apple Threat Notifications** envoyées depuis 2021. Le wording standard est « Apple a détecté que vous êtes potentiellement la cible d’une attaque parrainée par un État ». Apple ne précise pas le vecteur, mais publie les critères généraux. Ces notifications sont conservatrices — Apple privilégie d’alerter à risque légèrement avéré plutôt que tarder à le faire.
  - **Google Threat Analysis Group (TAG)** envoie des notifications équivalentes sur Gmail et Workspace pour ciblage par acteurs étatiques.
  - **Meta** alerte via WhatsApp dans les cas de zero-click exploit (cas Paragon Graphite, janvier 2025 : ~90 utilisateurs notifiés dans plusieurs pays dont l’Italie).
  - **Si tu reçois une telle notification** : prends-la au sérieux. C’est rare. Ces notifications sont quasi systématiquement validées par des éléments concrets côté plateforme. Application immédiate de la procédure 33.9.

## 33.9 Procédure post-compromission suspectée

1. **Isolation** : passer l’appareil en mode avion (vrai mode avion, vérifié). Faraday bag si disponible.
1. **Ne pas redémarrer** (perdrait des artefacts forensiques) — sauf si tu n’as pas accès à un analyste forensique.
1. **Contact d’experts** : Access Now Digital Security Helpline (gratuit pour HVT), Citizen Lab, Amnesty Security Lab.
1. **Sauvegarde** pour analyse (`idevicebackup2` ou Quicktime pour iOS sans iCloud).
1. **En attendant analyse** : appareil neuf, comptes audités, mots de passe critiques renouvelés, contacts prévenus.
1. **Long terme** : changement de modèle de menace, formation, montée en posture.

## 33.10 *Fil rouge* — Anya reçoit une notification Apple

Anya V. reçoit un mail d’Apple Threat Notification : « Apple détecte que vous êtes potentiellement la cible d’une attaque par un attaquant parrainé par un État ». Elle :

1. Met immédiatement son iPhone en mode avion, le glisse dans une pochette Faraday.
1. Contacte la Digital Security Helpline d’Access Now.
1. Avec leur aide, fait une sauvegarde via Mac, soumet à analyse Citizen Lab.
1. Diagnostic : présence d’IOC Predator. Confirmation après 10 jours.
1. Change tous ses comptes critiques depuis appareils propres. Bascule définitivement sur GrapheneOS. Communique publiquement, ce qui est sa stratégie : la publicité protège.

-----
