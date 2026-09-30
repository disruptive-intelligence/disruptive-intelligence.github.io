---
title: 3. Focus LSASS
source: IT/02_Windows/Fiche_Windows.md
note: Fiche Windows
up:
- - Fiche Windows
  - index.md
---

## 3.1 Définition

`lsass.exe` signifie **Local Security Authority Subsystem Service**.

C’est un processus critique de Windows chargé d’appliquer la politique de sécurité locale.

Il intervient notamment dans :

- l’authentification des utilisateurs ;
    
- la vérification des identifiants ;
    
- la création ou la gestion des access tokens ;
    
- les changements de mots de passe ;
    
- la journalisation des événements de connexion/déconnexion ;
    
- la gestion de certains secrets d’authentification.
    

---

## 3.2 LSASS et authentification

Quand un utilisateur se connecte :

1. l’utilisateur saisit ses identifiants ;
    
2. Windows transmet la demande au sous-système de sécurité ;
    
3. LSASS vérifie l’identité ;
    
4. si l’authentification réussit, Windows crée un access token ;
    
5. ce token est attaché aux processus de l’utilisateur.
    

Schéma simplifié :

```text
Login user
   ↓
LSASS vérifie l’identité
   ↓
Création d’un access token
   ↓
Lancement de la session utilisateur
   ↓
Les processus héritent du token
```


---

## 3.3 Pourquoi LSASS est une cible critique ?

LSASS peut contenir en mémoire des informations sensibles liées à l’authentification.

Selon la version de Windows, la configuration et les protections activées, on peut y trouver :

- hashes NTLM ;
    
- tickets Kerberos ;
    
- secrets liés au SSO ;
    
- informations de session ;
    
- parfois mots de passe en clair sur anciens systèmes ou configurations faibles.
    

C’est pourquoi LSASS est une cible majeure pour le vol d’identifiants.

---

## 3.4 Logs associés

Les événements liés aux connexions sont journalisés dans le journal **Security** de Windows.

|Event ID|Signification|
|---|---|
|4624|Connexion réussie.|
|4625|Échec de connexion.|
|4634|Déconnexion.|
|4648|Connexion avec identifiants explicites.|
|4672|Privilèges spéciaux attribués à une nouvelle connexion.|
|4688|Création de processus, si l’audit est activé.|

---

## 3.5 Protections autour de LSASS

Protections utiles :

- **Credential Guard** : isole certains secrets d’authentification via Virtualization-Based Security.
    
- **LSA Protection / RunAsPPL** : limite l’accès non autorisé à LSASS.
    
- **Defender / EDR** : surveille les tentatives de dump ou d’accès suspect à LSASS.
    
- **Réduction des privilèges admin** : moins d’utilisateurs capables d’interagir avec LSASS.
    
- **Désactivation de WDigest** sur anciens systèmes.
    

Commandes utiles :

```powershell
Get-Process lsass
Get-Process lsass | Format-List *
```


---
