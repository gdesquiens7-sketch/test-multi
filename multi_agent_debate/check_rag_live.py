#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour vérifier le RAG pendant qu'un débat est en cours
Vérifie plusieurs emplacements possibles de ChromaDB
"""
import os
import sys
from pathlib import Path
import time

# Forcer UTF-8 pour Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def find_chromadb_locations():
    """Trouve tous les emplacements possibles de ChromaDB"""
    locations = []
    
    # 1. Emplacement standard CrewAI
    try:
        from crewai.utilities.paths import db_storage_path
        standard_path = Path(db_storage_path()) / "knowledge"
        locations.append(("Standard CrewAI", standard_path))
    except:
        pass
    
    # 2. AppData Local (Windows)
    if sys.platform == "win32":
        appdata_local = os.getenv("LOCALAPPDATA", "")
        if appdata_local:
            paths = [
                Path(appdata_local) / "CrewAI" / "knowledge",
                Path(appdata_local) / "CrewAI" / "multi_agent_debate" / "knowledge",
            ]
            for path in paths:
                locations.append(("Windows AppData", path))
    
    # 3. Répertoire courant
    current_dir = Path.cwd()
    local_paths = [
        current_dir / ".crewai" / "knowledge",
        current_dir / "crewai_cache" / "knowledge",
        current_dir / ".chromadb",
        current_dir / "chroma_db",
        current_dir / "knowledge",
    ]
    for path in local_paths:
        locations.append(("Répertoire local", path))
    
    # 4. Home directory
    home = Path.home()
    home_paths = [
        home / ".local" / "share" / "CrewAI" / "knowledge",
        home / ".crewai" / "knowledge",
    ]
    for path in home_paths:
        locations.append(("Home directory", path))
    
    return locations

def check_chromadb(path, label):
    """Vérifie si ChromaDB existe à cet emplacement"""
    if not path.exists():
        return None, None
    
    try:
        import chromadb
        client = chromadb.PersistentClient(path=str(path))
        collections = client.list_collections()
        
        collections_info = []
        for collection in collections:
            count = collection.count()
            collections_info.append({
                "name": collection.name,
                "count": count
            })
        
        return True, collections_info
    except Exception as e:
        return False, str(e)

def main():
    """Fonction principale"""
    print("=" * 80)
    print("RECHERCHE DE CHROMADB PENDANT UN DEBAT")
    print("=" * 80)
    print()
    print("🔍 Recherche de ChromaDB dans tous les emplacements possibles...")
    print()
    
    locations = find_chromadb_locations()
    
    found_any = False
    all_collections = {}
    
    for label, path in locations:
        print(f"📁 {label}: {path}")
        exists = path.exists()
        
        if exists:
            print(f"   ✅ Répertoire existe")
            status, info = check_chromadb(path, label)
            
            if status is True:
                print(f"   ✅ ChromaDB accessible")
                if info:
                    for col_info in info:
                        col_name = col_info["name"]
                        col_count = col_info["count"]
                        print(f"      📚 Collection: {col_name} ({col_count} documents)")
                        
                        if path not in all_collections:
                            all_collections[path] = []
                        all_collections[path].append(col_info)
                    found_any = True
                else:
                    print(f"      ℹ️  Aucune collection trouvée (pas encore initialisée)")
            elif status is False:
                print(f"   ⚠️  ChromaDB non accessible: {info}")
            else:
                print(f"   ⚠️  Erreur inconnue")
        else:
            print(f"   ❌ Répertoire n'existe pas")
        
        print()
    
    if found_any:
        print("=" * 80)
        print("✅ CHROMADB TROUVÉ ET ACTIF")
        print("=" * 80)
        print()
        print("📊 Récapitulatif des collections :")
        for path, collections in all_collections.items():
            print(f"\n   Emplacement : {path}")
            for col in collections:
                print(f"      - {col['name']} : {col['count']} documents")
        
        print()
        print("💡 Les agents utilisent bien le RAG !")
        print()
    else:
        print("=" * 80)
        print("⚠️  CHROMADB NON TROUVÉ OU PAS ENCORE INITIALISÉ")
        print("=" * 80)
        print()
        print("Cela peut signifier :")
        print("   1. Le débat vient de commencer et le RAG n'est pas encore initialisé")
        print("   2. Le RAG sera créé lors du premier kickoff()")
        print("   3. Le débat n'utilise pas encore le RAG")
        print()
        print("💡 Suggestions :")
        print("   - Attendez que le débat progresse")
        print("   - Réessayez dans quelques secondes")
        print("   - Utilisez le script de monitoring : python example_with_rag_monitor.py")
        print()

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Vérifie ChromaDB pendant un débat",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  # Vérification unique
  python check_rag_live.py
  
  # Surveillance en continu (recommandé pendant un débat)
  python check_rag_live.py --watch
  
  # Surveillance avec intervalle personnalisé (toutes les 2 secondes)
  python check_rag_live.py --watch --interval 2
        """
    )
    parser.add_argument("--watch", "-w", action="store_true", 
                       help="Surveille en continu (appuyez sur Ctrl+C pour arrêter)")
    parser.add_argument("--interval", "-i", type=int, default=3,
                       help="Intervalle entre les vérifications en secondes (défaut: 3)")
    
    args = parser.parse_args()
    
    if args.watch:
        print("=" * 80)
        print("🔍 MODE SURVEILLANCE ACTIVÉ")
        print("=" * 80)
        print(f"   Vérification toutes les {args.interval} secondes")
        print("   Appuyez sur Ctrl+C pour arrêter")
        print("=" * 80)
        print()
        
        iteration = 0
        try:
            while True:
                iteration += 1
                print(f"\n{'='*80}")
                print(f"VÉRIFICATION #{iteration} - {time.strftime('%H:%M:%S')}")
                print(f"{'='*80}\n")
                
                main()
                
                print(f"\n⏳ Prochaine vérification dans {args.interval} secondes...")
                print("   (Appuyez sur Ctrl+C pour arrêter)")
                time.sleep(args.interval)
                
                # Effacer l'écran pour la prochaine itération
                if sys.platform == 'win32':
                    os.system('cls')
                else:
                    os.system('clear')
                
        except KeyboardInterrupt:
            print("\n\n" + "="*80)
            print("✅ SURVEILLANCE ARRÊTÉE")
            print("="*80)
            print(f"\nNombre de vérifications effectuées : {iteration}")
            print()
    else:
        main()
        
        print("\n💡 TIP : Pour surveiller en continu pendant un débat :")
        print("   python check_rag_live.py --watch")
        print()

