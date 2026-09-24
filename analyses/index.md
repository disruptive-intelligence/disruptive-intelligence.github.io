---
title: Analyses
---

# Analyses

Analyses ponctuelles de rapports, articles, publications et documents.

{% assign analyses = site.pages | where: "kind", "analysis" | sort: "date" | reverse %}

## Analyses publiées

<div class="analysis-archive">
{% include analysis-list.html items=analyses limit=analyses.size %}
</div>

---

[← Retour à l’accueil]({{ '/' | relative_url }})
