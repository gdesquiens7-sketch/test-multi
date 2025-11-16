#!/usr/bin/env python3
"""
Script de test propre - Force le rechargement complet
"""
import sys
import os

# Supprimer les modules déjà importés pour forcer le rechargement
modules_to_remove = [k for k in sys.modules.keys() if 'debate' in k or 'config' in k]
for mod in modules_to_remove:
    del sys.modules[mod]

# Maintenant importer proprement
from debate_crew import MultiAgentDebateCrew
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

print("="*80)
print("TEST DE CRÉATION DU CREW")
print("="*80)

# Vérifier la clé API
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("\n❌ ERREUR : OPENAI_API_KEY non définie dans .env")
    print("\nConfiguration requise :")
    print("  1. Copiez .env.example vers .env")
    print("  2. Ajoutez votre clé API")
    exit(1)

print(f"\n✅ Clé API configurée : {api_key[:10]}...")

# Test simple de cahier des charges
cahier_test = """
CAHIER DES CHARGES : Test Simple

1. OBJECTIF
Tester le système de débat multi-agent.

2. EXIGENCES
- EF1 : Fonctionnalité A
- EF2 : Fonctionnalité B

3. CONTRAINTES
- Budget : 10 000 €
- Délai : 1 mois

4. CRITÈRES DE SUCCÈS
- CS1 : Livraison dans les temps
"""

print("\n🎯 Création du système de débat...")

try:
    debate_system = MultiAgentDebateCrew(
        model_name=os.getenv("MODEL_NAME", "deepseek-chat"),
        temperature=0.7
    )
    print("✅ MultiAgentDebateCrew créé avec succès")

    print("\n🏗️  Création du crew...")
    crew = debate_system.create_crew(cahier_test)
    print("✅ Crew créé avec succès !")

    print("\n📋 Configuration du crew :")
    print(f"  - Nombre d'agents : {len(crew.agents)}")
    print(f"  - Nombre de tâches : {len(crew.tasks)}")
    print(f"  - Process : {crew.process}")
    print(f"  - Verbose : {crew.verbose}")
    print(f"  - Memory : {crew.memory}")

    print("\n" + "="*80)
    print("✅ TOUS LES TESTS PASSÉS - Le système est prêt !")
    print("="*80)

    # Option : lancer le débat complet
    response = input("\nVoulez-vous lancer le débat complet ? (o/n) : ")
    if response.lower() == 'o':
        print("\n🚀 Lancement du débat complet...")
        result = debate_system.run_debate(
            cahier_test,
            output_file="output/test_resultat.md"
        )
        print("\n✅ Débat terminé avec succès !")

except Exception as e:
    print(f"\n❌ ERREUR : {e}")
    print("\nDétails de l'erreur :")
    import traceback
    traceback.print_exc()
    exit(1)
