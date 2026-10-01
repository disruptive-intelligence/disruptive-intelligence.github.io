---
title: Chapitre 22 — Cadre juridique, éthique et sécurité de l'analyste
source: Cyber/01 CTI & renseignement/Menace cyber/Dark Web.md
note: Dark Web
up:
- - Dark Web
  - ../index.md
- - Partie V — Investigation, veille et collecte
  - index.md
---

Avant tout outil technique, l'analyste dark web doit maîtriser le cadre légal qui encadre son activité. Consulter un forum cybercriminel n'est pas illégal en soi — mais certains actes d'investigation le sont, et d'autres sont dans une **zone grise** qu'il faut savoir naviguer.

## 22.1 Le cadre français

**Code pénal articles 323-1 à 323-8**. Atteinte aux STAD (systèmes de traitement automatisé de données). Incrimine :

- **323-1** : l'accès ou le maintien frauduleux dans un STAD (maximum 3 ans d'emprisonnement et 100 000 € d'amende ; circonstances aggravantes si suppression/modification de données : 5 ans, 150 000 €).
- **323-2** : l'entrave du fonctionnement d'un STAD (7 ans, 300 000 €).
- **323-3** : la modification frauduleuse de données (7 ans, 300 000 €).
- **323-3-1** : la détention et la diffusion d'outils conçus pour commettre ces infractions — **article clé pour l'analyste**, qui encadre la manipulation d'outils offensifs.

**Loi du 24 juillet 2015 sur le renseignement** et articles associés dans le Code de la sécurité intérieure : cadre des activités de renseignement encadrées par l'État. L'analyste privé n'opère pas sous ce régime, mais les agences partenaires (DGSI, DGSE) peuvent.

**Loi Informatique et Libertés + RGPD**. La collecte et le traitement de données personnelles exposées (même exposées par un attaquant) restent soumis aux régimes de protection. Un analyste qui capture un dump contenant des données personnelles doit gérer ce stock selon les règles applicables — base légale de traitement, minimisation, sécurisation, suppression post-exploitation.

**Code de procédure pénale article 40**. Tout fonctionnaire qui, dans l'exercice de ses fonctions, acquiert la connaissance d'un crime ou d'un délit, est tenu d'en aviser le procureur. Un analyste fonctionnaire (service public, OIV) peut être concerné — même en secteur privé, la logique de signalement est structurante.

**Cadre ANSSI / OIV**. Les OIV ont obligation de notification d'incidents significatifs à l'ANSSI. Les prestataires PASSI/PDIS/PRIS opèrent sous qualification.

## 22.2 Le cadre européen

**Directive NIS 2 (UE 2022/2555)**. Transposée en France et dans tous les États membres. Obligations de cybersécurité et notification pour les entités essentielles et importantes dans 18 secteurs. Les analystes opérant pour ces entités ont un rôle dans la posture de notification.

**RGPD**. Régit les données personnelles. Les dumps contenant données personnelles doivent être traités avec base légale (intérêt légitime de l'investigation, mission de service public, etc.), minimisation, sécurité.

**Convention de Budapest sur la cybercriminalité (2001) et ses protocoles additionnels**. Cadre de coopération internationale en matière cybercriminalité. Protocole additionnel de mai 2022 facilite l'accès transfrontière à la preuve électronique.

**EU Cyber Solidarity Act (2024)**. Crée un réseau européen de SOC et un mécanisme de réponse d'urgence pour incidents cyber transfrontaliers.

**EU Cyber Sanctions Regime**. Sanctions ciblées contre cyberacteurs malveillants.

## 22.3 Les zones grises

Plusieurs activités sont **dans la zone grise** — techniquement légales mais nécessitent prudence.

**Consulter des forums criminels**. Légal en tant que tel. La simple consultation d'un contenu publiquement accessible (même sur .onion) n'est pas une infraction.

**Créer un compte sur un forum criminel**. Nécessaire pour accéder aux zones fermées. Légal, avec précautions — le pseudonyme ne doit pas être utilisé pour commettre des infractions (solliciter des services criminels, acheter des données, participer à des discussions opérationnelles).

**Télécharger des échantillons**. Zone sensible. Télécharger un fichier contenant des données personnelles (même publiquement exposées par l'attaquant) peut contrevenir au RGPD. Télécharger du malware pour analyse est **généralement accepté** dans un cadre de recherche, mais la détention de malware est encadrée par l'article 323-3-1. Pratique recommandée : n'en télécharger que ce qui est strictement nécessaire à la mission, documenter la justification, sécuriser le stock, supprimer après exploitation.

**Télécharger des données volées**. Encore plus sensible. Principe : **nécessité et proportionnalité**. Télécharger un échantillon pour authentification est différent de télécharger l'intégralité d'un dump.

**Télécharger du CSAM**. **Interdit absolument**. Même dans un cadre d'investigation, la détention est criminelle. Les investigations CSAM relèvent des autorités judiciaires avec cadre spécifique (pornographie enfantine, articles 227-23 et suivants du Code pénal).

**Payer pour obtenir de l'information**. Dépend du contexte. Payer un droit d'entrée forum pour investigation : généralement accepté avec autorisation hiérarchique et traçabilité. Acheter des données volées : **risqué** — peut constituer recel. La DGSI accompagne ces cas.

**Contacter un vendeur en se faisant passer pour acheteur**. Zone grise classique. Généralement accepté pour investigation avec encadrement, mais peut constituer provocation dans certains cadres — la jurisprudence française est restrictive sur la **provocation à la commission d'infraction**. L'analyste doit se présenter comme acheteur potentiel pour obtenir des échantillons, mais ne pas pousser le vendeur à augmenter son activité criminelle.

**Infiltrer un groupe comme membre actif**. Réservé aux forces de l'ordre avec mandat judiciaire. Un analyste privé qui « infiltrerait » un groupe criminel dépasse largement le cadre légal.

## 22.4 L'éthique professionnelle

Au-delà de la légalité stricte, plusieurs principes éthiques s'appliquent.

**Minimisation**. Collecter le minimum nécessaire à la mission. Ne pas stocker plus que ce qu'on exploite. Supprimer après exploitation.

**Non-prolifération**. Ne pas rediffuser les données collectées au-delà du cercle justifié. Un dump contenant des données personnelles ne se partage pas lightly, même entre analystes.

**Non-exploitation abusive**. Les données volées peuvent contenir des informations sensibles (vie privée, communications intimes, données médicales). L'analyste ne les exploite qu'au strict nécessaire à la mission, pas par curiosité.

**Transparence hiérarchique**. Les choix d'investigation sensibles (contact vendeur, paiement, téléchargement) sont documentés et autorisés par la hiérarchie.

**Respect des victimes**. Les victimes de breach sont des personnes. Contact avec elles doit respecter leur dignité — ni sensationnaliser, ni exploiter leur détresse.

**Coopération avec autorités**. Si l'investigation révèle des infractions graves (trafic humain, CSAM, terrorisme), signalement obligatoire aux autorités compétentes. Le secret professionnel n'est pas absolu.

## 22.5 La sécurité personnelle de l'analyste

L'investigation dark web expose à plusieurs risques **personnels**.

**Risque technique**. Compromission du poste d'investigation via malware piégé. Les fichiers téléchargés, les liens cliqués, les sites visités peuvent contenir des exploits ciblant les analystes. Mesures : machine dédiée, VM jetables (Whonix + VM d'exécution), pas de comptes personnels sur la machine.

**Risque d'identification par les cibles**. Les acteurs malveillants font de la contre-surveillance. Un analyste qui utilise ses accès personnels, qui lit systématiquement les posts d'un vendeur spécifique, qui pose des questions révélatrices — peut être identifié comme investigateur. Conséquences : ciblage du compte d'investigation, tentative d'identification réelle (dox), voire menaces physiques dans les cas extrêmes.

**Risque juridique transfrontalier**. Un analyste français qui interagit avec un vendeur russe via un forum hébergé aux Pays-Bas peut techniquement tomber sous multiple juridictions. En pratique, si l'activité est légale en France et dans le cadre d'une mission professionnelle, le risque est faible, mais pas nul.

**Risque de manipulation psychologique**. L'immersion dans l'écosystème dark web expose à des contenus difficiles (violences, CSAM accidentellement croisé, narratifs extrêmes). L'analyste doit être soutenu par son organisation — debriefing psychologique, rotation des missions, limitation de l'exposition aux contenus traumatisants.

**Risque de compromission éthique**. Dérive possible — un analyste exposé longtemps à l'écosystème peut développer de l'empathie pour les cibles, se laisser tenter par des relations personnelles avec des sources, perdre la distance professionnelle. Supervision hiérarchique et rotation atténuent.

## 22.6 Fil rouge — DARKSTREAM : encadrement légal

> **🌐 DARKSTREAM — Épisode 12 : cadrage DGSI**
>
> Lucas prépare son premier contact avec aero_source. Avant action, validation DGSI obligatoire.
>
> Réunion avec l'officier DGSI référent. Points validés :
> - **Contact OK** sous persona « mapletech » — acheteur technologique intéressé par specs aéronautiques. Légende crédible.
> - **Pas d'engagement ferme d'achat** — Lucas peut exprimer intérêt, demander échantillons, négocier indirectement, mais jamais confirmer la transaction. La DGSI précise : « ne provoquez pas la vente, cherchez à comprendre ».
> - **Pas de téléchargement de l'intégralité** — échantillons acceptés pour authentification, le dump complet non.
> - **Remontée bi-hebdomadaire** : Lucas briefe la DGSI tous les 3-4 jours sur l'évolution.
> - **Arrêt immédiat** si Lucas perçoit un risque d'exposition (persona identifiée comme analyste, menaces, contre-enquête).
> - **Pas d'achat** des données. Si aero_source impose paiement pour les échantillons (rare), arrêt de l'investigation de ce côté.
>
> Tous les échanges XMPP sont archivés (logs chiffrés chez Athéna, accessibles DGSI). Capture d'écran au fur et à mesure. Hash des fichiers téléchargés. Documentation exhaustive du cheminement d'investigation.
>
> Cette rigueur procédurale est **la condition de l'utilisabilité** de ce que Lucas produira. Un rapport sans chain of custody documentée n'a aucune valeur judiciaire. Un rapport trop fondé sur des actions juridiquement douteuses peut être écarté.

---
