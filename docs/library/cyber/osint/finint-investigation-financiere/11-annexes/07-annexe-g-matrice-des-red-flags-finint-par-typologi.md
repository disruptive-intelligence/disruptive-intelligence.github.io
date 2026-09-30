---
title: Annexe G — Matrice des red flags FININT (par typologie)
source: Cyber/02_OSINT/FININT_Investigation_Financiere_vFULL.md
note: FININT — investigation financière
up:
- - FININT — investigation financière
  - ../index.md
- - Annexes
  - index.md
---

*Tableau synthétique des signaux d’alerte les plus courants, organisés par typologie. À utiliser comme grille de lecture rapide, non comme checklist mécanique : un red flag isolé ne prouve rien ; plusieurs convergents justifient l’investigation.*

|Typologie                        |Red flags principaux                                                                                                                                                                                                                                                                               |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Blanchiment — placement**      |Dépôts cash fractionnés sous seuils, comptes alimentés par activités à forte composante cash incohérente avec profil client, onboarding rapide sur PSP/EME suivi d’activité immédiate inhabituelle, achats cash de biens revendables, multiplication de comptes de mules.                          |
|**Blanchiment — layering**       |Cascades de virements en cycle court, multi-juridictions sans rationale, conversions multiples de devises, transferts en cascade entre fintechs, sorties crypto via mixers/bridges, comptes courts (ouverts et clos rapidement), libellés vagues.                                                  |
|**Blanchiment — intégration**    |Acquisitions immobilières disproportionnées avec revenus, achats d’art à prix élevés, investissements dans sociétés sans expérience préalable, donations à organismes avec retours indirects, achats de luxe en cash ou crypto.                                                                    |
|**TBML**                         |Marges disproportionnées vs marché, décalages valeur facture / valeur de marché, contreparties sans activité réelle, transits par juridictions sans rationale, documents douaniers incohérents, paiements en avance disproportionnés, flux financiers déconnectés des flux physiques.              |
|**Corruption / PEP**             |Flux entrants depuis fournisseurs publics vers comptes personnels ou de proches, sociétés de conseil sans activité réelle, acquisitions disproportionnées par proches, train de vie incohérent, HATVP partielle ou contradictoire, lien temporel sortie de fonctions / début d’activité de conseil.|
|**Fraude TVA carrousel**         |Cycles d’opérations entre mêmes acteurs, sociétés sans substance faisant transit, crédits TVA disproportionnés, sociétés disparaissant brutalement, secteurs à risque (téléphonie, métaux, énergie, services digitaux).                                                                            |
|**Évasion fiscale**              |Charges intragroupe disproportionnées vers juridictions à faible imposition, prêts intragroupe sans intérêts, holdings intermédiaires sans substance, transferts de PI vers offshore + redevances.                                                                                                 |
|**ABS**                          |Virements société → comptes personnels du dirigeant sans contrepartie, factures personnelles payées par société, biens à usage privé, compte courant associé gonflé sans cohérence.                                                                                                                |
|**BEC / fraude au virement**     |IBAN nouveau et juridiction inhabituelle, libellé urgent, demande hors heures ouvrées, discrépance nom bénéficiaire / titulaire compte, activité immédiate de fractionnement et cashout sur compte récepteur, typosquatting d’email.                                                               |
|**Contournement de sanctions**   |Flux soudains vers juridictions tierces (Turquie, Émirats, Géorgie, Asie centrale), sociétés intermédiaires récemment créées, UBO lié à entité sanctionnée, activités dual-use, triangulation incohérente.                                                                                         |
|**Ponzi / pig butchering**       |Rendements promis très supérieurs au marché, pression à recruter, plateforme inconnue en juridiction obscure, retraits difficiles, garanties auto-désignées, endorsements suspects.                                                                                                                |
|**Criminalité organisée**        |Acquisitions opaques d’entreprises en difficulté, dirigeants à profil suspect, croissance soudaine inexpliquée, sous-traitance fictive, présence multi-juridictionnelle sans rationale.                                                                                                            |
|**Cybercriminalité / ransomware**|Paiements crypto urgents et significatifs, demandes en USDT/BTC/XMR, contextes d’incident IT en parallèle, conversions multiples sur exchanges asiatiques non-KYC.                                                                                                                                 |

-----
