# ⚛️ Disruptive Intelligence

Veille quotidienne consacrée à la technologie, aux technologies émergentes,
à la cybersécurité et aux enjeux géopolitiques et économiques.

---

## ☕ Dernière édition

### 12 septembre 2026

[Lire le Morning Intelligence Brief du 12 septembre 2026](./veille/2026/09/20260912_morning-intelligence-brief.html)

---

## 🗂️ Veille quotidienne

Dernières éditions :

- [12 septembre 2026](./veille/2026/09/20260912_morning-intelligence-brief.html)
- [11 septembre 2026](./veille/2026/09/20260911_morning-intelligence-brief.html)
- [10 septembre 2026](./veille/2026/09/20260910_morning-intelligence-brief.html)

[Consulter toutes les archives →](./veille/)

---

## 📰 Analyses

Analyses approfondies d’articles, rapports et publications.

{% assign analyses = site.pages | where: "kind", "analysis" | sort: "date" | reverse %}

{% for item in analyses limit:3 %}
- [{{ item.title }}]({{ item.url | relative_url }}) — {{ item.date | date: "%d/%m/%Y" }}
{% endfor %}

[Consulter toutes les analyses →](./analyses/)

---

## 📚 Dossiers / synthèses

Synthèses transversales produites à partir de plusieurs analyses.

{% assign dossiers = site.pages | where: "kind", "dossier" | sort: "date" | reverse %}

{% for item in dossiers limit:3 %}
- [{{ item.title }}]({{ item.url | relative_url }}) — {{ item.date | date: "%d/%m/%Y" }}
{% endfor %}

[Consulter tous les dossiers →](./dossiers/)
