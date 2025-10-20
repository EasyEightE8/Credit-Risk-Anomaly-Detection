# Credit-Risk-Anomaly-Detection

**API REST (Python/Flask) pour le scoring de risque de crédit et la détection d'anomalies en temps réel.**

## Objectif du Projet

Ce projet consiste à développer un service web complet (API REST) capable d'évaluer en temps réel les demandes de prêt. Le service remplit trois fonctions principales :
1.  **Analyser** une demande de prêt soumise en JSON.
2.  **Prédire** la probabilité de défaut de paiement (scoring de crédit) à l'aide d'un modèle de machine learning.
3.  **Détecter** si la demande présente un caractère atypique ou potentiellement frauduleux (détection d'anomalies).
4.  **Servir** ces prédictions via un endpoint sécurisé et performant.

---

### Phase 1 : Conception de la Base de Données et Data Engineering

* **Objectif :** Mettre en place l'infrastructure de données (data persistence layer) simulant un environnement bancaire. Cette base sert de "source de vérité" (Single Source of Truth) pour l'entraînement et la validation des modèles.
* **Compétences et Technologies :**
    * **[ ] SGBD Relationnel (MySQL/MariaDB)** : Conception d'un schéma relationnel optimisé incluant les tables `clients` (données démographiques), `comptes` (soldes, historique), `demandes_de_pret` (montant, durée, etc.) et la variable cible `statut_pret` (Remboursé / Défaut).
    * **[ ] SQL & Optimisation** : Développement de requêtes SQL performantes pour l'extraction des données. Documentation des stratégies d'indexation visant à garantir une faible latence (en s'inspirant de [l'expérience de réduction de latence de 350ms à 50ms](https://www.linkedin.com/in/easy-eight-e8/details/experience/)).
    * **[ ] Data Engineering** : Application des principes d'ingénierie des données pour assurer la cohérence et l'intégrité du schéma (similaire à l'architecture de la [base de données patients](https://www.linkedin.com/in/easy-eight-e8/details/experience/)).

### Phase 2 : Modélisation, IA et Data Science

* **Objectif :** Développer, entraîner et évaluer les deux cœurs algorithmiques du service : un modèle de scoring de crédit (classification supervisée) et un modèle de détection d'anomalies (non supervisé).
* **Compétences et Technologies :**
    * **[ ] R&D (Jupyter Notebooks)** : Utilisation de notebooks pour l'analyse exploratoire des données (EDA), le prototypage et l'évaluation des modèles.
    * **[ ] Python (Pandas, NumPy)** : Scripts d'extraction, de nettoyage (cleaning) et de transformation (feature engineering) des données issues de la base SQL.
    * **[ ] Data Visualization (Matplotlib/Seaborn)** : Création de visualisations pour analyser les profils des emprunteurs et la distribution des variables.
    * **[ ] Machine Learning (Scikit-learn)** :
        * **[ ] Modèle 1 (Scoring de Crédit)** : Entraînement d'un modèle de classification (ex: Random Forest, Gradient Boosting) pour prédire `statut_pret`.
        * **[ ] Modèle 2 (Détection d'Anomalies)** : Entraînement d'un modèle non supervisé (ex: Isolation Forest) pour identifier les demandes atypiques, en s'appuyant sur [l'expérience en détection d'anomalies à 92%](https://www.linkedin.com/in/easy-eight-e8/details/experience/).

### Phase 3 : Industrialisation (API REST & DevOps)

* **Objectif :** "Industrialiser" les modèles de machine learning en les exposant via une API REST robuste, performante et scalable. Mise en place d'un pipeline d'intégration et de déploiement continus (CI/CD).
* **Compétences et Technologies :**
    * **[ ] Back-end (Flask)** : Développement d'une API RESTful en Python (similaire à [l'expérience chez Digital Life Data](https://www.linkedin.com/in/easy-eight-e8/details/experience/)) pour servir les modèles.
    * **[ ] API Design** : Création d'un endpoint principal `/score` acceptant les données de demande en JSON et retournant un score de risque et un flag d'anomalie.
    * **[ ] Conteneurisation (Docker)** : Création d'un `Dockerfile` pour encapsuler l'application Flask et ses dépendances, assurant une portabilité et une reproductibilité parfaites.
    * **[ ] CI/CD (Git / GitHub Actions)** : Hébergement du code source sur [GitHub (Easy Eight E8)](https://github.com/Easy-Eight-E8) et configuration d'un pipeline CI/CD simple pour automatiser le build de l'image Docker à chaque `push`.

### Phase 4 : Interface de Consommation (Front-End)

* **Objectif :** Développer une interface utilisateur légère (client web) pour consommer l'API. Cette interface sert de démonstrateur et permet de soumettre de nouvelles demandes et de visualiser les scores en temps réel.
* **Compétences et Technologies :**
    * **[ ] Front-end (HTML, CSS, JavaScript)** : Création d'une page web statique avec un formulaire pour saisir les informations d'une demande de prêt.
    * **[ ] Interaction API (JavaScript)** : Utilisation de l'API `fetch` (ou `async/await`) pour appeler l'endpoint `/score` de l'API Flask de manière asynchrone et afficher la réponse à l'utilisateur.
    * **[ ] *Alternative (PHP)*:** (Envisageable) Utilisation de [PHP](https://www.linkedin.com/in/easy-eight-e8/details/experience/) pour générer le formulaire côté serveur, bien qu'une approche JS client-side soit plus moderne pour une API REST.

### Phase 5 : Analyse Métier et Contexte Macro-économique

* **Objectif :** Démontrer une compréhension approfondie des limites d'un modèle purement "statique" et proposer une feuille de route d'amélioration en intégrant des facteurs de risque de marché.
* **Compétences et Technologies :**
    * **[ ] Analyse Financière** : Rédaction d'une analyse critique dans ce `README` (ou un Jupyter Notebook dédié) sur les limites du modèle (basé uniquement sur des données "micro" et idiosyncratiques).
    * **[ ] Connaissances Marché (Bloomberg)** : Proposition conceptuelle d'amélioration du modèle par l'intégration de "features" macro-économiques (ex: taux directeurs, taux de chômage, volatilité) pour capturer le risque systémique.
    * **[ ] Extraction de Données (Bloomberg BQL/BFF)** : Explication de la méthode d'extraction de ces données via les [API Bloomberg (BMC, BFF, BQL)](https://www.linkedin.com/in/easy-eight-e8/details/skills/) pour enrichir le "feature set" du modèle de scoring.