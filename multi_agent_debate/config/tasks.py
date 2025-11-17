"""
Configuration des tâches pour le système multi-agent de débat et validation.
"""
from crewai import Task


class DebateTasks:
    """Classe contenant toutes les tâches du système de débat."""

    @staticmethod
    def multi_perspective_proposal(innovateur, stratege, cahier_des_charges: str) -> Task:
        """
        TOUR 1 : Proposition Initiale Multi-Perspectives.

        Args:
            innovateur: L'agent Innovateur
            stratege: L'agent Stratège
            cahier_des_charges: Le cahier des charges complet

        Returns:
            Task: La tâche configurée
        """
        return Task(
            description=f"""
            CAHIER DES CHARGES :
            {cahier_des_charges}

            MISSION - DÉLÉGATION OBLIGATOIRE :
            Vous devez analyser en détail le cahier des charges ci-dessus et produire des propositions initiales.

            ⚠️ CETTE TÂCHE NÉCESSITE LA DÉLÉGATION À 2 AGENTS :
            - L'Innovateur (The Innovator)
            - Le Stratège (The Strategist)

            VOUS DEVEZ utiliser l'outil "Ask question to coworker" pour :
            1. Consulter l'Innovateur pour obtenir ses propositions créatives
            2. Consulter le Stratège pour obtenir son analyse stratégique
            3. Faciliter les échanges entre eux pour enrichir les propositions

            L'INNOVATEUR doit (via délégation) :
            - Analyser chaque exigence du cahier des charges
            - Proposer 3 solutions créatives DISTINCTES répondant à TOUTES les exigences
            - Pour chaque solution, expliquer comment elle adresse chaque exigence majeure
            - Identifier les points d'innovation de chaque proposition

            LE STRATÈGE doit (via délégation) :
            - Commenter immédiatement l'alignement stratégique de chaque proposition
            - Évaluer la valeur business de chaque option
            - Identifier les opportunités et risques stratégiques
            - Dialoguer avec l'Innovateur pour enrichir les propositions

            RÈGLES DU DÉBAT :
            1. DÉLÉGUEZ systématiquement aux 2 agents spécifiés
            2. Citez EXPLICITEMENT les exigences du cahier des charges dans vos arguments
            3. Facilitez les échanges entre agents pour améliorer les propositions
            4. Aucune proposition ne doit être présentée sans avoir été discutée
            5. Créez une matrice de conformité pour chaque proposition
            """,
            expected_output="""
            **RAPPORT : PROPOSITIONS INITIALES MULTI-PERSPECTIVES**

            ## 1. ANALYSE DU CAHIER DES CHARGES
            - Liste des exigences identifiées (numérotées)
            - Catégorisation : exigences critiques / importantes / secondaires
            - Contraintes identifiées

            ## 2. PROPOSITION 1 : [NOM DESCRIPTIF]
            ### Description détaillée
            [Description complète de la solution]

            ### Perspective Innovation (par L'Innovateur)
            - Points d'innovation
            - Originalité de l'approche
            - Avantages créatifs

            ### Perspective Stratégique (par Le Stratège)
            - Alignement stratégique
            - Valeur business
            - Impact à long terme

            ### Matrice de Conformité
            | Exigence | Comment adressée | Statut |
            |----------|------------------|--------|
            | Ex.1     | ...              | ✓/✗/⚠  |

            ## 3. PROPOSITION 2 : [NOM DESCRIPTIF]
            [Même structure que Proposition 1]

            ## 4. PROPOSITION 3 : [NOM DESCRIPTIF]
            [Même structure que Proposition 1]

            ## 5. SYNTHÈSE DES ÉCHANGES
            - Principaux débats entre Innovateur et Stratège
            - Points de convergence
            - Points de tension

            ## 6. COMPARATIF DES 3 PROPOSITIONS
            | Critère | Prop. 1 | Prop. 2 | Prop. 3 |
            |---------|---------|---------|---------|
            | Innovation | ... | ... | ... |
            | Faisabilité perçue | ... | ... | ... |
            | Valeur stratégique | ... | ... | ... |
            | Taux conformité | X% | X% | X% |
            """
        )

    @staticmethod
    def first_critique_round(pragmatique, avocat_du_diable, multi_perspective_proposal_task) -> Task:
        """
        TOUR 2 : Premier Round de Critique Croisée.

        Args:
            pragmatique: L'agent Pragmatique
            avocat_du_diable: L'agent Avocat du Diable
            multi_perspective_proposal_task: La tâche précédente (contexte)

        Returns:
            Task: La tâche configurée
        """
        return Task(
            description=f"""
            CONTEXTE DU CAHIER DES CHARGES :
            Le cahier des charges complet a été analysé en Task 1. Consultez la mémoire système (RAG)
            ou référez-vous à l'analyse détaillée de l'Innovateur et du Stratège pour les exigences.

            MISSION - DÉLÉGATION OBLIGATOIRE :
            Vous devez critiquer de manière constructive les 3 propositions présentées.

            ⚠️ CETTE TÂCHE NÉCESSITE LA DÉLÉGATION À 2 AGENTS :
            - Le Pragmatique (The Pragmatist)
            - L'Avocat du Diable (The Devil's Advocate)

            VOUS DEVEZ utiliser l'outil "Ask question to coworker" pour :
            1. Consulter le Pragmatique pour sa critique de faisabilité
            2. Consulter l'Avocat du Diable pour identifier les failles
            3. Faciliter le débat entre eux sur le niveau de criticité

            CONTEXTE DES PROPOSITIONS :
            Référez-vous aux propositions initiales fournies par l'Innovateur et le Stratège
            dans la tâche précédente (disponibles automatiquement via le contexte).

            LE PRAGMATIQUE doit (via délégation) :
            - Vérifier que les propositions respectent TOUTES les contraintes du cahier des charges
            - Identifier les contraintes de faisabilité (délais, budget, ressources, technique)
            - Évaluer la réalisabilité de chaque proposition
            - Pointer les risques opérationnels

            L'AVOCAT DU DIABLE doit (via délégation) :
            - Identifier les failles et incohérences dans chaque proposition
            - Vérifier qu'aucune exigence n'est mal adressée ou oubliée
            - Challenger les hypothèses implicites
            - Pointer les contradictions potentielles

            RÈGLES DU DÉBAT :
            1. DÉLÉGUEZ systématiquement aux 2 agents spécifiés
            2. Débattez entre vous (via délégation) sur le niveau de criticité de chaque point
            3. Utilisez la délégation pour consulter les autres agents si nécessaire
            4. Utilisez la mémoire partagée (RAG) pour récupérer le cahier des charges complet
            5. Citez les exigences du cahier des charges qui posent problème
            6. Priorisez les risques (critique / important / mineur)
            7. Argumentez vos positions de manière constructive
            """,
            expected_output="""
            **RAPPORT : CRITIQUE CROISÉE DES PROPOSITIONS**

            ## 1. PROPOSITION 1 - ANALYSE CRITIQUE

            ### Critique Pragmatique (Faisabilité)
            **Points de friction :**
            - [Point 1] - Criticité : [Critique/Important/Mineur]
              - Exigence concernée : [Ref. cahier des charges]
              - Problème identifié
              - Impact sur la réalisation

            **Contraintes non respectées :**
            - [Liste des contraintes]

            ### Critique de l'Avocat du Diable (Failles)
            **Failles identifiées :**
            - [Faille 1] - Criticité : [Critique/Important/Mineur]
              - Exigence mal adressée : [Ref.]
              - Nature du problème
              - Conséquences potentielles

            **Exigences manquantes ou mal couvertes :**
            - [Liste des exigences]

            ### Débat Pragmatique vs Avocat du Diable
            - Points de convergence
            - Points de désaccord
            - Consensus obtenu

            ## 2. PROPOSITION 2 - ANALYSE CRITIQUE
            [Même structure]

            ## 3. PROPOSITION 3 - ANALYSE CRITIQUE
            [Même structure]

            ## 4. RAPPORT DE CRITIQUE CONSENSUEL

            ### Matrice des Risques
            | Proposition | Risques Critiques | Risques Importants | Risques Mineurs |
            |-------------|-------------------|--------------------|--------------------|
            | Prop. 1     | X                 | X                  | X                  |
            | Prop. 2     | X                 | X                  | X                  |
            | Prop. 3     | X                 | X                  | X                  |

            ### Exigences du cahier des charges non ou mal couvertes
            | Exigence | Prop. 1 | Prop. 2 | Prop. 3 | Criticité |
            |----------|---------|---------|---------|-----------|
            | Ex.X     | ✗/⚠     | ✗/⚠     | ✗/⚠     | Critique  |

            ### Recommandations pour l'amélioration
            - [Recommandation 1]
            - [Recommandation 2]
            """,
            context=[multi_perspective_proposal_task]
        )

    @staticmethod
    def defense_and_improvement(innovateur, stratege, first_critique_round_task) -> Task:
        """
        TOUR 3 : Défense et Amélioration.

        Args:
            innovateur: L'agent Innovateur
            stratege: L'agent Stratège
            first_critique_round_task: La tâche précédente (contexte)

        Returns:
            Task: La tâche configurée
        """
        return Task(
            description=f"""
            CONTEXTE DU CAHIER DES CHARGES :
            Le cahier des charges complet a été analysé en Task 1. Consultez la mémoire système (RAG)
            pour les exigences spécifiques si nécessaire.

            MISSION - DÉLÉGATION OBLIGATOIRE :
            Vous devez répondre aux critiques et améliorer les propositions.

            ⚠️ CETTE TÂCHE NÉCESSITE LA DÉLÉGATION À 2 AGENTS :
            - L'Innovateur (The Innovator)
            - Le Stratège (The Strategist)

            VOUS DEVEZ utiliser l'outil "Ask question to coworker" pour :
            1. Consulter l'Innovateur pour ses réponses aux critiques et ajustements
            2. Consulter le Stratège pour sa validation stratégique des ajustements
            3. Faciliter les échanges pour co-créer les propositions V2

            CONTEXTE :
            Référez-vous au rapport de critique croisée de la tâche précédente
            (disponible automatiquement via le contexte).

            L'INNOVATEUR doit (via délégation) :
            - Répondre point par point aux critiques reçues
            - Proposer des ajustements concrets pour lever les objections
            - Adapter les solutions pour couvrir les exigences manquantes
            - Défendre les aspects innovants qui restent pertinents

            LE STRATÈGE doit (via délégation) :
            - Compléter la défense avec des arguments stratégiques
            - Proposer des arbitrages entre innovation et faisabilité
            - Valider que les ajustements maintiennent la valeur business
            - Participer aux propositions V2

            RÈGLES DU DÉBAT :
            1. DÉLÉGUEZ systématiquement aux 2 agents spécifiés
            2. Adressez CHAQUE critique reçue (acceptation ou contre-argument)
            3. Proposez des PROPOSITIONS V2 améliorées
            4. Utilisez la délégation pour consulter les autres agents si nécessaire
            5. Utilisez la mémoire partagée pour récupérer le cahier des charges complet
            6. Mettez à jour la matrice de conformité
            7. Documentez les compromis effectués
            """,
            expected_output="""
            **RAPPORT : DÉFENSE ET PROPOSITIONS V2**

            ## 1. RÉPONSE AUX CRITIQUES - PROPOSITION 1

            ### Critiques Pragmatiques
            | Critique | Notre Réponse | Action V2 |
            |----------|---------------|-----------|
            | [Critique 1] | [Acceptée/Contestée] | [Ajustement proposé] |

            ### Critiques de l'Avocat du Diable
            | Critique | Notre Réponse | Action V2 |
            |----------|---------------|-----------|
            | [Critique 1] | [Acceptée/Contestée] | [Ajustement proposé] |

            ### Débat avec les Critiques
            - Échanges principaux
            - Points de convergence obtenus
            - Désaccords résiduels

            ## 2. PROPOSITION 1 - VERSION 2 (AMÉLIORÉE)

            ### Description de la solution V2
            [Description détaillée avec les améliorations]

            ### Changements par rapport à V1
            - [Changement 1] - Raison : [Réponse à critique X]
            - [Changement 2] - Raison : [Couverture exigence Y]

            ### Matrice de Conformité Mise à Jour
            | Exigence | Comment adressée (V2) | Statut | Amélioration |
            |----------|----------------------|--------|--------------|
            | Ex.1     | ...                  | ✓/✗/⚠  | V1→V2       |

            ### Taux de Conformité
            - V1 : X%
            - V2 : Y%
            - Progression : +Z%

            ## 3. PROPOSITION 2 - VERSION 2
            [Même structure]

            ## 4. PROPOSITION 3 - VERSION 2
            [Même structure]

            ## 5. LISTE DES COMPROMIS EFFECTUÉS

            | Compromis | Raison | Impact sur Innovation | Impact sur Faisabilité | Validation Stratégique |
            |-----------|--------|----------------------|------------------------|------------------------|
            | [Compromis 1] | ... | ... | ... | ✓/✗ |

            ## 6. COMPARATIF V1 vs V2

            | Proposition | Taux Conformité V1 | Taux Conformité V2 | Principaux Gains |
            |-------------|-------------------|-------------------|------------------|
            | Prop. 1     | X%                | Y%                | ...              |
            | Prop. 2     | X%                | Y%                | ...              |
            | Prop. 3     | X%                | Y%                | ...              |

            ## 7. CONSENSUS PARTIEL OBTENU
            - Points validés par tous
            - Points encore en débat
            - Prochaines étapes
            """,
            context=[first_critique_round_task]
        )

    @staticmethod
    def intensive_challenge(pragmatique, defense_and_improvement_task) -> Task:
        """
        TOUR 4 : Second Round de Challenge Intensif.

        Cette tâche implique TOUS les agents (sauf le Facilitateur) via la délégation.

        Args:
            pragmatique: L'agent Pragmatique (agent principal, peut déléguer)
            defense_and_improvement_task: La tâche précédente (contexte)

        Returns:
            Task: La tâche configurée
        """
        return Task(
            description=f"""
            CONTEXTE DU CAHIER DES CHARGES :
            Le cahier des charges complet a été analysé en Task 1. Consultez la mémoire système (RAG)
            pour les exigences spécifiques si nécessaire.

            MISSION COLLECTIVE :
            Chaque agent doit challenger les propositions V2 depuis son angle d'expertise.

            CONTEXTE :
            Référez-vous aux propositions V2 améliorées de la tâche précédente
            (disponibles automatiquement via le contexte).
            Vous devez DÉLÉGUER aux autres agents pour obtenir leurs perspectives.

            CHAQUE AGENT doit :
            - L'INNOVATEUR : Vérifier que l'innovation n'a pas été trop sacrifiée
            - LE PRAGMATIQUE : Re-vérifier la faisabilité des V2
            - L'AVOCAT DU DIABLE : Chercher les nouvelles failles introduites
            - LE STRATÈGE : Confirmer l'alignement stratégique des V2

            OBJECTIFS COLLECTIFS :
            1. Vérification croisée de la conformité au cahier des charges
            2. Débat ouvert sur les points de désaccord
            3. Identification des derniers points de friction
            4. Validation collective que TOUTES les exigences sont adressées

            RÈGLES DU DÉBAT :
            1. Utilisez la DÉLÉGATION (Ask question to coworker) pour impliquer tous les agents
            2. Chaque agent doit être consulté via délégation pour obtenir sa perspective
            3. Utilisez la mémoire partagée pour accéder au cahier des charges et à l'historique
            4. Débat ouvert et contradictoire
            5. Citez les exigences problématiques (récupérez-les via RAG si nécessaire)
            6. Documentez convergences ET divergences
            """,
            expected_output="""
            **RAPPORT : CHALLENGE INTENSIF DES PROPOSITIONS V2**

            ## 1. PROPOSITION 1 V2 - CHALLENGE MULTI-PERSPECTIVES

            ### Challenge de l'Innovateur
            - Points d'innovation préservés : ✓/✗
            - Innovations sacrifiées : [Liste]
            - Proposition de récupération : [Suggestions]
            - Note Innovation : X/10

            ### Challenge du Pragmatique
            - Faisabilité technique : ✓/✗/⚠
            - Nouveaux risques identifiés : [Liste]
            - Estimation réaliste : [Budget/Délai]
            - Note Faisabilité : X/10

            ### Challenge de l'Avocat du Diable
            - Nouvelles failles détectées : [Liste]
            - Exigences encore mal couvertes : [Références]
            - Points de vigilance : [Liste]
            - Note Robustesse : X/10

            ### Challenge du Stratège
            - Alignement stratégique : ✓/✗/⚠
            - ROI estimé : [Évaluation]
            - Opportunités manquées : [Liste]
            - Note Stratégique : X/10

            ### Débat Collectif sur Proposition 1
            - Points de convergence (tous d'accord)
            - Points de désaccord (qui/quoi/pourquoi)
            - Niveau de consensus : X%

            ## 2. PROPOSITION 2 V2 - CHALLENGE MULTI-PERSPECTIVES
            [Même structure]

            ## 3. PROPOSITION 3 V2 - CHALLENGE MULTI-PERSPECTIVES
            [Même structure]

            ## 4. SYNTHÈSE COMPARATIVE

            ### Tableau de Conformité au Cahier des Charges
            | Proposition | Taux Conformité | Exigences ✓ | Exigences ⚠ | Exigences ✗ |
            |-------------|----------------|-------------|-------------|-------------|
            | Prop. 1 V2  | X%             | X           | X           | X           |
            | Prop. 2 V2  | X%             | X           | X           | X           |
            | Prop. 3 V2  | X%             | X           | X           | X           |

            ### Matrice de Scoring Multi-Critères
            | Proposition | Innovation | Faisabilité | Robustesse | Stratégie | MOYENNE |
            |-------------|-----------|-------------|------------|-----------|---------|
            | Prop. 1 V2  | X/10      | X/10        | X/10       | X/10      | X/10    |
            | Prop. 2 V2  | X/10      | X/10        | X/10       | X/10      | X/10    |
            | Prop. 3 V2  | X/10      | X/10        | X/10       | X/10      | X/10    |

            ## 5. DÉSACCORDS RÉSIDUELS ET CONVERGENCES

            ### Désaccords Majeurs
            | Sujet | Agents en Désaccord | Nature du Désaccord | Criticité |
            |-------|---------------------|---------------------|-----------|
            | [Sujet 1] | [Agents] | [Description] | Critique/Important/Mineur |

            ### Convergences Obtenues
            - [Point de consensus 1]
            - [Point de consensus 2]

            ## 6. RISQUES IDENTIFIÉS ET CRITICITÉ

            ### Risques Critiques (BLOQUANTS)
            - [Risque 1] - Proposition(s) concernée(s) - Exigence liée

            ### Risques Importants (À TRAITER)
            - [Risque 1] - Proposition(s) concernée(s) - Exigence liée

            ### Risques Mineurs (À SURVEILLER)
            - [Risque 1] - Proposition(s) concernée(s)

            ## 7. RECOMMANDATIONS POUR LA CONVERGENCE

            - Points nécessitant encore du débat
            - Arbitrages à effectuer
            - Propositions à fusionner ou éliminer
            - Axes d'amélioration finale
            """,
            context=[defense_and_improvement_task]
        )

    @staticmethod
    def forced_convergence(innovateur, intensive_challenge_task) -> Task:
        """
        TOUR 5 : Convergence Forcée.

        Cette tâche implique TOUS les agents (sauf le Facilitateur) via la délégation.

        Args:
            innovateur: L'agent Innovateur (agent principal, peut déléguer)
            intensive_challenge_task: La tâche précédente (contexte)

        Returns:
            Task: La tâche configurée
        """
        return Task(
            description=f"""
            CONTEXTE DU CAHIER DES CHARGES :
            Le cahier des charges complet a été analysé en Task 1. Consultez la mémoire système (RAG)
            pour les exigences spécifiques si nécessaire.

            MISSION COLLECTIVE - CONVERGENCE OBLIGATOIRE :
            Vous DEVEZ trouver des compromis et converger vers UNE solution finale unique.

            CONTEXTE :
            Référez-vous aux résultats du challenge intensif de la tâche précédente
            (disponibles automatiquement via le contexte).
            Utilisez la DÉLÉGATION pour impliquer tous les agents dans la négociation.

            RÈGLES STRICTES :
            1. Les agents DOIVENT faire des concessions argumentées
            2. Négociation jusqu'à consensus sur UNE solution finale
            3. La solution DOIT couvrir 100% des exigences du cahier des charges
            4. Si une exigence ne peut être couverte → justification collective OBLIGATOIRE
            5. Tous les désaccords résiduels doivent être résolus ou documentés
            6. Utilisez la DÉLÉGATION pour consulter tous les agents et obtenir leur accord
            7. Utilisez la mémoire partagée (RAG) pour récupérer le cahier des charges complet

            CHAQUE AGENT doit être consulté via délégation :
            - L'INNOVATEUR : Accepter des compromis sur l'innovation si nécessaire
            - LE PRAGMATIQUE : Trouver des solutions pour rendre faisable
            - L'AVOCAT DU DIABLE : Valider que les compromis ne créent pas de failles critiques
            - LE STRATÈGE : Confirmer que la solution finale maximise la valeur

            ATTENDU :
            - UNE solution unique consensuelle
            - 100% de conformité au cahier des charges (ou justifications)
            - Documentation des compromis de chaque agent
            - Consensus obtenu via délégation avec tous les agents
            """,
            expected_output="""
            **RAPPORT : SOLUTION FINALE CONSENSUELLE**

            ## 1. PROCESSUS DE CONVERGENCE

            ### Débat de Négociation
            - [Échange 1 entre agents]
            - [Échange 2 entre agents]
            - [Points de tension et leur résolution]

            ### Compromis par Agent

            **L'INNOVATEUR accepte de :**
            - [Concession 1] - Raison : [Argument]
            - [Concession 2] - Raison : [Argument]
            - Ligne rouge non franchie : [Ce qui ne peut être compromis]

            **LE PRAGMATIQUE accepte de :**
            - [Concession 1] - Raison : [Argument]
            - [Concession 2] - Raison : [Argument]
            - Ligne rouge non franchie : [Ce qui ne peut être compromis]

            **L'AVOCAT DU DIABLE accepte de :**
            - [Concession 1] - Raison : [Argument]
            - [Concession 2] - Raison : [Argument]
            - Ligne rouge non franchie : [Ce qui ne peut être compromis]

            **LE STRATÈGE accepte de :**
            - [Concession 1] - Raison : [Argument]
            - [Concession 2] - Raison : [Argument]
            - Ligne rouge non franchie : [Ce qui ne peut être compromis]

            ## 2. SOLUTION FINALE UNIQUE - [NOM]

            ### Description Complète
            [Description détaillée de la solution co-construite, intégrant les meilleures
            idées des 3 propositions V2 et les compromis négociés]

            ### Origine de la Solution
            - Éléments issus de Proposition 1 V2 : [Liste]
            - Éléments issus de Proposition 2 V2 : [Liste]
            - Éléments issus de Proposition 3 V2 : [Liste]
            - Nouveaux éléments co-créés : [Liste]

            ### Architecture / Approche
            [Description technique ou méthodologique]

            ### Ressources Nécessaires
            - Humaines : [Détail]
            - Techniques : [Détail]
            - Financières : [Budget estimé]

            ### Timeline
            - Phase 1 : [Description] - Durée : X
            - Phase 2 : [Description] - Durée : X
            - Phase 3 : [Description] - Durée : X
            - TOTAL : X

            ## 3. MATRICE DE CONFORMITÉ FINALE AU CAHIER DES CHARGES

            | # | Exigence | Comment Adressée | Statut | Responsable | Validation |
            |---|----------|------------------|--------|-------------|------------|
            | 1 | [Ex. 1]  | [Description]    | ✓      | [Qui]       | Tous ✓     |
            | 2 | [Ex. 2]  | [Description]    | ✓      | [Qui]       | Tous ✓     |
            | ... | ...    | ...              | ...    | ...         | ...        |

            ### Taux de Conformité Global : X%

            ### Exigences Non Couvertes (si < 100%)
            | Exigence | Raison | Justification Collective | Alternative Proposée |
            |----------|--------|--------------------------|----------------------|
            | [Ex. X]  | [Pourquoi] | [Consensus des agents] | [Solution de contournement] |

            ## 4. ARGUMENTAIRE PAR AGENT

            ### L'INNOVATEUR valide que :
            - [Argument 1 d'approbation]
            - [Argument 2 d'approbation]
            - Niveau de satisfaction Innovation : X/10

            ### LE PRAGMATIQUE valide que :
            - [Argument 1 d'approbation]
            - [Argument 2 d'approbation]
            - Niveau de confiance Faisabilité : X/10

            ### L'AVOCAT DU DIABLE valide que :
            - [Argument 1 d'approbation]
            - [Argument 2 d'approbation]
            - Niveau de confiance Robustesse : X/10

            ### LE STRATÈGE valide que :
            - [Argument 1 d'approbation]
            - [Argument 2 d'approbation]
            - Niveau de confiance Stratégie : X/10

            ## 5. DOCUMENT DES COMPROMIS ET CONCESSIONS

            | Compromis | Qui a Cédé | Qui a Gagné | Impact | Bénéfice | Validation Collective |
            |-----------|------------|-------------|--------|----------|----------------------|
            | [Compromis 1] | [Agent] | [Agent] | [Description] | [Description] | ✓ Tous |

            ## 6. CONSENSUS FINAL

            **Déclaration de Consensus :**
            "Nous, agents du système de débat, validons collectivement cette solution finale
            comme étant la meilleure réponse possible au cahier des charges, compte tenu des
            contraintes et des compromis nécessaires."

            **Signatures :**
            - L'Innovateur : ✓ Approuvé
            - Le Pragmatique : ✓ Approuvé
            - L'Avocat du Diable : ✓ Approuvé
            - Le Stratège : ✓ Approuvé

            ## 7. RISQUES RÉSIDUELS ET PLANS DE MITIGATION

            | Risque | Probabilité | Impact | Plan de Mitigation | Responsable |
            |--------|-------------|--------|-------------------|-------------|
            | [Risque 1] | Faible/Moyen/Fort | Faible/Moyen/Fort | [Actions] | [Qui] |

            ## 8. INDICATEURS DE SUCCÈS

            - [Indicateur 1] - Cible : X - Mesure : [Comment]
            - [Indicateur 2] - Cible : X - Mesure : [Comment]
            """,
            context=[intensive_challenge_task]
        )

    @staticmethod
    def final_synthesis(facilitateur, all_previous_tasks: list) -> Task:
        """
        TOUR 6 : Synthèse et Validation Finale par le Manager (Facilitateur).

        Args:
            facilitateur: L'agent Facilitateur (Manager)
            all_previous_tasks: Liste de toutes les tâches précédentes (contexte complet)

        Returns:
            Task: La tâche configurée
        """
        return Task(
            description=f"""
            CONTEXTE DU CAHIER DES CHARGES :
            Le cahier des charges complet a été analysé en Task 1. Consultez la mémoire système (RAG)
            pour valider chaque exigence point par point dans votre synthèse finale.

            HISTORIQUE COMPLET DU DÉBAT :
            Vous avez accès à tous les échanges précédents via le contexte des tâches précédentes.
            Utilisez la mémoire partagée pour récupérer toutes les informations pertinentes.

            MISSION DU FACILITATEUR (MANAGER) :
            En tant que manager de ce débat, vous devez produire le DOCUMENT FINAL DE RECOMMANDATION.

            AGENTS DISPONIBLES :
            Vous avez accès à 4 agents workers que vous DEVEZ utiliser via la délégation :
            - L'Innovateur (The Innovator) : pour valider les aspects innovants de la solution finale
            - Le Pragmatique (The Pragmatist) : pour valider la faisabilité et les contraintes
            - L'Avocat du Diable (The Devil's Advocate) : pour valider qu'il n'y a pas de failles critiques
            - Le Stratège (The Strategist) : pour valider l'alignement stratégique et la valeur business
            
            INSTRUCTIONS CRITIQUES :
            1. N'ATTENDEZ PAS de réponse de l'utilisateur - vous avez tous les agents nécessaires
            2. Utilisez la délégation (Ask question to coworker) pour consulter chaque agent sur la solution finale
            3. Consultez la mémoire partagée pour récupérer le cahier des charges et l'historique complet
            4. Si une information manque, cherchez-la dans la mémoire ou les tâches précédentes
            5. Produisez directement le document final sans demander de choix à l'utilisateur

            VOS RESPONSABILITÉS :
            1. Synthétiser l'ensemble du processus de débat en utilisant le contexte des tâches précédentes
            2. Valider que la solution répond à 100% du cahier des charges (point par point) via RAG
            3. Consulter chaque agent worker pour obtenir leur validation finale sur la solution
            4. Documenter le processus de convergence et les débats clés
            5. Identifier les risques résiduels et plans de mitigation
            6. Créer un document actionnable pour la mise en œuvre

            VALIDATION OBLIGATOIRE :
            - Vérifier CHAQUE exigence du cahier des charges (utilisez RAG pour les récupérer)
            - Consulter TOUS les agents workers pour obtenir leur consensus final
            - Documenter tous les compromis effectués (dans les tâches précédentes)
            - Identifier les risques et leurs mitigations

            FORMAT IMPOSÉ :
            Respectez scrupuleusement la structure du Expected Output ci-dessous.
            """,
            expected_output="""
            # DOCUMENT DE RECOMMANDATION FINALE
            ## Système Multi-Agent de Débat et Validation

            ---

            ## 1. SYNTHÈSE EXÉCUTIVE

            ### Solution Retenue
            [Description de la solution finale en 3-4 phrases maximum]

            ### Bénéfices Clés
            1. [Bénéfice 1]
            2. [Bénéfice 2]
            3. [Bénéfice 3]

            ### Prochaines Étapes Immédiates
            1. [Étape 1] - Deadline : [Date]
            2. [Étape 2] - Deadline : [Date]
            3. [Étape 3] - Deadline : [Date]

            ### Indicateurs Clés
            - Taux de conformité au cahier des charges : X%
            - Niveau de consensus des agents : X%
            - Nombre de compromis effectués : X
            - Risques résiduels critiques : X

            ---

            ## 2. SOLUTION DÉTAILLÉE

            ### Description Complète
            [Description détaillée de la solution finale consensuelle, incluant tous les
            aspects techniques, organisationnels et stratégiques]

            ### Architecture / Approche / Méthodologie
            [Schéma ou description structurée de l'approche]

            #### Composantes Principales
            1. [Composante 1] : [Description]
            2. [Composante 2] : [Description]
            3. [Composante 3] : [Description]

            ### Ressources Nécessaires

            #### Ressources Humaines
            - [Profil 1] : X personnes - Rôle : [Description]
            - [Profil 2] : X personnes - Rôle : [Description]

            #### Ressources Techniques
            - [Ressource 1] : [Description]
            - [Ressource 2] : [Description]

            #### Budget Estimé
            - Phase 1 : XXX €
            - Phase 2 : XXX €
            - Phase 3 : XXX €
            - **TOTAL : XXX €**

            ### Timeline de Mise en Œuvre

            | Phase | Description | Durée | Livrables | Jalons |
            |-------|-------------|-------|-----------|--------|
            | Phase 1 | [Desc.] | X semaines | [Liste] | [Jalons] |
            | Phase 2 | [Desc.] | X semaines | [Liste] | [Jalons] |
            | Phase 3 | [Desc.] | X semaines | [Liste] | [Jalons] |

            **Durée Totale : X semaines/mois**

            ---

            ## 3. CONFORMITÉ AU CAHIER DES CHARGES

            ### Validation Point par Point

            | # | Exigence du Cahier des Charges | Comment Adressée | Validation | Criticité |
            |---|-------------------------------|------------------|------------|-----------|
            | 1 | [Exigence complète]           | [Description détaillée de la réponse] | ✓ | Critique |
            | 2 | [Exigence complète]           | [Description détaillée de la réponse] | ✓ | Important |
            | 3 | [Exigence complète]           | [Description détaillée de la réponse] | ✓ | Secondaire |
            | ... | ... | ... | ... | ... |

            ### Taux de Conformité Global : X%

            #### Exigences Critiques : X/X (100%)
            #### Exigences Importantes : X/X (X%)
            #### Exigences Secondaires : X/X (X%)

            ### Exigences Non Couvertes (Si Applicable)

            | Exigence | Raison de Non-Couverture | Justification Collective | Impact | Alternative |
            |----------|-------------------------|--------------------------|--------|-------------|
            | [Ex.]    | [Raison]                | [Consensus]              | Faible/Moyen/Fort | [Solution] |

            ---

            ## 4. TRAÇABILITÉ DU DÉBAT

            ### Propositions Initiales vs Solution Finale

            #### Évolution des Propositions

            **TOUR 1 - Propositions Initiales :**
            - Proposition 1 : [Résumé] - Taux conformité : X%
            - Proposition 2 : [Résumé] - Taux conformité : X%
            - Proposition 3 : [Résumé] - Taux conformité : X%

            **TOUR 2 - Critiques Reçues :**
            - Principaux points de friction : [Liste]
            - Exigences mal couvertes : [Liste]

            **TOUR 3 - Propositions V2 :**
            - Proposition 1 V2 : [Résumé] - Taux conformité : X%
            - Proposition 2 V2 : [Résumé] - Taux conformité : X%
            - Proposition 3 V2 : [Résumé] - Taux conformité : X%

            **TOUR 4 - Challenge Intensif :**
            - Désaccords majeurs identifiés : [Liste]
            - Convergences obtenues : [Liste]

            **TOUR 5 - Convergence :**
            - Solution finale co-construite : [Résumé]
            - Taux conformité final : X%

            ### Principaux Débats et Leur Résolution

            | Sujet du Débat | Agents Impliqués | Position Initiales | Résolution | Impact sur Solution |
            |----------------|------------------|-------------------|------------|---------------------|
            | [Débat 1]      | [Agents]         | [Positions]       | [Comment résolu] | [Impact] |
            | [Débat 2]      | [Agents]         | [Positions]       | [Comment résolu] | [Impact] |

            ### Compromis Effectués et Justifications

            | Compromis | Agent(s) Ayant Cédé | Bénéfice Obtenu | Justification | Validation |
            |-----------|---------------------|-----------------|---------------|------------|
            | [Compromis 1] | [Agent] | [Bénéfice] | [Pourquoi accepté] | ✓ Collective |

            ### Contribution de Chaque Agent

            **L'INNOVATEUR a apporté :**
            - [Contribution 1]
            - [Contribution 2]
            - Éléments innovants intégrés : [Liste]

            **LE PRAGMATIQUE a apporté :**
            - [Contribution 1]
            - [Contribution 2]
            - Contraintes majeures identifiées : [Liste]

            **L'AVOCAT DU DIABLE a apporté :**
            - [Contribution 1]
            - [Contribution 2]
            - Failles critiques évitées : [Liste]

            **LE STRATÈGE a apporté :**
            - [Contribution 1]
            - [Contribution 2]
            - Alignements stratégiques validés : [Liste]

            ---

            ## 5. PLAN D'ACTION

            ### Phase 1 : [NOM PHASE] (Durée : X)

            **Objectifs :**
            - [Objectif 1]
            - [Objectif 2]

            **Actions :**
            1. [Action 1] - Responsable : [Qui] - Deadline : [Date]
            2. [Action 2] - Responsable : [Qui] - Deadline : [Date]

            **Livrables :**
            - [Livrable 1]
            - [Livrable 2]

            **Critères de Succès :**
            - [Critère 1]
            - [Critère 2]

            ### Phase 2 : [NOM PHASE] (Durée : X)
            [Même structure]

            ### Phase 3 : [NOM PHASE] (Durée : X)
            [Même structure]

            ### Quick Wins (Actions Immédiates)

            | Action | Impact | Effort | Deadline | Responsable |
            |--------|--------|--------|----------|-------------|
            | [Action 1] | Fort | Faible | J+X | [Qui] |
            | [Action 2] | Moyen | Faible | J+X | [Qui] |

            ### Jalons Clés

            | Jalon | Date | Critères de Validation | Risques |
            |-------|------|----------------------|---------|
            | [Jalon 1] | [Date] | [Critères] | [Risques] |
            | [Jalon 2] | [Date] | [Critères] | [Risques] |

            ---

            ## 6. RISQUES ET MITIGATIONS

            ### Risques Résiduels Identifiés

            #### RISQUES CRITIQUES

            | Risque | Description | Probabilité | Impact | Score | Plan de Mitigation | Responsable | Indicateur d'Alerte |
            |--------|-------------|-------------|--------|-------|-------------------|-------------|-------------------|
            | [R1]   | [Desc.]     | Faible/Moyen/Fort | Faible/Moyen/Fort | X/10 | [Actions préventives] | [Qui] | [Indicateur] |

            #### RISQUES IMPORTANTS
            [Même structure]

            #### RISQUES MINEURS
            [Même structure]

            ### Plans de Mitigation Détaillés

            **Risque 1 : [NOM]**
            - **Actions Préventives :**
              1. [Action 1]
              2. [Action 2]
            - **Actions Correctives (si survient) :**
              1. [Action 1]
              2. [Action 2]
            - **Indicateurs de Suivi :**
              - [Indicateur 1] - Seuil d'alerte : X
              - [Indicateur 2] - Seuil d'alerte : X

            ### Matrice de Suivi des Risques

            | Risque | Statut | Évolution | Dernière Révision | Prochaine Révision | Responsable |
            |--------|--------|-----------|------------------|-------------------|-------------|
            | [R1]   | Actif/Fermé | ↗↘→ | [Date] | [Date] | [Qui] |

            ---

            ## 7. DISSENSUS ET ALERTES

            ### Points de Désaccord Non Résolus (Si Applicable)

            | Sujet | Positions en Conflit | Agents Concernés | Criticité | Recommandation |
            |-------|---------------------|------------------|-----------|----------------|
            | [Sujet 1] | [Positions] | [Agents] | Faible/Moyen/Fort | [Action suggérée] |

            ### Zones d'Attention Particulière

            **ZONE 1 : [NOM]**
            - **Nature de l'Attention :** [Description]
            - **Pourquoi Surveiller :** [Raison]
            - **Actions de Surveillance :**
              1. [Action 1]
              2. [Action 2]
            - **Fréquence de Révision :** [Hebdomadaire/Mensuelle/etc.]

            ### Recommandations de Vigilance

            1. **[Recommandation 1]**
               - Contexte : [Pourquoi]
               - Action : [Quoi faire]
               - Responsable : [Qui]

            2. **[Recommandation 2]**
               [Même structure]

            ### Conditions de Révision de la Solution

            La solution devra être révisée si :
            1. [Condition 1]
            2. [Condition 2]
            3. [Condition 3]

            ---

            ## 8. CONCLUSION ET VALIDATION MANAGÉRIALE

            ### Évaluation Globale par le Facilitateur

            **Qualité du Débat :** X/10
            - Profondeur des échanges : [Appréciation]
            - Implication des agents : [Appréciation]
            - Richesse des perspectives : [Appréciation]

            **Qualité de la Solution :** X/10
            - Conformité au cahier des charges : X%
            - Équilibre innovation/faisabilité : [Appréciation]
            - Robustesse : [Appréciation]
            - Alignement stratégique : [Appréciation]

            **Niveau de Consensus :** X%
            - Unanimité obtenue sur : [X points clés]
            - Compromis nécessaires : [X compromis]
            - Dissensus résiduels : [X points]

            ### Validation Managériale Finale

            ✓ **JE VALIDE** cette solution comme étant la meilleure réponse au cahier des charges.

            **Justification :**
            [Argumentaire du Facilitateur expliquant pourquoi cette solution est optimale compte
            tenu des contraintes, des débats et du processus de convergence]

            **Réserves éventuelles :**
            [Points de vigilance ou conditions de mise en œuvre]

            ### Approbation Finale

            **Document approuvé par :**
            - Le Facilitateur (Manager) : ✓
            - L'Innovateur : ✓
            - Le Pragmatique : ✓
            - L'Avocat du Diable : ✓
            - Le Stratège : ✓

            **Date du Consensus : [Date]**

            ---

            **FIN DU DOCUMENT DE RECOMMANDATION FINALE**
            """,
            context=all_previous_tasks
        )
