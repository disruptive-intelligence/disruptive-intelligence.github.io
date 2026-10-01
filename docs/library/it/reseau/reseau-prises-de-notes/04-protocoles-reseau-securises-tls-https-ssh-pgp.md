---
title: Protocoles réseau sécurisés [TLS, HTTPS, SSH, PGP]
source: IT/04 Réseau/Réseau — prises de notes.md
note: Réseau — prises de notes
up:
- - Réseau — prises de notes
  - index.md
---

> - TLS : Connexion sécurisée entre client et serveur sur réseau non sec
<details markdown="1">
<summary>🔸 Première étape pour serv/client qui a besoin de s’identifier.</summary>

</details>

<details markdown="1">
<summary>🔸 Avoir certificat TLS signé.</summary>

<details markdown="1">
<summary>▫️ Admin créé Certificat Signing Request (CSR) > soumet Certificate Authority (CA)</summary>

</details>

<details markdown="1">
<summary>▫️ CA vérifie CSR puis émet certificat numérique.</summary>

</details>

<details markdown="1">
<summary>▫️ Une fois Certificat (signé) reçu, p-ê utilisé pour identifier serv/client auprès d’autres personnes, peuvent confirmer validité de signature.</summary>

</details>

<details markdown="1">
<summary>▫️ Pour hôte confirmer validité, certificat de l’autorité besoin d’être installé sur hôte.</summary>

</details>

<details markdown="1">
<summary>▫️ Autorité “trust” installé sur navigateur</summary>

        
> > > ![image.png](../../../assets/reseau-prises-de-notes-image-21.png)
        
</details>

</details>

<details markdown="1">
<summary>🔸 Généralement payer taxe pour avoir certificat signé, sinon Let’s Encrypt</summary>

</details>

<details markdown="1">
<summary>🔸 Créer certif autosigné, cependant, peut pas prouver authenticité server car n’a pas de third party pour confirmer</summary>

</details>

## HTTPS

> Chiffre trafic

> > - **Négociation (Client Hello / Server Hello) :** Ils se mettent d'accord sur la version de TLS (1.2 ou 1.3) et les algorithmes de chiffrement à utiliser.
> > - **L'Authentification (Asymétrique) :** Le serveur envoie son **Certificat** (sa Carte d'Identité). Ton navigateur vérifie la signature (comme le Secure Boot vérifie le Kernel). *"Ok, tu es bien la banque"*.
> > - **L'Échange de Clés (Key Exchange) :**
<details markdown="1">
<summary>▫️ Ton PC génère une "clé de session" (temporaire).</summary>

</details>

<details markdown="1">
<summary>▫️ Il la chiffre avec la **Clé Publique** du serveur et l'envoie.</summary>

</details>

<details markdown="1">
<summary>▫️ Seul le serveur (qui a la **Clé Privée**) peut la déchiffrer.</summary>

> > > - **Le passage en Symétrique :** Maintenant, les deux ont la même clé secrète ("clé de session"). Ils abandonnent la crypto asymétrique (trop lente) et utilisent cette clé unique pour chiffrer tout le reste de la conversation à très haute vitesse (AES).
    
> > > HTTPS est une modification de HTTP qui utilise TLS ou SSL.
    
> > > 1. Client et serveur échangent  messages **hello** pour convenir des paramètres de connexion.
> > > 2. Client et serveur échangent les paramètres crypto pour établir un **premaster secret**.
> > > 3. Client et serveur échangent des **certificats X.509** et des informations cryptographiques permettant l’**authentification** au sein de la session.
> > > 4. À partir du premaster secret et des valeurs aléatoires échangées, ils génèrent un **master secret**.
> > > 5. Le client et le serveur appliquent les **paramètres de sécurité négociés** à la couche **record** du protocole TLS.
> > > 6. Le client et le serveur **vérifient** que leur pair a calculé les mêmes paramètres de sécurité et que le **handshake** s’est déroulé sans altération par un attaquant.
</details>

<details markdown="1">
<summary>🔸 Utilisation courante cryptographie asymétrique consiste échanger clés pour un chiffrement symétrique.</summary>

<details markdown="1">
<summary>▫️ Mécanisme d’échange de clés</summary>

            
<details markdown="1">
<summary>• Le Problème</summary>

            
> > > > > Tu es "Alice" (le Navigateur). Tu veux envoyer un message secret à "Bob" (le Serveur de la Banque).
> > > > > Mais vous êtes dans une pièce remplie d'espions (Internet/Hackers) qui voient tout ce qui passe de main en main.
            
> > > > > Tu ne peux pas crier le code secret à travers la pièce, sinon les espions l'auront aussi.
            
</details>

<details markdown="1">
<summary>• La Solution : L'Échange Hybride</summary>

> L'Échange Hybride

            
> > > > > Voici exactement ce qui se passe lors de l'échange de clés (étape 3 du schéma précédent), décomposé au ralenti.
            
</details>

<details markdown="1">
<summary>• 1. La préparation (Côté Serveur)</summary>

            
> > > > > Bob (la Banque) possède deux objets mathématiques liés entre eux :
            
</details>

<details markdown="1">
<summary>• Une **Clé Publique** 🔓 (Imagine un cadenas ouvert). Il en a des millions d'exemplaires et les distribue à tout le monde. N'importe qui peut le fermer (clic !), mais personne ne peut le rouvrir.</summary>

</details>

<details markdown="1">
<summary>• Une **Clé Privée** 🗝️ (La petite clé en métal). Il est le **seul** au monde à l'avoir. Elle sert à rouvrir les cadenas.</summary>

            
</details>

<details markdown="1">
<summary>• 2. L'envoi du Cadenas (Server Hello)</summary>

            
> > > > > Tu te connectes à la banque.
> > > > > La banque te dit : *"Coucou ! Pour me parler en sécurité, voici mon **Cadenas Ouvert** (Clé Publique)."*
> > > > > Les espions voient passer le cadenas. Ils s'en fichent, un cadenas ouvert ne permet pas de déchiffrer quoi que ce soit.
            
</details>

<details markdown="1">
<summary>• 3. La création du Secret (Côté Client)</summary>

            
> > > > > Ton navigateur (Toi) va générer le secret final.
> > > > > Il crée une chaîne de caractères aléatoire (ex: `X9sP2m...`). On appelle ça le **Secret Pré-Maître**.
> > > > > C'est ça, la future **Clé Symétrique**. C'est le code qui servira à chiffrer toute la conversation.
            
> > > > > Pour l'instant, ce secret est juste dans ta tête (ta RAM). Personne ne l'a vu.
            
</details>

<details markdown="1">
<summary>• 4. L'Emballage (L'Asymétrique entre en jeu)</summary>

            
> > > > > Tu prends ce secret, tu le mets dans une petite boîte, et **tu le verrouilles avec le Cadenas Ouvert de la Banque**. 📦🔒
> > > > > *Clac !* C'est verrouillé.
            
> > > > > À partir de cette seconde précise :
            
</details>

<details markdown="1">
<summary>• Même toi, tu ne peux plus rouvrir la boîte (tu n'as pas la clé en métal).</summary>

</details>

<details markdown="1">
<summary>• Les espions voient passer une boîte verrouillée. Impossible de l'ouvrir sans la clé privée.</summary>

            
</details>

<details markdown="1">
<summary>• 5. La Livraison et l'Ouverture</summary>

            
> > > > > Tu envoies la boîte verrouillée à la Banque.
> > > > > La Banque la reçoit. Elle sort sa **Clé Privée** (qu'elle n'a jamais envoyée sur le réseau !), elle ouvre la boîte, et elle récupère le secret `X9sP2m...`.
            
</details>

<details markdown="1">
<summary>• 6. Le Changement de mode (Passage au Symétrique)</summary>

            
> > > > > Maintenant :
            
</details>

<details markdown="1">
<summary>• Tu as le code `X9sP2m...` (tu l'as créé).</summary>

</details>

<details markdown="1">
<summary>• La Banque a le code `X9sP2m...` (elle l'a reçu dans la boîte blindée).</summary>

</details>

<details markdown="1">
<summary>• Les espions n'ont rien (ils ont juste vu un cadenas ouvert et une boîte fermée).</summary>

            
> > > > > Puisque vous avez le même code, vous jetez les cadenas et vous commencez à utiliser ce code pour tout chiffrer très vite (AES).
            
> > > > > ---
            
</details>

<details markdown="1">
<summary>• Résumé en une phrase</summary>

            
> > > > > La cryptographie **Asymétrique** (Lente/Complexe) sert uniquement de **camion blindé** 🚛 pour transporter la **Clé Symétrique** (Rapide/Légère) 🏎️ de chez toi vers le serveur. Une fois le camion arrivé, on sort la voiture de course.
            
</details>

</details>

<details markdown="1">
<summary>▫️ Le but est d’utiliser **l’asymétrique au début**, juste pour **échanger une clé symétrique**, puis **faire tout le reste en symétrique** (comme HTTPS).</summary>

> > > > - **La métaphore du cadenas (excellente) :**
> > > > 1. Tu veux envoyer une **clé secrète** à ton ami (le serveur)
> > > > 2. Tu n’as **pas envie que quelqu’un puisse l’intercepter**
> > > > 3. Ton ami t’envoie **un cadenas (sa clé publique)**
> > > > 4. Tu mets la clé secrète dans une **boîte verrouillée avec son cadenas** (tu chiffres avec sa clé publique)
> > > > 5. Tu envoies la boîte → **seul ton ami peut l’ouvrir avec sa clé privée**
> > > > 6. Maintenant que vous avez tous les deux la **même clé**, vous pouvez **parler en secret avec un chiffrement symétrique**
</details>

<details markdown="1">
<summary>▫️ Dans le monde réel</summary>

> HTTPS

<details markdown="1">
<summary>• Quand tu te connectes à un site en HTTPS</summary>

> > > > > 1. Le **navigateur récupère le certificat** (qui contient la clé publique du serveur)
> > > > > 2. Il **génère une clé symétrique aléatoire**
> > > > > 3. Il chiffre cette clé avec la **clé publique du serveur**
> > > > > 4. Le serveur la reçoit, la déchiffre avec sa **clé privée**
> > > > > 5. Les deux côtés ont maintenant la **même clé symétrique**, utilisée pour chiffrer tout le reste de la communication
</details>

</details>

<details markdown="1">
<summary>▫️ Certificats garantissent que la clé pub appartient bien au bon domaine.</summary>

</details>

</details>

<details markdown="1">
<summary>🔸 HTTP</summary>

> Trafic en clair

<details markdown="1">
<summary>▫️ Tout trafic est envoyé en clair.</summary>

</details>

<details markdown="1">
<summary>▫️ Navigateur demande page HTTP</summary>

<details markdown="1">
<summary>• Etablit TCP three-way handshake avec serveur</summary>

</details>

<details markdown="1">
<summary>• Communique en utilisant protocol HTTP comme GET /HTTP/1.1</summary>

> > > > > - Wireshark
> > > > > - 1 : 3 packets handshaker
> > > > > - 2 : HTTP communication
> > > > > - 3 : TCP connection terminaison
            
> > > > > ![image.png](../../../assets/reseau-prises-de-notes-image-22.png)
            
> > > > > - HTTP over TLS
</details>

</details>

<details markdown="1">
<summary>▫️ Demander page HTTPS</summary>

<details markdown="1">
<summary>• Etablir TCP three-way handshake vers serv</summary>

</details>

<details markdown="1">
<summary>• Etablir TLS session</summary>

</details>

<details markdown="1">
<summary>• Communicate using HTTP protocol, ex</summary>

> GET /HTTP/1.1

> > > > > - Wireshark
> > > > > - 1 : TCP session
> > > > > - 2 : Packets négociants TLS protocol
> > > > > - 3 : HTTP application data sont échangés (écrit Application Data car ne sait pas si c’est HTTP ou autre proto)
                    
> > > > > ![image.png](../../../assets/reseau-prises-de-notes-image-23.png)
                    
</details>

<details markdown="1">
<summary>• Si tentative suivre stream, trafic sera chiffré donc illisible</summary>

            
> > > > > ![image.png](../../../assets/reseau-prises-de-notes-image-24.png)
            
</details>

</details>

</details>

<details markdown="1">
<summary>🔸 Getting the Encryption Key</summary>

<details markdown="1">
<summary>▫️ Add TLS to HTTP, chiffre et rend illisible</summary>

</details>

<details markdown="1">
<summary>▫️ Si on possède clé privé, on peut voir content</summary>

</details>

</details>

## SMTPS, POP3S, IMAPS

> Ajoute TLS

<details markdown="1">
<summary>🔸 Comme pour HTTPS, ajoute TLS, même principe</summary>

> > > - SSH : Sécurise authentification
> > > - ssh username@hostname / Port 22
</details>

<details markdown="1">
<summary>🔸 Secure authentification</summary>

> En plus couple login mdp. Supporte public key & 2FA

</details>

<details markdown="1">
<summary>🔸 Confidentialité</summary>

> OpenSSH end-to-end encryption, protège eavesdropping & MITM, notifie nouvelle clé de serveur

</details>

<details markdown="1">
<summary>🔸 Intégrité</summary>

> Crypto garantit

</details>

<details markdown="1">
<summary>🔸 Tunneling</summary>

> Peut créer “tunnel” à l’image d’un VPN-like

</details>

## OpenPGP

> Standard pour signature/chiffrement mail.

<details markdown="1">
<summary>🔸 Norme / Standard ouvert pour la signature et le chiffrement de fichiers et de mail. GnuGPG implémentation open-source.</summary>

</details>

<details markdown="1">
<summary>🔸 Utilisé pour mail, besoin de générer une paire de clés, clé privée et clé publique.</summary>

<details markdown="1">
<summary>▫️ La clé privée de l’émetteur est utilisée pour signer pendant que la clé publique du destinataire est utilisée pour le chiffrement.</summary>

</details>

<details markdown="1">
<summary>▫️ Du point de vue du destinataire, la clé publique de l’émetteur est utilisée pour check la signature, pendant que la clé privée du destinataire est utilisée pour le déchiffrement.</summary>

</details>

</details>

## SFTP

> SSH & FTPS : TLS

<details markdown="1">
<summary>🔸 SFTP</summary>

> SSH File Transfer Protocol : Sécurise transfert de fichier

</details>

<details markdown="1">
<summary>🔸 FTPS</summary>

> File Transfer Protocol Secure : Utilise TLS, comme HTTPS

<details markdown="1">
<summary>▫️ Port 990, requière certificat</summary>

</details>

</details>
