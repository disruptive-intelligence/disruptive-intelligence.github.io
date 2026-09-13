---
title: Analyses
---

# Analyses

Analyses ponctuelles de rapports, articles, publications et documents.

{% assign analyses = site.pages | where: "kind", "analysis" | sort: "date" | reverse %}

## Analyses publiées

{% for item in analyses %}
- [{{ item.title }}]({{ item.url | relative_url }}) — {{ item.date | date: "%d/%m/%Y" }}
{% endfor %}

---

[← Retour à l’accueil](../)
