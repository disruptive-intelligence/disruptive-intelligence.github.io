---
title: 'Chapitre 7 — Vishing : l''arme de la voix'
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie II — Social engineering numérique
  - index.md
---

## 7.1 Pourquoi le vishing est plus dangereux que le phishing

Le vishing (voice phishing) est, de l'avis consensuel des praticiens de red team, le vecteur de social engineering le plus efficace. Plusieurs facteurs expliquent cette efficacité supérieure au phishing par email.

La voix crée un lien personnel et immédiat. Un email est un objet passif que le destinataire peut analyser à son rythme, comparer avec des exemples connus, transférer à un collègue pour avis. Un appel téléphonique est une interaction en temps réel qui engage émotionnellement le destinataire et ne lui laisse pas le temps de la réflexion distanciée.

La pression est exercée en temps réel. L'attaquant ajuste son discours en fonction des réponses de la cible : s'il perçoit une hésitation, il renforce l'urgence ; s'il perçoit de la méfiance, il change d'angle ; s'il perçoit de la coopération, il escalade. Cette adaptabilité en temps réel est impossible par email.

L'autorité vocale est puissante. Un ton assuré, un vocabulaire technique maîtrisé, un rythme de parole contrôlé projettent une autorité que le texte écrit reproduit difficilement. L'expérience de Milgram a démontré que la présence physique (ou vocale) de la figure d'autorité augmente significativement la compliance.

La documentation est plus difficile. Un email suspect peut être transféré au SOC pour analyse (headers, URLs, pièces jointes). Un appel téléphonique ne laisse pas de trace exploitable (sauf enregistrement — qui pose des questions légales dans de nombreuses juridictions). Le signalement d'un appel suspect repose sur la mémoire et le récit de l'employé.

## 7.2 Les pretextes classiques du vishing

Les pretextes de vishing les plus efficaces exploitent des situations où un appel téléphonique est attendu ou normal.

**Le support IT.** « Bonjour, je suis Paul de l'équipe support informatique. Nous avons détecté une activité suspecte sur votre compte — je dois vérifier quelques informations avec vous pour sécuriser votre accès. » Ce pretexte est redoutablement efficace parce qu'il combine autorité (IT), urgence (activité suspecte) et bienveillance (sécuriser votre compte). Le rapport Unit 42 2025 documente de nombreux cas où ce pretexte a permis le reset de credentials MFA via le helpdesk.

**Le prestataire ou fournisseur.** Après avoir identifié le prestataire IT par OSINT, l'attaquant se présente comme un technicien de ce prestataire pour une intervention planifiée ou d'urgence. La crédibilité est renforcée par la connaissance du nom du prestataire, du contrat en cours, des interlocuteurs habituels.

**La direction.** « Bonjour, je suis l'assistante de Marc Tessier. Il est en déplacement et il a besoin que vous fassiez un virement urgent — je vous envoie les coordonnées par email. » La combinaison appel + email (social engineering multi-canal, détaillé au Ch.8) renforce la crédibilité.

**Le recruteur.** Approche LinkedIn suivie d'un appel : « Suite à votre profil que j'ai trouvé très intéressant, j'ai une opportunité confidentielle à vous présenter. » Ce pretexte est le vecteur préféré des groupes APT comme Lazarus (opération « Dream Job ») et des services de renseignement pour l'élicitation (voir Ch.3 et Ch.17).

## 7.3 Techniques vocales

La voix est un outil qui se travaille. Les red teamers expérimentés maîtrisent plusieurs techniques vocales qui augmentent l'efficacité du vishing.

**Le matching de ton.** Adapter son registre au profil de la cible : formel et technique avec un ingénieur, chaleureux et empathique avec une réceptionniste, directif et pressé avec un cadre. Le ton doit être cohérent avec le pretexte — un technicien IT qui parle comme un commercial ou un DG qui parle comme un stagiaire crée une dissonance cognitive qui active la vigilance.

**Le name-dropping.** Mentionner des noms de personnes réelles de l'organisation (collectés par OSINT) est l'un des marqueurs de crédibilité les plus puissants. « Frédéric Morin m'a demandé de vous appeler » ou « j'ai vu avec Lucie Ferraro hier » crée un lien implicite avec l'organisation qui désarme la méfiance.

**Le « oui building ».** Commencer par des questions auxquelles la réponse est évidemment « oui » (« c'est bien le poste de [nom] ? », « vous êtes bien dans le service [service] ? ») avant d'escalader vers la demande réelle. Chaque « oui » renforce l'engagement de la cible dans la conversation (principe d'engagement et de cohérence, Ch.2).

**Le silence stratégique.** Après avoir posé une question sensible, ne pas combler le silence. La plupart des gens sont mal à l'aise avec le silence dans une conversation téléphonique et le comblent en parlant — souvent en fournissant plus d'information que ce qui leur était demandé. Le silence est l'une des techniques d'élicitation les plus sous-estimées.

## 7.4 Caller ID spoofing

Le caller ID spoofing permet à l'attaquant d'afficher un numéro de téléphone arbitraire sur l'écran de la cible. Des services en ligne (SpoofCard, SpoofTel — attention, l'usage est réglementé dans de nombreuses juridictions et interdit pour fraude) et des services VoIP configurables permettent de simuler le numéro du standard de l'entreprise, du prestataire IT ou même du supérieur hiérarchique.

Le protocole STIR/SHAKEN (Secure Telephony Identity Revisited / Signature-based Handling of Asserted information using toKENs), déployé aux États-Unis depuis 2021 et en cours de déploiement en Europe, vise à authentifier l'identité de l'appelant au niveau du réseau téléphonique. En 2025, son déploiement reste inégal et contournable dans certains contextes (appels internationaux, réseaux VoIP non conformes). La contre-mesure la plus fiable reste le callback de vérification : ne jamais agir sur la base d'un appel entrant sans rappeler l'interlocuteur sur un numéro de référence connu (annuaire interne, site web officiel).

## 7.5 Le vishing AI-enabled : deepfake vocal

Le clonage vocal par IA représente la menace émergente la plus sérieuse en matière de vishing. En 2025, plusieurs plateformes permettent de cloner une voix à partir d'échantillons de quelques secondes à quelques minutes (ElevenLabs, Respeecher, technologies open source). La qualité est suffisante pour tromper un interlocuteur non prévenu dans un appel téléphonique standard.

Les cas documentés se multiplient. En 2024, une entreprise de Hong Kong a perdu 25 millions de dollars dans une fraude utilisant un deepfake vidéo et vocal du CFO en visioconférence (plusieurs « participants » étaient des deepfakes en temps réel). Des cas de vishing par deepfake vocal ciblant des DAF pour des virements urgents ont été rapportés par plusieurs cabinets d'incident response.

Les défenses sont encore immatures. Les détecteurs de deepfake vocal existent mais sont peu fiables en conditions réelles (environnement bruité, compression téléphonique, variété des technologies de synthèse). La défense la plus efficace reste procédurale : pour toute demande sensible (virement, reset de credentials, communication d'informations confidentielles), imposer une vérification out-of-band (callback sur numéro connu, confirmation par un second canal, validation hiérarchique). La technologie seule ne suffit pas — le processus est la dernière ligne de défense.

---
