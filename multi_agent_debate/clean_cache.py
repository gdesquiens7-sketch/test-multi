#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de nettoyage complet des caches pour Windows/Linux/macOS
Nettoie : Python cache, CrewAI cache, ChromaDB, etc.
"""
import os
import shutil
import sys
from pathlib import Path

# Forcer UTF-8 pour Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def clean_python_cache():
    """Nettoie les caches Python (__pycache__, *.pyc, *.pyo)"""
    print("🧹 Nettoyage du cache Python...")
    
    current_dir = Path(__file__).parent
    cleaned = 0
    
    # Supprimer __pycache__
    for pycache_dir in current_dir.rglob("__pycache__"):
        try:
            shutil.rmtree(pycache_dir)
            print(f"  ✅ Supprimé : {pycache_dir.relative_to(current_dir)}")
            cleaned += 1
        except Exception as e:
            print(f"  ⚠️  Erreur avec {pycache_dir}: {e}")
    
    # Supprimer *.pyc et *.pyo
    for pyc_file in current_dir.rglob("*.pyc"):
        try:
            pyc_file.unlink()
            print(f"  ✅ Supprimé : {pyc_file.relative_to(current_dir)}")
            cleaned += 1
        except Exception as e:
            print(f"  ⚠️  Erreur avec {pyc_file}: {e}")
    
    for pyo_file in current_dir.rglob("*.pyo"):
        try:
            pyo_file.unlink()
            print(f"  ✅ Supprimé : {pyo_file.relative_to(current_dir)}")
            cleaned += 1
        except Exception as e:
            print(f"  ⚠️  Erreur avec {pyo_file}: {e}")
    
    print(f"✅ Cache Python nettoyé ({cleaned} éléments supprimés)\n")
    return cleaned

def clean_crewai_cache():
    """Nettoie le cache CrewAI (mémoire, connaissances, ChromaDB)"""
    print("🧹 Nettoyage du cache CrewAI...")
    
    # Chemins possibles pour le cache CrewAI
    if sys.platform == "win32":
        # Windows
        appdata_local = os.getenv("LOCALAPPDATA", os.path.expanduser("~\\AppData\\Local"))
        crewai_cache = Path(appdata_local) / "CrewAI"
    elif sys.platform == "darwin":
        # macOS
        crewai_cache = Path.home() / ".local" / "share" / "CrewAI"
    else:
        # Linux
        crewai_cache = Path.home() / ".local" / "share" / "CrewAI"
    
    cleaned_items = []
    
    if crewai_cache.exists():
        try:
            # Compter le nombre d'éléments avant suppression
            items_before = sum(1 for _ in crewai_cache.rglob("*") if _.is_file())
            
            # Supprimer tout le cache CrewAI
            shutil.rmtree(crewai_cache)
            print(f"  ✅ Cache CrewAI supprimé : {crewai_cache}")
            print(f"     ({items_before} fichiers/dossiers supprimés)")
            cleaned_items.append(str(crewai_cache))
        except Exception as e:
            print(f"  ⚠️  Erreur lors de la suppression du cache CrewAI : {e}")
    else:
        print(f"  ℹ️  Pas de cache CrewAI trouvé à : {crewai_cache}")
    
    # Vérifier aussi dans le répertoire courant
    current_dir = Path(__file__).parent
    local_crewai_dirs = [
        current_dir / ".crewai",
        current_dir / "crewai_cache",
        current_dir / ".chromadb",
        current_dir / "chroma_db",
    ]
    
    for cache_dir in local_crewai_dirs:
        if cache_dir.exists():
            try:
                items = sum(1 for _ in cache_dir.rglob("*") if _.is_file())
                shutil.rmtree(cache_dir)
                print(f"  ✅ Cache local supprimé : {cache_dir.relative_to(current_dir)}")
                print(f"     ({items} fichiers/dossiers supprimés)")
                cleaned_items.append(str(cache_dir))
            except Exception as e:
                print(f"  ⚠️  Erreur avec {cache_dir}: {e}")
    
    if cleaned_items:
        print(f"✅ Cache CrewAI nettoyé ({len(cleaned_items)} dossier(s) supprimé(s))\n")
    else:
        print("✅ Pas de cache CrewAI à nettoyer\n")
    
    return len(cleaned_items)

def clean_output_dir():
    """Nettoie le dossier de sortie (optionnel)"""
    print("🧹 Nettoyage du dossier de sortie...")
    
    current_dir = Path(__file__).parent
    output_dir = current_dir / "output"
    
    if output_dir.exists():
        try:
            items = sum(1 for _ in output_dir.rglob("*") if _.is_file())
            shutil.rmtree(output_dir)
            output_dir.mkdir(exist_ok=True)
            print(f"  ✅ Dossier de sortie nettoyé : {output_dir.relative_to(current_dir)}")
            print(f"     ({items} fichiers supprimés)\n")
            return items
        except Exception as e:
            print(f"  ⚠️  Erreur avec {output_dir}: {e}\n")
            return 0
    else:
        print(f"  ℹ️  Pas de dossier output trouvé\n")
        return 0

def main():
    """Fonction principale"""
    print("=" * 80)
    print("NETTOYAGE COMPLET DES CACHES")
    print("=" * 80)
    print()
    
    total_cleaned = 0
    
    # 1. Cache Python
    total_cleaned += clean_python_cache()
    
    # 2. Cache CrewAI
    total_cleaned += clean_crewai_cache()
    
    # 3. Dossier de sortie (optionnel - décommentez si vous voulez le nettoyer aussi)
    # total_cleaned += clean_output_dir()
    
    print("=" * 80)
    print(f"✅ NETTOYAGE TERMINÉ")
    print("=" * 80)
    print()
    print("📋 Prochaines étapes :")
    print("  1. Fermez toutes les sessions Python actives")
    print("  2. Relancez votre script")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Nettoyage interrompu par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Erreur lors du nettoyage : {e}")
        sys.exit(1)

