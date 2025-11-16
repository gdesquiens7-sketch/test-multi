# SYSTÈME MULTI-AGENT DE DÉBAT ET VALIDATION

Un système collaboratif basé sur **CrewAI** où plusieurs agents IA débattent, challengent et raffinent des solutions jusqu'à obtenir un résultat optimal validant un cahier des charges à 100%.

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Les Agents](#les-agents)
4. [Le Processus de Débat](#le-processus-de-débat)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Utilisation](#utilisation)
8. [Structure du Projet](#structure-du-projet)
9. [Exemples](#exemples)
10. [Règles du Débat](#règles-du-débat)

---

## 🎯 VUE D'ENSEMBLE

Ce système implémente un **débat structuré en 6 tours** entre 5 agents IA spécialisés :

- **L'Innovateur** 🎨 : Propose des solutions créatives
- **Le Pragmatique** ⚙️ : Challenge la faisabilité technique
- **L'Avocat du Diable** 👹 : Identifie les failles et contradictions
- **Le Stratège** 📊 : Valide l'alignement business
- **Le Facilitateur** 🎯 : Manager qui orchestre et synthétise

### Pourquoi ce système ?

✅ **Qualité maximale** : Chaque solution est challengée sous tous les angles
✅ **Conformité garantie** : Validation point par point du cahier des charges
✅ **Traçabilité totale** : Tous les débats et décisions sont documentés
✅ **Consensus forcé** : Convergence obligatoire vers une solution unique
✅ **Documentation complète** : Rapport final structuré et actionnable

### Stack Technique

- **CrewAI 0.98.0** - Framework multi-agent (dernière version, janvier 2025)
- **LangChain 0.3.0** - Intégration LLM
- **Python 3.10+** - Langage (compatible jusqu'à 3.13)
- **Support multi-modèles** - DeepSeek, OpenAI, Claude, Gemini, Ollama

---

## 🏗️ ARCHITECTURE

```
CAHIER DES CHARGES (Input)
         ↓
┌────────────────────────────────────────┐
│  TOUR 1 : Propositions Initiales      │
│  Innovateur + Stratège                │
│  → 3 propositions créatives            │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│  TOUR 2 : Critique Croisée            │
│  Pragmatique + Avocat du Diable       │
│  → Identification des failles          │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│  TOUR 3 : Défense et Amélioration     │
│  Innovateur + Stratège                │
│  → Propositions V2 améliorées          │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│  TOUR 4 : Challenge Intensif          │
│  TOUS les agents (sauf Facilitateur)  │
│  → Challenge multi-perspectives        │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│  TOUR 5 : Convergence Forcée          │
│  TOUS les agents (sauf Facilitateur)  │
│  → Solution finale consensuelle        │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│  TOUR 6 : Synthèse Finale             │
│  Facilitateur (Manager)               │
│  → Document de recommandation          │
└────────────────────────────────────────┘
         ↓
DOCUMENT FINAL (Output)
```

**Process** : Hierarchical (Le Facilitateur est le manager)
**Memory** : Activée (les agents se souviennent)
**Max Iterations** : 15 (pour plusieurs rounds de débat)

---

## 👥 LES AGENTS

### 🎨 L'Innovateur (The Innovator)

**Rôle** : Proposer des solutions créatives et innovantes

**Responsabilités** :
- Analyser le cahier des charges
- Proposer des idées audacieuses mais réalistes
- Défendre les aspects innovants
- Faire des compromis si nécessaire

**Expertise** : Innovation, créativité, pensée disruptive

---

### ⚙️ Le Pragmatique (The Pragmatist)

**Rôle** : Challenger les propositions sur leur faisabilité

**Responsabilités** :
- Évaluer la viabilité technique
- Identifier les contraintes de délai et budget
- Pointer les risques opérationnels
- Proposer des solutions réalisables

**Expertise** : Gestion de projet, contraintes techniques, faisabilité

---

### 👹 L'Avocat du Diable (The Devil's Advocate)

**Rôle** : Identifier les failles et contradictions

**Responsabilités** :
- Remettre en question systématiquement
- Détecter les failles cachées
- Vérifier la conformité au cahier des charges
- Stress-tester toutes les idées

**Expertise** : Analyse critique, détection de failles, scepticisme constructif

---

### 📊 Le Stratège (The Strategist)

**Rôle** : Aligner les propositions avec les objectifs business

**Responsabilités** :
- Évaluer la valeur business
- Analyser l'impact à long terme
- Valider l'alignement stratégique
- Penser ROI et opportunités

**Expertise** : Stratégie, vision business, alignement organisationnel

---

### 🎯 Le Facilitateur (The Facilitator) - **MANAGER**

**Rôle** : Orchestrer le débat et synthétiser

**Responsabilités** :
- Gérer les interactions entre agents
- Relancer les débats si nécessaire
- Valider la conformité au cahier des charges
- Produire le document final de recommandation

**Expertise** : Médiation, synthèse, gestion de débats, validation

---

## 🔄 LE PROCESSUS DE DÉBAT

### TOUR 1 : Proposition Initiale Multi-Perspectives

**Participants** : L'Innovateur, Le Stratège
**Objectif** : Générer 3 propositions créatives

**Livrables** :
- 3 propositions détaillées
- Matrice de conformité pour chaque proposition
- Analyse des exigences critiques vs secondaires

---

### TOUR 2 : Premier Round de Critique Croisée

**Participants** : Le Pragmatique, L'Avocat du Diable
**Objectif** : Identifier les failles et contraintes

**Livrables** :
- Rapport de critique consensuel
- Liste des exigences non ou mal couvertes
- Priorisation des risques

---

### TOUR 3 : Défense et Amélioration

**Participants** : L'Innovateur, Le Stratège
**Objectif** : Améliorer les propositions suite aux critiques

**Livrables** :
- Propositions V2 améliorées
- Matrice de conformité mise à jour
- Documentation des compromis

---

### TOUR 4 : Second Round de Challenge Intensif

**Participants** : TOUS (sauf Le Facilitateur)
**Objectif** : Challenge multi-perspectives des V2

**Livrables** :
- Analyse multi-critères (Innovation, Faisabilité, Robustesse, Stratégie)
- Désaccords résiduels et convergences
- Scoring de chaque proposition

---

### TOUR 5 : Convergence Forcée

**Participants** : TOUS (sauf Le Facilitateur)
**Objectif** : Converger vers UNE solution unique

**Livrables** :
- Solution finale consensuelle
- 100% de conformité au cahier des charges
- Documentation des compromis de chaque agent

---

### TOUR 6 : Synthèse et Validation Finale

**Participant** : Le Facilitateur (Manager)
**Objectif** : Produire le document final de recommandation

**Livrables** :
- **Document de Recommandation Finale** structuré en 8 sections :
  1. Synthèse Exécutive
  2. Solution Détaillée
  3. Conformité au Cahier des Charges
  4. Traçabilité du Débat
  5. Plan d'Action
  6. Risques et Mitigations
  7. Dissensus et Alertes
  8. Conclusion et Validation Managériale

---

## 🚀 INSTALLATION

### Prérequis

- Python 3.10+
- pip

### Installation des dépendances

```bash
cd multi_agent_debate
pip install -r requirements.txt
```

---

## ⚙️ CONFIGURATION

### Variables d'environnement

Créez un fichier `.env` à la racine du projet :

```bash
# Pour DeepSeek
OPENAI_API_KEY=votre-api-key-deepseek
OPENAI_API_BASE=https://api.deepseek.com

# OU pour OpenAI
OPENAI_API_KEY=votre-api-key-openai
OPENAI_API_BASE=https://api.openai.com/v1
```

### Configuration du modèle

Dans `debate_crew.py`, vous pouvez modifier :

```python
debate_system = MultiAgentDebateCrew(
    model_name="deepseek-chat",  # ou "gpt-4", "gpt-3.5-turbo", etc.
    temperature=0.7               # 0.0 à 1.0
)
```

---

## 💻 UTILISATION

### Utilisation basique

```python
from debate_crew import MultiAgentDebateCrew
import os

# Configuration API
os.environ["OPENAI_API_KEY"] = "votre-api-key"
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"

# Votre cahier des charges
cahier_des_charges = """
CAHIER DES CHARGES : [Votre projet]

1. OBJECTIF
[Décrivez l'objectif principal]

2. EXIGENCES FONCTIONNELLES
- EF1 : ...
- EF2 : ...

3. EXIGENCES TECHNIQUES
- ET1 : ...
- ET2 : ...

4. CONTRAINTES
- C1 : Budget maximal : XXX €
- C2 : Délai : X mois

5. CRITÈRES DE SUCCÈS
- CS1 : ...
- CS2 : ...
"""

# Lancement du débat
debate_system = MultiAgentDebateCrew()
result = debate_system.run_debate(
    cahier_des_charges=cahier_des_charges,
    output_file="output/ma_recommandation.md"
)

print(result)
```

### Utilisation avancée

```python
# Personnalisation du modèle et de la température
debate_system = MultiAgentDebateCrew(
    model_name="gpt-4",
    temperature=0.5  # Plus conservateur
)

# Lancement sans sauvegarde automatique
result = debate_system.run_debate(cahier_des_charges)

# Accès aux détails du résultat
if hasattr(result, 'raw'):
    print("Résultat brut :", result.raw)
if isinstance(result, dict):
    print("Tasks outputs :", result.get('tasks_outputs'))
```

---

## 📁 STRUCTURE DU PROJET

```
multi_agent_debate/
│
├── config/
│   ├── __init__.py           # Init du package config
│   ├── agents.py             # Définition des 5 agents
│   └── tasks.py              # Définition des 6 tâches
│
├── examples/
│   ├── exemple_cahier_des_charges_1.md
│   ├── exemple_cahier_des_charges_2.md
│   └── exemple_cahier_des_charges_3.md
│
├── output/
│   └── [Fichiers de résultats générés]
│
├── debate_crew.py            # Classe principale du crew
├── requirements.txt          # Dépendances Python
└── README.md                 # Cette documentation
```

---

## 📝 EXEMPLES

### Exemple 1 : Plateforme de Formation en Ligne

```python
cahier_des_charges = """
CAHIER DES CHARGES : Plateforme de Formation en Ligne

1. OBJECTIF
Créer une plateforme de formation en ligne pour PME.

2. EXIGENCES FONCTIONNELLES
- EF1 : Gestion des utilisateurs (admin, formateur, apprenant)
- EF2 : Parcours de formation personnalisés
- EF3 : Bibliothèque multimédia (vidéos, documents, quiz)
- EF4 : Suivi de progression en temps réel
- EF5 : Certification automatique
- EF6 : Dashboard analytics
- EF7 : Forum de discussion

3. CONTRAINTES
- Budget : 150 000 €
- Délai : 6 mois
- Équipe : 3 devs, 1 designer, 1 PM
"""

result = debate_system.run_debate(
    cahier_des_charges,
    output_file="output/plateforme_formation.md"
)
```

Voir `examples/exemple_cahier_des_charges_1.md` pour un exemple complet.

### Exemple 2 : Application Mobile E-commerce

Voir `examples/exemple_cahier_des_charges_2.md`

### Exemple 3 : Système CRM pour PME

Voir `examples/exemple_cahier_des_charges_3.md`

---

## 📜 RÈGLES DU DÉBAT

1. **Référence permanente** : Chaque agent doit citer explicitement les exigences du cahier des charges

2. **Pas de monologue** : Chaque agent DOIT répondre aux arguments des autres

3. **Challenge obligatoire** : Aucune proposition ne passe sans avoir été challengée par AU MOINS 2 agents

4. **Désaccords explicites** : Les désaccords doivent être documentés et débattus jusqu'à résolution

5. **Pouvoir du Facilitateur** : Le Facilitateur peut relancer le débat s'il juge les échanges insuffisants

6. **Convergence conditionnée** : Le TOUR 5 ne peut commencer qu'après validation que toutes les exigences critiques sont adressées

7. **Consensus obligatoire** : La solution finale DOIT avoir le consensus de TOUS les agents

8. **Compromis documentés** : Chaque compromis doit être justifié par rapport au cahier des charges

9. **100% de conformité** : Toute exigence non couverte doit être explicitement justifiée

10. **Traçabilité totale** : Chaque décision doit être traçable jusqu'aux débats qui l'ont produite

---

## 🔧 PERSONNALISATION

### Modifier un agent

Éditez `config/agents.py` :

```python
@staticmethod
def innovateur(llm) -> Agent:
    return Agent(
        role="Votre nouveau rôle",
        goal="Votre nouvel objectif",
        backstory="Votre nouvelle histoire",
        verbose=True,
        allow_delegation=True,
        llm=llm
    )
```

### Ajouter une tâche

Éditez `config/tasks.py` et ajoutez votre tâche :

```python
@staticmethod
def ma_nouvelle_task(agent, context_task, cahier_des_charges: str) -> Task:
    return Task(
        description=f"""
        {cahier_des_charges}

        [Vos instructions]
        """,
        expected_output="[Format attendu]",
        agent=agent,
        context=[context_task],
        async_execution=False
    )
```

Puis intégrez-la dans `debate_crew.py`.

---

## 🐛 DÉPANNAGE

### Erreur d'API

```
OpenAI API error: Unauthorized
```

**Solution** : Vérifiez vos variables d'environnement `OPENAI_API_KEY` et `OPENAI_API_BASE`.

### Erreur de mémoire

```
Out of memory error
```

**Solution** : Réduisez `max_iter` dans `debate_crew.py` ou utilisez un modèle plus léger.

### Débat qui boucle

**Solution** : Augmentez la `temperature` pour plus de variété dans les réponses.

---

## 📊 PERFORMANCE

**Temps d'exécution moyen** : 15-30 minutes (selon le modèle et la complexité du cahier des charges)

**Coût estimé** (avec DeepSeek) : ~0.50€ par débat complet

**Coût estimé** (avec GPT-4) : ~5-10€ par débat complet

---

## 🤝 CONTRIBUTION

Les contributions sont les bienvenues ! N'hésitez pas à :

- Ouvrir des issues pour des bugs ou suggestions
- Proposer des améliorations via Pull Requests
- Partager vos exemples de cahiers des charges

---

## 📄 LICENCE

MIT License - Libre d'utilisation et de modification

---

## 📞 SUPPORT

Pour toute question ou problème :

- Ouvrez une issue sur le dépôt
- Consultez la documentation CrewAI : https://docs.crewai.com

---

## 🙏 REMERCIEMENTS

- **CrewAI** : Framework multi-agent
- **LangChain** : Intégration LLM
- **OpenAI / DeepSeek** : Modèles de langage

---

**Bon débat ! 🚀**
