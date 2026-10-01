---
title: Partie III — Mobilité, espaces publics et risques physiques
source: Cyber/11 Concepts/Cybersécurité du quotidien.md
note: Cybersécurité du quotidien
up:
- - Cybersécurité du quotidien
  - index.md
---

*Les risques de la mobilité — Wi-Fi public, recharge, QR codes, Bluetooth, voyage. Chaque situation crée une exposition temporaire mais réelle.*

---

<a id="chapitre-11"></a>

## Chapitre 11 — Wi-Fi public : risques réels et bons réflexes

Le Wi-Fi public (café, hôtel, aéroport, train, coworking) est pratique mais intrinsèquement risqué. Les risques réels — ni paranoïa ni naïveté.

Le **Evil Twin** : un faux hotspot qui porte le même nom que le Wi-Fi légitime — « Starbucks_WiFi_Free » à côté du vrai « Starbucks WiFi ». Le téléphone ou l'ordinateur se connecte au faux point d'accès, et tout le trafic passe par l'attaquant. La différence n'est pas visible pour l'utilisateur. Le **portail captif piégé** : la page de connexion du Wi-Fi (celle qui s'affiche quand on se connecte et qui demande d'accepter les conditions ou de s'identifier) peut être falsifiée pour demander un email et un mot de passe — un portail malveillant capture ces informations. L'**écoute locale** : sur un Wi-Fi ouvert (non chiffré), le trafic non HTTPS est lisible par quiconque sur le même réseau. En 2025, la majorité du trafic web est HTTPS (le cadenas dans la barre d'adresse), mais certaines applications et certains sites utilisent encore des connexions non chiffrées.

Les **bons réflexes** : préférer le partage de connexion 4G/5G depuis le téléphone (le réseau mobile est beaucoup plus sûr que le Wi-Fi public — c'est le premier réflexe à acquérir), ne JAMAIS se connecter à un Wi-Fi ouvert pour des opérations sensibles (banque, email, achats — même avec un VPN, le risque existe), vérifier que le cadenas HTTPS est présent dans la barre d'adresse, et « oublier » le réseau après utilisation (sinon le téléphone s'y reconnectera automatiquement la prochaine fois).

Le **VPN** : un VPN chiffre le trafic entre l'appareil et le serveur VPN. Il protège contre l'écoute sur le Wi-Fi public. Mais un VPN ne protège PAS contre le phishing, les malwares, les sites malveillants, ni le social engineering. Et un VPN gratuit est souvent pire que pas de VPN — le fournisseur du VPN gratuit voit tout le trafic et peut le monétiser. Si un VPN est nécessaire, utiliser un fournisseur payant réputé (ProtonVPN, Mullvad). Le faux sentiment de sécurité : « j'ai un VPN donc je suis protégé » → le VPN protège le canal, pas l'utilisateur.

---

<a id="chapitre-12"></a>

## Chapitre 12 — Recharge, USB, QR codes et pièges de proximité

Les **ports de recharge publics** (aéroport, gare, hôtel — juice jacking) : un port USB public peut théoriquement être modifié pour extraire des données ou installer un malware quand on y branche son téléphone. Le risque est faible en pratique (peu de cas documentés), mais le réflexe est simple et gratuit : utiliser son propre chargeur secteur (prise murale), ou un câble charge-only / data-blocker (un câble ou un adaptateur qui ne transmet que l'alimentation, pas les données). Les **câbles trafiqués** (O.MG Cable — un câble USB qui contient un implant informatique miniaturisé ; prix de vente ~200 $) : ne pas utiliser un câble trouvé, offert par un inconnu, ou abandonné dans un lieu public. Les **périphériques inconnus** : ne JAMAIS brancher une clé USB trouvée sur son ordinateur. Les clés USB piégées (BadUSB) sont un vecteur d'attaque classique — la clé se fait passer pour un clavier et tape des commandes malveillantes en quelques secondes.

Les **QR codes** — le quishing : un QR code malveillant redirige vers un site de phishing. Le risque principal : les faux QR codes **collés par-dessus les vrais** (parkings, restaurants, bornes de recharge de véhicules électriques, affiches, tables de restaurant). Un autocollant avec un QR code frauduleux est collé sur le QR code légitime — visuellement indiscernable. La méthode de vérification : scanner le QR code, le téléphone affiche l'URL de destination → vérifier que l'URL correspond au contexte (le QR code du parking devrait pointer vers le site de la société de stationnement, pas vers « parking-paiement-securise.com »). Ne JAMAIS entrer des informations bancaires via un QR code scanné dans un lieu public sans avoir vérifié l'URL.

Le **NFC** (paiement sans contact) : le risque de lecture à distance d'une carte bancaire NFC existe en théorie mais est extrêmement faible en pratique (les montants sont plafonnés, la distance de lecture est de quelques centimètres, et les transactions nécessitent un terminal de paiement enregistré). Le vrai risque NFC est plus simple : un terminal de paiement dont le montant a été modifié, ou un paiement sans contact accidentel → toujours vérifier le montant affiché sur le terminal avant de taper.

> **🔵 Lina — Épisode 5 :** Lina scanne un QR code sur une borne de parking à Marseille pour payer le stationnement. Le QR code est un autocollant collé par-dessus le vrai. Elle est redirigée vers un faux site de paiement qui imite parfaitement le site de la société de stationnement. Elle entre ses coordonnées bancaires. Elle ne s'en rend compte que le lendemain quand elle voit un prélèvement de 89 € sur un site qu'elle ne connaît pas. L'opposition est faite, le remboursement est obtenu après 3 semaines — mais le stress et le temps perdu sont réels.

---

<a id="chapitre-13"></a>

## Chapitre 13 — Bluetooth, AirDrop et proximités radio

Le **Bluetooth** : l'appairage frauduleux (un appareil inconnu tente de s'appairer → ne jamais accepter un appairage non sollicité), la visibilité (un appareil en mode « visible » diffuse son nom — « iPhone de Lina » → ne laisser le Bluetooth visible/découvrable que le temps strictement nécessaire pour l'appairage), et le suivi via balises (AirTag Apple, SmartTag Samsung — un tracker physique glissé dans un sac, une poche, ou un véhicule suit les déplacements de la victime ; iOS et Android détectent les trackers inconnus qui voyagent avec vous et affichent une alerte — « un AirTag inconnu se déplace avec vous » → prendre ces alertes au sérieux ; ce sujet est détaillé dans le contexte de la surveillance par un proche au Ch.38).

L'**AirDrop abuse** (iOS) et le **Nearby Share/Quick Share** (Android) : envoi non sollicité de contenus (photos inappropriées, liens malveillants) à des personnes à proximité. Le réglage : AirDrop → « Contacts uniquement » ou « Désactivé », jamais « Tout le monde » (sauf le temps d'un transfert volontaire). Quick Share → idem.

Les réglages recommandés : Bluetooth activé uniquement quand nécessaire (il peut rester activé pour les écouteurs/montre mais en mode non-découvrable), AirDrop/Quick Share sur « Contacts uniquement », notifications de tracker activées, et révision périodique des appareils appairés (supprimer les appareils inconnus ou plus utilisés).

---

<a id="chapitre-14"></a>

## Chapitre 14 — Voyage, hôtel, déplacement et fatigue numérique

*Le voyage concentre les risques : Wi-Fi d'hôtel, fatigue, précipitation, appareils exposés, documents visibles, et niveau de vigilance en baisse. C'est le moment où les erreurs de confort s'accumulent.*

Le **shoulder surfing** : quelqu'un regarde l'écran par-dessus l'épaule — code de déverrouillage du téléphone (méthode courante pour accéder au contenu d'un téléphone volé : le voleur observe le code, puis vole le téléphone), mot de passe, informations bancaires, messages personnels. Le réflexe : utiliser un filtre de confidentialité sur le laptop (un film polarisé qui rend l'écran illisible de côté), orienter l'écran du téléphone dans les transports, et utiliser la biométrie plutôt que le code en lieu public. Les **appels en public** : réciter un numéro de carte bancaire au téléphone dans le train, confirmer une adresse dans un hall d'hôtel, donner un numéro de réservation dans un café → toute personne à portée de voix entend.

Le **Wi-Fi d'hôtel** : souvent non chiffré, parfois configuré de manière peu sécurisée, et partagé avec des centaines de personnes. Le réflexe : utiliser le partage de connexion mobile pour les opérations sensibles. Le **checkout d'hôtel** : vérifier que les sessions sont fermées sur la smart TV de la chambre (Netflix, YouTube — les credentials restent si on ne se déconnecte pas), sur l'iPad ou le téléphone de la chambre (certains hôtels fournissent des appareils), et sur le PC de l'espace business.

La **valise numérique de voyage** : avant de partir (sauvegarder les données, activer la localisation à distance, noter les numéros de blocage SIM et d'opposition bancaire sur un support hors du téléphone, vérifier les mises à jour), pendant le voyage (minimiser les connexions Wi-Fi, verrouiller systématiquement, ne pas laisser les appareils sans surveillance — le coffre de la chambre d'hôtel est là pour ça), et au retour (vérifier les sessions actives sur les comptes, supprimer les Wi-Fi enregistrés pendant le voyage).

> **🔵 Lina — Épisode 6 :** Lina en déplacement professionnel à Barcelone. Dans le lobby de l'hôtel, elle travaille écran visible sur le Wi-Fi de l'hôtel, fait un appel Teams en public (le nom du client et les chiffres du projet sont audibles), et recharge son téléphone sur le port USB du fauteuil du lobby. Le soir, fatiguée, elle commande un repas via un QR code sur la table du restaurant sans vérifier l'URL. Trois erreurs de confort en une journée — chacune individuellement à faible risque, mais leur accumulation augmente significativement l'exposition.

---

> ### 🟦 Réflexes — Fin de Partie III
>
> **À configurer** :
> - Partage de connexion mobile prêt (alternative au Wi-Fi public)
> - AirDrop / Quick Share en « Contacts uniquement »
> - Notifications de trackers inconnus activées
> - Filtre de confidentialité sur l'écran du laptop si déplacements fréquents
>
> **À éviter** :
> - Wi-Fi public pour banque ou email maître
> - Branchement sur un port USB public sans data-blocker
> - QR code dans un lieu public sans vérifier l'URL avant d'ouvrir
> - Appairage Bluetooth non sollicité
> - Écran visible en transport pour des informations sensibles
>
> **À vérifier en voyage** :
> - Cadenas HTTPS dans la barre d'adresse
> - URL du QR code avant d'ouvrir
> - Sessions fermées sur les TV / appareils d'hôtel au checkout
> - Wi-Fi de l'hôtel oublié au retour
>
> **Si quelque chose arrive** :
> - QR code malveillant scanné avec saisie bancaire → opposition immédiate (Ch.44)
> - Téléphone volé en voyage → kit de survie numérique (Ch.10, Ch.42)

---
