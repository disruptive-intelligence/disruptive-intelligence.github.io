---
title: Chapitre 38 — Les tiers sur un schéma
source: IT/06 Infrastructure & architecture/Architecture des systèmes d'information.md
note: Architecture des systèmes d'information
up:
- - Architecture des systèmes d'information
  - ../index.md
- - PARTIE VI — Lire une architecture
  - index.md
---

## 38.1 Ce qui n'est pas chez vous et vous concerne

| Type de tiers | Ce qu'il apporte | Ce qu'il vous coûte en maîtrise |
|---|---|---|
| **Service en ligne** | Une fonction sans infrastructure | Aucune visibilité, aucun contrôle de disponibilité |
| **Prestataire d'infogérance** | Des compétences et une astreinte | **Des accès d'administration à votre système** |
| **Partenaire connecté** | Un échange automatisé | Un chemin d'entrée dont vous ne maîtrisez pas l'extrémité |
| **Fournisseur de composants** | Du logiciel intégré à vos produits | Une exposition héritée |
| **Fournisseur d'identité externe** | Une authentification simplifiée | **Une dépendance de disponibilité hors de vos mains** |

## 38.2 Comment on les représente

🖼 **SCHÉMA 38.1 — Les trois façons de dessiner un tiers**

```
  A — LE NUAGE           [ ~~~ service ~~~ ]
      Ce qu'on ne détaille pas. Honnête, et peu informatif.

  B — LA BOÎTE NOIRE     ┌───────────────┐
                         │  fournisseur  │  ← on dessine l'interface,
                         └───────┬───────┘     pas l'intérieur
                                 │
                          protocole, sens,
                          authentification

  C — L'OMISSION         (rien)
      Le cas majoritaire. Le tiers n'est pas dessiné du tout.
```


**Le modèle B est le seul utile.** Il ne prétend pas décrire ce qu'on ne connaît pas, et il documente ce qui compte : **l'interface, le sens du flux, et la nature de l'authentification.**

## 38.3 Les trois questions à poser à tout tiers

```
1. Que peut-il atteindre chez nous ?
   → un flux entrant · un accès d'administration · rien

2. Que pouvons-nous faire s'il tombe ?
   → rien, dégradé, ou fonctionnement autonome

3. Comment s'authentifie-t-il, et qui peut révoquer cet accès ?
   → et surtout : quelqu'un le pourrait-il en urgence, un dimanche ?
```


**La troisième est celle qu'on ne pose jamais.** Un accès de prestataire créé en 2018 fonctionne encore en 2026, et personne ne sait qui a le pouvoir de le couper.

## 38.4 Le cas du prestataire d'infogérance

**L'un des tiers les plus puissants et les moins représentés**, et le §6.6 l'a annoncé.

| Ce qu'il possède | Conséquence |
|---|---|
| Des comptes d'administration sur vos serveurs | Une compromission chez lui devient une compromission chez vous |
| Des postes que vous ne maîtrisez pas | Hors de votre inventaire, hors de votre supervision |
| Un accès distant permanent | Un chemin d'entrée toujours ouvert |
| Une connaissance de votre architecture | Souvent supérieure à la vôtre |

⚠️ **Sur un schéma, il apparaît au mieux comme un nuage à côté du pare-feu.** Sa position réelle est **au cœur de la zone d'administration** — §27. **C'est l'un des écarts les plus importants entre l'architecture dessinée et l'architecture réelle en matière de sécurité.**

⚖️ **CONTRAINTE ET COÛT**

| Résout | Coûte |
|---|---|
| Des compétences et une astreinte sans les recruter | **Des accès privilégiés hors de votre maîtrise** |
| Une capacité 24 heures sur 24 | Une dépendance contractuelle à la sécurité d'un tiers |
| Un coût prévisible | **Une surface d'attaque qui n'apparaît sur aucun schéma** |

🏭 **TROIS TAILLES** — Atelier Martin : un prestataire local, **avec un accès permanent et aucune traçabilité** — le risque le plus élevé de son architecture après le segment industriel. HELIOMED : un infogérant sur le parc bureautique et le support, accès via le rebond. Novaris : plusieurs prestataires, accès nominatifs, sessions enregistrées — **parce que la traçabilité individuelle est une exigence contractuelle de ses clients**.

---
