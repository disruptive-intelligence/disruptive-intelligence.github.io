---
title: Dossiers
---

# 📚 Dossiers / synthèses

Synthèses transversales produites à partir de plusieurs analyses ou documents.

{% assign dossiers = site.pages | where: "kind", "dossier" | sort: "date" | reverse %}

## Dossiers publiés

{% for item in dossiers %}
- [{{ item.title }}]({{ item.url | relative_url }}) — {{ item.date | date: "%d/%m/%Y" }}
{% endfor %}

---

[← Retour à l’accueil](../)
