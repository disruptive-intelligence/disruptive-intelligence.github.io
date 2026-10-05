---
title: "Active Directory au quotidien"
cours:
  - library/it/active-directory/active-directory/index.md
  - library/it/windows/powershell/index.md
---

# Active Directory au quotidien

Trouver un compte et son état, déverrouiller, réinitialiser, créer, gérer les groupes ; ranger les objets dans les OU, lire un mot de passe LAPS, créer un gMSA ; diagnostiquer les GPO, Kerberos et les contrôleurs de domaine ; contrôles d'hygiène.

Les incontournables : `Get-ADUser` · `Get-ADComputer` · `Search-ADAccount` · `Get-ADGroupMember` · `gpresult` · `klist` · `nltest` · `dcdiag`
{ .kw-cs-top }

Les cmdlets `*-AD*` demandent le module ActiveDirectory (RSAT sur un poste d'administration, présent sur les DC).

## Sous-rubriques

| Sous-rubrique | Ce qu'on y trouve |
|---|---|
| [**Comptes et groupes**](comptes-groupes.md) | Tout savoir sur un compte, le déverrouiller, réinitialiser son mot de passe, le désactiver, le créer ; gérer les membres des groupes. |
| [**OU, ordinateurs et GPO**](ou-ordinateurs-gpo.md) | Ranger les objets dans les OU, lister les ordinateurs, lire un mot de passe LAPS ; voir, forcer et lister les GPO. |
| [**Kerberos, DC et comptes de service**](kerberos-dc.md) | Créer un gMSA ; voir et purger ses tickets Kerberos, diagnostiquer un échec ; trouver les contrôleurs de domaine, leurs rôles et leur santé. |
| [**Contrôles d'hygiène**](hygiene.md) | Comptes inactifs, mots de passe qui n'expirent jamais, comptes privilégiés, comptes porteurs d'un SPN, âge du mot de passe de krbtgt. |

## Tous les besoins

- [Comptes et groupes](comptes-groupes.md) — [Tout savoir sur un compte](comptes-groupes.md#tout-savoir-sur-un-compte) · [Trouver les comptes verrouillés et les déverrouiller](comptes-groupes.md#trouver-les-comptes-verrouilles-et-les-deverrouiller) · [Réinitialiser un mot de passe](comptes-groupes.md#reinitialiser-un-mot-de-passe) · [Désactiver un compte](comptes-groupes.md#desactiver-un-compte) · [Créer un compte](comptes-groupes.md#creer-un-compte) · [Voir les membres d'un groupe, imbrications comprises](comptes-groupes.md#voir-les-membres-dun-groupe-imbrications-comprises) · [Voir les groupes d'un compte](comptes-groupes.md#voir-les-groupes-dun-compte) · [Ajouter ou retirer un membre](comptes-groupes.md#ajouter-ou-retirer-un-membre)
- [OU, ordinateurs et GPO](ou-ordinateurs-gpo.md) — [Voir l'OU d'un objet et l'y déplacer](ou-ordinateurs-gpo.md#voir-lou-dun-objet-et-ly-deplacer) · [Supprimer une OU protégée](ou-ordinateurs-gpo.md#supprimer-une-ou-protegee) · [Lister les ordinateurs du domaine et leur système](ou-ordinateurs-gpo.md#lister-les-ordinateurs-du-domaine-et-leur-systeme) · [Lire le mot de passe LAPS d'un poste](ou-ordinateurs-gpo.md#lire-le-mot-de-passe-laps-dun-poste) · [Voir les GPO appliquées à un poste et à un utilisateur](ou-ordinateurs-gpo.md#voir-les-gpo-appliquees-a-un-poste-et-a-un-utilisateur) · [Forcer l'application des GPO](ou-ordinateurs-gpo.md#forcer-lapplication-des-gpo) · [Lister les GPO et leurs dates de modification](ou-ordinateurs-gpo.md#lister-les-gpo-et-leurs-dates-de-modification)
- [Kerberos, DC et comptes de service](kerberos-dc.md) — [Créer un compte de service géré (gMSA)](kerberos-dc.md#creer-un-compte-de-service-gere-gmsa) · [Voir et purger ses tickets Kerberos](kerberos-dc.md#voir-et-purger-ses-tickets-kerberos) · [Diagnostiquer un échec Kerberos](kerberos-dc.md#diagnostiquer-un-echec-kerberos) · [Trouver les contrôleurs de domaine et leurs rôles](kerberos-dc.md#trouver-les-controleurs-de-domaine-et-leurs-roles) · [Vérifier la santé des contrôleurs de domaine](kerberos-dc.md#verifier-la-sante-des-controleurs-de-domaine)
- [Contrôles d'hygiène](hygiene.md) — [Trouver les comptes inactifs](hygiene.md#trouver-les-comptes-inactifs) · [Trouver les mots de passe qui n'expirent jamais](hygiene.md#trouver-les-mots-de-passe-qui-nexpirent-jamais) · [Lister les comptes privilégiés (actuels et anciens)](hygiene.md#lister-les-comptes-privilegies-actuels-et-anciens) · [Inventorier les comptes utilisateurs qui portent un SPN](hygiene.md#inventorier-les-comptes-utilisateurs-qui-portent-un-spn) · [Vérifier l'âge du mot de passe de krbtgt](hygiene.md#verifier-lage-du-mot-de-passe-de-krbtgt)
