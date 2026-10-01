---
title: 'Ch.13 — Sécuriser le RAG : sources, RBAC vectoriel et sanitization'
source: Cyber/09 IA & sécurité/IA et sécurité.md
note: IA et sécurité
up:
- - IA et sécurité
  - ../index.md
- - Partie III — Sécuriser le déploiement
  - index.md
---

## 13.1 Contrôle des sources

Seuls les documents validés et provenant de sources approuvées doivent être indexés dans le RAG. Cela suppose un inventaire des sources (SharePoint, Confluence, bases documentaires, tickets résolus), un workflow de validation (qui approuve l’ajout d’une nouvelle source ?), un contrôle d’accès en écriture sur les sources (qui peut modifier un document qui sera indexé ?), et un monitoring des modifications (alerte quand un document source est modifié).

Le RAG poisoning (voir Ch.7) exploite précisément l’absence de ces contrôles. Un prestataire avec un accès en écriture trop large sur le SharePoint peut insérer un document malveillant qui sera indexé sans validation.

## 13.2 RBAC vectoriel en détail

L’implémentation du RBAC vectoriel passe par plusieurs étapes. Lors de l’indexation, chaque chunk de document est enrichi avec les métadonnées de permission : identifiant du propriétaire, groupe(s) autorisé(s), niveau de classification, date de validité. Ces métadonnées sont stockées dans la base vectorielle aux côtés du vecteur d’embedding.

Lors du retrieval, le système injecte automatiquement un filtre de permission dans la requête de recherche vectorielle. En pgvector, cela se traduit par une clause WHERE sur les colonnes de permission qui est évaluée AVANT le calcul de similarité cosinus. En Pinecone ou Weaviate, c’est un filtre de métadonnées natif.

Le point critique est la synchronisation des permissions : quand les droits d’un utilisateur changent dans le système source (changement d’équipe, de rôle, départ), les filtres du RBAC vectoriel doivent être mis à jour. Un mécanisme de synchronisation régulière (ou en temps réel via webhook) entre l’annuaire (AD/LDAP) et les métadonnées de la base vectorielle est nécessaire.

## 13.3 Sanitization des documents

Avant indexation, chaque document doit être scanné pour détecter les injections cachées. Les vecteurs à chercher incluent le texte invisible (police blanche sur fond blanc, texte en taille 0, texte caché par CSS ou formatage), les instructions dans les métadonnées (propriétés du document, commentaires, champs personnalisés), le contenu encodé (base64, hex, Unicode homoglyphe), et les instructions dans les champs de formulaire, les cellules Excel cachées, ou les notes de bas de page.

La sanitization peut être automatisée (extraction de texte brut et comparaison avec le texte visible, détection de patterns d’injection par classificateur ML) mais doit aussi inclure une revue manuelle pour les documents provenant de sources à risque (prestataires, partenaires, sources publiques).

## 13.4 Traçabilité et anti-exfiltration

Chaque réponse de l’assistant RAG doit citer les sources utilisées — les documents (ou chunks) qui ont été injectés dans le contexte pour produire la réponse. Cette traçabilité permet à l’utilisateur de vérifier la cohérence de la réponse, au monitoring de détecter l’utilisation de documents suspects, et à l’audit de retracer l’origine de toute information.

L’anti-exfiltration complète la traçabilité : un filtre de sortie vérifie que la réponse ne contient pas de données que l’utilisateur n’est pas censé voir (même après le filtrage RBAC — défense en profondeur), de PII non pertinentes pour la requête, ou de patterns d’injection (l’attaquant tente d’injecter du code ou des URLs dans la réponse via un document RAG poisoned).

-----
