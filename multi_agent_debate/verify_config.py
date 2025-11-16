#!/usr/bin/env python3
"""
Script de vérification de configuration pour OpenRouter
"""
import os
from dotenv import load_dotenv

# Charger .env
load_dotenv()

print("="*80)
print("VÉRIFICATION DE CONFIGURATION OPENROUTER")
print("="*80)

# Récupérer les variables
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE")
model_name = os.getenv("MODEL_NAME", "deepseek-chat")

print("\n📋 Configuration détectée :")
print(f"  OPENAI_API_KEY : {api_key[:15]}...{api_key[-4:] if api_key else 'NON DÉFINIE'}")
print(f"  OPENAI_API_BASE : {base_url if base_url else 'NON DÉFINIE'}")
print(f"  MODEL_NAME : {model_name}")

# Vérifications
errors = []
warnings = []

# Vérifier la clé API
if not api_key:
    errors.append("❌ OPENAI_API_KEY n'est pas définie dans .env")
elif api_key.startswith("sk-or-v1-"):
    print("\n✅ Clé OpenRouter détectée (format correct)")
elif api_key.startswith("sk-"):
    warnings.append("⚠️  La clé semble être pour DeepSeek/OpenAI direct, pas OpenRouter")
    warnings.append("    Pour OpenRouter, la clé doit commencer par 'sk-or-v1-'")
else:
    errors.append("❌ Format de clé API invalide")

# Vérifier la base URL
if not base_url:
    errors.append("❌ OPENAI_API_BASE n'est pas définie dans .env")
elif base_url == "https://openrouter.ai/api/v1":
    print("✅ Base URL OpenRouter correcte")
elif "openrouter" in base_url.lower():
    warnings.append(f"⚠️  Base URL OpenRouter non standard : {base_url}")
    warnings.append("    URL recommandée : https://openrouter.ai/api/v1")
elif "deepseek" in base_url.lower():
    errors.append("❌ Base URL pointe vers DeepSeek direct, pas OpenRouter")
    errors.append("    Changez pour : https://openrouter.ai/api/v1")
elif "openai" in base_url.lower():
    errors.append("❌ Base URL pointe vers OpenAI direct, pas OpenRouter")
    errors.append("    Changez pour : https://openrouter.ai/api/v1")
else:
    warnings.append(f"⚠️  Base URL non reconnue : {base_url}")

# Vérifier le nom du modèle
if "/" in model_name:
    print(f"✅ Format de modèle OpenRouter détecté : {model_name}")
    if model_name.startswith("deepseek/"):
        print("   → Utilisera DeepSeek via OpenRouter")
    elif model_name.startswith("anthropic/"):
        print("   → Utilisera Claude via OpenRouter")
    elif model_name.startswith("openai/"):
        print("   → Utilisera GPT via OpenRouter")
    elif model_name.startswith("google/"):
        print("   → Utilisera Gemini via OpenRouter")
else:
    warnings.append(f"⚠️  Nom de modèle sans '/' : {model_name}")
    warnings.append("    Format OpenRouter : provider/model-name")
    warnings.append("    Exemple : deepseek/deepseek-chat")

# Afficher les avertissements
if warnings:
    print("\n⚠️  AVERTISSEMENTS :")
    for warning in warnings:
        print(f"  {warning}")

# Afficher les erreurs
if errors:
    print("\n❌ ERREURS :")
    for error in errors:
        print(f"  {error}")

    print("\n🔧 ACTIONS REQUISES :")
    print("  1. Créez un compte sur https://openrouter.ai/")
    print("  2. Générez une clé API sur https://openrouter.ai/keys")
    print("  3. Modifiez votre fichier .env :")
    print("")
    print("     OPENAI_API_KEY=sk-or-v1-votre-cle-openrouter")
    print("     OPENAI_API_BASE=https://openrouter.ai/api/v1")
    print("     MODEL_NAME=deepseek/deepseek-chat")
    print("")
    print("  4. Ajoutez du crédit sur https://openrouter.ai/credits")
    print("")
else:
    print("\n✅ CONFIGURATION CORRECTE !")
    print("\n🧪 Test de connexion...")

    try:
        import requests

        url = f"{base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/test-multi-agent",
            "X-Title": "Multi-Agent Debate System"
        }
        data = {
            "model": model_name,
            "messages": [{"role": "user", "content": "Dis juste 'bonjour'"}],
            "max_tokens": 10
        }

        print(f"  Envoi requête à : {url}")
        print(f"  Modèle : {model_name}")

        response = requests.post(url, headers=headers, json=data, timeout=30)

        if response.status_code == 200:
            result = response.json()
            message = result['choices'][0]['message']['content']
            print(f"\n🎉 SUCCÈS !")
            print(f"  Réponse du modèle : {message}")
            print("\n✅ Votre configuration OpenRouter fonctionne parfaitement !")
            print("   Vous pouvez maintenant lancer : python example.py")
        elif response.status_code == 401:
            print(f"\n❌ Erreur 401 : Authentification échouée")
            print(f"   Vérifiez votre clé API sur https://openrouter.ai/keys")
        elif response.status_code == 402:
            print(f"\n❌ Erreur 402 : Crédit insuffisant")
            print(f"   Ajoutez du crédit sur https://openrouter.ai/credits")
        elif response.status_code == 404:
            print(f"\n❌ Erreur 404 : Modèle non trouvé")
            print(f"   Modèle demandé : {model_name}")
            print(f"   Vérifiez le nom sur https://openrouter.ai/models")
        else:
            print(f"\n❌ Erreur {response.status_code}")
            print(f"   Réponse : {response.text}")

    except Exception as e:
        print(f"\n❌ Erreur lors du test : {e}")

print("\n" + "="*80)
