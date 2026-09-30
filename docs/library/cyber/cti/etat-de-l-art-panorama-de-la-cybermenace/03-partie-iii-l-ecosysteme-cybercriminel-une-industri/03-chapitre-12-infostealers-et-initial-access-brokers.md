---
title: Chapitre 12 — Infostealers et Initial Access Brokers
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - 'PARTIE III — L''écosystème cybercriminel : une industrie de la menace'
  - index.md
---

les fondations de la chaîne d'attaque

## 12.1 — Les infostealers comme pilier de l'écosystème

Microsoft identifie dans son MDDR 2025 l'une des tendances les plus préoccupantes de la période : « la montée rapide de l'utilisation des infostealers ». Traditionnellement considérés comme des outils de post-exploitation, des familles comme Lumma Stealer, RedLine, Vidar et Raccoon Stealer sont désormais déployés comme **payloads de première étape** — le premier malware exécuté sur un poste compromis.

Ce changement est structurant pour l'écosystème. Les infostealers permettent une « division du travail à travers l'écosystème cybercriminel : les opérateurs initiaux déploient le malware, les courtiers en accès monétisent les données volées, et des utilisateurs comme les groupes ransomware les utilisent pour prendre pied dans les environnements d'entreprise ». En conséquence, « les infections par infostealer représentent plus que de simples compromissions locales — elles posent un risque stratégique d'intrusions d'entreprise plus larges ».

## 12.2 — Mécanismes et vecteurs de distribution

Les infostealers sont typiquement distribués via **malvertising** (publicités malveillantes sur les moteurs de recherche), **SEO poisoning** (sites malveillants positionnés en haut des résultats de recherche), **logiciels craqués** (installateurs piégés de logiciels populaires), et techniques de tromperie comme **ClickFix** (fenêtres pop-up imitant des erreurs système qui incitent l'utilisateur à exécuter un script malveillant).

Les données collectées incluent : les credentials stockées dans les navigateurs (mots de passe, auto-complete), les cookies de session (permettant de contourner le MFA en réutilisant une session déjà authentifiée), les tokens d'authentification, les données de formulaire, les informations système, et les wallets de cryptomonnaies.

## 12.3 — IAB : passerelle vers le ransomware

Les Initial Access Brokers (IAB) constituent le maillon intermédiaire entre les infostealers et le ransomware. L'ASD documente leur modèle économique : « Les IAB profitent de la vente d'accès aux réseaux de victimes (y compris les credentials). L'accès est vendu sur le dark web, avec des annonces listant un prix demandé et des détails sur la victime, comme le type d'entreprise, le pays d'origine et le chiffre d'affaires. Typiquement, le prix de l'accès est relativement bas, permettant à des cybercriminels qui n'auraient autrement pas pu obtenir un point d'entrée dans un système victime. »

L'Europol note que les IAB « font de plus en plus de publicité pour ces services, ainsi que pour les matières premières qui y sont liées, sur des plateformes criminelles spécialisées utilisées par un ensemble très divers de cybercriminels ». La commoditisation de l'accès initial transforme le ransomware d'une opération technique complexe en une opération essentiellement logistique et financière.

## 12.4 — Opérations de démantèlement et résilience

Les forces de l'ordre ont ciblé l'infrastructure infostealer et IAB. L'opération Magnus (2024) a visé des infostealers. Le démantèlement de LummaC2 en 2025 a temporairement perturbé l'un des infostealers les plus prolifiques. Mais la résilience structurelle de l'écosystème reste élevée : les opérateurs de services démantelés relancent sous un nouveau nom, et les clients migrent vers des alternatives.

## 12.5 — 🔴 Fil rouge : reconstruction de la timeline

> **📌 FIL ROUGE — Épisode 12**
>
> L'analyse forensique de l'incident du prestataire permet à Sophie de reconstituer la timeline complète. L'infection initiale par Lumma Stealer remonte à janvier 2025 — six mois avant l'attaque ransomware. Un employé du prestataire a téléchargé un logiciel craqué contenant Lumma. Le stealer a collecté les credentials VPN et les a exfiltrées vers un serveur C2. En mars, les credentials apparaissent sur un forum underground. En juin, Sophie les repère. En juillet, un affilié Qilin les achète et lance l'attaque.
>
> La leçon clé : la chaîne infostealer → IAB → ransomware peut s'étaler sur des mois. La détection à n'importe quel maillon de la chaîne aurait pu prévenir l'attaque finale. La fenêtre d'intervention existait — elle n'a pas été exploitée parce que personne ne surveillait les forums pour les credentials du prestataire.

---
