---
title: Chapitre 17 — Les bases du réseau Linux
source: IT/01 Linux/Administration Linux.md
note: Administration Linux
up:
- - Administration Linux
  - ../index.md
- - PARTIE 5 — Linux en réseau
  - index.md
---

## Le minimum à savoir

### Le strict nécessaire de TCP/IP

Pas besoin d'être expert réseau pour administrer Linux, mais quelques notions sont indispensables :

- **Adresse IP** : l'adresse numérique d'une machine sur un réseau (ex. `192.168.1.10`). C'est son « numéro de téléphone ».
- **Masque de sous-réseau** : il définit quelles machines sont sur le **même** réseau local que toi.
- **Passerelle (gateway)** : la « porte de sortie » du réseau local vers le reste du monde (souvent ta box ou ton routeur).
- **Port** : sur une même machine, chaque service écoute sur un **port** numéroté (ex. 22 pour SSH, 80 pour le web, 443 pour le web sécurisé). Si l'IP est l'adresse de l'immeuble, le port est le numéro de l'appartement.
- **DNS** : le système qui traduit les noms (`exemple.com`) en adresses IP. C'est l'annuaire d'Internet.

### Voir sa configuration réseau : `ip`

La commande moderne pour tout ce qui touche au réseau est `ip` :

```bash
ip a             # affiche les interfaces et leurs adresses IP (a = address)
ip r             # affiche la table de routage, dont la passerelle (r = route)
```


`ip a` te montre tes **interfaces réseau** (carte filaire, Wi-Fi, interface locale `lo`…) et l'adresse IP de chacune. `ip r` te montre par où sortent tes paquets (notamment la ligne `default via ...` qui désigne ta passerelle).

### Tester la connectivité : `ping`

`ping` envoie de petits paquets à une machine pour vérifier qu'elle répond et mesurer le temps d'aller-retour :

```bash
ping 8.8.8.8             # teste la connectivité vers une IP (Ctrl + C pour arrêter)
ping exemple.com         # teste aussi la résolution DNS (nom → IP)
```


> **Réflexe de diagnostic :** si `ping 8.8.8.8` (une IP) fonctionne mais que `ping exemple.com` (un nom) échoue, ton problème vient probablement du **DNS**, pas de la connexion elle-même. Ce simple test isole déjà la cause.

## Très utile en pratique

### Voir les ports ouverts : `ss` (et le vieux `netstat`)

Quels services écoutent sur ta machine, et donc quelles « portes » sont ouvertes ? La réponse vient de `ss` :

```bash
ss -tulpn        # tous les ports en écoute, avec le programme associé
```


Décortiquons ces options très utilisées : `-t` (TCP), `-u` (UDP), `-l` (uniquement ce qui **écoute**, *listening*), `-p` (le **programme** qui écoute — nécessite souvent `sudo`), `-n` (afficher les **numéros** de port plutôt que les noms).

> **`ss` vs `netstat` :** tu croiseras souvent `netstat` dans d'anciens cours, scripts ou tutoriels. **`ss` est l'outil moderne recommandé** ; `netstat` est ancien et considéré comme déprécié, mais encore présent partout, donc utile à savoir lire. Sur les systèmes récents, `netstat` n'est même plus installé par défaut (il fait partie du paquet `net-tools`). Apprends `ss`, reconnais `netstat`.

> **Très utile en sécurité :** `ss -tulpn` révèle la **surface d'attaque locale** de la machine — chaque port en écoute est une porte potentielle. Côté défense, on vérifie que **seuls les services attendus** écoutent, et on ferme ou désactive le reste (lien avec le durcissement, chapitre 25). Un port inattendu en écoute est un signal à investiguer.

### Interroger le DNS : `dig` et `nslookup`

Pour traduire un nom en adresse IP (ou enquêter sur la configuration DNS d'un domaine) :

```bash
dig exemple.com          # interrogation DNS détaillée (paquet dnsutils)
nslookup exemple.com     # alternative plus simple à lire
```


`dig` n'est pas toujours installé : `sudo apt install dnsutils` (réflexe de la Partie 0).

### Télécharger et tester des services web : `curl` et `wget`

Deux outils pour parler à des serveurs web depuis le terminal :

```bash
curl https://exemple.com           # récupère et affiche le contenu d'une URL
curl -I https://exemple.com        # -I : seulement les en-têtes (code de réponse, serveur…)
wget https://exemple.com/fichier   # télécharge un fichier et l'enregistre sur le disque
```


> **À retenir :** `curl` sert surtout à **interroger/tester** un service (et afficher la réponse) ; `wget` sert surtout à **télécharger** un fichier. `curl -I` est un réflexe pratique pour vérifier rapidement qu'un site répond et avec quel code (200 = OK, 404 = absent, 500 = erreur serveur…).

### Suivre le chemin réseau : `traceroute` (notion)

`traceroute exemple.com` montre les étapes (les routeurs) par lesquelles passent tes paquets pour atteindre une destination. Utile pour localiser **où** une connexion se bloque. Outil à installer au besoin (`sudo apt install traceroute`), bon à connaître de nom.

## ❌ Erreur classique

```bash
# Utiliser ifconfig/netstat par habitude alors qu'ils ne sont plus là
ifconfig                 # ❌ souvent absent sur les systèmes récents
ip a                     # ✅ l'équivalent moderne
netstat -tulpn           # ❌ déprécié / absent par défaut
ss -tulpn                # ✅ l'équivalent moderne

# Oublier sudo pour voir le programme derrière un port
ss -tulpn                # le champ "programme" peut rester vide
sudo ss -tulpn           # ✅ pour voir quel processus écoute

# Conclure trop vite à une panne réseau
ping exemple.com         # échoue...
ping 8.8.8.8             # ✅ teste d'abord par IP : si ça marche, c'est le DNS

# Confondre curl et wget
wget https://api...      # télécharge un fichier au lieu d'afficher la réponse
curl https://api...      # ✅ affiche la réponse dans le terminal
```


## Exercices

**Guidé :** Affiche tes interfaces réseau avec `ip a` et repère ton adresse IP locale (souvent en `192.168.x.x` ou `10.x.x.x`). Affiche ensuite ta passerelle avec `ip r` (la ligne `default via ...`). Enfin, vérifie ta connectivité avec `ping -c 4 8.8.8.8` (le `-c 4` limite à 4 paquets).

**Autonome :** Liste les ports en écoute sur ta machine avec `sudo ss -tulpn`. Pour chaque ligne, identifie le port et, si possible, le programme. Le port 22 (SSH) est-il ouvert ? Reconnais-tu tous les services qui écoutent, ou certains te surprennent-ils ?

**Défi (orientation sécurité) :** Dresse l'inventaire réseau de ta machine comme le ferait un analyste. Enregistre dans un fichier (avec `tee`, chapitre 7) la sortie de `sudo ss -tulpn`. Pour chaque port en écoute, demande-toi : ce service doit-il **vraiment** tourner ? Doit-il être accessible depuis l'extérieur, ou seulement en local ? Cette réflexion est exactement celle du durcissement : **fermer ce qui n'a pas besoin d'être ouvert**.

## ✅ Tu sais maintenant…

- Les notions clés : **IP, masque, passerelle, port, DNS**
- Voir ta config réseau avec `ip a` (adresses) et `ip r` (routage/passerelle)
- Tester la connectivité avec `ping`, et isoler un problème **DNS** vs **réseau**
- Lister les ports en écoute avec **`ss -tulpn`** (la surface d'attaque locale)
- Que `ss` est l'outil **moderne** et `netstat` l'ancien **déprécié** (mais à savoir lire)
- Interroger le DNS (`dig`, `nslookup`) et tester un service web (`curl`, `curl -I`, `wget`)
- Que `traceroute` montre le chemin réseau vers une destination

---
