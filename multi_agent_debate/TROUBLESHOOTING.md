# 🔧 Guide de Dépannage - Problèmes CrewAI 0.98.0

## ❌ Erreurs courantes

### Erreur 1 : `verbose` doit être un booléen

```
1 validation error for Crew
verbose
  Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value=2, input_type=int]
```

### Erreur 2 : Manager agent dans la liste agents

```
1 validation error for Crew
Manager agent should not be included in agents list. [type=manager_agent_in_agents, ...]
```

**Cause** : Dans CrewAI 0.98.0, le `manager_agent` ne doit PAS être inclus dans la liste `agents`.

**Solution** : Voir section "Solutions" ci-dessous.

---

## 🎯 Cause du problème

Vous avez **CrewAI 0.98.0** installé (qui nécessite `verbose=True/False`), mais Python utilise **une version en cache du code** avec l'ancien paramètre `verbose=2`.

---

## ✅ Solutions (par ordre de préférence)

### Solution 1 : Redémarrage complet (RECOMMANDÉ)

```bash
# 1. Fermer TOUTES les sessions Python actives
# (terminal, Jupyter, IPython, IDE, etc.)

# 2. Nettoyer le cache
cd /home/user/test-multi/multi_agent_debate
bash clean_cache.sh

# 3. Relancer le script
python3 example.py
```

### Solution 2 : Utiliser le script de test propre

```bash
cd /home/user/test-multi/multi_agent_debate
python3 test_clean.py
```

Ce script force le rechargement complet de tous les modules.

### Solution 3 : Exécution sans cache

```bash
cd /home/user/test-multi/multi_agent_debate
python3 -B example.py
```

Le flag `-B` désactive l'utilisation des fichiers `.pyc` en cache.

### Solution 4 : Forcer le rechargement dans votre code

Si vous utilisez un script personnalisé :

```python
import sys

# Supprimer les modules en cache
modules_to_remove = [k for k in sys.modules.keys()
                     if 'debate' in k or 'config' in k]
for mod in modules_to_remove:
    del sys.modules[mod]

# Maintenant importer
from debate_crew import MultiAgentDebateCrew
```

---

## 🔍 Vérification que le code est correct

Le code source actuel utilise bien `verbose=True` :

```bash
# Vérifier le fichier principal
grep "verbose" debate_crew.py
# Résultat attendu : verbose=True,  # CrewAI 0.98.0...

# Vérifier tous les fichiers
grep -r "verbose.*2" .
# Résultat attendu : (aucun résultat)
```

---

## 🧪 Test rapide

Pour tester si le problème est résolu :

```bash
cd /home/user/test-multi/multi_agent_debate

python3 << 'EOF'
import sys
# Force le rechargement
for k in list(sys.modules.keys()):
    if 'debate' in k or 'config' in k:
        del sys.modules[k]

from debate_crew import MultiAgentDebateCrew
import os

os.environ['OPENAI_API_KEY'] = 'test'
os.environ['OPENAI_API_BASE'] = 'https://api.deepseek.com'

system = MultiAgentDebateCrew()
crew = system.create_crew("Test")
print(f"✅ Verbose = {crew.verbose} (type: {type(crew.verbose).__name__})")
print("✅ Pas d'erreur de validation !")
EOF
```

Si vous voyez `✅ Verbose = True (type: bool)`, le problème est résolu !

---

## 🐛 Si le problème persiste

### Vérifier la version de CrewAI installée

```bash
pip show crewai
```

Vous devriez voir :
```
Version: 0.98.0 (ou supérieur)
```

Si vous voyez une version < 0.98.0 :

```bash
pip install --upgrade crewai>=0.98.0
```

### Vérifier les imports

Assurez-vous de ne pas avoir de fichier `debate_crew.py` ou `config.py` dans votre **répertoire de travail actuel** qui pourrait masquer les vrais fichiers.

```bash
# Vérifier où Python trouve les modules
python3 -c "import debate_crew; print(debate_crew.__file__)"
```

Le chemin doit être : `/home/user/test-multi/multi_agent_debate/debate_crew.py`

### Vérifier les variables d'environnement Python

Certaines variables peuvent forcer Python à utiliser des caches :

```bash
# Désactiver tous les caches pour cette session
export PYTHONDONTWRITEBYTECODE=1
python3 example.py
```

---

## 📋 Checklist de diagnostic

- [ ] J'ai fermé toutes les sessions Python/IPython/Jupyter
- [ ] J'ai exécuté `bash clean_cache.sh`
- [ ] J'ai vérifié que `grep "verbose" debate_crew.py` retourne `verbose=True`
- [ ] J'ai vérifié que CrewAI >= 0.98.0 est installé (`pip show crewai`)
- [ ] J'ai essayé `python3 -B example.py`
- [ ] J'ai essayé `python3 test_clean.py`

Si tous les points sont cochés et l'erreur persiste, contactez le support.

---

## ✨ Une fois le problème résolu

Supprimez les fichiers de dépannage si vous le souhaitez :

```bash
rm clean_cache.sh test_clean.py TROUBLESHOOTING.md
```

---

**Dernière mise à jour** : 16 novembre 2024
