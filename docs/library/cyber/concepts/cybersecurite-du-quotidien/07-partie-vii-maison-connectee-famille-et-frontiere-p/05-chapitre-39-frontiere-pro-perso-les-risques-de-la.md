---
title: 'Chapitre 39 — Frontière pro/perso : les risques de la porosité'
source: Cyber/11 Concepts/Au quotidien/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - ../index.md
- - Partie VII — Maison connectée, famille et frontière pro/perso
  - index.md
---

Le **téléphone perso avec usages pro** (BYOD) : les emails pro sur le téléphone perso = si le téléphone perso est compromis (malware, vol, perte), les données pro le sont aussi. Le **cloud perso pour les documents pro** : envoyer un fichier pro sur Google Drive perso pour « travailler ce weekend » → le document pro est maintenant dans un cloud personnel potentiellement moins sécurisé que le cloud d'entreprise, sans les contrôles de sécurité de l'entreprise (DLP, audit, chiffrement). Les **messageries non prévues** : discuter d'un projet client sur WhatsApp perso, envoyer un devis par iMessage, partager un fichier via un lien Dropbox personnel → les données pro circulent sur des canaux non maîtrisés par l'entreprise, non archivés, non auditables. L'**impression à domicile** : imprimer un document confidentiel chez soi → le document est dans la corbeille à papier, dans la mémoire de l'imprimante, et potentiellement visible par les membres du foyer.

Le **risque dans les deux sens** : le perso contamine le pro (malware sur le téléphone perso → accès aux emails pro) et le pro contamine le perso (l'entreprise a un droit de regard sur le téléphone BYOD en cas d'incident → les données personnelles sont potentiellement accessibles dans le cadre d'une investigation). Le cas des **outils IA** est devenu central : coller un document client dans ChatGPT pour le résumer = exfiltrer ce document hors du périmètre de l'entreprise (cf. Ch.27).

Le réflexe : séparer les mots de passe (ne JAMAIS réutiliser un mot de passe entre un compte pro et un compte perso), ne pas synchroniser les comptes pro et perso sur le même appareil sans mesures de protection (conteneurisation, profil séparé), connaître la politique de l'entreprise (certaines entreprises ont des outils de MDM — Mobile Device Management — qui donnent un accès à distance au téléphone BYOD), et ne pas confondre « plus pratique » avec « autorisé ». Si l'entreprise n'a pas mis en place le bon outil pour un usage légitime, c'est un sujet à remonter à la DSI, pas à contourner par un outil personnel.

---

<a id="chapitre-40"></a>
