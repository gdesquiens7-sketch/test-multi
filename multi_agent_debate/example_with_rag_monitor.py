#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemple avec monitoring RAG en temps réel pendant le débat
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
import chromadb
from pathlib import Path
from crewai.utilities.paths import db_storage_path
import time
import threading

class RAGMonitor:
    """Monitor pour surveiller l'utilisation du RAG pendant un débat"""
    
    def __init__(self, check_interval=2):
        """
        Args:
            check_interval: Intervalle en secondes entre chaque vérification
        """
        self.check_interval = check_interval
        self.monitoring = False
        self.storage_path = Path(db_storage_path()) / "knowledge"
        self.last_collection_counts = {}
        self.query_count = 0
        self.monitor_thread = None
    
    def start_monitoring(self):
        """Démarre le monitoring en arrière-plan"""
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        print("\n" + "="*80)
        print("🔍 MONITORING RAG ACTIVÉ")
        print("="*80)
        print("   Surveillance des requêtes RAG en temps réel...")
        print("   (Appuyez sur Ctrl+C pour arrêter le monitoring)")
        print("="*80 + "\n")
    
    def stop_monitoring(self):
        """Arrête le monitoring"""
        self.monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=1)
        print("\n" + "="*80)
        print("✅ MONITORING RAG TERMINÉ")
        print("="*80)
        print(f"   Nombre total de requêtes RAG détectées : {self.query_count}")
        print("="*80 + "\n")
    
    def _monitor_loop(self):
        """Boucle de monitoring"""
        while self.monitoring:
            try:
                self._check_rag_activity()
                time.sleep(self.check_interval)
            except Exception as e:
                if self.monitoring:  # Ne pas afficher l'erreur si on arrête volontairement
                    print(f"⚠️  Erreur monitoring: {e}")
    
    def _check_rag_activity(self):
        """Vérifie l'activité RAG dans ChromaDB"""
        if not self.storage_path.exists():
            return
        
        try:
            client = chromadb.PersistentClient(path=str(self.storage_path))
            collections = client.list_collections()
            
            for collection in collections:
                collection_name = collection.name
                current_count = collection.count()
                
                # Si c'est la première fois qu'on voit cette collection
                if collection_name not in self.last_collection_counts:
                    self.last_collection_counts[collection_name] = current_count
                    if current_count > 0:
                        print(f"\n📚 Collection RAG détectée : {collection_name}")
                        print(f"   Documents initiaux : {current_count}")
                
                # Si le nombre de documents a augmenté
                elif current_count > self.last_collection_counts[collection_name]:
                    diff = current_count - self.last_collection_counts[collection_name]
                    self.last_collection_counts[collection_name] = current_count
                    self.query_count += diff
                    
                    # Afficher l'activité
                    agent_name = collection_name.split('(')[0].strip() if '(' in collection_name else collection_name
                    print(f"\n🔍 RAG ACTIVITÉ DÉTECTÉE")
                    print(f"   Agent : {agent_name}")
                    print(f"   Nouveaux documents : +{diff}")
                    print(f"   Total documents : {current_count}")
                    
                    # Afficher un échantillon du dernier document
                    if current_count > 0:
                        try:
                            results = collection.get(limit=1, offset=current_count-1)
                            if results.get('documents') and results['documents']:
                                doc_preview = results['documents'][0][:150] + "..." if len(results['documents'][0]) > 150 else results['documents'][0]
                                print(f"   📄 Dernier chunk : {doc_preview}")
                        except:
                            pass
                
        except Exception as e:
            pass  # Ignorer les erreurs pendant le monitoring
    
    def get_final_stats(self):
        """Récupère les statistiques finales"""
        stats = {
            "query_count": self.query_count,
            "collections": {}
        }
        
        if self.storage_path.exists():
            try:
                client = chromadb.PersistentClient(path=str(self.storage_path))
                collections = client.list_collections()
                
                for collection in collections:
                    stats["collections"][collection.name] = {
                        "documents": collection.count()
                    }
            except:
                pass
        
        return stats

def monitor_rag_during_debate(cahier_des_charges, output_file=None):
    """Lance un débat avec monitoring RAG en temps réel"""
    
    # Créer le système de débat
    debate_system = MultiAgentDebateCrew(
        model_name=os.getenv("MODEL_NAME", "openrouter/deepseek/deepseek-chat"),
        temperature=float(os.getenv("TEMPERATURE", "0.7"))
    )
    
    # Créer le monitor
    monitor = RAGMonitor(check_interval=1)  # Vérifie toutes les secondes
    
    # Démarrer le monitoring
    monitor.start_monitoring()
    
    try:
        # Lancer le débat
        print("\n🚀 Lancement du débat avec monitoring RAG...\n")
        result = debate_system.run_debate(
            cahier_des_charges=cahier_des_charges,
            output_file=output_file
        )
        
        # Attendre un peu pour laisser le RAG finir
        time.sleep(2)
        
        return result, monitor.get_final_stats()
    
    finally:
        # Arrêter le monitoring
        monitor.stop_monitoring()
        
        # Afficher les statistiques finales
        stats = monitor.get_final_stats()
        print("\n" + "="*80)
        print("📊 STATISTIQUES RAG FINALES")
        print("="*80)
        print(f"   Requêtes RAG détectées : {stats['query_count']}")
        print(f"   Collections créées : {len(stats['collections'])}")
        
        if stats['collections']:
            print("\n   Détails par collection :")
            for collection_name, data in stats['collections'].items():
                agent_name = collection_name.split('(')[0].strip() if '(' in collection_name else collection_name
                print(f"      - {agent_name} : {data['documents']} documents")
        
        print("="*80 + "\n")

def main():
    """Fonction principale"""
    
    print("\n" + "="*80)
    print("EXEMPLE : Débat avec Monitoring RAG en Temps Réel")
    print("="*80 + "\n")
    
    # Vérification de la configuration
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ ERREUR : OPENROUTER_API_KEY non définie")
        print("\nVeuillez configurer votre clé API dans .env")
        return
    
    # Cahier des charges de test (plus court pour démonstration)
    cahier_des_charges = """
CAHIER DES CHARGES : Test RAG avec Monitoring

1. OBJECTIF
Tester le système RAG avec monitoring en temps réel.

2. EXIGENCES FONCTIONNELLES
- EF1 : Les agents doivent pouvoir interroger le cahier des charges
- EF2 : Le monitoring doit afficher les requêtes RAG en temps réel

3. EXIGENCES TECHNIQUES
- ET1 : ChromaDB doit fonctionner correctement
- ET2 : Les embeddings doivent être générés

4. CONTRAINTES
- Budget : 10 000 €
- Délai : 1 mois

5. CRITÈRES DE SUCCÈS
- CS1 : Le monitoring détecte les requêtes RAG
- CS2 : Les agents utilisent le cahier des charges
"""
    
    # Lancer avec monitoring
    try:
        result, stats = monitor_rag_during_debate(
            cahier_des_charges=cahier_des_charges,
            output_file="output/test_rag_monitor.md"
        )
        
        print("\n" + "="*80)
        print("✅ DÉBAT TERMINÉ")
        print("="*80)
        print("\n📄 Le résultat a été sauvegardé.")
        print("\n💡 Pour inspecter ChromaDB en détail :")
        print("   python test_rag_access.py --check-chromadb")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Débat interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n\n❌ Erreur lors du débat : {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

