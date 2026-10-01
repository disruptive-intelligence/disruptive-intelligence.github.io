---
title: Annexe E — Matrice de décision cloud vs on-premise vs hybride
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Annexes
  - index.md
---

|Critère                                 |Cloud (API)                                   |On-premise                   |Hybride                                    |
|----------------------------------------|----------------------------------------------|-----------------------------|-------------------------------------------|
|**Données sensibles (santé, financier)**|⚠️ DPA obligatoire, transfert hors UE à évaluer|✅ Données restent dans le SI |✅ Données sensibles on-prem, reste en cloud|
|**Réglementation HDS**                  |❌ Peu de fournisseurs LLM certifiés HDS       |✅ Infrastructure certifiable |✅ Séparation par criticité                 |
|**Coût initial**                        |✅ Faible (pay-per-use)                        |❌ Élevé (GPU, infrastructure)|⚠️ Modéré                                   |
|**Coût récurrent**                      |⚠️ Variable, peut exploser                     |✅ Prévisible (amortissement) |⚠️ Double gestion                           |
|**Performance / qualité**               |✅ Meilleurs modèles disponibles               |⚠️ Modèles plus petits        |✅ Best of both                             |
|**Contrôle**                            |❌ Dépendance fournisseur                      |✅ Contrôle total             |⚠️ Complexité accrue                        |
|**Maintenance**                         |✅ Gérée par le fournisseur                    |❌ Responsabilité interne     |⚠️ Mixte                                    |
|**Latence**                             |⚠️ Variable (réseau)                           |✅ Prévisible (locale)        |⚠️ Variable selon le composant              |
|**Disponibilité**                       |⚠️ Dépendance fournisseur                      |✅ Maîtrisée                  |⚠️ Points de défaillance multiples          |
|**Compétences requises**                |✅ Faibles (API)                               |❌ ML Ops, GPU management     |⚠️ Les deux                                 |

**Recommandation NovaSanté :** on-premise pour l’assistant RAG (données HDS) et le module fraude, cloud possible pour des cas d’usage à données non sensibles (génération de contenu marketing, assistance à la rédaction sans données personnelles).

-----
