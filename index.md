---
title: Intelligence Desk
home: true
---
{% assign veilles = site.pages | where: "kind", "veille" | sort: "date" | reverse %}
{% assign analyses = site.pages | where: "kind", "analysis" | sort: "date" | reverse %}
{% assign dossiers = site.pages | where: "kind", "dossier" | sort: "date" | reverse %}
{% assign latest = veilles | first %}

<div class="front-page">
<div class="desk-intro">
  <p class="eyebrow">La revue · Intelligence Desk</p>
  <h1>Veille & analyse stratégique</h1>
  <p>Veille quotidienne, analyses approfondies et synthèses transversales sur les technologies et leurs implications stratégiques.</p>
</div>

{% if latest %}
<section class="featured" aria-labelledby="latest-title">
  <div class="content-meta"><span>Dernière veille</span><time datetime="{{ latest.date | date: '%Y-%m-%d' }}">{{ latest.date | date: '%d/%m/%Y' }}</time></div>
  <h2 id="latest-title"><a href="{{ latest.url | relative_url }}">{{ latest.title | escape }}</a></h2>
  <p>Les événements retenus, leur contexte et les sources pour approfondir.</p>
  <a class="read-link" href="{{ latest.url | relative_url }}">Lire cette édition <span aria-hidden="true">→</span></a>
</section>
{% endif %}
</div>

<div class="editorial-grid">
<section class="desk-section section-veille" aria-labelledby="veille-title">
  <div class="section-heading"><h2 id="veille-title">Veille quotidienne</h2><a href="{{ '/veille/' | relative_url }}">Toutes les veilles <span aria-hidden="true">→</span></a></div>
  {% include editorial-list.html items=veilles limit=3 label="Veille" %}
</section>

<section class="desk-section section-analyses" aria-labelledby="analyses-title">
  <div class="section-heading"><h2 id="analyses-title">Analyses</h2><a href="{{ '/analyses/' | relative_url }}">Toutes les analyses <span aria-hidden="true">→</span></a></div>
  <p class="section-description">Une lecture approfondie des rapports, articles et publications.</p>
  {% include analysis-list.html items=analyses limit=3 %}
</section>

<section class="desk-section section-dossiers" aria-labelledby="dossiers-title">
  <div class="section-heading"><h2 id="dossiers-title">Dossiers & synthèses</h2><a href="{{ '/dossiers/' | relative_url }}">Tous les dossiers <span aria-hidden="true">→</span></a></div>
  <p class="section-description">Croiser les analyses pour mettre les enjeux en perspective.</p>
  {% include editorial-list.html items=dossiers limit=3 label="Dossier" %}
</section>

</div>
