---
title: Chapitre 14 — Convertir texte et nombres
source: IT/07 Scripting & programmation/Bas niveau/Assembleur.md
note: Assembleur
up:
- - Assembleur
  - ../index.md
- - Partie V — Entrées, sorties et conversions
  - index.md
---

## Le minimum à savoir

### Le problème : `'5'` ≠ `5`

Si l'utilisateur tape `5`, le buffer contient l'**octet 53** (le code ASCII de `'5'`), pas le nombre 5. Tenter de calculer `[buffer] + 1` te donnerait 54 (`'6'`), pas 6.

> **Confusion classique du débutant.** Mémorise : le caractère `'5'` vaut **53** en mémoire. Pour avoir le nombre 5, il faut **soustraire 48** (le code de `'0'`).

### Convertir un caractère en chiffre

```nasm
mov al, '5'          ; al = 0x35 = 53
sub al, '0'          ; al = 53 - 48 = 5
```


Ou de façon équivalente :

```nasm
sub al, 0x30
```


Ces deux écritures sont identiques. La 1ère est plus lisible.

### Convertir un chiffre en caractère

L'opération inverse :

```nasm
mov al, 7            ; al = 7
add al, '0'          ; al = 7 + 48 = 55 = '7'
```


### Vérifier que c'est bien un chiffre

Avant de soustraire `'0'`, il vaut mieux vérifier que c'est entre `'0'` et `'9'`. On verra comment au chapitre 16 (avec `cmp` et les sauts).

### Cas simple : lire et afficher un chiffre + 1

```nasm
; chiffre.asm — Lit un chiffre, ajoute 1, l'affiche

section .data
    prompt   db "Tape un chiffre (0-9) : ", 0
    prompt_l equ $ - prompt - 1

section .bss
    buffer  resb 4

section .text
global _start
_start:
    ; afficher le prompt
    mov rax, 1
    mov rdi, 1
    mov rsi, prompt
    mov rdx, prompt_l
    syscall

    ; lire 2 octets (un chiffre + le \n)
    mov rax, 0
    mov rdi, 0
    mov rsi, buffer
    mov rdx, 2
    syscall

    ; convertir le caractère en nombre
    mov al, [buffer]       ; al = code ASCII du chiffre
    sub al, '0'            ; al = chiffre réel (0-9)
    inc al                 ; al = chiffre + 1
    add al, '0'            ; al = code ASCII du résultat
    mov [buffer], al       ; remplacer le 1er octet du buffer

    ; afficher le résultat (1 octet)
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 1
    syscall

    ; un retour ligne pour faire propre
    mov byte [buffer], 10
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, 1
    syscall

    mov rax, 60
    mov rdi, 0
    syscall
```


Sortie :

```
Tape un chiffre (0-9) : 4
5
```


🎉 **Tu viens de coder une mini-calculatrice à 1 chiffre.**

### Et pour plusieurs chiffres ?

Convertir une chaîne comme `"123"` en l'entier 123 demande **une boucle** : on parcourt chaque chiffre, on accumule. L'algorithme :

```
résultat = 0
pour chaque chiffre c :
    résultat = résultat * 10 + (c - '0')
```


Sans boucle (ch. 17), on ne peut pas encore le coder. On va y revenir.

### Algorithme inverse : nombre → chaîne

C'est encore plus tordu. Pour transformer 123 en `"123"` :

```
si nombre == 0 → afficher '0'
sinon, tant que nombre > 0 :
    chiffre = nombre % 10
    caractère = chiffre + '0'
    stocker dans buffer (à l'envers !)
    nombre = nombre / 10
puis afficher buffer dans l'ordre inverse
```


C'est pourquoi on dit qu'**afficher un nombre en ASM est non trivial**. On en fera un mini-projet de boucles (ch. 17).

## Très utile en pratique

### Code ASCII des chiffres : à connaître par cœur

| Caractère | Décimal | Hexa |
|-----------|---------|------|
| `'0'` | 48 | `0x30` |
| `'1'` | 49 | `0x31` |
| `'2'` | 50 | `0x32` |
| `'9'` | 57 | `0x39` |

Donc :

- Pour **caractère → chiffre** : `sub al, 48` (ou `sub al, '0'`).
- Pour **chiffre → caractère** : `add al, 48` (ou `add al, '0'`).

### Petite astuce mémo : la différence est toujours `0x30`

`'0' = 0x30`, `'1' = 0x31`, … `'9' = 0x39`. La différence entre le chiffre et son ASCII est **toujours 0x30 = 48**.

### Avec d'autres caractères

Même logique pour les lettres :

```nasm
; transformer 'A'..'Z' en 'a'..'z'
sub al, 'A'         ; al = 0..25
add al, 'a'         ; al = 'a'..'z'
; ou plus directement :
add al, 0x20        ; +32 = passe en minuscule
```


## Bonus

### Pourquoi `'0'` vaut 48 et pas 0 ?

Historiquement, ASCII range les caractères affichables après les codes de contrôle (0-31). Les chiffres viennent à `48-57`, les majuscules à `65-90`, les minuscules à `97-122`. La table est conçue pour que :

- Toutes les minuscules diffèrent de leur majuscule de exactement **32**.
- Les chiffres `'0'-'9'` se suivent.

C'est cette ergonomie qui rend les conversions si simples avec `sub` et `add`.

## ❌ Erreur classique

```
Additionner '5' + 3 et croire qu'on obtient '8'
→ '5' + 3 = 53 + 3 = 56 = '8'. OK !
→ Mais '5' + '3' = 53 + 51 = 104 ≠ '8'. Piège classique.

Oublier de convertir avant de faire un calcul
→ "5" en buffer = 53. "5" + 1 = 54 = '6' (heureusement, mais c'est par chance).

Oublier add '0' avant d'afficher un chiffre
→ Tu affiches un caractère de contrôle (invisible) au lieu d'un chiffre.

Croire que read renvoie un entier
→ NON. read renvoie un texte (octets). Toi de convertir.

Confondre la longueur du buffer et le nombre lu
→ Toujours utiliser rax (renvoyé par read) pour la longueur.
```


## Exercices

**Guidé :** Reprends et exécute `chiffre.asm` ci-dessus. Teste avec différents chiffres.

**Autonome :** Modifie le programme pour qu'il **double** le chiffre saisi (au lieu d'ajouter 1). Attention : si tu saisis 5, ça donne 10, qui ne tient plus sur un seul chiffre. **Limite ton test** à des saisies de 0 à 4 pour l'instant.

**Défi :** Écris un programme qui demande **deux** chiffres (en deux saisies successives via `read`) et affiche leur somme (si elle reste < 10).

## 🧩 Mini-projet (chapitres 13-14) — Addition à 1 chiffre

Crée `add_chiffres.asm` qui :

1. Affiche `"Premier chiffre : "`.
2. Lit (read avec rdx=2 pour avoir chiffre + \n).
3. Convertit (sub '0') et stocke dans une variable `a` en `.bss`.
4. Affiche `"Deuxieme chiffre : "`.
5. Lit, convertit, stocke dans `b`.
6. Calcule `a + b` (résultat dans `al`).
7. Reconvertit en ASCII (`add '0'`).
8. Affiche le résultat suivi d'un retour ligne.

> **Limitation :** ne fonctionnera correctement que si la somme est ≤ 9.

## ✅ Tu sais maintenant…

- Que `'5'` ≠ `5` : un caractère est un code ASCII
- Convertir **caractère → chiffre** avec `sub al, '0'`
- Convertir **chiffre → caractère** avec `add al, '0'`
- Lire un chiffre saisi et le manipuler comme un nombre
- Pourquoi convertir un **entier multi-chiffres** demande une boucle
- Que tu sais maintenant écrire des programmes **vraiment interactifs**

---
