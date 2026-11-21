---
title: "Réseau et accès distant"
cours:
  - library/it/windows/windows-en-profondeur/index.md
---

# Réseau et accès distant

N'exposer que le nécessaire : pare-feu actif sur les trois profils, peu de règles entrantes et restreintes à leur source ; couper la chaîne résolution usurpée → authentification NTLM → relais (LLMNR, NetBIOS, mDNS, WPAD et PAC, signature SMB et LDAP, WebDAV, DHCP et DNS) ; partages contrôlés, bureau à distance et WinRM fermés ou bornés.

Les incontournables : `Get-NetFirewallProfile` · `Set-NetFirewallProfile` · `Get-NetFirewallRule` · `EnableMulticast` · `DisableWpad` · `Get-SmbServerConfiguration` · `Get-SmbShareAccess` · `fDenyTSConnections`
{ .kw-cs-top }

Un pare-feu local bien réglé freine fortement les déplacements latéraux : le poste n'a pas à accepter SMB, RDP ou WinRM de tous les autres postes.

## Pare-feu

### Activer le pare-feu sur les trois profils

| Profil | Appliqué quand… |
|---|---|
| Domaine | La machine joint un contrôleur de son domaine |
| Privé | Réseau marqué de confiance |
| Public | Tout autre réseau (le plus restrictif) |

```powershell title="Vérifier"
Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
Get-NetFirewallProfile | Where-Object Enabled -eq $false   # rien en retour : les trois profils sont actifs
```

```powershell title="Appliquer"
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled True -DefaultInboundAction Block
```

En parc : *Paramètres de sécurité → Pare-feu Windows Defender avec fonctions avancées de sécurité* dans une GPO (ou Intune), pour qu'un utilisateur ou un attaquant ne le coupe pas durablement.

Ensuite : [voir le profil et l'état du pare-feu](../fondamentaux/reseau.md#voir-le-profil-et-letat-du-pare-feu) — Pour comprendre : [Windows en profondeur, ch. 14.2 (le pare-feu)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#142-le-pare-feu-windows) · [PowerShell, ch. 18](../../../library/it/windows/powershell/03-partie-iii-administration-reseau-windows/04-chapitre-18-pare-feu-windows.md) — Ajout hors cours : `Set-NetFirewallProfile`
{ .kw-cs-meta }

### Réduire les règles entrantes au strict nécessaire

Chaque règle `Allow` entrante est une porte. Lister ce qui est ouvert, supprimer l'inutile, restreindre le reste au profil et à la plage d'adresses qui en ont besoin (réseau d'administration, serveur de supervision). Sur les serveurs, filtrer aussi la sortie.

```powershell title="Vérifier"
Get-NetFirewallRule -Direction Inbound -Action Allow -Enabled True | ForEach-Object {
    [PSCustomObject]@{
        Regle  = $_.DisplayName
        Profil = $_.Profile
        Port   = ($_ | Get-NetFirewallPortFilter).LocalPort
        Source = ($_ | Get-NetFirewallAddressFilter).RemoteAddress
    }
} | Sort-Object Port
```

```powershell title="Exemple — restreindre une règle existante à sa source"
Set-NetFirewallRule -DisplayName "<règle>" -RemoteAddress 192.168.100.0/24 -Profile Domain
```

`Source = Any` sur RDP (3389), SMB (445), WinRM (5985/5986) : à restreindre. Ne pas couper la règle dont dépend sa propre session à distance.

Ensuite : [ouvrir un port en restreignant la source](../administration/reseau.md#ouvrir-un-port-dans-le-pare-feu) · [lister et supprimer des règles](../administration/reseau.md#lister-et-supprimer-des-regles) — Pour comprendre : [PowerShell, ch. 18 (auditer les règles entrantes)](../../../library/it/windows/powershell/03-partie-iii-administration-reseau-windows/04-chapitre-18-pare-feu-windows.md) — Ajout hors cours : la colonne `Source` (`Get-NetFirewallAddressFilter`)
{ .kw-cs-meta }

### Journaliser les connexions refusées par le pare-feu

Sans journalisation, `pfirewall.log` reste vide : on ne voit ni les balayages, ni les tentatives refusées.

```powershell title="Appliquer"
Set-NetFirewallProfile -All -LogBlocked True -LogMaxSizeKilobytes 16384
```

```powershell title="Vérifier"
Get-NetFirewallProfile | Select-Object Name, LogBlocked, LogAllowed, LogFileName, LogMaxSizeKilobytes
```

Fichier : `%SystemRoot%\System32\LogFiles\Firewall\pfirewall.log` (`DROP` / `ALLOW`). Les changements de règles se lisent dans *Journaux des applications et des services → Microsoft → Windows → Windows Firewall With Advanced Security → Firewall* (2004 ajout, 2005 modification, 2003 réglage changé).

Ensuite : [retracer les changements du pare-feu](../fondamentaux/logs/pare-feu-defender.md#retracer-les-changements-du-pare-feu) — Pour comprendre : [Analyse des journaux, pare-feu Windows](../../../library/it/windows/analyse-des-journaux-d-evenements-windows-event-logs/10-pare-feu-windows.md) — Ajout hors cours : la commande d'activation
{ .kw-cs-meta }

## Résolution de noms et relais NTLM

Une même famille de risques : un attaquant présent sur le réseau **se fait passer pour une ressource légitime**, le poste se connecte à lui et **lui présente une authentification Windows** (NTLM), que l'attaquant casse hors ligne ou relaie vers un autre service.

```text
1. Un poste cherche un nom introuvable          \\SRV-FICHEIRS (faute de frappe), wpad, imprimante.local
2. Il pose la question à tout le segment        LLMNR, NBT-NS, mDNS (ou WPAD via DNS / DHCP)
3. L'attaquant répond « c'est moi »             réponse usurpée, rien ne l'authentifie
4. Le poste s'y connecte et s'authentifie       NTLM, par SMB ou HTTP
5. L'attaquant exploite l'authentification      cassage hors ligne de la réponse NTLMv2 (mot de passe faible)
                                                ou relais vers un service sans protection (SMB, LDAP, AD CS)
```

| Étape | Ce qui joue | Ce qui protège |
|---|---|---|
| **Découvrir** une configuration ou une ressource | WPAD, DHCP, DNS | WPAD coupé, DHCP et DNS maîtrisés |
| **Décider** du chemin des connexions web | Fichier PAC | URL de PAC explicite et protégée |
| **Usurper** une résolution de noms | LLMNR, NBT-NS, mDNS, DNS | Protocoles de diffusion coupés, DNS seul |
| **Exploiter** l'authentification | NTLM | Kerberos, NTLM réduit, signature SMB, signature et liaison de canal LDAP, EPA |

La chaîne n'aboutit que si les trois maillons sont réunis : **une résolution usurpable + NTLM autorisé + un service cible sans protection contre le relais**. Casser un seul maillon suffit ; les fermer tous, c'est la défense en profondeur. La réponse NTLMv2 capturée n'est ni le mot de passe ni le hash NT : elle ne se casse que si le mot de passe est faible. En audit, l'outil le plus connu pour cette chaîne est Responder (empoisonnement LLMNR / NBT-NS / mDNS / WPAD), suivi de ntlmrelayx (Impacket) pour le relais.

| Mécanisme | Rôle | Port | Risque |
|---|---|---|---|
| LLMNR | Résolution de noms sur le segment, sans DNS | 5355/UDP | Réponse usurpée, authentification NTLM captée |
| NetBIOS / NBT-NS | Résolution historique des noms Windows (WINS en version centralisée) | 137/UDP | Même principe que LLMNR |
| mDNS | Noms en `.local` (imprimantes, appareils Apple, découverte de services) | 5353/UDP | Réponse usurpée, connexion détournée |
| WPAD | Découverte automatique du proxy | DNS 53, DHCP 67/68, puis HTTP | Faux serveur WPAD, faux proxy |
| PAC | Script qui choisit le proxy pour chaque URL | HTTP / HTTPS | Trafic web envoyé à un proxy de l'attaquant |
| DNS | Résolution centralisée, localisation des DC (enregistrements SRV) | 53 | Enregistrement modifié ou réponse falsifiée |
| DHCP / DHCPv6 | Adresse, passerelle, serveurs DNS | 67/68 · 546/547/UDP | Faux serveur qui impose son DNS ou sa passerelle |
| NTLM | Authentification héritée | Aucun (porté par SMB, HTTP, LDAP…) | Cassage hors ligne, relais |
| SMB | Partages, administration | 445/TCP | Cible de relais, déplacement latéral |
| LDAP / LDAPS | Annuaire Active Directory | 389 / 636/TCP | Cible de relais vers l'AD |

Pour comprendre : [Windows en profondeur, ch. 16 (résolution de noms et protocoles à risque)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#162-les-protocoles-de-secours) · [Active Directory, ch. 5 (faiblesses de NTLM, protocoles de secours)](../../../library/it/active-directory/active-directory/02-partie-ii-authentification/02-chapitre-5-ntlm-le-protocole-herite-qui-refuse-de.md#53-les-faiblesses-de-conception) · [ch. 15 (relay et coercion)](../../../library/it/active-directory/active-directory/04-partie-iv-attaques-ad.md)
{ .kw-cs-meta }

| Ordre | Chantier | Fiche |
|---|---|---|
| 1 | Désactiver LLMNR | [ci-dessous](#desactiver-llmnr-et-netbios) |
| 2 | Désactiver NetBIOS sur TCP/IP, après contrôle des applications anciennes | [ci-dessous](#desactiver-llmnr-et-netbios) |
| 3 | Couper WPAD s'il ne sert pas, maîtriser le fichier PAC s'il sert | [WPAD](#couper-la-decouverte-automatique-du-proxy-wpad) · [PAC](#maitriser-le-fichier-de-configuration-du-proxy-pac) |
| 4 | Exiger la signature SMB | [ci-dessous](#desactiver-smbv1-et-exiger-la-signature-smb) |
| 5 | Signature LDAP et liaison de canal sur les DC, après audit | [ci-dessous](#exiger-la-signature-ldap-et-la-liaison-de-canal-controleurs-de-domaine) |
| 6 | Auditer puis réduire NTLM, au profit de Kerberos | [Identifiants](identifiants.md#reduire-ntlm-dabord-en-audit) |
| 7 | Contrôler mDNS, DHCPv6 et les annonces IPv6 | [mDNS](#couper-mdns-sil-ne-sert-pas) · [DHCP, DHCPv6, ARP](#proteger-la-configuration-reseau-dhcp-dhcpv6-dns-arp) |
| 8 | Désactiver SMBv1, segmenter les flux SMB et LDAP | [ci-dessous](#desactiver-smbv1-et-exiger-la-signature-smb) |

![[cheatsheets/windows/administration/reseau#Désactiver LLMNR et NetBIOS]]

Pour couper LLMNR par GPO, il faut **activer** la stratégie *Configuration ordinateur → Modèles d'administration → Réseau → Client DNS → Désactiver la résolution de noms multidiffusion*. Dans le même dossier, *Désactiver la résolution de noms intelligente multirésident* empêche le poste d'envoyer ses requêtes sur toutes ses interfaces à la fois. Couper NetBIOS ne coupe pas SMB : SMB moderne passe directement par TCP 445.
{ .kw-cs-meta }

### Couper mDNS s'il ne sert pas

mDNS résout les noms en `.local` sans serveur : utile pour certaines imprimantes et la découverte d'appareils, inutile sur la plupart des postes d'entreprise. Le protocole n'est pas une faille en soi : le risque vient de ce qu'on fait confiance à une réponse que personne n'authentifie.

```powershell title="Vérifier"
Get-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters -Name EnableMDNS -ErrorAction SilentlyContinue
```

```powershell title="Appliquer"
Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters -Name EnableMDNS -Value 0 -Type DWord
```

Vérifier avant les usages d'impression et de découverte (une imprimante ajoutée par son nom `.local` ne sera plus trouvée).

Pour comprendre : [Windows en profondeur, ch. 16.2 (les protocoles de secours)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#162-les-protocoles-de-secours) — Ajout hors cours : la valeur `EnableMDNS`
{ .kw-cs-meta }

### Couper la découverte automatique du proxy (WPAD)

WPAD évite de configurer le proxy poste par poste : le poste demande au DHCP (option 252) ou au DNS (`wpad.<domaine>`) où trouver le fichier de configuration, souvent `http://wpad.<domaine>/wpad.dat`, puis le télécharge. Qui répond à cette recherche, en usurpant le DNS, avec un faux DHCP ou par LLMNR / NBT-NS quand le nom `wpad` n'existe pas, devient le proxy du poste et peut lui réclamer une authentification NTLM.

```bat title="Vérifier"
netsh winhttp show proxy
```

```powershell title="Exemple — la détection automatique côté WinHTTP"
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp' -Name DisableWpad -ErrorAction SilentlyContinue
```

```powershell title="Appliquer — si aucun proxy automatique n'est utilisé"
New-Item 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp' -Force | Out-Null
Set-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp' -Name DisableWpad -Value 1 -Type DWord
```

`DisableWpad = 1` coupe la découverte pour **WinHTTP** (services Windows, mises à jour, beaucoup d'applications), pas forcément pour les navigateurs : désactiver aussi *Détecter automatiquement les paramètres* (*Paramètres → Réseau et Internet → Proxy*, ou par GPO pour Edge et Chrome). Si un proxy est nécessaire, le **déclarer explicitement** (adresse du proxy ou URL de PAC) plutôt que de le laisser découvrir. Côté serveur DNS Windows, le nom `wpad` figure par défaut dans la liste de blocage des requêtes globales : le laisser bloqué (`Get-DnsServerGlobalQueryBlockList`).

Pour comprendre : [Windows en profondeur, ch. 16.2 (WPAD)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#162-les-protocoles-de-secours) — Ajout hors cours : `DisableWpad`, `netsh winhttp`, l'option DHCP 252 et la liste de blocage DNS
{ .kw-cs-meta }

### Maîtriser le fichier de configuration du proxy (PAC)

WPAD répond à « **où** trouver la configuration du proxy ? », le fichier PAC à « **quel** proxy prendre pour cette URL ? ». Le PAC est un petit script JavaScript dont la fonction `FindProxyForURL(url, host)` renvoie `DIRECT`, `PROXY hôte:port`, ou une liste de replis.

```javascript title="Exemple — fichier PAC"
function FindProxyForURL(url, host) {
    if (dnsDomainIs(host, ".entreprise.example")) {
        return "DIRECT";                              // sites internes : connexion directe
    }
    return "PROXY proxy.entreprise.example:8080";     // tout le reste : par le proxy
}
```

```powershell title="Vérifier — quel PAC ou quel proxy l'utilisateur utilise"
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' |
    Select-Object AutoConfigURL, ProxyEnable, ProxyServer
```

Un PAC modifié ou usurpé envoie les connexions web vers un proxy de l'attaquant : métadonnées de navigation et contenu HTTP en clair visibles, authentifications réclamées, accès perturbé. Il ne donne **pas** accès au contenu HTTPS (il faudrait en plus casser la confiance TLS), et ne fait qu'aiguiller les connexions : il n'exécute pas de commandes sur le poste.

Un PAC légitime est acceptable s'il est maîtrisé : URL déclarée explicitement par GPO plutôt que découverte, en HTTPS quand le client le permet, fichier sur un serveur où peu de comptes peuvent écrire, modifications surveillées. Un `AutoConfigURL` inconnu sur un poste est à investiguer.

Pour comprendre : [Windows en profondeur, ch. 16.2](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#162-les-protocoles-de-secours) — Ajout hors cours : toute l'entrée
{ .kw-cs-meta }

![[cheatsheets/windows/administration/reseau#Désactiver SMBv1 et exiger la signature SMB]]

Côté client aussi : `Set-SmbClientConfiguration -RequireSecuritySignature $true -Force` (*Client réseau Microsoft : communications signées numériquement (toujours)*). La signature empêche de relayer une authentification NTLM vers SMB ; tester d'abord les équipements anciens (copieurs, NAS). Windows 11 24H2 et Windows Server 2025 renforcent la signature SMB par défaut, mais le réglage réel, les exceptions et les serveurs plus anciens restent à vérifier. SMBv3 permet aussi de chiffrer un partage sensible (`EncryptData`).
{ .kw-cs-meta }

### Exiger la signature LDAP et la liaison de canal (contrôleurs de domaine)

Après un empoisonnement, la cible la plus intéressante d'un relais NTLM est l'annuaire. Deux protections complémentaires sur les DC :

| Protection | Ce qu'elle fait | Limite |
|---|---|---|
| **Signature LDAP** | Exige l'intégrité des échanges LDAP non chiffrés (liaisons SASL) | Ne protège pas LDAPS : seule, elle ne ferme pas tous les relais |
| **Liaison de canal** (*channel binding*, CBT) | Lie l'authentification à la session TLS de LDAPS : relayée dans une autre session, elle est refusée | Les clients doivent la gérer |

```text title="GPO (contrôleurs de domaine)"
Paramètres de sécurité → Stratégies locales → Options de sécurité
→ Contrôleur de domaine : conditions requises pour la signature de serveur LDAP → Exiger la signature
→ Contrôleur de domaine : exigences de jeton de liaison de canal du serveur LDAP → Toujours
   (registre : LdapEnforceChannelBinding = 2)
Postes : Sécurité réseau : conditions requises pour la signature de client LDAP → Négocier la signature (au minimum)
```

**Auditer avant d'imposer** : sur chaque DC, le journal *Journaux des applications et des services → Directory Service* signale les clients qui font des liaisons non signées (2887 résumé, 2889 détail par client, une fois la journalisation de diagnostic *16 LDAP Interface Events* passée à `2`) et ceux qui échoueraient à la liaison de canal (3039).

Le relais vise aussi l'**inscription web d'AD CS** (attaque dite ESC8) : HTTPS avec EPA (*Extended Protection for Authentication*), ou Web Enrollment désactivé s'il ne sert pas.

Pour comprendre : [Active Directory, ch. 24.2 (signer et lier les canaux)](../../../library/it/active-directory/active-directory/06-partie-vi-hardening.md#242-signer-et-lier-les-canaux) · [ch. 25.1 (AD CS)](../../../library/it/active-directory/active-directory/06-partie-vi-hardening.md#251-ad-cs) — Ajout hors cours : libellés des GPO, événements 2887, 2889 et 3039
{ .kw-cs-meta }

### Fermer les autres déclencheurs d'authentification (WebDAV)

Le client WebDAV de Windows (service *WebClient*) permet d'ouvrir un partage par HTTP ; il sert aussi à forcer un poste à s'authentifier par HTTP vers une machine de l'attaquant, une authentification plus facile à relayer vers LDAP que celle de SMB. Sur un poste qui n'en a pas l'usage (SharePoint ou OneDrive en lecteur réseau), le désactiver.

```powershell title="Vérifier"
Get-Service WebClient -ErrorAction SilentlyContinue | Select-Object Status, StartType
```

```powershell title="Appliquer"
Stop-Service WebClient
Set-Service -Name WebClient -StartupType Disabled
```

Ensuite : [désactiver les services inutiles](services.md#desactiver-les-services-inutiles) — Ajout hors cours : toute l'entrée
{ .kw-cs-meta }

### Protéger la configuration réseau (DHCP, DHCPv6, DNS, ARP)

Ces protections se posent surtout sur le réseau et les serveurs, pas sur le poste, mais elles ferment l'étape 1 de la chaîne : qui contrôle le DNS ou la passerelle d'un poste choisit où il se connecte.

| Menace | Principe | Protection |
|---|---|---|
| Faux serveur DHCP | Impose son DNS, sa passerelle, son WPAD | *DHCP snooping* sur les commutateurs, contrôle d'accès au réseau (NAC), surveillance des serveurs DHCP |
| Faux DHCPv6 / annonces IPv6 | Windows préfère IPv6 : un faux serveur DHCPv6 devient le DNS du poste, même sur un réseau « IPv4 » | *RA Guard* et *DHCPv6 Guard* sur les commutateurs, filtrage des annonces non autorisées |
| DNS falsifié | Enregistrement modifié ou réponse usurpée : faux SMB, LDAP, HTTP, WPAD | Mises à jour dynamiques sécurisées uniquement, administration DNS restreinte, transferts de zone limités, modifications surveillées |
| ARP spoofing | Une machine du segment se fait passer pour la passerelle | *Dynamic ARP Inspection*, segmentation |

Ne pas **désactiver IPv6** pour régler DHCPv6 : Microsoft le déconseille (des composants en dépendent). On sécurise la configuration réseau, ou on fait préférer IPv4 si besoin.

```powershell title="Vérifier — quels DNS le poste utilise réellement"
Get-DnsClientServerAddress | Where-Object ServerAddresses | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Un serveur DNS inconnu, surtout en IPv6 (`fe80::…` ou une adresse qui n'est pas celle des DC), est à investiguer.

Pour comprendre : [Sécurité système Windows, sécurité DNS et DHCP](../../../library/cyber/hardening/securite-systeme-windows/02-securite-active-directory.md#securite-dns-sous-windows) · [Fiche Segmentation réseau](../../../library/cyber/notions/segmentation-reseau.md) — Ajout hors cours : DHCPv6, RA Guard, ARP et la commande
{ .kw-cs-meta }

## Partages

### Fermer les partages inutiles et resserrer leurs droits

Un partage lisible par `Everyone` expose son contenu à tout le réseau ; les partages administratifs (`C$`, `ADMIN$`, `IPC$`) sont réservés aux administrateurs locaux, d'où l'importance de LAPS. Par le réseau, le plus restrictif des droits de partage et des droits NTFS l'emporte : partage large pour les utilisateurs authentifiés, finesse en NTFS.

```powershell title="Vérifier"
Get-SmbShare | Where-Object Name -notmatch '\$$' | ForEach-Object { Get-SmbShareAccess -Name $_.Name } |
    Select-Object Name, AccountName, AccessRight
```

```powershell title="Appliquer"
Revoke-SmbShareAccess -Name "<partage>" -AccountName Everyone -Force
Grant-SmbShareAccess -Name "<partage>" -AccountName "<groupe>" -AccessRight Change -Force
```

`Remove-SmbShare -Name "<partage>"` supprime un partage qui ne sert plus (les fichiers restent sur le disque).

Ensuite : [voir qui a accès à un partage](../fondamentaux/reseau.md#voir-qui-a-acces-a-un-partage) — Pour comprendre : [Windows en profondeur, ch. 15 (SMB, partages)](../../../library/it/windows/windows-en-profondeur/04-partie-iv-reseau-et-communication.md#152-permissions-de-partage-et-permissions-ntfs) · [PowerShell, ch. 28](../../../library/it/windows/powershell/05-partie-v-gpo-et-services-windows-server/04-chapitre-28-file-server-et-partages-smb.md) — Ajout hors cours : `Revoke-SmbShareAccess`, `Remove-SmbShare`
{ .kw-cs-meta }

## Accès distant

### Fermer le bureau à distance, ou le borner

Sur un poste, le bureau à distance est souvent inutile : le désactiver. S'il sert : authentification au niveau du réseau (NLA), groupe *Utilisateurs du Bureau à distance* réduit, port ouvert seulement depuis le réseau d'administration, MFA, Remote Credential Guard pour les administrateurs.

```powershell title="Vérifier"
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections                 # 1 = RDP fermé
Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication # 1 = NLA exigée
```

```powershell title="Appliquer — fermer"
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name fDenyTSConnections -Value 1
```

```powershell title="Exemple — garder, mais avec NLA"
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name UserAuthentication -Value 1
```

GPO : *Composants Windows → Services Bureau à distance → Hôte de la session Bureau à distance → Connexions* (autoriser ou non) et *→ Sécurité → Requérir l'authentification utilisateur pour les connexions à distance à l'aide de l'authentification au niveau du réseau*.

Ensuite : [ne pas déposer ses identifiants en RDP](identifiants.md#ne-pas-laisser-ses-identifiants-sur-la-machine-administree-rdp) · [repérer les connexions RDP](../fondamentaux/logs/sessions-rdp.md#reperer-les-connexions-rdp-et-les-echecs-dauthentification) — Pour comprendre : [Sécurité système Windows, journaux RDP](../../../library/cyber/hardening/securite-systeme-windows/07-infrastructure-de-journalisation-windows.md#remote-desktop-rdp-logs) — Ajout hors cours : toute l'entrée (valeurs de registre et GPO)
{ .kw-cs-meta }

### Restreindre WinRM et PowerShell Remoting

En domaine, Kerberos authentifie et chiffre le contenu même sur le port HTTP 5985. Hors domaine : HTTPS (5986, avec certificat), pas `TrustedHosts = *`. Ouvrir WinRM seulement depuis le réseau d'administration, et déléguer des tâches précises par **JEA** (*Just Enough Administration*) plutôt que des droits d'administrateur complets.

```powershell title="Vérifier"
Get-Service WinRM | Select-Object Status, StartType
Get-Item WSMan:\localhost\Client\TrustedHosts
```

```powershell title="Appliquer — limiter TrustedHosts au nécessaire"
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "<machine>" -Force
```

`TrustedHosts` à `*` fait confiance à toutes les machines et contourne des protections : à remplacer par la liste nécessaire, ou par HTTPS.

Pour comprendre : [PowerShell, ch. 29 (WinRM, authentification et sécurité)](../../../library/it/windows/powershell/06-partie-vi-administration-distante-api-et-automatis/01-chapitre-29-powershell-remoting.md) · [ch. 35 (JEA)](../../../library/it/windows/powershell/08-partie-viii-powershell-pour-la-cybersecurite/02-chapitre-35-securite-de-l-execution-et-durcissemen.md#jea-just-enough-administration) — Ajout hors cours : la lecture de `TrustedHosts`
{ .kw-cs-meta }

### Vérifier ce qui écoute sur le poste

Chaque port en écoute doit correspondre à un besoin connu. `0.0.0.0` écoute sur toutes les interfaces (le pare-feu peut encore bloquer), `127.0.0.1` seulement en local.

```powershell title="Vérifier"
Get-NetTCPConnection -State Listen | Sort-Object LocalPort |
    Select-Object LocalAddress, LocalPort, OwningProcess, @{n='Processus';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
```

Ensuite : [voir les ports en écoute](../fondamentaux/reseau.md#voir-les-ports-en-ecoute) · [identifier un port et son processus](../fondamentaux/enumeration.md#identifier-un-port-en-ecoute-et-son-processus) — Pour comprendre : [Élévation de privilèges, 127.0.0.1 vs 0.0.0.0](../../../library/it/windows/elevation-de-privileges-sous-windows-windows-privilege-escalation/03-enumeration-initiale.md)
{ .kw-cs-meta }

## Vue d'ensemble

| Mesure | Vérifier | Attendu |
|---|---|---|
| Pare-feu | `Get-NetFirewallProfile` | `Enabled = True` sur les trois profils, entrant `Block` |
| Règles entrantes | `Get-NetFirewallRule -Direction Inbound -Action Allow` | Peu de règles, source restreinte |
| Journal du pare-feu | `Get-NetFirewallProfile` → `LogBlocked` | `True` |
| LLMNR | `…\Windows NT\DNSClient\EnableMulticast` | `0` |
| NetBIOS sur TCP/IP | `TcpipNetbiosOptions` | `2` |
| mDNS | `…\Dnscache\Parameters\EnableMDNS` | `0` s'il ne sert pas |
| WPAD | `…\Internet Settings\WinHttp\DisableWpad` ; « Détecter automatiquement les paramètres » | `1` ; décoché, sauf proxy automatique voulu |
| Fichier PAC | `AutoConfigURL` (HKCU) | Vide, ou URL connue déclarée par GPO, en HTTPS si possible |
| SMBv1 | `Get-SmbServerConfiguration` → `EnableSMB1Protocol` | `False` |
| Signature SMB | `RequireSecuritySignature` (serveur et client) | `True` |
| Signature LDAP (DC) | GPO *conditions requises pour la signature de serveur LDAP* ; événements 2887 / 2889 | Exiger la signature, plus aucun client non signé |
| Liaison de canal LDAP (DC) | `LdapEnforceChannelBinding` ; événement 3039 | `2` (toujours), après audit |
| AD CS Web Enrollment | IIS de la CA | HTTPS + EPA, ou désactivé |
| WebDAV | `Get-Service WebClient` | `Disabled` s'il ne sert pas |
| DNS du poste | `Get-DnsClientServerAddress` | Seulement les DNS de l'entreprise, y compris en IPv6 |
| DHCP, DHCPv6, ARP | Commutateurs | DHCP snooping, RA Guard / DHCPv6 Guard, Dynamic ARP Inspection |
| Partages | `Get-SmbShareAccess` | Pas d'`Everyone`, partages inutiles supprimés |
| Bureau à distance | `fDenyTSConnections` ; `UserAuthentication` | `1` (fermé) ; sinon NLA `1` et source restreinte |
| WinRM | `TrustedHosts` | Pas de `*` ; HTTPS hors domaine ; JEA |
| Ports en écoute | `Get-NetTCPConnection -State Listen` | Chacun justifié |

| Port | Service | Pourquoi le restreindre |
|---|---|---|
| 445/TCP | SMB | Partages, partages administratifs, déplacement latéral |
| 3389/TCP | RDP | Ouverture de session à distance |
| 5985 / 5986/TCP | WinRM (HTTP / HTTPS) | Exécution de commandes à distance |
| 135/TCP | RPC (WMI, DCOM) | Exécution à distance |
| 5355/UDP · 137/UDP · 5353/UDP | LLMNR · NBT-NS · mDNS | Résolution par diffusion, captation d'authentifications |
| 80/TCP (`wpad.<domaine>`) | WPAD, fichier PAC | Faux proxy |
| 389 / 636/TCP | LDAP / LDAPS | Cible de relais vers l'annuaire |
| 67/68 · 546/547/UDP | DHCP · DHCPv6 | Faux serveur qui impose son DNS |
