---
title: Chapitre 23 — Recherche et filtrage AD
source: IT/02 Windows/Ligne de commande/PowerShell.md
note: PowerShell
up:
- - PowerShell
  - ../index.md
- - Partie IV — Administration active directory
  - index.md
---

## 🟢 Le minimum à savoir

### Pourquoi ce chapitre est important

Un annuaire d'entreprise contient des milliers d'objets. Savoir **filtrer efficacement** est ce qui sépare un script qui met 10 minutes (et surcharge le DC) d'un script instantané. La clé : filtrer **côté serveur** avec `-Filter`, pas côté client avec `Where-Object`.

### `-Filter` : le filtrage côté serveur

`-Filter` envoie la condition au contrôleur de domaine, qui ne renvoie **que** les objets correspondants. C'est rapide et économe.

```powershell
# Utilisateurs activés
Get-ADUser -Filter "Enabled -eq '$true'"

# Utilisateurs d'un service
Get-ADUser -Filter "Department -eq 'Comptabilité'" -Properties Department

# Recherche par motif
Get-ADUser -Filter "Surname -like 'Dup*'"

# Combiner des conditions
Get-ADUser -Filter "Enabled -eq '$true' -and Department -eq 'IT'" -Properties Department
```


> **Syntaxe du `-Filter` :** elle ressemble aux opérateurs PowerShell (`-eq`, `-like`, `-and`) mais s'écrit **entre guillemets** et suit des règles propres à AD. Les attributs utilisés dans le filtre doivent exister dans AD (ex : `Surname`, pas `Nom`).

### `-Filter` vs `Where-Object` : la différence cruciale

```powershell
# ❌ LENT : récupère TOUS les utilisateurs, puis filtre côté client
Get-ADUser -Filter * -Properties Department | Where-Object { $_.Department -eq "IT" }

# ✅ RAPIDE : le DC ne renvoie que les utilisateurs IT
Get-ADUser -Filter "Department -eq 'IT'" -Properties Department
```


> **Règle d'or :** filtre **toujours** au plus près de la source. `-Filter` (côté serveur) d'abord ; `Where-Object` (côté client) seulement pour ce que `-Filter` ne sait pas faire (calculs complexes, propriétés dérivées). Sur un annuaire de 50 000 objets, la différence est spectaculaire.

### `-SearchBase` : limiter la recherche à une OU

```powershell
# Ne chercher que dans l'OU IT
Get-ADUser -Filter * -SearchBase "OU=IT,DC=lab,DC=local"

# Combiner filtre et périmètre
Get-ADUser -Filter "Enabled -eq '$true'" -SearchBase "OU=Comptabilité,DC=lab,DC=local"
```


`-SearchBase` restreint la recherche à une branche de l'arbre — plus rapide et plus ciblé. `-SearchScope` affine (`Base`, `OneLevel`, `Subtree`).

### `-Properties` : récupérer les bons attributs

Rappel (Ch.19-20) : par défaut, seul un jeu réduit d'attributs revient. `-Properties` charge ceux dont tu as besoin :

```powershell
Get-ADUser -Filter * -Properties mail, Department, LastLogonDate |
    Select-Object Name, mail, Department, LastLogonDate
```


> **Performance :** ne demande que les attributs nécessaires. `-Properties *` charge **tout** (100+ attributs par objet) — pratique pour explorer un seul objet, mais coûteux sur une recherche de masse. En production, liste explicitement les attributs voulus.

## 🟡 Très utile en pratique

### Un rapport ciblé et performant

```powershell
# Comptes IT activés, avec leurs infos clés — filtré et projeté proprement
Get-ADUser -Filter "Enabled -eq '$true'" `
           -SearchBase "OU=IT,DC=lab,DC=local" `
           -Properties mail, Title, LastLogonDate |
    Select-Object Name, SamAccountName, mail, Title, LastLogonDate |
    Sort-Object Name |
    Export-Csv "C:\rapports\users_IT.csv" -NoTypeInformation -Encoding UTF8
```


Ce pipeline combine `-Filter` (serveur), `-SearchBase` (périmètre), `-Properties` (attributs), `Select-Object` (projection) et `Export-Csv` — le schéma type d'un rapport AD.

### Compter par catégorie

```powershell
# Répartition des utilisateurs par service
Get-ADUser -Filter * -Properties Department |
    Group-Object Department |
    Select-Object Count, Name |
    Sort-Object Count -Descending
```


## 🔴 Bonus

### `Get-ADObject` : chercher tous types d'objets

Quand on ne sait pas si l'objet est un utilisateur, un groupe ou un ordinateur, `Get-ADObject` cherche par-delà les types :

```powershell
Get-ADObject -Filter "Name -like 'SRV*'" |
    Select-Object Name, ObjectClass, DistinguishedName
```


### Filtres LDAP

Pour des recherches très pointues, `-LDAPFilter` accepte la syntaxe LDAP native :

```powershell
Get-ADUser -LDAPFilter "(&(objectCategory=user)(!(mail=*)))"    # utilisateurs sans email
```


Puissant mais plus aride — à réserver aux cas que `-Filter` ne couvre pas.

## ❌ Erreur classique

```powershell
# Tout ramener puis filtrer côté client (lent, surcharge le DC)
Get-ADUser -Filter * | Where-Object { $_.Department -eq "IT" }   # ❌
Get-ADUser -Filter "Department -eq 'IT'"                          # ✅

# Filtrer sur un attribut non chargé
Get-ADUser -Filter * | Where-Object { $_.mail -like "*@lab*" }    # ❌ mail non chargé → vide
Get-ADUser -Filter "mail -like '*@lab*'" -Properties mail         # ✅

# Utiliser -Properties * en masse
Get-ADUser -Filter * -Properties *    # ⚠️ très lourd sur un gros annuaire
Get-ADUser -Filter * -Properties mail, Department   # ✅ juste le nécessaire
```


## 💡 Exercices

**Guidé :** Liste les utilisateurs activés de l'OU IT avec leur email et leur `Title`, triés par nom, en utilisant `-Filter`, `-SearchBase` et `-Properties`.

**Autonome :** Produis un rapport CSV de la répartition des utilisateurs par service (`Department`), avec le compte par service, trié du plus grand au plus petit.

## ✅ Tu sais maintenant...

- Filtrer **côté serveur** avec `-Filter` (et pourquoi c'est bien plus rapide que `Where-Object`)
- Restreindre le périmètre avec `-SearchBase` / `-SearchScope`
- Charger les bons attributs avec `-Properties` (sans abuser de `*`)
- Construire des rapports AD performants (filtre → périmètre → attributs → projection → export)

## 💬 Questions d'entretien typiques

- **`-Filter` ou `Where-Object` en AD ?** → `-Filter` (côté serveur) chaque fois que possible : le DC ne renvoie que le nécessaire. `Where-Object` seulement pour ce que `-Filter` ne peut pas exprimer.
- **Pourquoi un attribut apparaît-il vide alors qu'il existe ?** → Il n'a pas été chargé ; il faut `-Properties <attribut>`.
- **À quoi sert `-SearchBase` ?** → Limiter la recherche à une OU précise, pour la rapidité et le ciblage.

---
