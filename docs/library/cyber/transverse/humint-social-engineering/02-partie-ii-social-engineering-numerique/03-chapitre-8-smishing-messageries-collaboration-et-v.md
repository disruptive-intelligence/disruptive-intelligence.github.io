---
title: Chapitre 8 — Smishing, messageries, collaboration et vecteurs alternatifs
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - Partie II — Social engineering numérique
  - index.md
---

## 8.1 SMS et smishing

Le smishing (SMS phishing) exploite les spécificités du canal SMS : messages courts, contexte limité, URLs raccourcies qui masquent la destination réelle, et confiance instinctive dans les SMS (perçus comme plus personnels et plus fiables que les emails). Le spoofing d'expéditeur SMS (sender ID spoofing) permet d'afficher un nom d'entreprise (« Helios-RH », « IT-Support ») au lieu d'un numéro, ce qui renforce la crédibilité.

Les pretextes classiques incluent : notification de livraison avec lien de suivi, alerte bancaire avec demande de vérification, message RH sur les congés ou la paie, et alerte de sécurité (« accès suspect à votre compte »). Les taux de clic sur SMS sont généralement supérieurs à ceux sur email, parce que les utilisateurs mobiles sont moins entraînés à la vigilance sur ce canal et que les indicateurs de fraude (URL complète, en-têtes, adresse d'expéditeur) sont moins visibles sur un écran de smartphone.

## 8.2 Messageries chiffrées et réseaux sociaux

WhatsApp, Signal, Telegram et les messageries intégrées des réseaux sociaux sont devenus des vecteurs de social engineering à part entière. Leur utilisation par les attaquants s'explique par plusieurs facteurs : le chiffrement de bout en bout complique la surveillance et l'analyse par les équipes de sécurité, le sentiment de confidentialité encourage le partage d'informations sensibles, et les fonctionnalités de messages éphémères réduisent les traces.

**LinkedIn InMail** est le vecteur de choix pour le ciblage professionnel. Les faux recruteurs (vecteur utilisé par le groupe APT Lazarus dans l'opération « Dream Job » et par des services de renseignement pour l'élicitation) exploitent la norme de la plateforme : recevoir un InMail d'un recruteur est un événement normal et positif sur LinkedIn. La transition vers WhatsApp ou Signal (« pour discuter plus librement ») isole la cible du contexte professionnel et élimine les contrôles de la plateforme.

**Les groupes** sur Telegram, Discord et WhatsApp sont exploités pour le social engineering de masse ciblé : infiltrer un groupe professionnel ou communautaire permet de gagner de la crédibilité par la présence dans un espace de confiance, de collecter de l'information en écoutant les conversations, et d'approcher des cibles individuelles avec un pretexte renforcé (« on est dans le même groupe sur le forum X »).

## 8.3 Suites collaboratives : Teams, Slack, Google Workspace

Les plateformes de collaboration d'entreprise sont devenues des vecteurs de social engineering majeurs depuis la généralisation du travail hybride. Le rapport Unit 42 2025 documente plusieurs cas d'intrusions initiées via ces plateformes.

**Microsoft Teams.** L'ouverture des communications externes (External Access) permet à un attaquant d'envoyer des messages à des employés depuis un tenant Microsoft 365 externe. L'interface Teams affiche un avertissement « externe » souvent ignoré. Les pretextes incluent : partage de document « urgent » (lien vers une landing page de phishing), invitation à une réunion (lien Zoom/Meet malveillant), et prise de contact par un faux collègue d'un autre site ou d'un partenaire.

**Faux partages de documents.** Les notifications OneDrive/SharePoint/Google Drive « [Nom] a partagé un document avec vous » sont exploitées pour le phishing. L'attaquant crée un document sur sa propre instance et le partage avec la cible. Le lien pointe vers une page de connexion légitime (Microsoft ou Google) qui capture les identifiants ou les tokens de session. La difficulté est que le mécanisme de partage est identique au mécanisme légitime — seule l'analyse de l'expéditeur et du contexte permet de distinguer un partage légitime d'un phishing.

**OAuth consent phishing (consent grant attack).** L'attaquant crée une application OAuth malveillante qui demande des permissions d'accès au compte de la cible (lecture des emails, accès aux fichiers, accès au calendrier). La cible est redirigée vers une page de consentement légitime (Microsoft ou Google) et autorise l'accès — l'attaquant obtient alors un token d'accès persistant qui survit au changement de mot de passe et au MFA. Cette technique est particulièrement insidieuse parce que la page de consentement est une page légitime de Microsoft ou Google, pas une page de phishing. La défense repose sur la restriction des applications tierces autorisées (Azure AD : désactiver le consentement utilisateur, imposer l'approbation admin) et la surveillance des grants OAuth.

**Faux bots et automatisations.** Les plateformes comme Slack et Teams permettent l'intégration de bots et de workflows automatisés. Un attaquant qui compromet un workspace ou obtient un accès admin peut créer un faux bot (« Security-Bot », « HR-Assistant ») qui collecte des informations auprès des employés sous un pretexte automatisé.

## 8.4 QR codes malveillants (quishing)

Le quishing exploite les QR codes comme vecteur de redirection. L'utilisation massive des QR codes depuis 2020 (menus de restaurant, documents administratifs, affiches événementielles) a normalisé le scan de QR codes inconnus — ce qui constitue un vecteur d'attaque sous-estimé.

Les vecteurs de distribution incluent : QR codes physiques collés sur des panneaux légitimes (parking d'entreprise, accueil, salles de réunion), QR codes inclus dans des emails de phishing (contournant les filtres URL qui ne scannent pas les images), QR codes dans des documents imprimés (faux courriers RH, fausses affiches d'événement). La redirection pointe vers une landing page de credential harvesting ou un téléchargement de malware mobile.

La défense passe par la sensibilisation (ne pas scanner de QR code sans vérifier l'URL de destination — les smartphones modernes affichent l'URL avant la navigation), l'utilisation de QR codes sécurisés pour les communications légitimes de l'entreprise, et l'inspection physique régulière des QR codes affichés dans les locaux.

## 8.5 Social engineering multi-canal

La combinaison de plusieurs vecteurs dans une même opération augmente considérablement la crédibilité et le taux de succès. Le schéma typique est : email préparatoire → appel téléphonique → SMS de confirmation, ou approche LinkedIn → transition WhatsApp → appel téléphonique → demande par email.

Chaque canal renforce la crédibilité du précédent. Un email seul peut être analysé froidement. Mais un email suivi d'un appel téléphonique (« je vous appelle suite à l'email que je vous ai envoyé ce matin ») crée un effet de convergence qui désarme la vigilance — la cible perçoit une cohérence entre deux canaux distincts, ce qui renforce la perception de légitimité. Le rapport Unit 42 2025 documente cette hybridation croissante des tactiques où les techniques conventionnelles de social engineering sont de plus en plus complétées par des composantes multi-canaux.

---
