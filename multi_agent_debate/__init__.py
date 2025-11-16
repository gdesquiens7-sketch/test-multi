"""
Système Multi-Agent de Débat et Validation
==========================================

Un système collaboratif basé sur CrewAI où plusieurs agents IA débattent,
challengent et raffinent des solutions jusqu'à obtenir un résultat optimal
validant un cahier des charges à 100%.

Agents :
- L'Innovateur : Propose des solutions créatives
- Le Pragmatique : Challenge la faisabilité
- L'Avocat du Diable : Identifie les failles
- Le Stratège : Valide l'alignement stratégique
- Le Facilitateur : Manager qui synthétise

Usage:
    from debate_crew import MultiAgentDebateCrew

    debate_system = MultiAgentDebateCrew()
    result = debate_system.run_debate(
        cahier_des_charges="...",
        output_file="output/result.md"
    )
"""

__version__ = "1.0.0"
__author__ = "Multi-Agent Debate System"

from .debate_crew import MultiAgentDebateCrew
from .config.agents import DebateAgents
from .config.tasks import DebateTasks

__all__ = [
    'MultiAgentDebateCrew',
    'DebateAgents',
    'DebateTasks'
]
