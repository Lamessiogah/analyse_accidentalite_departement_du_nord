# 🚗 Analyse de l'accidentalité routière du Département du Nord (2024)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)

Projet d'analyse des données d'accidentalité routière du **Département du Nord** à partir des données ouvertes de la Sécurité routière (2024).

**Objectif :** exploiter les données d'accidentalité afin de produire des indicateurs d'aide à la décision permettant de contribuer à l'amélioration de la sécurité routière et à la priorisation des actions de sécurisation du réseau routier départemental.

---

# 📌 Présentation

Ce projet a été réalisé en lien avec les missions de la Direction de la Voirie Départementale.

À partir des données ouvertes de la Sécurité routière pour l'année 2024, l'objectif est d'identifier les principaux facteurs de risque, d'évaluer la gravité des accidents et de construire des indicateurs permettant d'aider à la décision dans le domaine de la sécurité routière.

Cette démarche s'inscrit dans une logique de valorisation des données publiques au service de la gestion du patrimoine routier.

---

# 📂 Structure du projet

```text
.
├── caract-2024.csv
├── lieux-2024.csv
├── usagers-2024.csv
├── analyse_accidents_nord.py
├── classement_risque_routes.csv
├── tableau_bord.png
└── README.md
```

---

# 📊 Données utilisées

Le projet exploite les données ouvertes de la Sécurité routière :

* caractéristiques des accidents ;
* localisation des accidents ;
* informations sur les usagers.

Les analyses sont centrées sur les accidents survenus dans le **Département du Nord**.

---

# 🛠 Technologies utilisées

* Python
* Pandas
* Matplotlib
* SQL (préparation des données)
* Git

---

# ⚙️ Méthodologie

### 1. Collecte des données

Import des différentes bases de données.

### 2. Nettoyage et préparation

* traitement des valeurs manquantes ;
* harmonisation des variables ;
* contrôle de la qualité des données.

### 3. Fusion des données

Fusion des différentes tables à l'aide de l'identifiant unique **Num_Acc**.

### 4. Construction d'indicateurs

Création de plusieurs indicateurs tels que :

* nombre d'accidents ;
* nombre de tués ;
* nombre de blessés hospitalisés ;
* taux de gravité ;
* score de risque.

### 5. Analyse exploratoire

Étude de l'influence :

* des conditions météorologiques ;
* du type de route ;
* de la vitesse maximale autorisée ;
* de la période de l'année.

### 6. Construction d'un score de risque

Le score utilisé est :

```text
Score = Accidents + 3 × Blessés graves + 5 × Tués
```

Ce score permet de hiérarchiser les catégories de routes selon leur niveau de risque.

---

# 📈 Résultats obtenus

Le projet permet de :

* identifier les catégories de routes les plus accidentogènes ;
* mesurer la gravité des accidents selon différents critères ;
* produire des indicateurs décisionnels ;
* générer automatiquement un classement des catégories de routes selon leur niveau de risque.
---
---

## 📊 Visualisations

Les visualisations permettent de transformer les données en informations directement exploitables par les décideurs. Elles facilitent l'identification des tendances, des facteurs de risque et des priorités d'intervention.

### 📋 Tableau de bord statistique

Vue d'ensemble des principaux indicateurs de l'accidentalité routière du Département du Nord :

- Nombre total d'accidents
- Nombre de tués
- Nombre de blessés hospitalisés
- Taux de gravité
- Score de risque par catégorie de route

[Tableau de bord](https://github.com/Lamessiogah/analyse_accidentalite_departement_du_nord/blob/main/tableaux_de_bord_sur_le_terminal.png)

---

### 📅 Évolution mensuelle des accidents

Visualisation de la répartition des accidents au cours de l'année afin d'identifier les périodes les plus accidentogènes.

![Accidents par mois](https://github.com/Lamessiogah/analyse_accidentalite_departement_du_nord/blob/main/accidents_par_mois.png)
---

### 🌧️ Accidents selon les conditions météorologiques

Analyse de l'influence des conditions météorologiques sur l'accidentalité.

Cette visualisation permet d'identifier les situations climatiques les plus propices aux accidents.

![Accidents selon la météo](https://github.com/Lamessiogah/analyse_accidentalite_departement_du_nord/blob/main/accidents_par_meteo.png)

---

### 🛣️ Accidents par catégorie de route

Comparaison du nombre d'accidents selon les différentes catégories de routes.

Cette analyse permet d'identifier les infrastructures les plus concernées par les accidents.

![Accidents par type de route](https://github.com/Lamessiogah/analyse_accidentalite_departement_du_nord/blob/main/accidents_par_type_de_route.png)

---

### 🚦 Accidents selon la vitesse maximale autorisée

Visualisation de la répartition des accidents en fonction des limitations de vitesse.

Elle permet d'étudier l'influence de la vitesse réglementaire sur l'accidentalité.

![Accidents selon la vitesse](LIEN_VERS_VITESSE)

---

### ⚠️ Classement des catégories de routes selon le score de risque

Le score de risque est calculé selon la formule :

```text
Score = Accidents + 3 × Blessés graves + 5 × Tués
```

Cette visualisation met en évidence les catégories de routes présentant le niveau de risque le plus élevé afin d'aider à la priorisation des actions de sécurisation.

[Classement du risque](https://github.com/Lamessiogah/analyse_accidentalite_departement_du_nord/blob/main/classement_risque_nord.csv)

---

### 📁 Export des résultats

Le projet génère automatiquement un fichier :

```text
classement_risque_routes.csv
```

Ce fichier contient le classement des catégories de routes du Département du Nord selon leur score de risque et peut être utilisé comme support d'aide à la décision.

---

# 🎯 Apport pour le Département du Nord

Ce projet pourrait contribuer à :

* orienter les politiques de prévention routière ;
* prioriser les travaux de sécurisation ;
* alimenter des tableaux de bord décisionnels ;
* améliorer l'exploitation des données d'accidentalité ;
* préparer le développement d'outils d'analyse prédictive.

---

# 💡 Perspectives

Le projet pourrait être enrichi par :

* l'intégration des données de trafic ;
* le croisement avec les données météorologiques ;
* l'utilisation des données relatives au patrimoine routier ;
* le développement d'un tableau de bord interactif sous Power BI ou Qlik Sense ;
* un modèle de Machine Learning permettant de prédire la gravité des accidents ;
* une cartographie dynamique des zones accidentogènes.

---

# 👤 Auteur

**Lamessi Jérôme OGAH**

Étudiant en Master Modélisation des Données – Université de Lille

Python • SQL • Analyse de données • Data Visualisation • Aide à la décision
