---
title: Chapitre 51 — GEOINT assisté par IA
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE VII — IMINT, GEOINT et transport
  - index.md
---

## 51.1 La rupture 2024-2026

L'**IA appliquée à la géolocalisation** a connu une rupture majeure en 2024-2026. Des outils comme **GeoSpy** (et son successeur **GeoSeer**) ont démontré la capacité d'agents IA à géolocaliser des photos à partir d'indices visuels avec une précision impressionnante — parfois meilleure qu'un analyste humain en temps record.

Cette rupture transforme la pratique GEOINT. L'analyste 2026 ne fait plus de géolocalisation purement manuelle : il **collabore avec des agents IA** spécialisés.

## 51.2 GeoSpy et GeoSeer

**GeoSpy** (geospy.ai). Premier outil grand public, lancé en 2023, devenu très populaire.

**Capacités.**

- Upload de photo, retour de géolocalisation suggérée.
- Estimation de probabilité par région.
- Multi-suggestions hierarchized.

**Forces.**

- Rapide (résultat en secondes).
- Souvent précis sur monuments / scènes distinctives.
- Bon sur grandes villes occidentales.

**Limites.**

- Hallucinations possibles.
- Moins bon sur zones rurales / pays sous-représentés dans l'entraînement.
- Précision variable.

**GeoSeer**, **PicArta**, autres : alternatives concurrentes.

## 51.3 Architecture multi-agents

Les outils 2026 utilisent souvent une **architecture multi-agents** :

- **Agent vision** : décrit l'image.
- **Agent géographique** : émet hypothèses régionales.
- **Agent cross-vérificateur** : confronte aux bases cartographiques.
- **Agent synthèse** : produit suggestion finale + confiance.

Cette architecture permet une **traçabilité** partielle : on peut voir quelles hypothèses ont été émises et lesquelles ont été éliminées.

## 51.4 LLMs multimodaux : usage géolocalisation

**GPT-4V** (OpenAI), **Claude** (Anthropic), **Gemini** (Google). Tous peuvent recevoir une image et produire description + suggestions de localisation.

**Méthode.** Prompt structuré demandant : description méthodique, hypothèses de localisation, raisonnement.

**Exemple de prompt.**

```
Tu es un expert OSINT spécialisé en géolocalisation. Analyse cette image :
1. Inventorie les éléments visuels suggérant une localisation
2. Émets 3 hypothèses de localisation avec probabilité
3. Justifie ton raisonnement
4. Indique les vérifications à mener pour confirmer
```


## 51.5 Limites et risques

**Hallucinations.** Un LLM peut inventer une localisation plausible mais fausse.

**Biais d'entraînement.** Surreprésentation de certaines régions.

**Confidentialité.** Upload d'image vers cloud (OpenAI, Anthropic, Google) = fuite d'intent OSINT.

**Sur-confiance.** L'analyste qui accepte la suggestion IA sans vérification produit du bruit.

## 51.6 Workflow GEOINT augmenté

Le workflow recommandé 2026 :

1. **Lecture méthodique humaine** (Ch.48).
2. **Suggestion IA** (GeoSpy / LLM multimodal) — comme **hypothèse de départ**.
3. **Vérification manuelle** sur Google Maps / Street View / Mapillary.
4. **Triangulation** classique.
5. **Confirmation** ou rejet.

L'IA accélère ; elle ne remplace pas.

## 51.7 OPSEC : upload d'images suspectes

**Si l'image est sensible**, ne pas l'uploader vers services cloud publics :

- Utiliser LLMs locaux (Ollama avec modèles multimodaux : LLaVA, Qwen-VL).
- GeoSpy a une version self-hosted limited.
- Préférer méthode manuelle pour très sensible.

## 51.8 Reconnaissance de scène par IA

Au-delà de la géolocalisation, les LLMs multimodaux excellent à :

- **Identifier monuments** (Eiffel Tower, Sagrada Familia).
- **Identifier types d'architecture régionale**.
- **Reconnaître activités** (manifestation, marché).
- **Décrire** finement.

Tous à utiliser comme suggestions, à valider.

## 51.9 Cas d'usage avancés

**Investigation de conflits.** Géolocalisation rapide de centaines de vidéos virales.

**Réfugiés et migrations.** Documentation de mouvements.

**Sites industriels.** Identification du contexte géographique d'une photo intérieure.

**Investigation criminelle.** Localisation d'images de crimes (kidnapping, traite humaine).

## 51.10 Synthèse 2026

| Capacité | Outils | Niveau de confiance |
|---|---|---|
| Géoloc rapide tentative | GeoSpy | Hypothèse, à vérifier |
| Description fine image | GPT-4V / Claude / Gemini | À vérifier |
| Identification monuments | Google Lens + LLM | Souvent fiable |
| Géoloc rurale précise | Méthode manuelle Bellingcat | Standard |
| Confirmation | Google Maps / Street View / OSM | Fiable |

> **Principe 2026.** L'IA est devenue un copilote GEOINT puissant. Mais le pilote reste l'analyste humain qui valide chaque suggestion contre des sources cartographiques canoniques.

-----
