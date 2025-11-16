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
api_key = os.getenv("OPENROUTER_API_KEY")
model_name = os.getenv("MODEL_NAME", "openrouter/deepseek/deepseek-chat")

print("\n📋 Configuration détectée :")
if api_key:
    print(f"  OPENROUTER_API_KEY : {api_key[:15]}...{api_key[-4:]}")
else:
    print(f"  OPENROUTER_API_KEY : NON DÉFINIE")
print(f"  MODEL_NAME : {model_name}")

# Vérifications
errors = []
warnings = []

# Vérifier la clé API
if not api_key:
    errors.append("❌ OPENROUTER_API_KEY n'est pas définie dans .env")
elif api_key.startswith("sk-or-v1-"):
    print("\n✅ Clé OpenRouter détectée (format correct)")
elif api_key.startswith("sk-"):
    errors.append("❌ La clé ne semble pas être pour OpenRouter")
    errors.append("    Pour OpenRouter, la clé doit commencer par 'sk-or-v1-'")
else:
    errors.append("❌ Format de clé API invalide")

# Vérifier le nom du modèle
if model_name.startswith("openrouter/"):
    print(f"✅ Format de modèle OpenRouter détecté : {model_name}")
    if "deepseek" in model_name:
        print("   → Utilisera DeepSeek via OpenRouter")
    elif "claude" in model_name or "anthropic" in model_name:
        print("   → Utilisera Claude via OpenRouter")
    elif "gpt" in model_name or "openai" in model_name:
        print("   → Utilisera GPT via OpenRouter")
    elif "gemini" in model_name or "google" in model_name:
        print("   → Utilisera Gemini via OpenRouter")
    elif "llama" in model_name or "meta" in model_name:
        print("   → Utilisera Llama via OpenRouter")
else:
    warnings.append(f"⚠️  Nom de modèle incorrect : {model_name}")
    warnings.append("    Format OpenRouter : openrouter/provider/model-name")
    warnings.append("    Exemple : openrouter/deepseek/deepseek-chat")

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
    print("     OPENROUTER_API_KEY=sk-or-v1-votre-cle-openrouter")
    print("     MODEL_NAME=openrouter/deepseek/deepseek-chat")
    print("     TEMPERATURE=0.7")
    print("")
    print("  4. Ajoutez du crédit sur https://openrouter.ai/credits")
    print("")
else:
    print("\n✅ CONFIGURATION CORRECTE !")
    print("\n🧪 Test de connexion...")

    try:
        import requests

        url = "https://openrouter.ai/api/v1/chat/completions"
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
