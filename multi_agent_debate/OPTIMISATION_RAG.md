# Optimisation RAG - Base de Connaissance CrewAI

## Vue d'ensemble

Ce système multi-agent utilise la **Knowledge Base de CrewAI** pour optimiser l'utilisation des tokens en stockant le cahier des charges dans une base vectorielle (ChromaDB) au lieu de le dupliquer dans chaque tâche.

## Architecture

### Avant l'optimisation ❌
```
Task 1: Cahier des charges (270 lignes) → Analysé
Task 2: Cahier des charges (270 lignes) → Analysé
Task 3: Cahier des charges (270 lignes) → Analysé
Task 4: Cahier des charges (270 lignes) → Analysé
Task 5: Cahier des charges (270 lignes) → Analysé
Task 6: Cahier des charges (270 lignes) → Analysé

Total: 1620 lignes dupliquées dans les prompts
```

### Après l'optimisation ✅
```
Knowledge Base (ChromaDB): Cahier des charges (270 lignes) → Stocké UNE SEULE FOIS

Task 1: Accès RAG → Récupère sections pertinentes
Task 2: Accès RAG → Récupère sections pertinentes
Task 3: Accès RAG → Récupère sections pertinentes
Task 4: Accès RAG → Récupère sections pertinentes
Task 5: Accès RAG → Récupère sections pertinentes
Task 6: Accès RAG → Récupère sections pertinentes

Total: 0 ligne dupliquée, ~90% d'économie de tokens
```

## Implémentation

### 1. Configuration de la Knowledge Base

Dans `debate_crew.py` :

```python
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Création de la source de connaissance
cahier_knowledge = StringKnowledgeSource(
    content=cahier_des_charges,
    metadata={"source": "cahier_des_charges", "type": "requirements"}
)

# Attribution aux agents
for agent in [innovateur, pragmatique, avocat_du_diable, stratege, facilitateur]:
    agent.knowledge_sources = [cahier_knowledge]
```

### 2. Accès automatique par les agents

Les agents accèdent automatiquement à la Knowledge Base lors de l'exécution de leurs tâches. Pas besoin de code spécial - CrewAI gère la récupération sémantique.

### 3. Modifications des tâches

Dans `tasks.py`, au lieu de :
```python
description=f"""
CAHIER DES CHARGES :
{cahier_des_charges}

MISSION : ...
"""
```

On utilise :
```python
description=f"""
ACCÈS AU CAHIER DES CHARGES :
Le cahier des charges est disponible dans la base de connaissance (RAG).
Vous y avez accès automatiquement.

MISSION : ...
"""
```

## Stack Technique

- **Vector Store** : ChromaDB (par défaut)
- **Embeddings** : OpenAI `text-embedding-3-small`
- **Retrieval** : Recherche sémantique automatique par CrewAI
- **Storage** : `~/.local/share/CrewAI/{project}/knowledge/` (Linux)

## Coûts

### Embeddings (OpenAI text-embedding-3-small)
- Coût : ~$0.002 par débat
- Calculé une seule fois au début (pas de ré-embedding)

### Tokens de prompt
- **Économie estimée** : ~90% sur les prompts
- **Avant** : 270 lignes × 6 tasks = 1620 lignes dans les prompts
- **Après** : 0 ligne dupliquée + retrieval sélectif via RAG

## Combinaison RAG + Memory

Le système utilise deux mécanismes complémentaires :

1. **RAG (Knowledge Base)**
   - **Rôle** : Stocke le cahier des charges (specs statiques)
   - **Bénéfice** : Évite la duplication dans les prompts
   - **Accès** : Requêtes sémantiques automatiques

2. **Memory (CrewAI Memory System)**
   - **Rôle** : Stocke les résultats des tâches précédentes
   - **Bénéfice** : Transmission du contexte de débat entre agents
   - **Accès** : Automatique via `memory=True` dans le Crew

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    memory=True,  # Pour le flow de travail
    # knowledge_sources assignées aux agents individuellement
)
```

## Avantages

✅ **Réduction massive des coûts** : ~90% d'économie sur les tokens de prompt
✅ **Recherche sémantique** : Les agents récupèrent uniquement les sections pertinentes
✅ **Scalabilité** : Fonctionne même avec des cahiers des charges très longs
✅ **Simplicité** : Pas de code complexe côté agent
✅ **Compatibilité** : Fonctionne avec le processus hiérarchique et la délégation

## Limitations

⚠️ **Dépendance OpenAI** : Par défaut, utilise les embeddings OpenAI (configurable)
⚠️ **Latence** : Légère latence pour les requêtes vectorielles (négligeable)
⚠️ **Storage local** : Les embeddings sont stockés localement (gérer l'espace disque)

## Configuration avancée

### Changer le provider d'embeddings

```python
from crewai import Agent, LLM

# Utiliser un autre provider
agent = Agent(
    role="...",
    llm=LLM(model="..."),
    embedder=dict(
        provider="google",  # ou "voyage", "ollama", etc.
        config=dict(model="...")
    )
)
```

### Nettoyer le cache

```bash
# Supprimer les embeddings stockés
crewai reset-memories --knowledge
```

### Changer le répertoire de stockage

```bash
export CREWAI_STORAGE_DIR=/custom/path
```

## Références

- [Documentation CrewAI Knowledge](https://docs.crewai.com/en/concepts/knowledge)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [OpenAI Embeddings Pricing](https://openai.com/pricing)

## Résumé

Cette optimisation RAG transforme le système multi-agent en une architecture **token-efficient** qui :
1. Stocke le cahier des charges UNE SEULE FOIS dans ChromaDB
2. Permet aux agents d'y accéder via recherche sémantique
3. Économise ~90% des tokens sur les prompts
4. Maintient la qualité du débat grâce à la récupération intelligente

**Résultat** : Un système plus économique, plus scalable, et tout aussi performant ! 🚀
