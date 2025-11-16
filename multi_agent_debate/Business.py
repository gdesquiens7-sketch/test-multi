#!/usr/bin/env python3
"""
Exemple d'utilisation du Système Multi-Agent de Débat et Validation
====================================================================

Ce script montre comment lancer un débat multi-agent avec un cahier des charges.
"""

import os
from debate_crew import MultiAgentDebateCrew
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()


def main():
    """Fonction principale - Exemple d'utilisation."""

    print("\n" + "="*80)
    print("EXEMPLE : Système Multi-Agent de Débat et Validation")
    print("="*80 + "\n")

    # Vérification de la configuration
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ ERREUR : OPENROUTER_API_KEY non définie")
        print("\nVeuillez :")
        print("1. Copier .env.example vers .env")
        print("2. Éditer .env et ajouter votre clé API OpenRouter")
        print("\nCommandes :")
        print("  cp .env.example .env")
        print("  nano .env  # ou votre éditeur préféré")
        print("\nVoir OPENROUTER_SETUP.md pour plus d'infos")
        return

    # Exemple de cahier des charges
    cahier_des_charges = """
CAHIER DES CHARGES : CAHIER DES CHARGES - Projet Revenu Complémentaire Original

## 1. CONTEXTE DU PROJET

**Porteur de projet** : Grégoire
- Profil : Chef de projet / Product Manager avec expertise en IA, développement (AppSheet, React, Python, VBA)
- Contexte : En poste à temps plein, recherche complément de revenu compatible avec activité principale
- Environnement de travail : Bureau avec ordinateur et connexion internet

**Problématique** : 
Trouver une source de revenu complémentaire viable, originale et rapidement rentable, nécessitant un investissement minimal et réalisable depuis un poste de travail.

---

## 2. OBJECTIFS

### Objectif Principal
Identifier UNE idée de génération de revenu complémentaire originale, faisable et rentable rapidement.

### Objectifs Secondaires
- Maximiser l'originalité (se démarquer des idées classiques type dropshipping, freelance générique, etc.)
- Minimiser le temps de mise en marché (max 1 semaine)
- Assurer la viabilité à moyen terme (pas un coup one-shot)
- Préserver la sécurité financière et légale

---

## 3. EXIGENCES FONCTIONNELLES (Obligatoires)

### EXI-001 : Originalité Forte
**Priorité** : CRITIQUE
- L'idée DOIT être originale et peu courante sur le marché
- Elle ne DOIT PAS être une variation évidente d'idées mainstream (freelancing, dropshipping, sondages rémunérés, affiliation classique)
- Critère de validation : "Cette idée est difficilement trouvable via une recherche Google standard"

### EXI-002 : Exécution Bureau
**Priorité** : CRITIQUE
- L'activité DOIT être 100% réalisable depuis un bureau avec ordinateur
- Pas de déplacements physiques requis
- Pas de logistique matérielle (stockage, envoi de colis, etc.)

### EXI-003 : Investissement Minimal
**Priorité** : CRITIQUE
- Budget de démarrage : **MAX 10€**
- Pas d'achats d'équipement supplémentaire
- Pas d'abonnements mensuels obligatoires (sauf si couverts par les 10€ du premier mois)

### EXI-004 : Génération Rapide de Revenus
**Priorité** : CRITIQUE
- Les premiers revenus DOIVENT être générés dans un délai MAX de **7 jours** après lancement
- Même si montants faibles au début, le flux doit être établi en 1 semaine
- Critère : "Argent sur compte bancaire ou plateforme de paiement sous 7 jours"

### EXI-005 : Fiabilité et Sécurité
**Priorité** : CRITIQUE
- L'activité DOIT être 100% légale en France
- Pas de zones grises juridiques ou fiscales
- Pas de risque de perte d'argent au-delà des 10€ investis
- Pas d'arnaques, pyramides, ou systèmes douteux
- Réputation protégée (pas d'activité compromettante)

---

## 4. EXIGENCES NON FONCTIONNELLES

### EXI-006 : Scalabilité
**Priorité** : HAUTE
- L'idée DEVRAIT permettre une augmentation progressive des revenus
- Potentiel d'automatisation partielle souhaité

### EXI-007 : Compatibilité avec Emploi Principal
**Priorité** : HAUTE
- Temps requis : Max 5-10h/semaine pour démarrer
- Pas de conflit d'intérêt avec l'employeur actuel
- Pas de clause de non-concurrence violée
- Horaires flexibles (compatible avec emploi 9h-18h)

### EXI-008 : Compétences Mobilisables
**Priorité** : MOYENNE
- Idéalement, l'idée DEVRAIT exploiter les compétences de Grégoire :
  - IA et prompt engineering
  - Développement (Python, React, AppSheet, VBA)
  - Product Management
  - UX/UI
  - Automation
- Mais ce n'est PAS une exigence bloquante si l'originalité compense

### EXI-009 : Durabilité
**Priorité** : MOYENNE
- L'activité DEVRAIT pouvoir durer au moins 6-12 mois
- Pas de mode éphémère vouée à disparaître rapidement

---

## 5. CONTRAINTES

### Contraintes Budgétaires
- Budget total phase 1 : **10€ max**
- Pas de crédit ou prêt possible
- Pas d'investissement matériel requis

### Contraintes Temporelles
- Délai d'implémentation : **Max 7 jours**
- Temps disponible par semaine : **5-10h**
- Premiers revenus : **Sous 7 jours**

### Contraintes Techniques
- Équipement disponible : Ordinateur, connexion internet
- Pas d'achat de matériel supplémentaire
- Utilisation d'outils gratuits ou couverts par le budget de 10€

### Contraintes Légales
- Conformité totale avec législation française
- Déclaration fiscale claire et simple
- Pas de statut juridique complexe requis au démarrage

### Contraintes Environnementales
- Travail depuis bureau (domicile ou bureau professionnel selon moments)
- Pas de déplacements
- Pas de rencontres physiques obligatoires

---

## 6. CRITÈRES DE SUCCÈS

### Critères Quantitatifs
1. **Originalité** : Score d'originalité > 8/10 (consensus des agents)
2. **Budget** : Investissement ≤ 10€
3. **Rapidité** : Premiers revenus sous 7 jours
4. **Rentabilité** : Projection > 50€/mois après 1 mois
5. **Temps** : ≤ 10h/semaine requis

### Critères Qualitatifs
1. **Faisabilité** : Plan d'action clair et réaliste
2. **Légalité** : 100% conforme et documenté
3. **Sécurité** : Aucun risque financier ou réputationnel
4. **Pérennité** : Viabilité sur 6+ mois
5. **Scalabilité** : Potentiel de croissance identifié

---

## 7. LIVRABLES ATTENDUS

Le système multi-agent doit produire :

### Livrable Principal
**Document de Recommandation** contenant :

1. **L'Idée Retenue** (1-2 pages)
   - Description détaillée du concept
   - En quoi c'est original (benchmark vs alternatives)
   - Proposition de valeur claire

2. **Plan d'Action Semaine 1** (très détaillé)
   - Jour par jour : quoi faire exactement
   - Checklist des actions
   - Ressources nécessaires (liens, outils, etc.)
   - Budget détaillé (comment dépenser les 10€)

3. **Stratégie de Génération de Revenus**
   - Comment les premiers revenus arrivent
   - Timeline réaliste
   - Montants attendus (fourchette basse/haute)

4. **Validation de Conformité**
   - Conformité légale (déclaration, fiscalité)
   - Conformité éthique
   - Gestion des risques

5. **Projection 1-3-6 Mois**
   - Évolution des revenus attendus
   - Stratégie de scalabilité
   - Indicateurs de succès à suivre

### Livrables Secondaires
- Argumentaire des débats (pourquoi cette idée vs autres)
- Liste des idées rejetées et pourquoi
- Risques identifiés et mitigations

---

## 8. PÉRIMÈTRE HORS PROJET

**Ce qui n'est PAS recherché** :
- ❌ Idées classiques type freelancing générique, dropshipping, affiliation Amazon standard
- ❌ MLM / Marketing de réseau / Systèmes pyramidaux
- ❌ Sondages rémunérés et micro-tâches sous-payées
- ❌ Trading / Crypto / Paris sportifs / Jeux d'argent
- ❌ Activités nécessitant investissement > 10€
- ❌ Activités nécessitant déplacements physiques
- ❌ Activités dans zones grises légales
- ❌ Création de contenu adulte / OnlyFans et similaires
- ❌ Revente de produits physiques (sauf si 100% digital)

---

## 9. INDICATEURS DE PERFORMANCE

Pour valider le succès de l'idée retenue :

| Indicateur | Cible Semaine 1 | Cible Mois 1 | Cible Mois 3 |
|------------|-----------------|--------------|--------------|
| Investissement | ≤ 10€ | ≤ 50€ | ≤ 200€ |
| Revenus générés | > 0€ | ≥ 50€ | ≥ 200€ |
| Temps investi | ≤ 10h | ≤ 40h | ≤ 120h |
| ROI | Positif | > 100% | > 200% |
| Score originalité | 8/10 | - | - |

---

## 10. QUESTIONS CLÉS À RÉSOUDRE

Les agents devront impérativement répondre à :

1. **Pourquoi cette idée est-elle vraiment originale ?** (benchmark obligatoire)
2. **Comment générer les premiers revenus en 7 jours exactement ?** (plan détaillé)
3. **Quels sont les risques cachés ?** (juridiques, financiers, réputationnels)
4. **Comment scaler après le premier mois ?** (stratégie de croissance)
5. **Quelle est la pire chose qui peut arriver ?** (analyse worst-case scenario)
6. **Pourquoi Grégoire spécifiquement peut réussir dans cette idée ?** (fit avec profil)

---

## 11. VALIDATION FINALE

L'idée sera considérée comme validée SI ET SEULEMENT SI :

✅ Consensus unanime des 5 agents  
✅ Conformité 100% aux exigences critiques (EXI-001 à EXI-005)  
✅ Score originalité ≥ 8/10  
✅ Plan d'action semaine 1 détaillé et réaliste  
✅ Aucun red flag légal ou éthique  
✅ Projection financière crédible et argumentée
"""

    print("📋 Cahier des charges chargé")
    print("🎯 Lancement du débat multi-agent...\n")

    # Créer le système de débat
    debate_system = MultiAgentDebateCrew(
        model_name=os.getenv("MODEL_NAME", "openrouter/deepseek/deepseek-chat"),
        temperature=float(os.getenv("TEMPERATURE", "0.7"))
    )

    # Lancer le débat
    try:
        result = debate_system.run_debate(
            cahier_des_charges=cahier_des_charges,
            output_file="output/exemple_resultat.md"
        )

        print("\n" + "="*80)
        print("✅ DÉBAT TERMINÉ AVEC SUCCÈS")
        print("="*80)
        print("\n📄 Le document de recommandation finale a été généré.")
        print("📁 Fichier : output/exemple_resultat.md")
        print("\nVous pouvez maintenant consulter le rapport complet.\n")

    except Exception as e:
        print("\n" + "="*80)
        print("❌ ERREUR LORS DU DÉBAT")
        print("="*80)
        print(f"\nErreur : {str(e)}")
        print("\nVérifiez :")
        print("  - Votre clé API est valide")
        print("  - Vous avez une connexion Internet")
        print("  - Le service API est accessible\n")


if __name__ == "__main__":
    main()
