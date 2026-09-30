---
title: Chapitre 36 — Maison connectée et objets du quotidien
source: Cyber/Cybersecurite_du_Quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie VII — Maison connectée, famille ET frontière pro/perso
  - index.md
---

## 36.1 La box Internet : la porte d'entrée du foyer

Changer le mot de passe Wi-Fi par défaut (le mot de passe imprimé sur l'étiquette sous la box est accessible à quiconque a eu un accès physique — technicien, voisin, visiteur, ancien locataire), activer le WPA3 si disponible (WPA2 minimum — ne JAMAIS utiliser WEP ou un réseau ouvert), désactiver le WPS (Wi-Fi Protected Setup — vulnérable au brute force), et mettre à jour le firmware de la box (les mises à jour sont souvent automatiques chez les FAI mais pas toujours).

L'**interface d'administration** de la box (généralement accessible via 192.168.1.1 ou freebox.fr / mafreebox.freebox.fr / livebox.fr) a son propre mot de passe, distinct du Wi-Fi. Beaucoup de gens ne l'ont jamais changé. Or, depuis cette interface, on peut modifier le DNS (rediriger tout le trafic du foyer vers des serveurs malveillants), ouvrir des ports vers Internet, et voir les appareils connectés. Mot de passe à changer dès l'installation.

## 36.2 Caméras, babyphones, sonnettes connectées

Si elles sont accessibles depuis Internet, elles doivent avoir un mot de passe fort et unique (PAS le mot de passe par défaut « admin/admin » ou « 123456 »), un firmware à jour, et idéalement un accès restreint (certaines caméras permettent de limiter l'accès à certaines IP ou à un VPN). Les caméras avec mot de passe par défaut sont indexées par des moteurs comme Shodan et accessibles à quiconque — des milliers de babyphones et caméras domestiques sont visibles publiquement.

Les **sonnettes connectées** (Ring, Nest Hello, etc.) enregistrent en continu et stockent dans le cloud. Vérifier qui a accès au flux (le compte principal + les utilisateurs partagés), à la durée de conservation, et à la politique de partage avec les autorités du fournisseur.

## 36.3 Assistants vocaux

Alexa, Google Home, Siri : ils écoutent en permanence pour détecter le mot de déclenchement. Les enregistrements sont stockés dans le cloud du fournisseur. Vérifier les paramètres de confidentialité, supprimer l'historique régulièrement (Amazon : Paramètres Alexa > Confidentialité ; Google : myactivity.google.com), et désactiver le micro physiquement (bouton dédié sur la plupart des appareils) quand l'assistant n'est pas utilisé. Ne pas placer un assistant vocal dans une chambre où sont tenues des conversations sensibles, ni à proximité d'un téléphone qui sonne en permanence.

## 36.4 NAS, imprimantes, et stockage familial

Le **NAS** (Network Attached Storage — Synology, QNAP, etc.) est un mini-serveur de stockage à la maison, souvent utilisé pour centraliser les photos et documents familiaux. Risques : interface d'administration exposée à Internet (si elle l'est, c'est une cible majeure — le NAS doit n'être accessible que depuis le réseau local, ou via un VPN), mot de passe admin par défaut, firmware non mis à jour. Les ransomwares ciblant les NAS particuliers existent (ex. famille Qlocker sur QNAP en 2021) — un NAS compromis = toutes les photos et documents familiaux chiffrés.

L'**imprimante connectée** : elle a souvent une interface d'administration accessible sur le réseau local et parfois exposée à Internet. Mot de passe à changer. La mémoire interne de certaines imprimantes conserve des copies des documents imprimés, scannés, ou faxés — point d'attention en cas de revente de l'imprimante (cf. Ch.43).

Les **clés USB familiales** qui circulent (la clé USB du grand-père, partagée pour transférer des photos, branchée sur l'ordinateur de chacun) sont un vecteur classique de propagation de malwares. Si un appareil de la famille est infecté, la clé qui passe partout propage. Réflexe : ne pas brancher de clé USB inconnue, et idéalement n'avoir qu'une clé dédiée par usage (sauvegarde, transfert, etc.).

## 36.5 La segmentation simple

Mettre les objets connectés sur un réseau Wi-Fi séparé. La plupart des box récentes permettent de créer un réseau invité — les objets connectés (caméras, TV, assistants, imprimantes, NAS exposé en lecture) vont sur le réseau invité, les ordinateurs et téléphones sur le réseau principal. Si un objet connecté est compromis (vulnérabilité du firmware, mot de passe par défaut), il n'a pas accès aux appareils principaux. C'est le geste qui réduit le plus le risque domestique pour un coût d'effort minime.

---

<a id="chapitre-37"></a>
