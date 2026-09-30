---
title: Chapitre 13 — Fraude en ligne, ingénierie sociale et flux financiers illicites
source: Cyber/01_CTI/EtatdeLart_Panorama_Cybermenace.md
note: État de l'art — panorama de la cybermenace
up:
- - État de l'art — panorama de la cybermenace
  - ../index.md
- - 'PARTIE III — L''écosystème cybercriminel : une industrie de la menace'
  - index.md
---

## 13.1 — Panorama des fraudes

Le FBI IC3 documente un paysage de fraude en ligne massif. L'**investment fraud** (arnaques à l'investissement, principalement liées aux cryptomonnaies) représente les pertes les plus élevées. Le **BEC/CEO fraud** (compromission de messagerie professionnelle pour détourner des virements) reste l'une des fraudes les plus rentables par incident. Les **romance scams** et le **pig butchering** (arnaques sentimentales à long terme culminant dans une arnaque d'investissement) sont en forte croissance, exploitant les plateformes de rencontres et les réseaux sociaux.

Les pertes totales déclarées au FBI IC3 est de **20,877 milliards de dollars** en 2025 — un chiffre qui ne représente qu'une fraction de la réalité mondiale, le FBI ne couvrant que les plaintes américaines.

## 13.2 — Phishing industrialisé et contournement MFA

Le phishing s'est industrialisé via le modèle **Phishing-as-a-Service (PhaaS)**. Les kits PhaaS fournissent des templates de pages de phishing, l'infrastructure d'hébergement, et des mécanismes de collecte de credentials — le tout accessible via un abonnement ou un paiement unique. L'innovation la plus significative est les kits **Adversary-in-the-Middle (AitM)** qui capturent non seulement les credentials mais aussi les tokens de session, permettant de contourner l'authentification multi-facteurs. Des kits comme **Sneaky 2FA** automatisent ce processus pour cibler spécifiquement les environnements Microsoft 365.

Le **vishing** (voice phishing) augmenté par IA représente une escalade qualitative. Les deepfakes vocaux permettent de cloner la voix d'un dirigeant à partir de quelques minutes d'enregistrement audio (disponibles sur YouTube, les podcasts, les conférences). Le cas documenté d'une fraude de 25 millions USD à Hong Kong — où un employé financier a effectué un virement après un appel vidéo avec un deepfake de son directeur financier — illustre le potentiel de cette technique.

## 13.3 — LLMs malveillants et IA offensive

L'écosystème cybercriminel a développé ses propres outils d'IA générative. **WormGPT**, **FraudGPT** et **Xanthorox AI** sont des LLMs modifiés ou créés pour assister les cybercriminels — générer des emails de phishing convaincants, créer des malwares, rédiger des scripts d'arnaque. Ces outils vont du simple jailbreak de modèles légitimes à des systèmes autonomes avec leurs propres modèles de langage.

Le FBI note que les cybercriminels « utilisent de plus en plus l'IA pour augmenter la qualité et l'efficacité de leurs attaques ». Le CERT-EU anticipe pour 2026 une augmentation de l'ingénierie sociale multi-canal assistée par IA — combinant email, voix et SMS dans des attaques coordonnées.

## 13.4 — Cryptomonnaies et blanchiment

Les cryptomonnaies sont le système circulatoire de l'écosystème cybercriminel. Le Bitcoin reste le medium principal pour les paiements de rançon, mais les monnaies à confidentialité renforcée (Monero) sont de plus en plus demandées. Les mécanismes de blanchiment incluent les **mixers** (services qui mélangent les transactions pour obscurcir la traçabilité), les **services de swap** (échange entre cryptomonnaies), et les **underground banking services** qui convertissent les cryptomonnaies en fiat.

Les outils d'analyse blockchain (Chainalysis, TRM Labs) ont considérablement amélioré les capacités de traçage. Cependant, leurs capacités ont des limites : les techniques de mixing avancées, les ponts cross-chain et les échanges décentralisés (DEX) compliquent le traçage. Le cadre réglementaire évolue : le règlement MiCA en Europe et la Travel Rule imposent des obligations de transparence aux échanges de cryptomonnaies.

Le modèle nord-coréen illustre le financement étatique par la cybercriminalité : les vols de cryptomonnaies attribués à Lazarus représentent certaines des plus grosses pertes individuelles de l'histoire de la crypto, les fonds étant utilisés pour financer les programmes d'armement de la RPDC en contournement des sanctions internationales.

## 13.5 — 🔴 Fil rouge : campagne de spearphishing augmenté IA

> **📌 FIL ROUGE — Épisode 13**
>
> En août 2025, trois cadres C-level d'EuroDefense reçoivent des appels téléphoniques apparemment du directeur financier du groupe, leur demandant de valider d'urgence un virement lié à une acquisition confidentielle. La voix est convaincante — mais le directeur financier est en vacances et n'a passé aucun appel.
>
> L'analyse révèle un deepfake vocal généré à partir d'enregistrements de conférences publiques du directeur financier. Le numéro d'appel est spoofé. Le scénario est soigneusement construit : acquisition confidentielle = urgence + confidentialité = pression à ne pas vérifier.
>
> Un seul des trois cadres a commencé le processus de validation avant de vérifier par un canal alternatif. Aucun virement n'a été effectué. Sophie rédige un bulletin d'alerte interne et recommande l'implémentation d'un protocole de vérification systématique pour tout virement supérieur à un seuil défini — y compris un callback sur un numéro pré-enregistré, jamais sur le numéro entrant.

---
