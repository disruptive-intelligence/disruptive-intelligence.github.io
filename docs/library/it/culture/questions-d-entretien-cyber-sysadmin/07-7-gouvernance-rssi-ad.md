---
title: 7) Gouvernance / RSSI / AD
source: IT/Culture/Questions_Entretien_Cyber_SysAdmin.md
note: Questions d'entretien cyber & sysadmin
up:
- - Questions d'entretien cyber & sysadmin
  - index.md
---

---

- **Question : Quelles sont les fonctions d'un RSSI ?**
  **Réponse type :** Le RSSI (Responsable de la Sécurité des Systèmes d'Information) pilote la stratégie de cybersécurité de l'organisation. Ses missions principales : définir et faire appliquer la politique de sécurité (PSSI), gérer les risques (cartographie, analyse, traitement), assurer la conformité réglementaire (NIS 2, RGPD, LPM), piloter la réponse à incident, gérer les budgets sécurité, sensibiliser les collaborateurs, et reporter à la direction. Il fait le lien entre la technique et le business — il doit traduire les risques techniques en impacts métier compréhensibles par le COMEX.

- **Question : Quand on arrive sur une fonction RSSI, quelles sont les premières choses qu'on demande ou qu'on fait ?**
  **Réponse type :** D'abord un état des lieux : existe-t-il une PSSI ? Un inventaire des actifs ? Une cartographie des risques ? Un PRA/PCA ? Quels sont les contrats de sécurité en place (SOC, PRIS, assurance cyber) ? Ensuite la visibilité technique : quel est le niveau de couverture EDR ? Les logs sont-ils centralisés ? L'AD est-il audité (PingCastle) ? Les sauvegardes sont-elles testées et hors réseau ? Les patchs sont-ils à jour ? Puis les quick wins : activer le MFA partout, lancer un audit AD, vérifier les accès admin, tester la restauration des sauvegardes. Enfin, construire la roadmap de maturité en priorisant par impact et faisabilité.

- **Question : Quelles sont les premières mesures à prendre pour sécuriser un Active Directory ?**
  **Réponse type :** Par impact décroissant : activer l'Advanced Audit Policy sur tous les DC (visibilité), déployer LAPS pour avoir un mot de passe admin local unique par machine (supprime le Pass-the-Hash via admin local), séparer les comptes admin et utilisateur (pas de Domain Admin sur les postes), activer le SMB signing obligatoire (bloque le NTLM relay), désactiver LLMNR et NBT-NS (bloque le poisoning Responder), rotater le krbtgt (double rotation espacée — invalide tout Golden Ticket), auditer les ACLs avec BloodHound (identifier et couper les chemins d'attaque), supprimer les comptes inactifs et SPNs inutiles (réduire la surface de Kerberoasting), activer Protected Users pour les comptes Tier 0, et durcir les templates AD CS.

- **Question : C'est quoi le tiering model AD ?**
  **Réponse type :** Le tiering sépare l'environnement en trois niveaux : Tier 0 pour les DC et comptes Domain Admin (criticité maximale, isolation réseau, PAW obligatoire), Tier 1 pour les serveurs (comptes admin serveur), Tier 2 pour les postes utilisateurs. La règle fondamentale : un compte d'un tier supérieur ne se connecte JAMAIS à un tier inférieur. Si un DA a une session sur un serveur Tier 1 et que ce serveur est compromis, l'attaquant récupère le hash DA. Le tiering casse cette chaîne.

- **Question : C'est quoi BloodHound et à quoi ça sert ?**
  **Réponse type :** BloodHound modélise l'AD comme un graphe : les objets (users, machines, groupes) sont des nœuds, les relations et droits sont des arêtes. Il collecte les données avec SharpHound et visualise les chemins d'attaque vers Domain Admin. C'est aussi un outil défensif puissant : en le lançant sur son propre AD, on identifie les chemins avant l'attaquant et on coupe les nœuds de convergence — un seul nœud corrigé peut fermer des dizaines de chemins.

---
