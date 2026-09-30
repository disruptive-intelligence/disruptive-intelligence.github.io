---
title: Chapitre 19 — Red team social engineering
source: Cyber/HUMINT_Social_Engineering.md
note: HUMINT & social engineering
up:
- - HUMINT & social engineering
  - ../index.md
- - 'Partie IV — L''attaquant : perspectives offensives'
  - index.md
---

méthodologie professionnelle et OPSEC du praticien

## 19.1 Le cadre du red team

Le red team social engineering est une prestation professionnelle encadrée par un contrat, une lettre de mission et des rules of engagement qui définissent précisément ce qui est autorisé et ce qui ne l'est pas.

**La lettre de mission** est le document fondateur. Elle doit être signée par un représentant habilité de l'organisation (pouvoir de signature vérifié juridiquement) et doit couvrir : l'identité du prestataire et des testeurs, le scope géographique (quels sites), le scope humain (quels employés — tous, un service, des profils spécifiques), le scope technique (quels vecteurs — phishing, vishing, intrusion physique, élicitation), la durée, les objectifs, les limites explicites, le protocole d'urgence (safe word, contact de référence), et la clause de confidentialité.

**Les rules of engagement** complètent la lettre de mission avec les détails opérationnels : horaires autorisés, zones interdites (zones classifiées, locaux syndicaux, infirmerie), techniques exclues, procédure de communication avec le commanditaire (reports intermédiaires, alertes), gestion des découvertes incidentes (si le red team découvre une intrusion réelle pendant le test — qui prévenir et comment).

## 19.2 La planification

La planification couvre : les objectifs opérationnels (mesurables et réalistes), la reconnaissance (OSINT + reconnaissance physique), la construction des pretextes (chaque pretexte avec un pretexte de secours), l'infrastructure technique (domaines, landing pages, implants, communications sécurisées), la logistique (déplacements, tenues, matériel, hébergement si test multi-sites), la timeline (séquencement des phases — reconnaissance, phishing, vishing, intrusion physique, élicitation), et les points de décision (go/no-go à chaque phase).

## 19.3 L'exécution

L'exécution d'un test de social engineering est une opération à haute tension. Le red teamer est lui-même sous pression (risque d'être intercepté, nécessité de maintenir le pretexte en temps réel, gestion du stress de l'imposture) et doit prendre des décisions en quelques secondes (pivoter si le pretexte ne fonctionne pas, abandonner si le risque est trop élevé, escalader si l'opportunité se présente).

**La documentation en temps réel** est critique : photos (discrètes), notes, horodatage de chaque action, enregistrements audio/vidéo si autorisés par la lettre de mission et la législation locale. Chaque élément de documentation sera utilisé dans le rapport pour démontrer les vulnérabilités identifiées et proposer des remédiations.

**L'adaptation en temps réel** est la compétence la plus difficile à acquérir. Les plans ne survivent pas au contact — un gardien plus vigilant que prévu, un employé qui pose une question inattendue, une porte fermée qui devait être ouverte. Le red teamer doit improviser tout en maintenant la cohérence de son pretexte.

## 19.4 Le rapport

Le rapport de red team social engineering est le livrable final et le document qui justifie l'investissement du commanditaire. Il doit être factuel, constructif et actionnable.

**Structure type** : résumé exécutif (une page — résultats clés, risques majeurs, recommandations prioritaires), méthodologie (vecteurs utilisés, timeline, outils), résultats par vecteur (phishing : taux de clic, taux de compromission, temps de signalement ; vishing : taux de succès, informations obtenues ; intrusion physique : accès obtenus, temps de présence non détecté, implants posés), évaluation de l'impact (ce qu'un attaquant réel aurait pu faire avec les accès obtenus — sans les contraintes éthiques du red team), recommandations classées P0/P1/P2.

**Le ton** : le rapport documente des faits et propose des améliorations. Il ne blâme pas les individus, ne nomme pas les employés qui se sont fait piéger (sauf exception justifiée et avec l'accord du commanditaire), et ne ridiculise pas les défenses existantes. Un rapport humiliant ne produit pas de changement — il produit de la résistance.

## 19.5 L'éthique du red teamer

Le red teamer a un pouvoir de manipulation — et la responsabilité qui va avec est non négociable. Le debriefing post-test est une obligation éthique : les employés qui ont été piégés doivent être informés (individuellement ou collectivement, selon le format choisi avec le commanditaire), le mécanisme exploité doit être expliqué (pas le nom de l'employé, mais la technique), et la finalité doit être claire (améliorer les défenses, pas sanctionner les individus).

La confidentialité des résultats individuels est un impératif. Le rapport ne doit pas permettre au commanditaire d'identifier et de sanctionner un employé spécifique sur la base de sa vulnérabilité au social engineering — sauf si cette vulnérabilité révèle un manquement grave et délibéré aux procédures (ce qui est différent d'un échec face à un social engineering sophistiqué).

## 19.6 OPSEC du praticien

L'OPSEC (Operational Security) du praticien est un aspect souvent négligé de la formation au red team social engineering. Le praticien doit protéger sa propre sécurité, sa couverture opérationnelle et la traçabilité de sa mission.

**Préparation de la légende.** Chaque pretexte nécessite une identité crédible et compartimentée. Le red teamer ne doit jamais utiliser sa vraie identité pendant un test (sauf en phase de rapport). Les éléments de la légende (nom, entreprise, carte de visite, numéro de téléphone dédié, adresse email de pretexte, profils en ligne si nécessaire) doivent être préparés et testés avant le début de l'opération.

**La compartimentation.** Les identités de pretexte ne doivent pas être croisables entre elles ni traçables vers l'identité réelle du red teamer. Téléphones dédiés (burner ou SIM dédiée), adresses email distinctes, profils en ligne séparés, véhicule sans lien avec l'entreprise de red team.

**La gestion des supports.** Les photos, enregistrements, notes de terrain et copies de documents collectés pendant le test doivent être stockés de manière sécurisée (chiffrement), transmis au commanditaire via un canal sécurisé, et détruits après la livraison du rapport final (sauf obligation de conservation contractuelle). La perte d'un dispositif contenant des preuves de test peut constituer une fuite de données sensibles.

**La gestion de la confrontation.** Si le red teamer est intercepté, arrêté ou confronté par la sécurité ou les forces de l'ordre, il doit pouvoir s'identifier immédiatement comme testeur autorisé. La lettre de mission et le contact du commanditaire doivent être accessibles en permanence (version papier dans une poche intérieure, version numérique sur le téléphone). Le safe word doit être connu de toute l'équipe et du contact de référence.

**Les limites légales.** Le red teamer doit connaître le cadre juridique local. En France, même avec une lettre de mission signée par le DG, certaines actions restent juridiquement risquées si elles sont mal encadrées : l'enregistrement de conversations sans consentement est illégal (sauf dans le cadre strictement défini de la lettre de mission qui vaut consentement de l'employeur), la fabrication de faux documents peut constituer une infraction si elle est utilisée en dehors du cadre du test, l'usurpation de l'identité d'un vrai prestataire (et non d'un prestataire fictif) peut entraîner des complications juridiques. Le cadre juridique est détaillé à l'Annexe F.

---
