---
title: Annexe B — Cheat sheets outils
source: Cyber/03_Forensic/Digital_Forensics.md
note: Digital forensics
up:
- - Digital forensics
  - ../index.md
- - Annexes
  - index.md
---

## Acquisition disque

```bash
# dd (basique)
dd if=/dev/sdX of=/path/image.raw bs=4M status=progress

# dc3dd (avec hashing et logging)
dc3dd if=/dev/sdX hof=/path/image.dd hash=md5 hash=sha256 log=/path/log.txt

# FTK Imager (ligne de commande Linux)
ftkimager /dev/sdX /path/image --e01 --compress 6 --frag 4G --verify
```


## Acquisition mémoire

```bash
# DumpIt (Windows — double-clic ou CLI)
DumpIt.exe /OUTPUT /path/memory.dmp

# WinPmem (Windows)
winpmem_mini_x64.exe /path/memory.raw

# LiME (Linux)
insmod lime.ko "path=/path/memory.lime format=lime"
```


## Volatility 3

```bash
# Triage rapide
vol -f memory.raw windows.pstree
vol -f memory.raw windows.netscan
vol -f memory.raw windows.cmdline

# Investigation injection
vol -f memory.raw windows.malfind
vol -f memory.raw windows.dlllist --pid 7284

# Credentials
vol -f memory.raw windows.hashdump
vol -f memory.raw windows.lsadump

# Extraction
vol -f memory.raw windows.procdump --pid 7284 --dump-dir output/
vol -f memory.raw windows.dumpfiles --pid 7284 --dump-dir output/
```


## Eric Zimmerman tools

```bash
# MFT (timestamps, timestomping detection)
MFTECmd.exe -f '$MFT' --csv output/ --csvf mft.csv

# Prefetch (exécution de programmes)
PECmd.exe -d 'C:\Windows\Prefetch' --csv output/ --csvf prefetch.csv

# Amcache (programmes avec hash)
AmcacheParser.exe -f Amcache.hve --csv output/ --csvf amcache.csv

# ShimCache (historique d'exécution)
AppCompatCacheParser.exe -f SYSTEM --csv output/ --csvf shimcache.csv

# ShellBags (navigation explorateur)
SBECmd.exe -d 'C:\Users\JMallet' --csv output/ --csvf shellbags.csv

# LNK files (fichiers récents, chemins réseau)
LECmd.exe -d 'C:\Users\JMallet\AppData\Roaming\Microsoft\Windows\Recent' --csv output/

# Jump Lists
JLECmd.exe -d 'AutomaticDestinations' --csv output/

# Event Logs
EvtxECmd.exe -f Security.evtx --csv output/ --csvf security.csv

# Registre (batch)
RECmd.exe -d 'C:\evidence\registry' --bn RECmd_Batch_MC.reb --csv output/

# SRUM (consommation réseau)
SrumECmd.exe -f SRUDB.dat -r SOFTWARE --csv output/
```


## Plaso (Super Timeline)

```bash
# Extraction
log2timeline.py --storage-file timeline.plaso image.E01

# Filtrage et export
psort.py -o l2tcsv timeline.plaso -w timeline.csv \
  "date > '2026-01-01' AND date < '2026-03-08'"
```


## KAPE

```bash
# Triage complet
kape.exe --tsource C: --tdest E:\Output --target KapeTriage

# Collecte + parsing
kape.exe --tsource C: --tdest E:\Output --target KapeTriage \
  --mdest E:\Parsed --module !EZParser
```


## Réseau

```bash
# Capture tcpdump
tcpdump -i eth0 -w capture.pcap -c 1000000

# Filtrage Wireshark (CLI avec tshark)
tshark -r capture.pcap -Y "ip.addr == 103.xx.xx.xx" -w filtered.pcap

# Zeek
zeek -r capture.pcap local
# Résultat : conn.log, dns.log, http.log, ssl.log, files.log
```


## Hashing

```bash
# Double hash (Linux)
md5sum image.E01 && sha256sum image.E01

# Hash récursif (hashdeep)
hashdeep -r -c md5,sha256 /path/evidence/ > hashes.txt

# Vérification
hashdeep -r -k hashes.txt -a /path/evidence/
```


---
