---
title: VirusTotal
source: Cyber/99_Concepts/VirusTotal.md
---

### VirusTotal — Points d’attention [Stale Results, Reanalyse, Detection Tags]

### Résultats d’analyse anciens

VirusTotal peut afficher un **ancien résultat d’analyse** au lieu de rescanner immédiatement une URL ou un fichier.

Exemple :

```
URL analysée il y a 1 mois
→ tous les moteurs = Clean
```

Problème : le contenu derrière l’URL peut avoir changé depuis.

Scénario possible :

```
1. L’attaquant crée une URL inoffensive
2. Il la soumet à VirusTotal
3. Tous les moteurs la classent Clean
4. Plus tard, il remplace le contenu par du contenu malveillant
5. L’analyste consulte l’ancien résultat → faux sentiment de sécurité
```

Donc :

```
Old analysis ≠ Current state
```

### Reanalyse

Toujours vérifier :

- date du dernier scan ;
- date de dernière analyse ;
- éventuellement date de première soumission.

Si le résultat est ancien ou si le contenu peut avoir changé :

```
Reanalyse
```

→ force VirusTotal à refaire l’analyse avec l’état actuel de la ressource.

Particulièrement important pour :

- URLs ;
- domaines ;
- fichiers téléchargés dynamiquement ;
- infrastructures pouvant changer rapidement.

⚠️ **URL propre hier ≠ URL propre aujourd’hui**

Une URL est un IOC beaucoup plus “volatile” qu’un hash de fichier.

### Hash vs URL

Un hash comme :

```
SHA256
```

identifie précisément le contenu d’un fichier.

Si le fichier change, son hash change.

Une URL, elle, peut rester identique tout en servant un contenu complètement différent :

```
<https://site.com/update.exe>
```

Aujourd’hui :

```
→ programme légitime
```

Demain :

```
→ malware
```

Donc les résultats liés aux URLs doivent être considérés comme plus temporels.

---

### Detection Tags / Verdicts AV

Le nombre de détections ne suffit pas pour décider qu’un fichier est malveillant.

Exemple :

```
10 / 52
```

peut sembler inquiétant, mais il faut regarder **comment les vendors classifient le fichier**.

Exemple de verdicts :

```
Adware
PUA
PUP
Riskware
Trojan
Downloader
Ransomware
```

Ils n’ont pas tous la même gravité.

### PUA / PUP / Adware

Des logiciels légitimes peuvent être détectés car ils contiennent :

- publicité ;
- bundle avec d’autres logiciels ;
- comportements intrusifs ;
- fonctionnalités jugées indésirables.

Termes fréquents :

```
PUA = Potentially Unwanted Application
PUP = Potentially Unwanted Program
Adware = logiciel affichant de la publicité
Riskware = logiciel légitime pouvant être détourné
```

Exemple du cours : un installateur WinRAR légitime peut être signalé par certains moteurs, notamment à cause de composants/comportements associés à de l’adware ou des logiciels potentiellement indésirables.

Donc :

```
10 détections "Adware/PUA"
≠
10 détections "Trojan/Ransomware"
```

### Interprétation correcte d’un score

Ne pas faire :

```
20/60 → Malware
0/60  → Safe
```

Faire plutôt :

```
Ratio de détection
        +
Type des verdicts
        +
Behavior
        +
Relations
        +
History
        +
Contexte
```

Exemple :

```
3/60 détections
+
PowerShell suspect
+
connexion C2
+
persistance registre
```

→ beaucoup plus inquiétant qu’un simple `3/60`.

À l’inverse :

```
15/60
+
uniquement PUA/Adware
+
éditeur légitime
+
signature valide
```

→ peut être un logiciel légitime mais potentiellement indésirable.

---

### Faux positifs

Un **false positive** correspond à un élément légitime détecté comme malveillant.

Peut arriver avec :

- outils administratifs ;
- outils pentest ;
- installers ;
- scripts PowerShell ;
- outils de récupération de mots de passe ;
- logiciels utilisant des techniques similaires aux malwares.

Exemples classiques :

```
PsExec
Mimikatz
Nmap
PowerShell scripts
Remote administration tools
```

Certains sont légitimes mais peuvent aussi être utilisés offensivement.

→ Toujours replacer la détection dans son **contexte d’utilisation**.

---

### Points à retenir

- Toujours vérifier **la date de l’analyse VirusTotal**.
- Pour une URL, ancien résultat `Clean` ≠ URL actuellement sûre.
- Utiliser `Reanalyse` si le résultat est ancien.
- Ne jamais juger un fichier uniquement sur son **detection ratio**.
- Regarder les labels donnés par les AV : `Adware`, `PUA`, `Trojan`, `Ransomware`, etc.
- Plusieurs détections peuvent être des faux positifs.
- `0 detection` ne garantit pas non plus qu’un fichier soit sain.
- Toujours corréler VirusTotal avec le **contexte + Behavior + Relations + History**.
