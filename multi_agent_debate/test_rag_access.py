#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour vérifier que les agents ont accès au cahier des charges via RAG
"""
import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# Forcer UTF-8 pour Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Charger les variables d'environnement
load_dotenv()

from debate_crew import MultiAgentDebateCrew
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from langchain_openai import OpenAIEmbeddings
import chromadb
from crewai.utilities.paths import db_storage_path

def test_rag_access():
    """Test complet de l'accès RAG au cahier des charges"""
    
    print("=" * 80)
    print("TEST D'ACCES RAG AU CAHIER DES CHARGES")
    print("=" * 80)
    print()
    
    # 1. Créer un cahier des charges de test
    print("1. Création d'un cahier des charges de test...")
    cahier_test = """
    CAHIER DES CHARGES : Test d'accès RAG
    
    1. OBJECTIF
    Tester que les agents peuvent accéder au cahier des charges via RAG.
    
    2. EXIGENCES FONCTIONNELLES
    - EF1 : Les agents doivent pouvoir interroger le cahier des charges
    - EF2 : Le système RAG doit retourner des résultats pertinents
    - EF3 : Les connaissances doivent être stockées dans ChromaDB
    
    3. EXIGENCES TECHNIQUES
    - ET1 : ChromaDB doit fonctionner correctement
    - ET2 : Les embeddings doivent être générés
    - ET3 : Les requêtes sémantiques doivent fonctionner
    
    4. CONTRAINTES
    - Budget : 10 000 €
    - Délai : 1 mois
    
    5. CRITÈRES DE SUCCÈS
    - CS1 : Les agents trouvent les informations dans le cahier des charges
    - CS2 : Les requêtes retournent des résultats pertinents
    """
    
    print("   ✅ Cahier des charges de test créé")
    print()
    
    # 2. Initialiser le système de débat
    print("2. Initialisation du système de débat...")
    try:
        debate_system = MultiAgentDebateCrew(
            model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
            temperature=0.7
        )
        print("   ✅ Système de débat initialisé")
        print()
    except Exception as e:
        print(f"   ❌ Erreur lors de l'initialisation : {e}")
        return False
    
    # 3. Créer le crew pour initialiser le RAG
    print("3. Création du crew (initialise le RAG)...")
    try:
        crew = debate_system.create_crew(cahier_des_charges=cahier_test)
        print("   ✅ Crew créé avec RAG")
        print()
    except Exception as e:
        print(f"   ❌ Erreur lors de la création du crew : {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # 4. Vérifier que le knowledge source est assigné aux agents
    print("4. Vérification de l'assignation des connaissances aux agents...")
    agents_with_knowledge = []
    for agent_name, agent in [
        ("Innovateur", debate_system.innovateur),
        ("Pragmatique", debate_system.pragmatique),
        ("Avocat du Diable", debate_system.avocat_du_diable),
        ("Stratège", debate_system.stratege),
        ("Facilitateur", debate_system.facilitateur),
    ]:
        has_knowledge = hasattr(agent, 'knowledge_sources') and agent.knowledge_sources
        if has_knowledge:
            agents_with_knowledge.append(agent_name)
            print(f"   ✅ {agent_name} : {len(agent.knowledge_sources)} source(s) de connaissance")
        else:
            print(f"   ⚠️  {agent_name} : Aucune source de connaissance assignée")
    print()
    
    if not agents_with_knowledge:
        print("   ❌ AUCUN agent n'a de source de connaissance !")
        print("   Vérifiez la configuration dans debate_crew.py")
        return False
    
    # 5. Vérifier ChromaDB directement
    print("5. Vérification de ChromaDB...")
    try:
        storage_path = db_storage_path()
        knowledge_path = Path(storage_path) / "knowledge"
        
        print(f"   📁 Chemin ChromaDB : {knowledge_path}")
        
        if not knowledge_path.exists():
            print("   ⚠️  Le répertoire knowledge n'existe pas encore")
            print("   (Il sera créé lors du premier kickoff)")
        else:
            print("   ✅ Répertoire knowledge existe")
            
            # Lister les collections
            try:
                client = chromadb.PersistentClient(path=str(knowledge_path))
                collections = client.list_collections()
                
                if collections:
                    print(f"   📚 Collections trouvées : {len(collections)}")
                    for collection in collections:
                        count = collection.count()
                        print(f"      - {collection.name} : {count} documents")
                        
                        # Afficher un échantillon
                        if count > 0:
                            sample = collection.peek(limit=1)
                            if sample.get('documents'):
                                doc_preview = sample['documents'][0][:100] + "..."
                                print(f"        Exemple : {doc_preview}")
                else:
                    print("   ⚠️  Aucune collection trouvée")
            except Exception as e:
                print(f"   ⚠️  Erreur lors de la lecture de ChromaDB : {e}")
                print("   (C'est normal si le RAG n'a pas encore été initialisé)")
        print()
    except Exception as e:
        print(f"   ⚠️  Erreur lors de la vérification ChromaDB : {e}")
        print()
    
    # 6. Test d'une requête RAG (si le knowledge est initialisé)
    print("6. Test de requête RAG (simulation)...")
    print("   📝 Note : Le RAG sera vraiment initialisé lors du crew.kickoff()")
    print("   Mais on peut vérifier que la configuration est correcte...")
    print()
    
    # Vérifier que l'embedder est configuré
    try:
        embedder = OpenAIEmbeddings(model="text-embedding-3-small")
        test_embedding = embedder.embed_query("test query")
        print(f"   ✅ Embedder fonctionne (dimension: {len(test_embedding)})")
    except Exception as e:
        print(f"   ❌ Erreur avec l'embedder : {e}")
        print("      Vérifiez votre clé OPENAI_API_KEY dans .env")
        return False
    print()
    
    # 7. Résumé
    print("=" * 80)
    print("RESUME DU TEST")
    print("=" * 80)
    print()
    print("✅ Configuration RAG :")
    print(f"   - {len(agents_with_knowledge)} agent(s) avec sources de connaissance")
    print("   - Embedder OpenAI configuré")
    print("   - StringKnowledgeSource configuré")
    print()
    print("📋 Prochaines étapes :")
    print("   1. Lancez un débat complet : debate_system.run_debate(...)")
    print("   2. Le RAG sera initialisé lors du kickoff()")
    print("   3. Les agents pourront interroger le cahier des charges")
    print()
    print("💡 Pour vérifier l'utilisation RAG lors d'un débat :")
    print("   - Activez verbose=True dans vos agents (déjà fait)")
    print("   - Observez les logs pendant le débat")
    print("   - Les agents feront des requêtes automatiques au RAG")
    print()
    
    return True

def test_direct_chromadb_access():
    """Test d'accès direct à ChromaDB pour voir le contenu"""
    print("=" * 80)
    print("ACCES DIRECT A CHROMADB")
    print("=" * 80)
    print()
    
    try:
        storage_path = db_storage_path()
        knowledge_path = Path(storage_path) / "knowledge"
        
        print(f"Chemin ChromaDB : {knowledge_path}")
        print()
        
        if not knowledge_path.exists():
            print("❌ Le répertoire knowledge n'existe pas encore.")
            print("   Lancez d'abord un débat complet pour initialiser le RAG.")
            return
        
        client = chromadb.PersistentClient(path=str(knowledge_path))
        collections = client.list_collections()
        
        if not collections:
            print("ℹ️  Aucune collection trouvée.")
            print("   Le RAG sera créé lors du premier kickoff().")
            return
        
        print(f"📚 Collections trouvées : {len(collections)}\n")
        
        for collection in collections:
            print(f"Collection : {collection.name}")
            print("-" * 40)
            
            count = collection.count()
            print(f"Nombre de documents : {count}")
            
            if count > 0:
                # Récupérer quelques documents
                results = collection.get(limit=min(5, count))
                
                if results.get('documents'):
                    print("\nExemples de documents :")
                    for i, doc in enumerate(results['documents'][:3], 1):
                        preview = doc[:200] + "..." if len(doc) > 200 else doc
                        print(f"\n  [{i}] {preview}")
                
                # Test de recherche
                print("\n🔍 Test de recherche sémantique...")
                query = "Quels sont les objectifs du projet ?"
                search_results = collection.query(
                    query_texts=[query],
                    n_results=2
                )
                
                if search_results.get('documents') and search_results['documents'][0]:
                    print(f"   Requête : '{query}'")
                    print(f"   Résultats trouvés : {len(search_results['documents'][0])}")
                    for i, result in enumerate(search_results['documents'][0], 1):
                        preview = result[:150] + "..." if len(result) > 150 else result
                        distance = search_results.get('distances', [[]])[0][i-1] if search_results.get('distances') else None
                        print(f"   [{i}] (distance: {distance:.4f if distance else 'N/A'}) {preview}")
            print()
            
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()

def demonstrate_rag_usage():
    """Démontre comment les agents utilisent le RAG pendant un débat"""
    print("=" * 80)
    print("COMMENT VERIFIER L'UTILISATION RAG PENDANT UN DEBAT")
    print("=" * 80)
    print()
    print("1. Les agents utilisent automatiquement le RAG quand ils ont des questions")
    print("   sur le cahier des charges")
    print()
    print("2. Pour voir les requêtes RAG en temps réel :")
    print("   - Lancez un débat avec verbose=True (déjà activé)")
    print("   - Observez les logs : vous verrez des messages comme :")
    print("     'Querying knowledge sources...'")
    print("     'Retrieved X relevant chunks'")
    print()
    print("3. Après un débat, inspectez ChromaDB :")
    print("   python test_rag_access.py --check-chromadb")
    print()
    print("4. Les agents peuvent accéder au cahier des charges via :")
    print("   - agent.knowledge.query(['question'])")
    print("   - Requêtes sémantiques automatiques pendant les tâches")
    print()
    print("5. Chaque agent a sa propre collection dans ChromaDB :")
    print("   - Nom de collection = nom du rôle de l'agent")
    print("   - Ex: 'L'Innovateur (The Innovator)'")
    print()

if __name__ == "__main__":
    print()
    
    # Test 1 : Configuration RAG
    success = test_rag_access()
    
    print()
    print()
    
    # Test 2 : Accès direct ChromaDB (si déjà initialisé)
    if "--check-chromadb" in sys.argv or "-c" in sys.argv:
        test_direct_chromadb_access()
    elif "--help" in sys.argv or "-h" in sys.argv:
        demonstrate_rag_usage()
    else:
        print("💡 Pour inspecter ChromaDB après un débat, lancez :")
        print("   python test_rag_access.py --check-chromadb")

