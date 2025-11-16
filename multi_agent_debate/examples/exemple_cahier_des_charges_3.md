# CAHIER DES CHARGES : Système CRM Simplifié pour PME

## 1. OBJECTIF

Développer un CRM web simplifié et accessible pour les PME de 5 à 50 employés du secteur B2B, sans besoin de formation complexe.

---

## 2. EXIGENCES FONCTIONNELLES

### EF1 : Gestion des Contacts
- Fiche contact complète (nom, entreprise, téléphone, email, adresse, notes)
- Historique des interactions (emails, appels, rendez-vous)
- Tags et segmentation personnalisables
- Import/export CSV
- Détection des doublons

### EF2 : Pipeline Commercial
- Visualisation en colonnes type Kanban (Prospect, Contact, Proposition, Négociation, Gagné, Perdu)
- Glisser-déposer des opportunités
- Valeur estimée et probabilité de closing
- Prévision de chiffre d'affaires

### EF3 : Tâches et Rappels
- Création de tâches liées à un contact ou une opportunité
- Assignation à un utilisateur
- Dates d'échéance et rappels
- Vue calendrier et liste de tâches

### EF4 : Emails Intégrés
- Envoi d'emails depuis le CRM
- Synchronisation IMAP/SMTP (Gmail, Outlook)
- Templates d'emails personnalisables
- Tracking des ouvertures (optionnel)

### EF5 : Rapports et Tableaux de Bord
- Dashboard : pipeline value, taux de conversion, top performers
- Rapports : ventes par mois, source des leads, activité par commercial
- Export PDF/Excel

### EF6 : Gestion des Utilisateurs et Permissions
- Rôles : Admin, Manager, Commercial
- Permissions par rôle (lecture, écriture, suppression)
- Log des actions sensibles

---

## 3. EXIGENCES TECHNIQUES

### ET1 : Application Web Responsive
- Accessible desktop, tablette, smartphone
- Framework moderne (React, Vue.js, ou Angular)
- Interface intuitive (inspiration : Notion, Trello)

### ET2 : Backend
- API RESTful (Node.js, Python/Django, ou PHP/Laravel)
- Base de données : PostgreSQL ou MySQL
- Cache Redis pour performance

### ET3 : Authentification
- Login/password
- Authentification 2FA (Google Authenticator)
- SSO optionnel (Google Workspace, Microsoft 365)

### ET4 : Intégrations
- API REST documentée pour intégrations tierces
- Webhooks pour événements (nouvelle opportunité, contact créé, etc.)
- Zapier/Make.com pour automatisations sans code

### ET5 : Hébergement
- Cloud européen (OVH, Scaleway, AWS EU)
- Scalabilité horizontale
- Backups automatiques quotidiens

### ET6 : Performance
- Temps de chargement < 2s
- Support de 100 utilisateurs simultanés
- Uptime ≥ 99.5%

---

## 4. CONTRAINTES

### C1 : Budget
- **60 000 € TTC**
- Développement : 45 000 €
- Design : 8 000 €
- Infra (1 an) : 5 000 €
- PM : 2 000 €

### C2 : Délai
- **3 mois** pour le MVP
- **5 mois** pour la version complète

### C3 : Équipe
- 2 développeurs full-stack
- 1 designer (temps partiel)
- 1 PM (temps partiel)

### C4 : Conformité RGPD
- Consentement cookies
- Droit d'accès et de suppression des données
- Politique de confidentialité
- Hébergement données UE

---

## 5. CRITÈRES DE SUCCÈS

### CS1 : Adoption
- 20 PME pilotes dans les 2 mois après lancement
- Taux d'activation (utilisateur créé → utilisation) ≥ 70%

### CS2 : Satisfaction
- NPS ≥ 50
- Taux de désabonnement < 10% par an

### CS3 : Performance Technique
- Temps de réponse API < 200ms (P95)
- Disponibilité ≥ 99.5%

### CS4 : Business
- Modèle SaaS : 49€/utilisateur/mois
- Break-even à 24 mois

---

## 6. PÉRIMÈTRE HORS V1

- Application mobile native
- Intelligence artificielle (scoring des leads)
- Téléphonie intégrée (VOIP)
- Gestion de projets (hors CRM)
- Multi-langues (français uniquement)

---

## RÉSUMÉ

**Type** : CRM Web B2B pour PME
**Budget** : 60 000 €
**Délai** : 5 mois (MVP à 3 mois)
**Modèle** : SaaS (49€/user/mois)

**Date** : 22 janvier 2024
**Version** : 1.0
