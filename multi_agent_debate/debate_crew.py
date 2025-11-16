"""
Système Multi-Agent de Débat et Validation
===========================================

Ce module orchestre un débat structuré entre plusieurs agents IA pour converger
vers une solution optimale validant un cahier des charges.

Agents :
- L'Innovateur : Propose des solutions créatives
- Le Pragmatique : Challenge la faisabilité
- L'Avocat du Diable : Identifie les failles
- Le Stratège : Valide l'alignement stratégique
- Le Facilitateur : Manager qui synthétise (MANAGER)

Process : Hierarchical (Le Facilitateur est le manager)
"""

from crewai import Crew, Process, LLM
from config.agents import DebateAgents
from config.tasks import DebateTasks
import os
from typing import Union


class MultiAgentDebateCrew:
    """Classe principale pour orchestrer le système de débat multi-agent."""

    def __init__(self, model_name: str = "openrouter/deepseek/deepseek-chat", temperature: float = 0.7):
        """
        Initialise le crew de débat multi-agent.

        Args:
            model_name: Le nom du modèle à utiliser (default: openrouter/deepseek/deepseek-chat)
                       Pour OpenRouter: "openrouter/deepseek/deepseek-chat" (recommandé)
                       Pour DeepSeek direct: "deepseek/deepseek-chat"
                       Pour OpenAI: "gpt-4", "gpt-3.5-turbo"
            temperature: La température pour la génération (default: 0.7)
        """
        # Configuration du LLM via CrewAI LLM (utilise LiteLLM en interne)
        # LiteLLM lit automatiquement OPENROUTER_API_KEY depuis les variables d'environnement
        self.llm = LLM(
            model=model_name,
            temperature=temperature
        )

        # Initialisation des agents
        self.innovateur = DebateAgents.innovateur(self.llm)
        self.pragmatique = DebateAgents.pragmatique(self.llm)
        self.avocat_du_diable = DebateAgents.avocat_du_diable(self.llm)
        self.stratege = DebateAgents.stratege(self.llm)
        self.facilitateur = DebateAgents.facilitateur(self.llm)

    def create_crew(self, cahier_des_charges: str) -> Crew:
        """
        Crée le crew avec toutes les tâches de débat.

        Args:
            cahier_des_charges: Le cahier des charges complet

        Returns:
            Crew: Le crew configuré avec toutes les tâches
        """
        # TOUR 1 : Proposition Initiale Multi-Perspectives
        task1_multi_perspective = DebateTasks.multi_perspective_proposal(
            innovateur=self.innovateur,
            stratege=self.stratege,
            cahier_des_charges=cahier_des_charges
        )

        # TOUR 2 : Premier Round de Critique Croisée
        task2_first_critique = DebateTasks.first_critique_round(
            pragmatique=self.pragmatique,
            avocat_du_diable=self.avocat_du_diable,
            multi_perspective_proposal_task=task1_multi_perspective,
            cahier_des_charges=cahier_des_charges
        )

        # TOUR 3 : Défense et Amélioration
        task3_defense = DebateTasks.defense_and_improvement(
            innovateur=self.innovateur,
            stratege=self.stratege,
            first_critique_round_task=task2_first_critique,
            cahier_des_charges=cahier_des_charges
        )

        # TOUR 4 : Second Round de Challenge Intensif
        task4_challenge = DebateTasks.intensive_challenge(
            pragmatique=self.pragmatique,
            defense_and_improvement_task=task3_defense,
            cahier_des_charges=cahier_des_charges
        )

        # TOUR 5 : Convergence Forcée
        task5_convergence = DebateTasks.forced_convergence(
            innovateur=self.innovateur,
            intensive_challenge_task=task4_challenge,
            cahier_des_charges=cahier_des_charges
        )

        # TOUR 6 : Synthèse et Validation Finale
        task6_synthesis = DebateTasks.final_synthesis(
            facilitateur=self.facilitateur,
            all_previous_tasks=[
                task1_multi_perspective,
                task2_first_critique,
                task3_defense,
                task4_challenge,
                task5_convergence
            ],
            cahier_des_charges=cahier_des_charges
        )

        # Création du Crew avec processus hiérarchique
        # Note: Le manager_agent ne doit PAS être dans la liste agents (CrewAI 0.98.0)
        crew = Crew(
            agents=[
                self.innovateur,
                self.pragmatique,
                self.avocat_du_diable,
                self.stratege
                # self.facilitateur est le manager, donc EXCLU de la liste
            ],
            tasks=[
                task1_multi_perspective,
                task2_first_critique,
                task3_defense,
                task4_challenge,
                task5_convergence,
                task6_synthesis
            ],
            process=Process.hierarchical,
            manager_agent=self.facilitateur,  # Le Facilitateur gère les autres agents
            verbose=True,
            memory=True  # Système de mémoire RAG avec ChromaDB
        )

        return crew

    def run_debate(self, cahier_des_charges: str, output_file: str = None):
        """
        Lance le débat multi-agent complet.

        Args:
            cahier_des_charges: Le cahier des charges à analyser
            output_file: Fichier optionnel pour sauvegarder le résultat

        Returns:
            CrewOutput: L'objet de résultat complet du débat (CrewAI >= 0.41.0)
        """
        print("\n" + "="*80)
        print("SYSTÈME MULTI-AGENT DE DÉBAT ET VALIDATION")
        print("="*80)
        print("\n🚀 Lancement du débat entre les 5 agents...")
        print("\nAgents participants :")
        print("  - 🎨 L'Innovateur")
        print("  - ⚙️  Le Pragmatique")
        print("  - 👹 L'Avocat du Diable")
        print("  - 📊 Le Stratège")
        print("  - 🎯 Le Facilitateur (Manager)")
        print("\n" + "="*80 + "\n")

        # Création et lancement du crew
        crew = self.create_crew(cahier_des_charges)

        result = crew.kickoff(inputs={
            'cahier_des_charges': cahier_des_charges
        })

        print("\n" + "="*80)
        print("✅ DÉBAT TERMINÉ")
        print("="*80 + "\n")

        # Sauvegarde optionnelle du résultat
        if output_file:
            self._save_result(result, output_file)
            print(f"📄 Résultat sauvegardé dans : {output_file}\n")

        return result

    def _save_result(self, result, output_file: str):
        """
        Sauvegarde le résultat du débat dans un fichier.

        Args:
            result: L'objet CrewOutput du débat
            output_file: Le chemin du fichier de sortie
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            # CrewAI >= 0.41.0 retourne un objet CrewOutput avec l'attribut 'raw'
            if hasattr(result, 'raw'):
                f.write(str(result.raw))
            # CrewAI >= 0.41.0 peut aussi avoir 'final_output'
            elif hasattr(result, 'final_output'):
                f.write(str(result.final_output))
            # Fallback pour compatibilité avec anciennes versions
            elif isinstance(result, dict) and 'final_output' in result:
                f.write(str(result['final_output']))
            # Dernier recours : conversion en string
            else:
                f.write(str(result))


def main():
    """
    Fonction principale - Exemple d'utilisation.
    """
    # Exemple de cahier des charges
    cahier_des_charges_exemple = """
    CAHIER DES CHARGES : Plateforme de Formation en Ligne

    1. OBJECTIF
    Créer une plateforme de formation en ligne pour PME avec contenus personnalisés.

    2. EXIGENCES FONCTIONNELLES
    - EF1 : Système de gestion des utilisateurs (admin, formateur, apprenant)
    - EF2 : Création et gestion de parcours de formation personnalisés
    - EF3 : Bibliothèque de contenus multimédia (vidéos, documents, quiz)
    - EF4 : Système de suivi de progression en temps réel
    - EF5 : Certification automatique à la fin des parcours
    - EF6 : Dashboard analytics pour les formateurs
    - EF7 : Forum de discussion par formation

    3. EXIGENCES TECHNIQUES
    - ET1 : Compatible mobile (responsive design)
    - ET2 : Accessible (WCAG 2.1 niveau AA)
    - ET3 : Support de 1000 utilisateurs simultanés
    - ET4 : Temps de chargement < 2 secondes
    - ET5 : Hébergement en Europe (RGPD)
    - ET6 : API REST pour intégrations tierces

    4. CONTRAINTES
    - C1 : Budget maximal : 150 000 €
    - C2 : Délai de livraison : 6 mois
    - C3 : Équipe disponible : 3 développeurs, 1 designer, 1 chef de projet
    - C4 : Doit s'intégrer avec les systèmes RH existants (API SOAP)

    5. CRITÈRES DE SUCCÈS
    - CS1 : 80% des utilisateurs terminent leur formation
    - CS2 : Note de satisfaction ≥ 4/5
    - CS3 : Zéro faille de sécurité critique
    - CS4 : ROI positif à 18 mois
    """

    # Configuration (remplacer par vos vraies variables d'environnement)
    os.environ["OPENAI_API_KEY"] = "votre-api-key-deepseek"
    os.environ["OPENAI_API_BASE"] = "https://api.deepseek.com"

    # Création et lancement du débat
    debate_system = MultiAgentDebateCrew(
        model_name="deepseek-chat",
        temperature=0.7
    )

    result = debate_system.run_debate(
        cahier_des_charges=cahier_des_charges_exemple,
        output_file="output/recommendation_finale.md"
    )

    print("Résultat final :")
    print(result)


if __name__ == "__main__":
    main()
