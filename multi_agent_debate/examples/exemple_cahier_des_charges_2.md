# CAHIER DES CHARGES : Application Mobile E-commerce "FreshLocal"

## 1. OBJECTIF

Créer une application mobile (iOS + Android) pour connecter les producteurs locaux (agriculteurs, artisans) avec les consommateurs urbains pour la livraison de produits frais en circuit court.

---

## 2. EXIGENCES FONCTIONNELLES

### EF1 : Inscription et Profils Utilisateurs
- **2 types de profils** : Producteur et Consommateur
- Inscription via email ou réseaux sociaux (Google, Apple)
- Profil producteur : présentation, localisation, certifications (bio, label rouge, etc.)
- Profil consommateur : adresses de livraison, préférences alimentaires

### EF2 : Catalogue Produits Géolocalisés
- Affichage des producteurs dans un rayon de X km (paramétrable par l'utilisateur)
- Catalogue par producteur avec photos, descriptions, prix, stock disponible
- Filtres : type de produit, labels, prix, distance
- Recherche par mot-clé

### EF3 : Panier et Commande Multi-Producteurs
- Ajout de produits de plusieurs producteurs dans un même panier
- Gestion des paniers multiples (1 panier par producteur)
- Récapitulatif avec détail par producteur
- Minimum de commande par producteur (si applicable)

### EF4 : Paiement Sécurisé
- Carte bancaire (Stripe ou équivalent)
- Apple Pay / Google Pay
- Paiement fractionné par producteur
- Historique des paiements

### EF5 : Système de Livraison
- 2 modes : Livraison à domicile ou Retrait sur le point de vente
- Plages horaires de livraison proposées par le producteur
- Suivi de commande en temps réel (statut : préparée, en livraison, livrée)
- Notification push à chaque étape

### EF6 : Avis et Notations
- Note par producteur (1-5 étoiles)
- Commentaires textuels
- Réponse possible du producteur
- Modération (signalement abus)

### EF7 : Messagerie Producteur-Consommateur
- Chat in-app pour questions sur produits ou commandes
- Notifications push des nouveaux messages

---

## 3. EXIGENCES TECHNIQUES

### ET1 : Plateformes
- **iOS** : version 14 minimum (iPhone 8 et +)
- **Android** : version 9 minimum
- Framework : React Native ou Flutter (à décider)

### ET2 : Backend et Base de Données
- API REST (Node.js ou Python/Django)
- Base de données : PostgreSQL
- Stockage images : AWS S3 ou équivalent
- Hébergement : Cloud scalable (AWS, GCP, Azure)

### ET3 : Géolocalisation
- API Google Maps ou Mapbox
- Calcul de distance en temps réel
- Cache des positions pour limiter les appels API

### ET4 : Notifications Push
- Service de push (Firebase Cloud Messaging ou OneSignal)
- Notifications pour : nouvelle commande, changement de statut, nouveau message, promotions

### ET5 : Paiement
- Intégration Stripe ou équivalent (conformité PCI-DSS)
- Gestion des paiements fractionnés (split payment)
- Remboursements en cas d'annulation

### ET6 : Performance
- Temps de chargement des écrans : < 1.5s
- Images optimisées (WebP, lazy loading)
- Offline mode basique (cache des derniers produits consultés)

### ET7 : Sécurité
- HTTPS obligatoire
- Authentification JWT
- Validation côté serveur de toutes les entrées
- Conformité RGPD (données hébergées UE)

---

## 4. CONTRAINTES

### C1 : Budget
- **Budget total** : 80 000 € TTC
- Répartition :
  - Développement mobile : 45 000 €
  - Backend/API : 20 000 €
  - Design UX/UI : 10 000 €
  - Gestion de projet : 5 000 €

### C2 : Délai
- **Durée** : 4 mois
- **MVP à 2 mois** : Catalogue, panier, paiement, livraison basique (iOS uniquement)
- **Version complète à 4 mois** : iOS + Android + toutes les fonctionnalités

### C3 : Équipe
- 2 développeurs mobile (React Native/Flutter)
- 1 développeur backend
- 1 designer UX/UI (à temps partiel)
- 1 chef de projet

### C4 : Marketplace
- Commission de 15% par transaction pour financer la plateforme
- Paiement aux producteurs sous 7 jours après livraison
- Gestion des litiges (produits manquants, qualité)

---

## 5. CRITÈRES DE SUCCÈS

### CS1 : Adoption
- 100 producteurs inscrits dans les 3 mois après le lancement
- 1000 consommateurs actifs dans les 6 mois

### CS2 : Engagement
- Taux de conversion (visite → achat) ≥ 10%
- Panier moyen ≥ 25 €
- Taux de réachat à 30 jours ≥ 30%

### CS3 : Satisfaction
- Note moyenne de l'application ≥ 4.2/5 (App Store & Google Play)
- NPS (Net Promoter Score) ≥ 40

### CS4 : Technique
- Disponibilité de l'API ≥ 99%
- Taux de crash de l'app < 1%
- Temps moyen de paiement < 30 secondes

---

## 6. PÉRIMÈTRE HORS V1

- Abonnements consommateurs (livraison gratuite)
- Programme de fidélité (points, réductions)
- Recommandations personnalisées (IA)
- Application web (seulement mobile V1)
- Multi-langues (français uniquement)
- Paniers récurrents (commande hebdomadaire automatique)

---

## 7. RISQUES IDENTIFIÉS

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Adoption faible des producteurs | Moyenne | Critique | Marketing et démo avant lancement |
| Complexité split payment | Forte | Moyen | POC Stripe dès la semaine 1 |
| Problèmes de livraison | Moyenne | Fort | Partenariat avec un livreur local |
| Fraude paiement | Faible | Moyen | Validation manuelle premières commandes |

---

## RÉSUMÉ

**Produit** : Application mobile marketplace "circuit court"
**Cible** : iOS + Android
**Budget** : 80 000 €
**Délai** : 4 mois (MVP à 2 mois)
**Criticité max** : Catalogue géolocalisé, Paiement, Livraison

**Date** : 20 janvier 2024
**Version** : 1.0
