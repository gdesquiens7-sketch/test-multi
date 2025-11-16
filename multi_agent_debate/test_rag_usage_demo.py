#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Démonstration de l'utilisation du RAG par les agents
"""
import os
import sys
from dotenv import load_dotenv

# Forcer UTF-8 pour Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

load_dotenv()

from debate_crew import MultiAgentDebateCrew

def demo_rag_usage():
    """Démonstration minimale du RAG"""
    
    print("=" * 80)
    print("DEMONSTRATION DE L'UTILISATION RAG")
    print("=" * 80)
    print()
    
    # Cahier des charges simple
    cahier = """
    CAHIER DES CHARGES : Test RAG
    
    OBJECTIF : Créer une application de test
    
    EXIGENCES :
    - EF1 : L'application doit être rapide
    - EF2 : L'interface doit être intuitive
    
    CONTRAINTES :
    - Budget : 50 000 €
    - Délai : 3 mois
    """
    
    print("📋 Cahier des charges créé")
    print()
    
    # Créer le système
    print("🚀 Création du système de débat...")
    debate_system = MultiAgentDebateCrew(
        model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        temperature=0.7
    )
    
    # Créer le crew (initialise le RAG)
    print("🔧 Création du crew (initialise le RAG)...")
    crew = debate_system.create_crew(cahier_des_charges=cahier)
    print("   ✅ RAG initialisé")
    print()
    
    # Vérifier l'accès au knowledge pour un agent
    print("🔍 Test d'accès au knowledge pour l'agent Innovateur...")
    agent = debate_system.innovateur
    
    # Le knowledge sera initialisé lors du kickoff
    # Mais on peut vérifier la configuration
    if hasattr(agent, 'knowledge_sources') and agent.knowledge_sources:
        print(f"   ✅ Source de connaissance assignée : {type(agent.knowledge_sources[0]).__name__}")
        print(f"   📄 Contenu : {len(agent.knowledge_sources[0].content)} caractères")
    
    print()
    print("💡 IMPORTANT :")
    print("   Le RAG sera vraiment utilisé lors du crew.kickoff()")
    print("   Les agents feront des requêtes automatiques au cahier des charges")
    print()
    print("   Pour voir l'utilisation RAG en action :")
    print("   1. Lancez un débat complet avec : debate_system.run_debate(...)")
    print("   2. Observez les logs (verbose=True est déjà activé)")
    print("   3. Les agents interrogeront automatiquement le RAG pendant leurs tâches")
    print()
    print("   Après le débat, vérifiez ChromaDB :")
    print("   python test_rag_access.py --check-chromadb")
    print()

if __name__ == "__main__":
    demo_rag_usage()

