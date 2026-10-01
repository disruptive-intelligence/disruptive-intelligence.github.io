---
title: "Enquête initiale (triage)"
cours:
  - library/cyber/detection/reponse-a-incident/index.md
  - library/cyber/detection/reponse-a-incident-synthese/index.md
besoin: "Mener l'enquête initiale d'un incident (triage)"
---
# Enquête initiale — triage

Un événement suspect vient d'être signalé : établir le contexte **avant** de déclencher une réponse à grande
échelle. Une information isolée peut être trompeuse.

```
Alerte → Contextualiser → Valider → Délimiter → Prioriser
```

[Télécharger le modèle vierge à remplir](../modeles/enquete-initiale.md){ .md-button }

## 1. Contextualiser avant d'agir

Exemple : *compte administrateur → connexion à 10.0.10.15 → 03:00*. Sans contexte, impossible de conclure :

- [ ] Quel système correspond à cette IP ?
- [ ] Quel fuseau horaire pour cette heure ?
- [ ] L'utilisateur est-il légitime ?
- [ ] Une maintenance était-elle planifiée ?
- [ ] Est-ce une source habituelle ?
- [ ] Le MFA a-t-il été validé ?
- [ ] Quelle activité est associée ?

## 2. Informations générales

- [ ] Date et heure du signalement
- [ ] Personne qui a détecté ou signalé l'incident
- [ ] Méthode de détection : utilisateur, outil de sécurité (EDR, SIEM, IDS…), threat hunting, notification externe
- [ ] Type d'incident présumé : phishing, malware, compte compromis, fuite de données, indisponibilité, accès non autorisé

## 3. Systèmes impactés

Pour chaque système :

| À relever | Pour le collecter sous Linux |
|---|---|
| Hostname | [`hostnamectl`](../../linux/fondamentaux/systeme.md#connaitre-le-nom-dhote-le-fuseau-et-lheure) |
| Adresse IP | [`ip -br a`](../../linux/fondamentaux/reseau.md#voir-ses-adresses-ip) |
| OS et version | [`cat /etc/os-release`](../../linux/fondamentaux/systeme.md#connaitre-la-distribution-et-sa-version) |
| Localisation physique ou logique | inventaire, CMDB |
| Propriétaire | inventaire, CMDB |
| Fonction métier | inventaire, échange avec le métier |
| Criticité | inventaire, analyse de risques |
| État actuel | [`uptime`](../../linux/fondamentaux/systeme.md#voir-depuis-quand-la-machine-tourne-et-sa-charge), [`systemctl --failed`](../../linux/fondamentaux/processus.md#lister-les-services-actifs-ou-en-echec) |
| Utilisateurs ayant accédé au système | [`w`](../../linux/fondamentaux/systeme.md#voir-qui-est-connecte-maintenant), [`last`](../../linux/fondamentaux/systeme.md#voir-les-dernieres-connexions) |

## 4. Activité observée

- [ ] Actions effectuées
- [ ] Comptes impliqués
- [ ] Connexions
- [ ] Changements réalisés
- [ ] L'activité est-elle **encore en cours** ?

```
Activité suspecte → encore active ?
├─ oui → le confinement peut devenir urgent
└─ non → préserver et investiguer
```

## 5. Malware (s'il est impliqué)

- [ ] Date et heure de détection
- [ ] Famille ou type, si connu
- [ ] Systèmes impactés
- [ ] Fichiers associés (nom, chemin)
- [ ] Copies des échantillons
- [ ] Empreintes (SHA-256) — [`sha256sum`](../../linux/fondamentaux/fichiers-recherche.md#calculer-lempreinte-dun-fichier)
- [ ] Indicateurs réseau (IP, domaine, URL)
- [ ] Autres artefacts : processus, clé de registre, tâche planifiée…

!!! warning "Attention"
    Les échantillons se manipulent dans un environnement adapté et isolé.

## 6. Contexte métier et priorité

La même compromission technique n'a pas la même gravité selon l'actif : le portable d'un stagiaire, celui
du dirigeant et un contrôleur de domaine ne se traitent pas pareil.

```
Impact technique + criticité de l'actif + impact métier → priorité de l'incident
```

## Ensuite

- [Triage à chaud d'une machine Linux](../../forensic/linux/triage-a-chaud.md) pour collecter sur la machine.
- Construire la chronologie et délimiter l'étendue : [Réponse à incident — synthèse, phase de détection et d'analyse](../../../library/cyber/detection/reponse-a-incident-synthese/05-phase-de-detection-et-d-analyse.md).

*D'après mon cours [Réponse à incident — synthèse](../../../library/cyber/detection/reponse-a-incident-synthese/05-phase-de-detection-et-d-analyse.md) (enquête initiale, informations à collecter, contexte métier).*
