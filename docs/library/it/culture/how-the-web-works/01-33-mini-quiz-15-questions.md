---
title: 33. Mini-quiz (15 questions)
source: IT/Culture/Fiche_How-The-Web-Works.md
note: How the Web Works
up:
- - How the Web Works
  - index.md
---

1. Quels sont les deux seuls composants **obligatoires** d'une URL ?
2. Le fragment `#section` est-il envoyé au serveur ?
3. Sur quel port et quels protocoles de transport fonctionne le DNS ?
4. Dans quel ordre se fait la résolution DNS (cite les 4 grandes étapes après le cache) ?
5. `8.8.8.8` fournit-il automatiquement un DNS chiffré ?
6. À quoi sert ARP avant l'envoi du paquet ?
7. Décris le handshake TCP en 3 étapes.
8. Quels ports pour HTTP et HTTPS ?
9. Quelles sont les trois garanties apportées par HTTPS ?
10. Dans le handshake TLS, l'asymétrique sert à quoi, le symétrique à quoi ?
11. Un certificat autosigné chiffre-t-il ? Prouve-t-il l'authenticité ?
12. Différence entre **401** et **403** ?
13. Où sont les paramètres en GET ? En POST ?
14. Un cookie est-il stocké côté client ou serveur ? Et la session ?
15. Pourquoi une API autorisant DELETE sans contrôle d'accès est-elle dangereuse ?

<details markdown="1">
<summary>Réponses</summary>

1. Le **scheme** et le **host**.
2. Non, il est traité **côté client**.
3. Port **53**, en **UDP et TCP**.
4. cache → hosts → resolver → **root → TLD → authoritative → réponse IP**.
5. Non : c'est un **résolveur public**, pas chiffré sans **DoH/DoT**.
6. Trouver l'**adresse MAC de la gateway** (routeur) pour sortir du réseau local.
7. **SYN** → **SYN-ACK** → **ACK**.
8. HTTP = **80**, HTTPS = **443**.
9. **Confidentialité**, **intégrité**, **authentification du serveur**.
10. Asymétrique = **établir la confiance et échanger le secret** ; symétrique = **chiffrer rapidement la session**.
11. Oui il **chiffre**, mais il **ne prouve pas** l'authenticité (pas de CA tierce).
12. **401** = authentification requise ; **403** = authentifié mais accès interdit.
13. GET = dans l'**URL** (query string) ; POST = dans le **body**.
14. Le **cookie** est côté client ; la **session** qu'il référence peut être côté serveur.
15. N'importe qui peut **supprimer des données** (DoS / perte de données critiques), surtout avec une faille **IDOR/BOLA**.

</details>
