---
title: "Clore la collecte"
cours:
  - library/cyber/forensic/investigation-numerique-forensic/index.md
  - library/cyber/detection/reponse-a-incident/index.md
---
# Clore la collecte

Sceller ce qui a été collecté pour pouvoir le prouver ensuite.

Les incontournables : `sha256sum` · `date -u`
{ .kw-cs-top }

## Sceller la collecte

### Calculer les empreintes de la collecte

```bash title="Commande"
sha256sum <dossier_collecte>/* > <dossier_collecte>/empreintes-collecte.txt   # empreinte de chaque fichier collecté
```

```bash title="Exemple"
date -u | tee -a 00-debut.txt && sha256sum ./* > empreintes-collecte.txt
```

Pour comprendre : [Réponse à incident](../../../../library/cyber/detection/reponse-a-incident/index.md)
{ .kw-cs-meta }
