# 🌐 Guide de Configuration OpenRouter

**OpenRouter** est un agrégateur d'API qui vous donne accès à **tous les LLM** (DeepSeek, GPT-4, Claude, Llama, Gemini, etc.) avec une seule clé API.

## ✨ Avantages d'OpenRouter

✅ **Une seule clé API** pour tous les modèles
✅ **Basculer facilement** entre les modèles (changez juste MODEL_NAME)
✅ **Prix compétitifs** (souvent moins cher que direct)
✅ **Pas de quota complexe** par modèle
✅ **Fallback automatique** si un modèle est down
✅ **Tableau de bord unifié** pour suivre votre usage

---

## 🚀 Configuration en 3 étapes

### Étape 1 : Créer un compte OpenRouter

1. Allez sur **https://openrouter.ai/**
2. Cliquez sur **"Sign In"** en haut à droite
3. Connectez-vous avec Google, GitHub ou email
4. C'est **gratuit** pour commencer !

### Étape 2 : Obtenir votre clé API

1. Une fois connecté, allez sur **https://openrouter.ai/keys**
2. Cliquez sur **"Create Key"**
3. Donnez un nom à votre clé (ex: "Multi-Agent Debate")
4. **Copiez la clé** (format: `sk-or-v1-...`)
5. ⚠️ **Sauvegardez-la immédiatement** (vous ne pourrez plus la revoir)

### Étape 3 : Configurer votre `.env`

Éditez votre fichier `.env` :

```bash
# Configuration OpenRouter
OPENAI_API_KEY=sk-or-v1-VOTRE-CLE-ICI
OPENAI_API_BASE=https://openrouter.ai/api/v1

# Modèle à utiliser
MODEL_NAME=deepseek/deepseek-chat

# Température
TEMPERATURE=0.7
```

**Important** : Utilisez le format `provider/model-name` pour OpenRouter.

---

## 🎯 Modèles recommandés

### Pour débuter (gratuit ou très peu cher)

| Modèle | Prix (par 1M tokens) | Qualité | Usage recommandé |
|--------|---------------------|---------|------------------|
| `deepseek/deepseek-chat` | $0.14 / $0.28 | ⭐⭐⭐⭐ | **Meilleur rapport qualité/prix** |
| `meta-llama/llama-3.1-8b-instruct` | Gratuit | ⭐⭐⭐ | Tests et prototypage |
| `google/gemini-flash-1.5` | Gratuit | ⭐⭐⭐⭐ | Bonne alternative gratuite |

### Pour la qualité maximale

| Modèle | Prix (par 1M tokens) | Qualité | Usage recommandé |
|--------|---------------------|---------|------------------|
| `anthropic/claude-3.5-sonnet` | $3 / $15 | ⭐⭐⭐⭐⭐ | **Meilleure qualité** (cher) |
| `openai/gpt-4-turbo` | $10 / $30 | ⭐⭐⭐⭐⭐ | Qualité OpenAI |
| `openai/gpt-4o` | $2.50 / $10 | ⭐⭐⭐⭐ | Bon compromis |

### Modèles open-source puissants

| Modèle | Prix (par 1M tokens) | Qualité | Usage recommandé |
|--------|---------------------|---------|------------------|
| `meta-llama/llama-3.1-70b-instruct` | $0.59 / $0.79 | ⭐⭐⭐⭐ | Excellent rapport qualité/prix |
| `mistralai/mixtral-8x7b-instruct` | $0.24 / $0.24 | ⭐⭐⭐ | Rapide et pas cher |

**Liste complète** : https://openrouter.ai/models

---

## 💡 Exemples de configuration

### Configuration 1 : DeepSeek (recommandé, pas cher)

```bash
OPENAI_API_KEY=sk-or-v1-votre-cle
OPENAI_API_BASE=https://openrouter.ai/api/v1
MODEL_NAME=deepseek/deepseek-chat
TEMPERATURE=0.7
```

**Coût estimé pour un débat complet** : ~$0.05-0.10

### Configuration 2 : Claude 3.5 Sonnet (meilleure qualité)

```bash
OPENAI_API_KEY=sk-or-v1-votre-cle
OPENAI_API_BASE=https://openrouter.ai/api/v1
MODEL_NAME=anthropic/claude-3.5-sonnet
TEMPERATURE=0.7
```

**Coût estimé pour un débat complet** : ~$0.50-1.00

### Configuration 3 : Llama 3.1 70B (open-source puissant)

```bash
OPENAI_API_KEY=sk-or-v1-votre-cle
OPENAI_API_BASE=https://openrouter.ai/api/v1
MODEL_NAME=meta-llama/llama-3.1-70b-instruct
TEMPERATURE=0.7
```

**Coût estimé pour un débat complet** : ~$0.10-0.20

### Configuration 4 : Gratuit (Gemini Flash)

```bash
OPENAI_API_KEY=sk-or-v1-votre-cle
OPENAI_API_BASE=https://openrouter.ai/api/v1
MODEL_NAME=google/gemini-flash-1.5
TEMPERATURE=0.7
```

**Coût** : Gratuit !

---

## 🔍 Tester votre configuration

### Test rapide

```bash
cd /home/user/test-multi/multi_agent_debate
python3 test_deepseek.py
```

Ce script fonctionne aussi avec OpenRouter ! Il testera votre connexion.

### Test complet

```bash
python3 -B example.py
```

Lance un débat complet avec votre configuration.

---

## 💰 Gestion du budget

### Ajouter du crédit

1. Allez sur **https://openrouter.ai/credits**
2. Cliquez sur **"Add Credits"**
3. Montant minimum : **$5**
4. Modes de paiement : Carte bancaire, crypto

### Suivre votre consommation

- Dashboard : **https://openrouter.ai/activity**
- Voir l'usage par modèle
- Graphiques de consommation
- Alertes de budget

### Définir un budget limite

1. Allez sur **https://openrouter.ai/settings**
2. Section **"Limits"**
3. Définissez un **budget mensuel maximum**
4. OpenRouter s'arrêtera automatiquement si dépassé

---

## 🛡️ Sécurité

### Bonnes pratiques

✅ **Ne partagez JAMAIS votre clé API**
✅ Utilisez des **variables d'environnement** (.env)
✅ Ajoutez `.env` à votre `.gitignore`
✅ Créez des **clés différentes** par projet
✅ **Révoquez** les clés inutilisées

### Révoquer une clé

1. Allez sur **https://openrouter.ai/keys**
2. Cliquez sur la **poubelle** à côté de la clé
3. Confirmez la révocation
4. La clé est immédiatement invalidée

---

## 🔄 Basculer entre les modèles

C'est **très simple** avec OpenRouter ! Changez juste le `MODEL_NAME` dans `.env` :

```bash
# Essayer DeepSeek
MODEL_NAME=deepseek/deepseek-chat

# Essayer Claude
MODEL_NAME=anthropic/claude-3.5-sonnet

# Essayer GPT-4
MODEL_NAME=openai/gpt-4-turbo

# Essayer Llama
MODEL_NAME=meta-llama/llama-3.1-70b-instruct
```

Relancez votre script, c'est tout ! 🚀

---

## 🐛 Dépannage

### Erreur : "Insufficient credits"

**Solution** : Ajoutez du crédit sur https://openrouter.ai/credits

### Erreur : "Invalid API key"

**Solutions** :
1. Vérifiez que la clé commence par `sk-or-v1-`
2. Vérifiez qu'elle est bien copiée dans `.env`
3. Essayez de créer une nouvelle clé

### Erreur : "Model not found"

**Solution** : Vérifiez le nom du modèle sur https://openrouter.ai/models
- Format OpenRouter : `provider/model-name`
- Exemple : `deepseek/deepseek-chat` (pas juste `deepseek-chat`)

### Le modèle est lent

**Solutions** :
- Certains modèles sont plus lents (GPT-4, Claude)
- Essayez un modèle plus rapide : `deepseek/deepseek-chat`, `google/gemini-flash-1.5`
- Vérifiez le statut : https://openrouter.ai/status

---

## 📊 Comparaison des coûts

Pour un **débat complet** (environ 50k-100k tokens) :

| Modèle | Coût estimé | Qualité | Vitesse |
|--------|-------------|---------|---------|
| Gemini Flash (gratuit) | $0.00 | ⭐⭐⭐⭐ | ⚡⚡⚡ |
| DeepSeek Chat | $0.05-0.10 | ⭐⭐⭐⭐ | ⚡⚡⚡ |
| Llama 3.1 70B | $0.10-0.20 | ⭐⭐⭐⭐ | ⚡⚡ |
| GPT-4 Turbo | $0.50-1.00 | ⭐⭐⭐⭐⭐ | ⚡⚡ |
| Claude 3.5 Sonnet | $0.50-1.00 | ⭐⭐⭐⭐⭐ | ⚡⚡ |

---

## 🎓 Ressources

- **Site officiel** : https://openrouter.ai/
- **Documentation** : https://openrouter.ai/docs
- **Modèles disponibles** : https://openrouter.ai/models
- **Pricing** : https://openrouter.ai/models (prix par modèle)
- **Discord** : https://discord.gg/openrouter
- **Status** : https://openrouter.ai/status

---

## ✅ Checklist de configuration

- [ ] Compte OpenRouter créé
- [ ] Clé API générée (`sk-or-v1-...`)
- [ ] Fichier `.env` créé (copie de `.env.example`)
- [ ] `OPENAI_API_KEY` rempli avec votre clé OpenRouter
- [ ] `OPENAI_API_BASE` = `https://openrouter.ai/api/v1`
- [ ] `MODEL_NAME` choisi (ex: `deepseek/deepseek-chat`)
- [ ] Crédit ajouté (minimum $5)
- [ ] Test effectué avec `python3 test_deepseek.py`
- [ ] Débat lancé avec `python3 example.py`

---

**Vous êtes prêt à débattre ! 🎉**
