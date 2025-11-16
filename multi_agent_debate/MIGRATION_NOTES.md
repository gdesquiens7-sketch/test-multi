# Notes de Migration vers CrewAI 0.98.0

## Version précédente
- CrewAI 0.28.0
- LangChain 0.1.0
- OpenAI 1.10.0

## Version actuelle
- CrewAI 0.98.0
- LangChain 0.3.0
- OpenAI 1.50.0

---

## Changements Effectués

### 1. Mise à jour des dépendances (`requirements.txt`)

**Avant :**
```
crewai>=0.28.0
crewai-tools>=0.2.0
langchain>=0.1.0
langchain-openai>=0.0.5
openai>=1.10.0
```

**Après :**
```
crewai>=0.98.0
crewai-tools>=0.12.0
langchain>=0.3.0
langchain-openai>=0.2.0
openai>=1.50.0
```

### 2. Adaptation du code (`debate_crew.py`)

#### a) Gestion de CrewOutput
**Changement :** Depuis CrewAI 0.41.0, `crew.kickoff()` retourne un objet `CrewOutput` au lieu d'un dict.

**Méthode `_save_result` améliorée :**
```python
# Avant (basique)
if hasattr(result, 'raw'):
    f.write(result.raw)

# Après (robuste avec fallbacks)
if hasattr(result, 'raw'):
    f.write(str(result.raw))
elif hasattr(result, 'final_output'):
    f.write(str(result.final_output))
elif isinstance(result, dict) and 'final_output' in result:
    f.write(str(result['final_output']))
else:
    f.write(str(result))
```

#### b) Suppression de paramètres obsolètes

**Paramètres RETIRÉS de `Crew()` :**
- `max_iter=15` - N'existe plus dans l'API
- `full_output=True` - N'existe plus dans l'API

**Paramètres MODIFIÉS :**
- `verbose=2` → `verbose=True` ⚠️ **Type changé : int → boolean**
  - Avant : 0, 1, 2 (niveaux de verbosité)
  - Après : True/False (activé/désactivé)

**Structure AGENTS modifiée :**
- ⚠️ **Le manager_agent ne doit PLUS être dans la liste `agents`**
  - Avant (v0.28.0) : `agents=[agent1, agent2, manager]` + `manager_agent=manager`
  - Après (v0.98.0) : `agents=[agent1, agent2]` + `manager_agent=manager`
  - Le manager est maintenant **séparé** de la liste des agents workers

**Paramètres CONSERVÉS :**
- `process=Process.hierarchical` ✅
- `manager_agent=self.facilitateur` ✅ (toujours valide, mais exclu de agents)
- `memory=True` ✅

#### c) Type hints améliorés
```python
from typing import Union  # Ajouté pour compatibilité

def run_debate(...) -> CrewOutput:  # Type de retour mis à jour
```

---

## Breaking Changes Importants (CrewAI 0.28 → 0.98)

### ✅ Compatibles avec notre code

1. **Délégation désactivée par défaut (v0.60.0)**
   - ✅ Nous activons explicitement `allow_delegation=True` sur tous nos agents

2. **Mémoire désactivée par défaut (v0.14.4)**
   - ✅ Nous activons explicitement `memory=True` dans le Crew

3. **Retour de CrewOutput (v0.41.0)**
   - ✅ Code adapté pour gérer l'objet CrewOutput

4. **Suppression de Pipeline (v0.86.0)**
   - ✅ Nous n'utilisons pas de pipelines

### ⚠️ Points d'attention

1. **UserMemory deprecated (v0.157.0)**
   - ℹ️ Nous utilisons la mémoire standard du Crew, pas UserMemory

2. **Task.max_retries deprecated (v0.175.0)**
   - ℹ️ Nous n'utilisons pas ce paramètre

---

## Nouvelles Fonctionnalités de CrewAI 0.98.0

### Disponibles mais non utilisées dans cette version

1. **Support multimodal**
   - Les agents peuvent traiter des images
   - Activation : `multimodal=True` dans l'agent

2. **Conversational Crew**
   - Mode chat interactif : `crewai chat`

3. **Guardrails programmatiques**
   - Contrôle plus fin du comportement des agents

4. **CrewAI Flows**
   - État persistant entre les exécutions
   - Décorateur `@persist`

5. **Callbacks étendus**
   - `before_kickoff` et `after_kickoff` (v0.83.0)

### Intégrations ajoutées
- SambaNova
- NVIDIA NIM Provider
- VoyageAI

---

## Tests de Migration

### À effectuer avant utilisation en production

```bash
# 1. Installer les nouvelles dépendances
pip install -r requirements.txt

# 2. Vérifier la syntaxe
python3 -m py_compile debate_crew.py

# 3. Test basique (avec API key configurée)
python example.py
```

### Comportements à vérifier

- ✅ Le débat se lance correctement
- ✅ Les agents communiquent entre eux (délégation)
- ✅ La mémoire fonctionne (références aux échanges précédents)
- ✅ Le résultat est sauvegardé correctement (CrewOutput → fichier)
- ✅ Le processus hiérarchique fonctionne (Facilitateur manage)

---

## Compatibilité

### Python
- **Requis :** Python >= 3.10 < 3.14
- **Notre code :** Compatible

### Modèles LLM supportés
- ✅ DeepSeek (via OpenAI-compatible API)
- ✅ OpenAI (GPT-4, GPT-3.5, etc.)
- ✅ Azure OpenAI
- ✅ Anthropic Claude
- ✅ Google Gemini
- ✅ Ollama (local)

---

## Rollback (si nécessaire)

Si des problèmes surviennent avec CrewAI 0.98.0, rollback vers 0.28.0 :

```bash
# Restaurer les anciennes versions
pip install crewai==0.28.0 crewai-tools==0.2.0 langchain==0.1.0 langchain-openai==0.0.5 openai==1.10.0

# Restaurer l'ancien code
git checkout HEAD~1 multi_agent_debate/debate_crew.py
git checkout HEAD~1 multi_agent_debate/requirements.txt
```

---

## Références

- [CrewAI Changelog](https://docs.crewai.com/en/changelog)
- [CrewAI Documentation](https://docs.crewai.com)
- [Hierarchical Process](https://docs.crewai.com/how-to/hierarchical-process)
- [Custom Manager Agent](https://docs.crewai.com/how-to/custom-manager-agent)

---

**Date de migration :** 16 novembre 2024
**Version du système :** 1.0.0 → 1.1.0
