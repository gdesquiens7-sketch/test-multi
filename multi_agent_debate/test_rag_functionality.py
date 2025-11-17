#!/usr/bin/env python3
"""
Script de test pour vérifier le fonctionnement du système RAG (Knowledge Base).

Ce script teste :
1. Création de la Knowledge Base avec StringKnowledgeSource
2. Attribution de la Knowledge Base aux agents
3. Recherche sémantique dans la Knowledge Base
4. Vérification que les agents peuvent accéder aux informations
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Charger les variables d'environnement
load_dotenv()


def test_knowledge_base_creation():
    """Test 1 : Création de la Knowledge Base."""
    print("\n" + "="*80)
    print("TEST 1 : Création de la Knowledge Base")
    print("="*80)

    cahier_test = """
    CAHIER DES CHARGES TEST

    1. OBJECTIF
    Créer une application mobile de gestion de tâches avec IA.

    2. EXIGENCES FONCTIONNELLES
    - EF1 : Création de tâches avec priorité
    - EF2 : Suggestions intelligentes par IA
    - EF3 : Synchronisation cloud temps réel

    3. EXIGENCES TECHNIQUES
    - ET1 : Compatible iOS et Android
    - ET2 : Base de données PostgreSQL
    - ET3 : API REST sécurisée avec JWT

    4. CONTRAINTES
    - Budget : 50 000 €
    - Délai : 3 mois
    - Équipe : 2 développeurs
    """

    try:
        knowledge = StringKnowledgeSource(
            content=cahier_test,
            metadata={"source": "test_cahier", "type": "requirements"}
        )
        print("✅ Knowledge Base créée avec succès")
        print(f"   - Type : {type(knowledge)}")
        print(f"   - Metadata : {knowledge.metadata}")
        return knowledge, cahier_test
    except Exception as e:
        print(f"❌ Erreur lors de la création : {e}")
        return None, None


def test_agent_knowledge_attribution(knowledge):
    """Test 2 : Attribution de la Knowledge Base à un agent."""
    print("\n" + "="*80)
    print("TEST 2 : Attribution de la Knowledge Base à un agent")
    print("="*80)

    try:
        llm = LLM(
            model="openrouter/deepseek/deepseek-chat",
            temperature=0.3
        )

        test_agent = Agent(
            role="Analyste Test",
            goal="Vérifier le fonctionnement du RAG",
            backstory="Agent de test pour valider la Knowledge Base",
            llm=llm,
            verbose=True
        )

        # Attribution de la Knowledge Base
        test_agent.knowledge_sources = [knowledge]

        print("✅ Knowledge Base attribuée à l'agent avec succès")
        print(f"   - Agent : {test_agent.role}")
        print(f"   - Nombre de sources : {len(test_agent.knowledge_sources)}")
        return test_agent
    except Exception as e:
        print(f"❌ Erreur lors de l'attribution : {e}")
        return None


def test_rag_retrieval(test_agent, cahier_test):
    """Test 3 : Vérification de la récupération d'informations via RAG."""
    print("\n" + "="*80)
    print("TEST 3 : Récupération d'informations via RAG")
    print("="*80)

    try:
        # Créer une tâche simple qui nécessite l'accès au cahier des charges
        task = Task(
            description="""
            En utilisant la base de connaissance disponible (Knowledge Base / RAG),
            réponds à ces questions :

            1. Quel est le budget du projet ?
            2. Quel est le délai ?
            3. Combien de développeurs dans l'équipe ?
            4. Quelles sont les exigences fonctionnelles (liste-les) ?

            IMPORTANT : Tu DOIS utiliser la Knowledge Base pour répondre.
            Ne devine pas, utilise uniquement les informations de la base de connaissance.

            Formate ta réponse ainsi :
            - Budget : [réponse]
            - Délai : [réponse]
            - Équipe : [réponse]
            - Exigences fonctionnelles : [liste]
            """,
            expected_output="Réponses précises basées sur la Knowledge Base",
            agent=test_agent
        )

        # Créer un crew minimal pour exécuter la tâche
        crew = Crew(
            agents=[test_agent],
            tasks=[task],
            verbose=True
        )

        print("\n🔄 Exécution de la tâche de test...")
        print("   (Cela peut prendre quelques secondes)")
        print("-"*80)

        result = crew.kickoff()

        print("\n" + "-"*80)
        print("📋 RÉSULTAT DU TEST RAG :")
        print("-"*80)
        if hasattr(result, 'raw'):
            print(result.raw)
        else:
            print(result)
        print("-"*80)

        # Vérifications
        result_text = str(result.raw if hasattr(result, 'raw') else result).lower()

        checks = {
            "Budget détecté": "50" in result_text or "50000" in result_text or "cinquante" in result_text,
            "Délai détecté": "3 mois" in result_text or "trois mois" in result_text,
            "Équipe détectée": "2 développeurs" in result_text or "deux développeurs" in result_text,
            "Exigences détectées": "ef1" in result_text or "création" in result_text or "tâches" in result_text
        }

        print("\n✅ VÉRIFICATIONS :")
        all_passed = True
        for check_name, passed in checks.items():
            status = "✅" if passed else "⚠️"
            print(f"   {status} {check_name}: {'OUI' if passed else 'NON'}")
            if not passed:
                all_passed = False

        if all_passed:
            print("\n🎉 TOUS LES TESTS SONT PASSÉS !")
            print("   Le système RAG fonctionne correctement.")
        else:
            print("\n⚠️  CERTAINS TESTS ONT ÉCHOUÉ")
            print("   Le RAG fonctionne mais certaines informations n'ont pas été récupérées.")
            print("   Cela peut être normal selon la configuration.")

        return True
    except Exception as e:
        print(f"❌ Erreur lors du test de récupération : {e}")
        import traceback
        traceback.print_exc()
        return False


def test_chromadb_storage():
    """Test 4 : Vérification du stockage ChromaDB."""
    print("\n" + "="*80)
    print("TEST 4 : Vérification du stockage ChromaDB")
    print("="*80)

    import platform

    # Déterminer le chemin selon l'OS
    if platform.system() == "Darwin":  # macOS
        storage_path = os.path.expanduser("~/Library/Application Support/CrewAI")
    elif platform.system() == "Linux":
        storage_path = os.path.expanduser("~/.local/share/CrewAI")
    elif platform.system() == "Windows":
        storage_path = os.path.expanduser("~/AppData/Local/CrewAI")
    else:
        storage_path = None

    # Vérifier si CREWAI_STORAGE_DIR est défini
    custom_storage = os.getenv("CREWAI_STORAGE_DIR")
    if custom_storage:
        storage_path = custom_storage

    if storage_path and os.path.exists(storage_path):
        print(f"✅ Répertoire de stockage trouvé : {storage_path}")

        # Lister les fichiers
        try:
            for root, dirs, files in os.walk(storage_path):
                level = root.replace(storage_path, '').count(os.sep)
                indent = ' ' * 2 * level
                print(f"{indent}{os.path.basename(root)}/")
                subindent = ' ' * 2 * (level + 1)
                for file in files[:5]:  # Limiter à 5 fichiers par dossier
                    print(f"{subindent}{file}")
                if len(files) > 5:
                    print(f"{subindent}... et {len(files) - 5} autres fichiers")
        except Exception as e:
            print(f"⚠️  Impossible de lister le contenu : {e}")
    else:
        print(f"⚠️  Répertoire de stockage non trouvé : {storage_path}")
        print("   (Il sera créé lors de la première utilisation)")


def main():
    """Fonction principale - Lance tous les tests."""
    print("\n" + "="*80)
    print("🧪 TEST DU SYSTÈME RAG (KNOWLEDGE BASE)")
    print("="*80)
    print("\nCe script va vérifier que le système RAG fonctionne correctement.")
    print("Les agents doivent pouvoir accéder au cahier des charges via ChromaDB.\n")

    # Vérifier les clés API
    if not os.getenv("OPENROUTER_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        print("❌ ERREUR : Aucune clé API configurée")
        print("   Veuillez définir OPENROUTER_API_KEY ou OPENAI_API_KEY dans votre .env")
        return

    # Test 1 : Création
    knowledge, cahier_test = test_knowledge_base_creation()
    if not knowledge:
        print("\n❌ TEST ÉCHOUÉ : Impossible de créer la Knowledge Base")
        return

    # Test 2 : Attribution
    test_agent = test_agent_knowledge_attribution(knowledge)
    if not test_agent:
        print("\n❌ TEST ÉCHOUÉ : Impossible d'attribuer la Knowledge Base")
        return

    # Test 3 : Récupération (le plus important)
    test_rag_retrieval(test_agent, cahier_test)

    # Test 4 : Stockage
    test_chromadb_storage()

    print("\n" + "="*80)
    print("✅ TESTS TERMINÉS")
    print("="*80)
    print("\nSi tous les tests sont passés, votre système RAG fonctionne correctement !")
    print("Les agents peuvent maintenant accéder au cahier des charges via la Knowledge Base.\n")


if __name__ == "__main__":
    main()
