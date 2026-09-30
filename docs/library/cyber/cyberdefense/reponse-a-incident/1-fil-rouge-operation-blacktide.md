---
title: 'Fil rouge : Opération BLACKTIDE'
source: Cyber/05_Cyberdefense/20260401_Reponse_Incident.md
note: Réponse à incident
chapter: 1
chapters: 9
---

> **Contexte narratif — ce fil rouge traverse les 38 premiers chapitres du cours.**
>
> **Vendredi 14 mars 2026, 22h17.** Le SOC d'**Arvantis**, groupe industriel français coté au SBF 120 (12 000 collaborateurs, 15 sites de production en Europe, activité chimie fine et matériaux spéciaux, classé OIV sur 2 sites dont le complexe pétrochimique de Fos-sur-Mer), détecte une alerte EDR sur le contrôleur de domaine DC01 : exécution suspecte de `PsExec` couplée à une tentative de désactivation de Windows Defender via modification de GPO.
>
> L'analyste SOC N2 de garde, **Karim Belkacem**, vérifie l'alerte, confirme qu'il ne s'agit pas d'une opération d'administration planifiée, et escalade immédiatement vers l'IR lead.
>
> L'investigation va progressivement révéler une compromission profonde : un infostealer (variant Lumma) déployé 5 semaines plus tôt via un phishing ciblé sur le sous-traitant RH GestPaie, une élévation de privilèges via Kerberoasting sur un compte de service avec droits Domain Admin, un mouvement latéral méthodique via PsExec et RDP, une exfiltration de 380 Go de données R&D vers une instance AWS EC2 louée avec une carte prépayée, et le déploiement en cours d'un ransomware PhantomCrypt (connexion directe avec le cours *Cartographie des Écosystèmes Cybercriminels*) via GPO malveillante. Le chiffrement est partiellement contenu mais 3 sites sur 15 sont impactés, dont le site OIV de Fos-sur-Mer.
>
> L'équipe IR d'Arvantis, menée par **Nadia Moreau** (IR lead), sera confrontée à chaque chapitre à des décisions concrètes sous pression : quand couper le réseau et quand ne PAS le couper, comment préserver les preuves quand un admin a déjà redémarré 2 serveurs, quoi dire au CEO qui veut « redémarrer les usines lundi », comment articuler avec l'ANSSI et le CERT-FR, comment traiter la demande de rançon de 4,2 M€, comment reconstruire un AD dont le compte krbtgt est compromis, et comment s'assurer que l'attaquant n'est plus là avant de relancer la production chimique.
>
> Le coût total de l'incident sera estimé à 8,5 M€. Le retex final (Ch.38) produira 15 recommandations structurées et un plan d'amélioration sur 18 mois.

---
