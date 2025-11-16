#!/bin/bash
# Script de nettoyage complet pour résoudre le problème verbose

echo "🧹 Nettoyage complet du cache Python..."

# 1. Supprimer tous les caches Python
find /home/user/test-multi/multi_agent_debate -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find /home/user/test-multi/multi_agent_debate -name "*.pyc" -delete 2>/dev/null

# 2. Supprimer les éventuels .pyo
find /home/user/test-multi/multi_agent_debate -name "*.pyo" -delete 2>/dev/null

echo "✅ Cache nettoyé"

echo ""
echo "📝 Vérification du paramètre verbose dans le code..."
echo ""

# 3. Vérifier que verbose=True dans tous les fichiers
if grep -q "verbose=2" /home/user/test-multi/multi_agent_debate/debate_crew.py; then
    echo "❌ PROBLÈME TROUVÉ : verbose=2 encore présent dans debate_crew.py"
    echo "Fichiers à vérifier :"
    grep -n "verbose.*2" /home/user/test-multi/multi_agent_debate/*.py
else
    echo "✅ debate_crew.py : verbose=True (correct)"
fi

if grep -rq "verbose=2" /home/user/test-multi/multi_agent_debate/config/; then
    echo "❌ PROBLÈME TROUVÉ : verbose=2 dans config/"
    grep -rn "verbose.*2" /home/user/test-multi/multi_agent_debate/config/
else
    echo "✅ config/ : Pas de verbose=2"
fi

echo ""
echo "🔍 Fichiers Python dans le répertoire :"
find /home/user/test-multi/multi_agent_debate -name "*.py" -type f | grep -v __pycache__

echo ""
echo "✅ Nettoyage terminé !"
echo ""
echo "📋 Prochaines étapes :"
echo "  1. Fermer toute session Python/IPython active"
echo "  2. cd /home/user/test-multi/multi_agent_debate"
echo "  3. python3 example.py"
