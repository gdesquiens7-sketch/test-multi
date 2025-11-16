#!/usr/bin/env python3
"""
Script de test pour vérifier la connexion à DeepSeek
"""
import os
from dotenv import load_dotenv
import requests

# Charger les variables d'environnement
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE")

print("="*80)
print("TEST DE CONNEXION DEEPSEEK")
print("="*80)

print(f"\n📋 Configuration :")
print(f"  API Key : {api_key[:10]}...{api_key[-4:]}" if api_key else "  API Key : NON DÉFINIE")
print(f"  Base URL : {base_url}")

if not api_key:
    print("\n❌ ERREUR : OPENAI_API_KEY non définie dans .env")
    exit(1)

if not base_url:
    print("\n❌ ERREUR : OPENAI_API_BASE non définie dans .env")
    exit(1)

# Test 1 : Requête HTTP directe
print("\n" + "="*80)
print("TEST 1 : Requête HTTP directe à DeepSeek")
print("="*80)

try:
    # Construire l'URL complète
    # DeepSeek utilise le même format d'API qu'OpenAI
    url = f"{base_url}/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "Dis juste 'bonjour'"}
        ],
        "max_tokens": 10
    }

    print(f"\n🌐 Envoi de la requête à : {url}")
    response = requests.post(url, headers=headers, json=data, timeout=30)

    print(f"📊 Code HTTP : {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        message = result['choices'][0]['message']['content']
        print(f"✅ SUCCÈS !")
        print(f"📝 Réponse : {message}")
        print("\n✅ Votre clé API DeepSeek fonctionne correctement !")
    elif response.status_code == 401:
        print("❌ ERREUR 401 : Clé API invalide ou expirée")
        print(f"📋 Réponse : {response.text}")
        print("\n🔧 Actions à faire :")
        print("  1. Vérifiez votre clé sur https://platform.deepseek.com/")
        print("  2. Créez une nouvelle clé si nécessaire")
        print("  3. Vérifiez que vous avez du crédit")
    else:
        print(f"❌ ERREUR {response.status_code}")
        print(f"📋 Réponse : {response.text}")

except requests.exceptions.Timeout:
    print("❌ ERREUR : Timeout de connexion")
    print("Vérifiez votre connexion Internet")
except requests.exceptions.ConnectionError:
    print("❌ ERREUR : Impossible de se connecter à DeepSeek")
    print(f"URL testée : {url}")
    print("Vérifiez votre connexion Internet et que l'URL est correcte")
except Exception as e:
    print(f"❌ ERREUR : {e}")

# Test 2 : Via LangChain
print("\n" + "="*80)
print("TEST 2 : Via LangChain ChatOpenAI")
print("="*80)

try:
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model="deepseek-chat",
        temperature=0.7,
        base_url=base_url,
        api_key=api_key,
        max_tokens=10
    )

    print("\n🔧 Configuration LangChain :")
    print(f"  Model : deepseek-chat")
    print(f"  Base URL : {base_url}")
    print(f"  API Key : {api_key[:10]}...{api_key[-4:]}")

    print("\n📨 Envoi d'un message de test...")
    response = llm.invoke("Dis juste 'bonjour'")

    print(f"✅ SUCCÈS !")
    print(f"📝 Réponse : {response.content}")
    print("\n✅ LangChain fonctionne correctement avec DeepSeek !")

except Exception as e:
    print(f"❌ ERREUR : {e}")
    print("\n🔧 Cela peut indiquer un problème avec la configuration LangChain")

print("\n" + "="*80)
print("FIN DES TESTS")
print("="*80)
