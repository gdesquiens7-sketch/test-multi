# QUICKSTART - Démarrage Rapide

Guide pour lancer votre premier débat multi-agent en 5 minutes.

---

## ⚡ Installation en 3 étapes

### 1. Installer les dépendances

```bash
cd multi_agent_debate
pip install -r requirements.txt
```

### 2. Configurer votre clé API

```bash
# Copier le fichier d'exemple
cp .env.example .env

# Éditer le fichier .env et ajouter votre clé API
nano .env  # ou code .env, vim .env, etc.
```

Dans le fichier `.env`, décommentez et remplissez :

```bash
# Pour DeepSeek (moins cher)
OPENAI_API_KEY=sk-votre-cle-deepseek
OPENAI_API_BASE=https://api.deepseek.com

# OU pour OpenAI
# OPENAI_API_KEY=sk-votre-cle-openai
# OPENAI_API_BASE=https://api.openai.com/v1
```

**Où obtenir une clé API ?**

- **DeepSeek** : https://platform.deepseek.com/ (moins cher, performant)
- **OpenAI** : https://platform.openai.com/api-keys (GPT-4, GPT-3.5)

### 3. Lancer l'exemple

```bash
python example.py
```

Le système va :
1. Analyser le cahier des charges d'exemple
2. Lancer un débat entre les 5 agents (15-30 minutes)
3. Générer un document de recommandation dans `output/exemple_resultat.md`

---

## 📝 Utilisation Basique

### Dans votre propre script

```python
from debate_crew import MultiAgentDebateCrew
import os

# Configuration
os.environ["OPENAI_API_KEY"] = "votre-cle"
os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"

# Votre cahier des charges
cahier_des_charges = """
CAHIER DES CHARGES : [Votre projet]

1. OBJECTIF
[Décrivez votre objectif]

2. EXIGENCES FONCTIONNELLES
- EF1 : ...
- EF2 : ...

3. CONTRAINTES
- C1 : Budget : XXX €
- C2 : Délai : X mois
"""

# Lancer le débat
debate_system = MultiAgentDebateCrew()
result = debate_system.run_debate(
    cahier_des_charges,
    output_file="output/mon_resultat.md"
)
```

---

## 🎯 Exemples de Cahiers des Charges

Trois exemples complets sont fournis dans `examples/` :

1. **Plateforme de Formation en Ligne** (`exemple_cahier_des_charges_1.md`)
   - Complexe, budget 150k€, 6 mois

2. **Application Mobile E-commerce** (`exemple_cahier_des_charges_2.md`)
   - Moyen, budget 80k€, 4 mois

3. **CRM pour PME** (`exemple_cahier_des_charges_3.md`)
   - Simple, budget 60k€, 3 mois

Pour les tester :

```python
# Lire un exemple
with open("examples/exemple_cahier_des_charges_1.md", "r") as f:
    cahier = f.read()

# Lancer le débat
debate_system = MultiAgentDebateCrew()
result = debate_system.run_debate(
    cahier,
    output_file="output/plateforme_formation.md"
)
```

---

## ⚙️ Configuration Avancée

### Changer de modèle

```python
debate_system = MultiAgentDebateCrew(
    model_name="gpt-4",           # ou "gpt-3.5-turbo", "deepseek-chat"
    temperature=0.5               # 0.0 = déterministe, 1.0 = créatif
)
```

### Modèles recommandés

| Modèle | Coût | Performance | Recommandation |
|--------|------|-------------|----------------|
| `deepseek-chat` | 💰 | ⭐⭐⭐⭐ | **Best value** |
| `gpt-3.5-turbo` | 💰💰 | ⭐⭐⭐ | Bon rapport qualité/prix |
| `gpt-4` | 💰💰💰💰 | ⭐⭐⭐⭐⭐ | Maximum qualité |

---

## 🐛 Problèmes Courants

### ❌ Erreur : "OPENAI_API_KEY non définie"

**Solution** : Créez le fichier `.env` et ajoutez votre clé API.

```bash
cp .env.example .env
nano .env
```

### ❌ Erreur : "Unauthorized" ou "Invalid API key"

**Solution** : Vérifiez que votre clé API est correcte et active.

### ❌ Erreur : "Module 'crewai' not found"

**Solution** : Installez les dépendances.

```bash
pip install -r requirements.txt
```

### ❌ Le débat est trop long (> 30 min)

**Solutions** :
- Utilisez un modèle plus rapide (deepseek-chat au lieu de gpt-4)
- Simplifiez votre cahier des charges
- Réduisez `max_iter` dans `debate_crew.py` (ligne 126)

### ❌ Erreur de mémoire / timeout

**Solutions** :
- Réduisez `max_iter` à 10 (au lieu de 15)
- Utilisez un modèle plus léger
- Simplifiez le cahier des charges

---

## 📊 Comprendre le Résultat

Le document final généré dans `output/` contient :

1. **Synthèse Exécutive** (1 page)
   - Solution retenue en quelques phrases
   - Bénéfices clés
   - Prochaines étapes

2. **Solution Détaillée**
   - Description complète
   - Architecture / Approche
   - Ressources et budget
   - Timeline

3. **Conformité au Cahier des Charges**
   - Tableau exigence par exigence
   - Taux de conformité (objectif : 100%)

4. **Traçabilité du Débat**
   - Évolution des propositions
   - Principaux débats
   - Compromis effectués

5. **Plan d'Action**
   - Phases de mise en œuvre
   - Quick wins
   - Jalons

6. **Risques et Mitigations**
   - Liste des risques
   - Plans de mitigation

7. **Dissensus et Alertes**
   - Points de désaccord non résolus
   - Zones de vigilance

---

## 🚀 Prochaines Étapes

### Pour aller plus loin :

1. **Personnalisez les agents** : Éditez `config/agents.py`
2. **Modifiez les tâches** : Éditez `config/tasks.py`
3. **Ajustez le processus** : Éditez `debate_crew.py`

### Documentation complète :

Consultez le `README.md` pour :
- Architecture détaillée
- Description complète des agents
- Processus de débat en 6 tours
- Règles du débat
- Personnalisation avancée

---

## 💡 Conseils pour un Bon Cahier des Charges

Pour obtenir les meilleurs résultats :

✅ **Structurez clairement** : Objectif, Exigences, Contraintes, Critères de succès
✅ **Soyez précis** : Quantifiez (budget, délais, performances attendues)
✅ **Priorisez** : Distinguez exigences critiques / importantes / secondaires
✅ **Incluez les contraintes** : Budget, délais, équipe, technique
✅ **Définissez le succès** : Critères mesurables (KPI)

❌ **Évitez** :
- Cahiers des charges trop vagues
- Listes d'exigences sans priorité
- Oubli des contraintes réelles (budget, délais)

---

## 📞 Support

- **Issues GitHub** : Pour bugs et suggestions
- **Documentation** : `README.md` pour guide complet
- **Exemples** : `examples/` pour des cas d'usage réels

---

**Bon débat ! 🎉**
