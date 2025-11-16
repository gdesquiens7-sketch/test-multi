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
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ ERREUR : OPENAI_API_KEY non définie")
        print("\nVeuillez :")
        print("1. Copier .env.example vers .env")
        print("2. Éditer .env et ajouter votre clé API")
        print("\nCommandes :")
        print("  cp .env.example .env")
        print("  nano .env  # ou votre éditeur préféré")
        return

    # Exemple de cahier des charges
    cahier_des_charges = """
CAHIER DES CHARGES : Outil de Gestion de Tâches Collaboratif

## 1. OBJECTIF
Créer un outil web de gestion de tâches simple et collaboratif pour les équipes de 5-20 personnes.

## 2. EXIGENCES FONCTIONNELLES
- EF1 : Création et organisation de tâches (titre, description, assigné, date limite)
- EF2 : Tableaux Kanban (colonnes personnalisables)
- EF3 : Collaboration en temps réel (plusieurs utilisateurs en même temps)
- EF4 : Notifications (tâche assignée, deadline proche, commentaires)
- EF5 : Commentaires et pièces jointes sur les tâches
- EF6 : Recherche et filtres avancés

## 3. EXIGENCES TECHNIQUES
- ET1 : Application web responsive (desktop + mobile)
- ET2 : Backend API REST (Node.js ou Python)
- ET3 : Base de données relationnelle (PostgreSQL)
- ET4 : Authentification sécurisée (JWT)
- ET5 : Temps de chargement < 2s
- ET6 : Support de 50 utilisateurs simultanés

## 4. CONTRAINTES
- C1 : Budget maximal : 40 000 €
- C2 : Délai : 3 mois
- C3 : Équipe : 2 développeurs full-stack, 1 designer
- C4 : Hébergement cloud (AWS, GCP, ou Azure)

## 5. CRITÈRES DE SUCCÈS
- CS1 : 20 équipes pilotes dans les 2 premiers mois
- CS2 : Note de satisfaction ≥ 4/5
- CS3 : Temps de réponse de l'API < 200ms
- CS4 : Disponibilité ≥ 99%
"""

    print("📋 Cahier des charges chargé")
    print("🎯 Lancement du débat multi-agent...\n")

    # Créer le système de débat
    debate_system = MultiAgentDebateCrew(
        model_name=os.getenv("MODEL_NAME", "deepseek-chat"),
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
