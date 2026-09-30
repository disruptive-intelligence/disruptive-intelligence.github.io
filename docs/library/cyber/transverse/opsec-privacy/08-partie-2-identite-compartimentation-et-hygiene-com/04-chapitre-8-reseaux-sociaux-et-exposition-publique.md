---
title: Chapitre 8 — Réseaux sociaux et exposition publique
source: Cyber/OPSEC_Privacy.md
note: OPSEC & privacy
up:
- - OPSEC & privacy
  - ../index.md
- - Partie 2 — Identité, compartimentation et hygiène comportementale
  - index.md
---

## 8.1 Le modèle économique = surveillance

Les paramètres « privacy » des plateformes ne neutralisent pas le modèle : la plateforme te surveille toujours en interne (clics, durée de visualisation, position du pouce, contacts, photos, métadonnées). Ce qu’ils contrôlent, c’est ce que d’autres utilisateurs voient de toi. Ne pas confondre les deux.

## 8.2 Audit de présence

Avant de durcir, mesure. Pour chaque plateforme où tu as un compte :

- Date de création, fréquence d’usage.
- Quelles informations sont publiques sur ton profil (nom, date de naissance, employeur, ville, école, téléphone).
- Quelles photos sont publiques et taguées.
- Quelles relations sont publiques (followers, amis, contacts).
- Quel historique de publication est public et combien remonte.
- Quels paramètres de confidentialité par défaut sont actifs.

Pour Facebook spécifiquement, utiliser l’outil intégré « Apparaître en tant que » pour voir ton profil comme un inconnu le voit. Découverte fréquente : ce que tu croyais privé est public.

## 8.3 Paramétrage défensif par plateforme

**Facebook / Meta** : profil verrouillé (public uniquement nom et photo), audience par défaut « Amis », désactivation de la reconnaissance faciale, désactivation du tagging automatique, restriction des recherches par email/téléphone, vérification de l’historique de publications.

**Instagram** : compte privé si possible, désactivation du suggéré, désactivation de la synchronisation des contacts (Instagram aspire ton carnet d’adresses si activé), audit des photos taguées.

**X (Twitter)** : protéger les tweets si pertinent, désactiver la découverte par email/téléphone, désactiver les DM ouverts si pas indispensable.

**LinkedIn** : limitation de la visibilité du profil aux moteurs (paramètre dédié), choix de ce qui apparaît au public vs aux connexions, suppression des notifications publiques de changements (« John updated his profile »), désactivation du « people you may know ».

**TikTok** : compte privé, désactivation du téléchargement de tes vidéos par d’autres, restriction des duets/stitch.

**Bluesky, Mastodon** : décentralisé, mais ton serveur (instance) voit tout. Choisir une instance de confiance. Comportement à publication reste sous ton contrôle.

## 8.4 Photos et tagging

Les photos sont le vecteur sous-estimé. Quatre risques :

1. **Géolocalisation** : EXIF + arrière-plan + indices visuels.
1. **Identification croisée** : la même photo sur deux comptes les corrèle.
1. **Reconnaissance faciale** : PimEyes et FaceCheck.ID indexent en continu.
1. **Tagging par des tiers** : tu n’as pas le contrôle de ce que tes proches publient avec toi.

Mesures : photos de profil dédiées (jamais utilisées ailleurs), demande explicite à tes proches de ne pas te taguer, désactivation des suggestions de tag automatique, audit régulier des photos publiées par d’autres.

## 8.5 Métadonnées invisibles côté plateforme

Même quand une plateforme retire les EXIF côté serveur (la plupart le font), elle conserve en interne : horodatage exact, géolocalisation au moment de l’upload, modèle d’appareil. Ces données ne sont pas publiques mais sont accessibles à la plateforme et, sur réquisition, aux autorités.

## 8.6 Silence stratégique

Ce que tu **ne publies pas** compte autant que ce que tu publies :

- Pas de photos de vacances en temps réel (signale ta maison vide).
- Pas de check-in dans des lieux récurrents (signale tes habitudes).
- Pas d’humeur en temps réel sur tes opinions politiques clivantes si tu vis dans un contexte risqué.
- Pas de mention de tes proches sans leur consentement.
- Pas d’achat coûteux affiché (signale la valeur de ton logement).

## 8.7 Suppression vs désactivation vs anonymisation

**Désactivation** : compte invisible mais récupérable. Tes données restent chez la plateforme.

**Suppression** : effacement (en théorie) après un délai de grâce (30 jours typiquement). En pratique, les sauvegardes plateformes peuvent conserver certaines données plus longtemps. Les archives publiques (Wayback, ArchiveTeam) conservent ce qu’elles ont aspiré.

**Anonymisation progressive** : changer nom, photo, biographie, mais garder le compte. Permet de conserver l’historique de relations sans afficher l’identité. Utile sur les comptes anciens.

## 8.8 Alternatives décentralisées

Mastodon et Bluesky proposent un modèle fédéré qui change la juridiction (instance choisie) et le modèle économique (souvent associatif). Mais :

- Tes posts sont publics par design.
- Ton instance voit tout (administrateur compris).
- La fédération expose certaines données à d’autres instances.

Ce ne sont pas des refuges privacy, ce sont des alternatives au modèle économique. Pas la même chose.

-----
