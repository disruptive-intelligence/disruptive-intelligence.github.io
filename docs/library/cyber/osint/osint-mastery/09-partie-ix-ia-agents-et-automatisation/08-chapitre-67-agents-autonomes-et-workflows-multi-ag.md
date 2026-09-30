---
title: Chapitre 67 — Agents autonomes et workflows multi-agents
source: Cyber/02_OSINT/20260516_OSINT_Mastery_vFULL.md
note: OSINT Mastery
up:
- - OSINT Mastery
  - ../index.md
- - PARTIE IX — IA, agents et automatisation
  - index.md
---

## 67.1 Agentic AI : la rupture 2024-2026

Les **agents autonomes** sont des LLMs équipés d'**outils** (web search, calculatrice, code execution, bases de données, autres LLMs). Ils peuvent **planifier**, **exécuter**, **boucler** sur des tâches complexes.

Entre 2023 et 2026, l'agentic AI est passée du prototype à la maturité opérationnelle. Pour l'OSINT, c'est une révolution silencieuse.

## 67.2 Architecture agent

**Composantes.**

- **LLM core** : raisonne, planifie.
- **Tools** : capacités externes (web search, scraping, APIs, code).
- **Memory** : court terme (contexte conversation) et long terme (persistant).
- **Planner** : décompose les objectifs en sous-tâches.
- **Executor** : exécute les sous-tâches.
- **Validator** : vérifie les sorties.

**Frameworks.**

- **LangChain Agents** : standard.
- **AutoGPT, BabyAGI** : pionniers.
- **OpenAI Assistants API**.
- **Anthropic Claude tool use**.
- **CrewAI** : multi-agents orchestrés.
- **AutoGen** (Microsoft) : multi-agents conversationnels.

## 67.3 Cas d'usage OSINT

**Monitoring continu.** Agent surveille les mentions d'une entité sur réseaux sociaux et alertes en cas de pic.

**Profilage automatique de social graphs.** Agent identifie les comptes liés, extrait métadonnées, génère rapport.

**Géolocalisation multi-hypothèses.** Plusieurs agents proposent hypothèses, validateur cross-check, synthèse.

**Investigation préliminaire.** Agent reçoit nom d'une entité, conduit première investigation autonome, livre fiche entité de base.

**Veille concurrence / risque.** Agent monitore X entités, détecte changements significatifs, alerte.

## 67.4 Outils commerciaux 2026

**Bitsight, RiskIQ, SecurityScorecard.** ASM (Attack Surface Management) avec composantes agentiques.

**Fivecast** (Australie) : suite OSINT institutionnelle avec ONYX/LUNEX/MATRIX, agentic.

**Babel Street** : multi-source intelligence, AI-driven.

**ShadowDragon** : OSINT enterprise.

**Brandwatch, Talkwalker, Meltwater** : SOCMINT agentic.

Ces outils sont **chers** (10-200 k€/an) mais structurent l'OSINT institutionnelle.

## 67.5 Construire un agent OSINT

**Exemple simple : agent enrichissement entité.**

```python
from langchain_anthropic import ChatAnthropic
from langchain.agents import Tool, initialize_agent

llm = ChatAnthropic(model="claude-opus-4-7")

tools = [
    Tool(name="web_search", func=lambda q: search_web(q), description="..."),
    Tool(name="whois_lookup", func=lambda d: whois(d), description="..."),
    Tool(name="email_check", func=lambda e: holehe(e), description="..."),
    Tool(name="username_search", func=lambda u: sherlock(u), description="..."),
]

agent = initialize_agent(tools, llm, agent_type="react")
agent.run("Enrichir l'entité Marc Delaunay, DAF TechnoVert SAS.")
```


L'agent va décider quels outils utiliser dans quel ordre, exécuter, synthétiser.

## 67.6 Multi-agents orchestrés

Pour tâches complexes, plusieurs agents collaborent.

**Pattern type pour OSINT.**

- **Agent Collecteur** : exécute requêtes, captures.
- **Agent Vérificateur** : valide source, authenticité.
- **Agent Analyste** : corrèle, formule hypothèses.
- **Agent Rédacteur** : produit fiche, rapport.
- **Agent Superviseur** : orchestre, valide.

**Bénéfice.** Spécialisation, parallélisation, vérification croisée.

## 67.7 Knowledge graphs comme mémoire d'agent

Couplage **agent + knowledge graph local** = mémoire structurée persistante.

L'agent enrichit le graphe à chaque investigation. Le graphe devient une **mémoire institutionnelle** (avec déontologie : pas de mélange entre enquêtes selon mandats).

## 67.8 Validation layer

**Tout agent doit avoir un validation layer.**

**Validations typiques.**

- Sortie respecte format attendu (schéma JSON).
- Sources citées sont vérifiables.
- Cotation Admiralty cohérente.
- Pas d'hallucination détectable (cross-check).
- Pas de violation OPSEC / déontologique.

**Pour l'analyste.** Always-on validation by humain pour décisions critiques.

## 67.9 Auditabilité et accountability

Un agent qui agit en autonomie pose des questions d'**auditabilité** : qui est responsable des actions ? Comment retracer ?

**Pratiques.**

- Logs détaillés (chaque appel d'outil, chaque sortie LLM).
- Versioning des agents.
- Validation humaine pour actions à enjeu.
- Audit régulier des sorties.
- Documentation dans rapports : « l'investigation a mobilisé un agent autonome X.Y, configuré comme suit... ».

## 67.10 Limites et risques

**Boucles infinies.** L'agent boucle sur une tâche sans progresser.

**Coût d'exécution.** Agents agressifs consomment beaucoup de tokens / API calls.

**Hallucinations en chaîne.** Une hallucination précoce contamine toute la chaîne.

**Détection adverse.** Une cible peut détecter le pattern d'agent et réagir (counter-OSINT).

**Fuite d'intent.** Logs cloud, prompts révélateurs.

**Auditabilité limitée.** Plus l'agent est complexe, moins on suit son raisonnement.

## 67.11 Synthèse 2026

Les agents autonomes sont devenus **outils standards** de l'OSINT 2026 institutionnel. Pour l'analyste indépendant ou en cabinet moyen :

- **Outils commerciaux** (Bitsight, Fivecast) si budget.
- **Agents custom** (LangChain, CrewAI) si compétences techniques.
- **Workflows manuels assistés** sinon (LLM en complément, sans full autonomy).

**Discipline 2026.** L'agent doit servir l'enquête, pas la remplacer. La validation humaine reste centrale.

-----
