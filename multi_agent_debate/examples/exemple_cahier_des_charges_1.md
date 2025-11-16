# CAHIER DES CHARGES : Plateforme de Formation en Ligne

## 1. CONTEXTE ET OBJECTIF

### 1.1 Contexte
Les PME françaises ont des besoins croissants en formation continue de leurs employés, mais les solutions existantes sont soit trop chères (LMS entreprise), soit peu adaptées (plateformes grand public type Udemy).

### 1.2 Objectif Principal
Créer une plateforme de formation en ligne B2B dédiée aux PME (10-250 employés) avec des contenus personnalisables et un suivi granulaire de la progression.

---

## 2. EXIGENCES FONCTIONNELLES

### EF1 : Système de Gestion des Utilisateurs
- **Criticité** : Critique
- **Description** : 3 niveaux de rôles
  - **Administrateur** : Gestion globale de la plateforme entreprise
  - **Formateur** : Création de contenus et suivi des apprenants
  - **Apprenant** : Consultation et suivi des formations

### EF2 : Création et Gestion de Parcours de Formation Personnalisés
- **Criticité** : Critique
- **Description** :
  - Création de parcours modulaires par le formateur
  - Séquençage des modules avec prérequis
  - Affectation de parcours à des groupes d'apprenants
  - Duplication et modification de parcours existants

### EF3 : Bibliothèque de Contenus Multimédia
- **Criticité** : Critique
- **Description** :
  - Support vidéo (MP4, WebM) avec player intégré
  - Documents (PDF, DOCX, PPTX) avec visionneuse
  - Quiz interactifs (QCM, vrai/faux, réponses courtes)
  - Ressources téléchargeables
  - Tags et catégorisation des contenus

### EF4 : Système de Suivi de Progression en Temps Réel
- **Criticité** : Importante
- **Description** :
  - Barre de progression par module et parcours
  - Historique des activités (vidéos visionnées, quiz complétés)
  - Temps passé sur chaque contenu
  - Taux de complétion par apprenant

### EF5 : Certification Automatique
- **Criticité** : Importante
- **Description** :
  - Génération automatique de certificats PDF à la fin d'un parcours
  - Conditions paramétrables (taux de complétion, note minimale aux quiz)
  - Personnalisation du template de certificat
  - Traçabilité et vérification des certificats

### EF6 : Dashboard Analytics pour Formateurs
- **Criticité** : Importante
- **Description** :
  - Vue d'ensemble : nombre d'apprenants actifs, taux de complétion moyen
  - Graphiques de progression par parcours
  - Identification des contenus problématiques (taux d'abandon élevé)
  - Export des données en CSV/Excel

### EF7 : Forum de Discussion par Formation
- **Criticité** : Secondaire
- **Description** :
  - Forum associé à chaque parcours
  - Questions/réponses avec fil de discussion
  - Notification aux formateurs
  - Modération basique (suppression de messages)

---

## 3. EXIGENCES TECHNIQUES

### ET1 : Compatibilité Mobile (Responsive Design)
- **Criticité** : Critique
- **Description** :
  - Interface responsive (desktop, tablette, smartphone)
  - Priorité : expérience mobile first
  - Test sur iOS (Safari) et Android (Chrome)

### ET2 : Accessibilité (WCAG 2.1 Niveau AA)
- **Criticité** : Importante
- **Description** :
  - Contraste des couleurs conforme
  - Navigation au clavier
  - Support des lecteurs d'écran
  - Sous-titres pour les vidéos

### ET3 : Support de 1000 Utilisateurs Simultanés
- **Criticité** : Critique
- **Description** :
  - Architecture scalable (cloud)
  - Load balancing
  - Tests de charge avec 1000+ utilisateurs

### ET4 : Temps de Chargement < 2 Secondes
- **Criticité** : Importante
- **Description** :
  - Pages principales : < 2s (connexion 4G)
  - Vidéos : démarrage en < 3s
  - Optimisation images et lazy loading

### ET5 : Hébergement en Europe (RGPD)
- **Criticité** : Critique
- **Description** :
  - Données hébergées dans l'UE
  - Conformité RGPD complète
  - Politique de confidentialité
  - Consentement cookies
  - Droit à l'oubli

### ET6 : API REST pour Intégrations Tierces
- **Criticité** : Importante
- **Description** :
  - API REST documentée (OpenAPI/Swagger)
  - Endpoints : utilisateurs, parcours, progression
  - Authentification OAuth2
  - Rate limiting

---

## 4. CONTRAINTES

### C1 : Budget Maximal
- **Montant** : 150 000 € TTC
- **Répartition indicative** :
  - Développement : 100 000 €
  - Design UX/UI : 20 000 €
  - Gestion de projet : 15 000 €
  - Infrastructure (1ère année) : 10 000 €
  - Formation/doc : 5 000 €

### C2 : Délai de Livraison
- **Durée** : 6 mois maximum
- **Deadline** : 30 juin 2024
- **Jalons** :
  - M1 : Maquettes validées
  - M3 : MVP (EF1, EF2, EF3)
  - M5 : Version complète
  - M6 : Tests et déploiement

### C3 : Équipe Disponible
- **Composition** :
  - 3 développeurs full-stack (React + Node.js + Python)
  - 1 designer UX/UI
  - 1 chef de projet / Product Owner
- **Disponibilité** : Temps plein sur le projet

### C4 : Intégration Systèmes RH Existants
- **Criticité** : Critique
- **Description** :
  - Les PME clientes utilisent déjà des logiciels RH (ex: Sage, Cegid)
  - API SOAP pour synchronisation des utilisateurs
  - Import/export CSV en fallback
  - Mapping des champs utilisateurs

---

## 5. CRITÈRES DE SUCCÈS

### CS1 : Taux de Complétion des Formations
- **Cible** : 80% des utilisateurs terminent leur formation
- **Mesure** : Analytics intégrées, reporting mensuel

### CS2 : Note de Satisfaction
- **Cible** : ≥ 4/5
- **Mesure** :
  - Questionnaire de satisfaction en fin de parcours
  - NPS (Net Promoter Score) trimestriel

### CS3 : Zéro Faille de Sécurité Critique
- **Cible** : Aucune faille critique lors d'un audit de sécurité externe
- **Mesure** :
  - Audit de sécurité avant mise en production
  - Tests de pénétration par un cabinet tiers

### CS4 : ROI Positif à 18 Mois
- **Cible** : Rentabilité atteinte à 18 mois après le lancement
- **Mesure** :
  - 50 PME clientes minimum (abonnement 500€/mois)
  - Coût d'acquisition client < 2000€
  - Churn rate < 15% annuel

---

## 6. EXIGENCES NON-FONCTIONNELLES

### Performance
- Disponibilité : 99.5% (hors maintenance planifiée)
- Temps de réponse API : < 200ms (P95)
- Capacité vidéo : streaming adaptatif (HLS/DASH)

### Sécurité
- Chiffrement HTTPS (TLS 1.3)
- Mots de passe hashés (bcrypt)
- Protection CSRF/XSS
- Logs d'audit des actions critiques

### Maintenance
- Monitoring (uptime, erreurs, performances)
- Sauvegardes automatiques quotidiennes
- Procédure de rollback
- Documentation technique complète

---

## 7. PÉRIMÈTRE HORS PROJET (V1)

Les éléments suivants sont **EXCLUS** de la version 1 :

- Gamification (badges, points)
- Classes virtuelles en direct (webinaires)
- Application mobile native (iOS/Android)
- Intégration vidéoconférence (Zoom, Teams)
- Marketplace de contenus tiers
- Support multilingue (seulement français)

Ces fonctionnalités pourront être ajoutées dans une V2.

---

## 8. RISQUES IDENTIFIÉS (PRÉLIMINAIRES)

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Complexité intégration API SOAP | Moyenne | Fort | POC technique dès M1 |
| Dépassement budget hébergement | Faible | Moyen | Devis cloud avant démarrage |
| Retard livraison contenus | Moyenne | Moyen | Client doit fournir contenus à M2 |
| Accessibilité WCAG complexe | Moyenne | Fort | Audit accessibilité à M3 |

---

## RÉSUMÉ DES EXIGENCES PAR CRITICITÉ

### CRITIQUES (Must Have)
- EF1, EF2, EF3
- ET1, ET3, ET5
- C1, C2, C4
- CS3

### IMPORTANTES (Should Have)
- EF4, EF5, EF6
- ET2, ET4, ET6
- CS1, CS2

### SECONDAIRES (Could Have)
- EF7
- CS4 (nice to have mais pas bloquant)

---

**Date de rédaction** : 15 janvier 2024
**Version** : 1.0
**Contact** : chef-projet@entreprise.fr
