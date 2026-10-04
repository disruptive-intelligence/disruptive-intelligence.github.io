---
title: Chapitre 3 — Noyau, mémoire et pilotes
source: IT/02 Windows/Comprendre Windows/Windows en profondeur.md
note: Windows en profondeur
up:
- - Windows en profondeur
  - ../index.md
- - Partie I — Architecture fondamentale
  - index.md
---

## 3.1 Du programme au noyau

Quand un programme lit un fichier, la requête traverse plusieurs couches :

```text
Application → API Win32 (kernel32.dll) → ntdll.dll → appel système
  → ntoskrnl.exe (I/O Manager) → pilote de système de fichiers → pilote de disque
```


`ntdll.dll` est la dernière étape en mode utilisateur : c'est là que beaucoup d'EDR observent les appels (Ch.20).

## 3.2 La mémoire virtuelle

| Notion | À retenir |
|---|---|
| **Espace d'adressage virtuel** | Chaque processus a le sien ; la partie haute (noyau) est partagée et inaccessible au mode utilisateur |
| **Pages** | Unités de 4 Ko, avec des protections (lecture, écriture, exécution) |
| **pagefile.sys** | Pages déplacées sur disque ; peut contenir des fragments de données sensibles |
| **Working set** | Pages du processus présentes en RAM |

En investigation, une zone mémoire à la fois **inscriptible et exécutable** dans un processus légitime est un indice classique de code injecté (Ch.30).

## 3.3 Les pilotes

Un **pilote** (`.sys`) s'exécute en mode noyau, avec un accès total. D'où :

- **signature obligatoire** des pilotes sur les systèmes 64 bits ;
- **HVCI** (*Hypervisor-Protected Code Integrity*, appelé aussi « intégrité de la mémoire ») : l'hyperviseur vérifie le code noyau et bloque les pilotes non conformes, même pour un administrateur ;
- **liste de blocage des pilotes vulnérables** de Microsoft (Ch.20).

Les **pilotes mini-filtres** interceptent les opérations sur les fichiers : c'est ainsi qu'un antivirus analyse un fichier à l'ouverture et qu'un EDR observe l'activité disque.

---
