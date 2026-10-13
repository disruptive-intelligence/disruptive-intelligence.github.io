---
title: "Forensic"
---
# Forensic

Des procédures, dans l'ordre où on les déroule. Elles reprennent les entrées des fiches système (Linux,
Windows) — écrites une seule fois — et ajoutent ce qui est propre à l'investigation : préserver, calculer
les empreintes, chercher la persistance, lire les traces.

## Carte mentale

<div class="kw-mindmap" markdown>

- **Investiguer une machine**
    - Principes
        - Ordre de volatilité : mémoire → réseau → processus → disque
        - Noter l'heure en UTC : `date -u`
        - Binaires de confiance, depuis la clé de collecte
        - Écrire sur un support externe, jamais sur la machine
        - Sceller : empreintes `sha256sum` en dernier
    - [Linux : triage à chaud](linux/triage-a-chaud/index.md)
        - [Avant tout](linux/triage-a-chaud/index.md#ouvrir-un-dossier-de-collecte-et-noter-lheure) : dossier de collecte, heure
        - [Processus](linux/triage-a-chaud/processus.md)
            - Arbre : `ps auxf`
            - Effacés du disque : `ls -l /proc/*/exe | grep deleted`
            - Lancé depuis `/tmp`, `/dev/shm` : suspect
            - [Préserver le binaire](linux/triage-a-chaud/processus.md#preserver-le-binaire-dun-processus-suspect) : `cp /proc/<PID>/exe`
        - [Réseau](linux/triage-a-chaud/reseau.md)
            - Écoute et connexions : `ss -tunap`
            - Interfaces, routes, voisins : `ip -br a` · `ip r` · `ip neigh`
            - Port sortant inhabituel : `4444`, `1337`…
        - [Persistance](linux/triage-a-chaud/persistance.md)
            - cron : `/etc/cron*`, `/var/spool/cron`
            - systemd : services et timers récents
            - Connexion : `~/.bashrc`, `/etc/profile.d`
            - SSH : `~/.ssh/authorized_keys`
            - Comptes d'UID 0 autres que root
        - [Traces d'activité](linux/triage-a-chaud/traces.md)
            - Connexions : `last` · `lastb` · `auth.log`
            - [Historiques](linux/triage-a-chaud/traces.md#lire-lhistorique-des-commandes-des-utilisateurs) : `~/.bash_history`
            - Fichiers récents : `find / -xdev -mmin -120`
        - [Clore la collecte](linux/triage-a-chaud/cloture.md#calculer-les-empreintes-de-la-collecte) : `sha256sum ./*`
    - [Windows : artefacts](windows/artefacts/index.md)
        - [Collecter d'un coup](windows/artefacts/index.md#recuperer-les-artefacts-dun-coup) : KAPE
        - [Exécuté ?](windows/artefacts/execution.md)
            - [Prefetch](windows/artefacts/execution.md#savoir-quels-programmes-ont-ete-lances-prefetch) : lancé, combien de fois, quand
            - [BAM](windows/artefacts/execution.md#savoir-qui-a-lance-quoi-et-quand-en-dernier-bam) : qui, dernière exécution
            - [Amcache](windows/artefacts/execution.md#retrouver-les-executables-presents-sur-le-disque-amcache) · [ShimCache](windows/artefacts/execution.md#voir-les-executables-connus-du-systeme-shimcache) : présent, pas forcément lancé
            - [SRUM](windows/artefacts/execution.md#mesurer-lactivite-reseau-par-application-srum) : octets par application
            - 4688 : processus créé
        - [Ouvert ?](windows/artefacts/fichiers-ouverts.md)
            - [LNK](windows/artefacts/fichiers-ouverts.md#retrouver-les-fichiers-ouverts-recemment-lnk) · [Jump Lists](windows/artefacts/fichiers-ouverts.md#voir-les-fichiers-recents-de-chaque-application-jump-lists) : fichiers récents
            - [Shellbags](windows/artefacts/fichiers-ouverts.md#savoir-quels-dossiers-ont-ete-parcourus-shellbags) : dossiers parcourus
            - [RunMRU, TypedPaths](windows/artefacts/fichiers-ouverts.md#lire-les-commandes-tapees-et-les-chemins-saisis-runmru-typedpaths) : saisies
        - [USB ?](windows/artefacts/usb.md)
            - [USBSTOR](windows/artefacts/usb.md#lister-les-cles-usb-branchees-et-leur-numero-de-serie-usbstor) : clé et numéro de série
            - `setupapi.dev.log` : premier branchement
            - Ce qui a été copié : croiser avec LNK et Shellbags
        - [Connecté ?](windows/artefacts/connexions.md)
            - [Sessions](windows/artefacts/connexions.md#retrouver-les-ouvertures-de-session-reussies-ou-non) : 4624 / 4625 + type de logon
            - RDP reçu : 1149, 21, 24, 25
            - [RDP émis](windows/artefacts/connexions.md#retrouver-les-serveurs-rdp-contactes-depuis-un-poste-registre-et-fichiers) : 1102, 4648, registre du client
        - [Supprimé ?](windows/artefacts/suppressions.md)
            - [Corbeille](windows/artefacts/suppressions.md#retrouver-ce-qui-est-passe-par-la-corbeille) : `$I` (métadonnées) · `$R` (contenu)
            - [Clichés VSS](windows/artefacts/suppressions.md#remonter-dans-le-temps-avec-les-cliches-instantanes-vss) : version antérieure
        - [Se relance ?](windows/artefacts/persistance.md#lister-ce-qui-se-relance-tout-seul)
            - Clés `Run` · services (7045) · tâches (4698) · WMI
    - [Réseau : journaux](reseau/journaux/index.md)
        - [Pare-feu, NetFlow, VPN](reseau/journaux/pare-feu-vpn.md)
            - [Scan de ports](reseau/journaux/pare-feu-vpn.md#reperer-un-scan-de-ports) : beaucoup de ports, une source
            - [Volume sortant](reseau/journaux/pare-feu-vpn.md#mesurer-le-volume-envoye-vers-chaque-destination) : exfiltration ?
            - [Sessions VPN](reseau/journaux/pare-feu-vpn.md#retracer-les-connexions-vpn-dun-utilisateur) d'un utilisateur
        - [Proxy et DNS](reseau/journaux/proxy-dns.md)
            - [Gros envois](reseau/journaux/proxy-dns.md#reperer-les-plus-gros-envois)
            - [Tunneling DNS](reseau/journaux/proxy-dns.md#reperer-un-tunneling-dns) : sous-domaines longs
            - [DGA](reseau/journaux/proxy-dns.md#reperer-un-malware-a-dga-rafales-de-nxdomain) : rafales de NXDOMAIN
        - [IDS / IPS et WAF](reseau/journaux/ids-waf.md)
            - [Alertes par signature](reseau/journaux/ids-waf.md#compter-les-alertes-par-signature-et-par-source)
            - [Ce que le WAF a laissé passer](reseau/journaux/ids-waf.md#retrouver-dans-les-logs-web-ce-que-le-waf-a-laisse-passer)
        - [Logs web](reseau/journaux/web.md)
            - [Top des IP](reseau/journaux/web.md#reperer-les-ip-qui-envoient-le-plus-de-requetes) : `sort | uniq -c | sort -rn`
            - [Injections, traversées](reseau/journaux/web.md#chercher-des-injections-et-des-traversees-de-repertoire) : `grep -E`
            - [Brute force](reseau/journaux/web.md#reperer-un-brute-force-sur-une-page-de-connexion) : rafales de POST
            - Zeek `http.log` : `zeek-cut`

</div>



## [Linux](linux/index.md)

- [Triage à chaud](linux/triage-a-chaud/index.md) — [processus](linux/triage-a-chaud/processus.md), [réseau](linux/triage-a-chaud/reseau.md), [persistance](linux/triage-a-chaud/persistance.md), [traces d'activité](linux/triage-a-chaud/traces.md), [clore la collecte](linux/triage-a-chaud/cloture.md).

## [Windows](windows/index.md)

- [Artefacts Windows](windows/artefacts/index.md) — [exécution](windows/artefacts/execution.md), [fichiers ouverts](windows/artefacts/fichiers-ouverts.md), [USB](windows/artefacts/usb.md), [suppressions](windows/artefacts/suppressions.md), [connexions et RDP](windows/artefacts/connexions.md), [persistance](windows/artefacts/persistance.md) : où chercher et avec quoi lire.

## [Réseau](reseau/index.md)

- [Journaux réseau](reseau/journaux/index.md) — [pare-feu, NetFlow et VPN](reseau/journaux/pare-feu-vpn.md), [proxy et DNS](reseau/journaux/proxy-dns.md), [IDS / IPS et WAF](reseau/journaux/ids-waf.md), [logs web](reseau/journaux/web.md) : retrouver une attaque dans les journaux des équipements réseau.
