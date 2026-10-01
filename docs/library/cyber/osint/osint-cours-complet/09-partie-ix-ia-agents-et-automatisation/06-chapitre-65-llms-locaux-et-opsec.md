---
title: Chapitre 65 — LLMs locaux et OPSEC
source: Cyber/02 OSINT/OSINT — cours complet.md
note: OSINT — cours complet
up:
- - OSINT — cours complet
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 65.1 Pourquoi LLMs locaux

Les LLMs commerciaux (ChatGPT, Claude, Gemini) sont puissants mais posent des **risques OPSEC** :

- Prompts conservés par fournisseur.
- Apprentissage possible (variable selon politiques).
- Profilage du compte.
- Réquisitions judiciaires dans pays du fournisseur.
- Fuite d'intent.

**Pour les enquêtes sensibles**, les **LLMs locaux** offrent une alternative : pas de fuite, pas de cloud, données sous contrôle souverain.

## 65.2 État de l'art LLMs locaux 2026

L'écart entre LLMs commerciaux frontier et LLMs locaux open source s'est **réduit** entre 2023 et 2026. Modèles open source actuels :

- **Llama 3.3 / Llama 4** (Meta) : référence open source.
- **Mistral Large** (Mistral) : européen.
- **Qwen 2.5 / Qwen 3** (Alibaba) : multilingue fort.
- **DeepSeek R1** : raisonnement.
- **Gemma 2 / 3** (Google) : compact, multilingue.
- **Phi-4** (Microsoft) : compact mais performant.

**Performance.** Pour tâches OSINT standard (extraction, résumé, traduction, classification), LLMs locaux performants ~Claude / GPT-4 niveau de 2023. Pour raisonnement complexe, commerciaux restent supérieurs.

**Suffisant** pour la plupart des cas OSINT.

## 65.3 Outils de déploiement local

**Ollama** (ollama.com). Standard de fait. Installation simple, API locale, multi-modèles.

```bash
# Installation
curl https://ollama.ai/install.sh | sh

# Lancer Llama 3.3
ollama run llama3.3

# Lancer Mistral
ollama run mistral
```


**LM Studio**. Interface graphique. Pour utilisateurs moins techniques.

**vLLM** (auto-hébergé). Pour deployment production.

**Llama.cpp**. Très efficace, low-level.

**GPT4All**. Multi-OS, simple.

## 65.4 Matériel requis

**Minimum.** PC moderne avec GPU 8-12 Go VRAM. Modèles 7B-13B fonctionnent.

**Confortable.** GPU 24-48 Go VRAM. Modèles 30B-70B en quantization.

**Workstation OSINT type 2026.**

- CPU récent (Intel i7 / Ryzen 7).
- 32-64 Go RAM.
- GPU NVIDIA RTX 4090 (24 Go VRAM) ou équivalent.
- SSD 1 To.
- Coût : 2500-4000 €.

## 65.5 Modèles recommandés selon usage

**Extraction d'entités, classification, traduction.** Llama 3.3 70B (quantization Q4), ou Mistral Large.

**Multilingue.** Qwen 2.5 (excellence chinois, asiatique).

**Code.** DeepSeek Coder ou Qwen Coder.

**Compact (machine modeste).** Phi-4, Gemma 2 9B.

**Multimodal.** LLaVA, Qwen-VL.

## 65.6 Workflow local

**Mise en place.**

1. Installation Ollama.
2. Téléchargement des modèles utilisés.
3. Test des performances.
4. Intégration dans pipeline (Jupyter, scripts Python).

**Usage pour enquête sensible.**

1. Toutes les requêtes vont au LLM local.
2. Aucune donnée ne quitte la machine.
3. Logs locaux (Ollama tient un historique consultable).
4. Modèles peuvent être supprimés en fin d'enquête (purge).

## 65.7 API locale

Ollama expose une API HTTP locale :

```python
import requests

response = requests.post('http://localhost:11434/api/generate', 
    json={
        "model": "llama3.3",
        "prompt": "Extrais les entités de ce texte : ...",
        "stream": False
    })
print(response.json()['response'])
```


Intégration possible avec **LangChain**, **LlamaIndex** pour RAG local.

## 65.8 Quand basculer commercial vs local

| Cas | Commercial | Local |
|---|---|---|
| Enquête publique non sensible | ✓ | (option) |
| Enquête corporate confidentielle | (option) | **Préférable** |
| Cible avec ressources surveillance | (déconseillé) | **Obligatoire** |
| Cible étatique | (interdit) | **Obligatoire** |
| Cible avec compétences cyber | (déconseillé) | **Préférable** |
| Tâche multimodale complexe | (souvent supérieur) | (option si modèle dispo) |
| Tâche raisonnement complexe | (souvent supérieur) | (limite) |

## 65.9 Limites LLMs locaux

**Performance.** Sur tâches très complexes, écart avec commerciaux frontier.

**Maintenance.** Mise à jour des modèles, hardware.

**Pas de tools intégrés.** Pas de web search natif (à coupler avec autres outils).

**Coût hardware.** Investissement initial.

## 65.10 Synthèse

LLMs locaux 2026 sont **prêts pour usage professionnel** sur la plupart des tâches OSINT standard. Pour enquêtes sensibles, c'est le **standard**. Le coût hardware se rentabilise rapidement face aux risques OPSEC des solutions cloud.

> **MIRAGE — Note OPSEC IA.** L'enquête MIRAGE utilise principalement LLMs locaux (Ollama avec Llama 3.3 70B). Tâches sensibles (extraction d'entités sur documents, traduction de mémos chypriotes, analyse de patterns) : tout en local. Tâches non-sensibles (génération de dorks publics, reformulation) : commercial OK. Cette discipline OPSEC protège la confidentialité du dossier face à toute compromission cloud.

-----
