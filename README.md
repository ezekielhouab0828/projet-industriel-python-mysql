# Projet Industriel – Suivi des Mesures (Python + MySQL)

Ce projet simule, stocke et visualise des mesures industrielles dans un environnement Python/MySQL.  
Il a été réalisé dans le cadre d’un projet d’analyse et de gestion de données industrielles.

---

## Objectifs du projet

- Simuler des mesures industrielles (température, pression, vitesse…)
- Stocker ces mesures dans une base MySQL
- Lire et analyser les données enregistrées
- Visualiser les tendances grâce à des graphiques
- Structurer un projet Python complet avec plusieurs modules

---

## Architecture du projet

```
projet_industriel/
│
├── DATABASE Projet Industriel.sql   # Script de création de la base et des tables
├── db.py                            # Connexion à MySQL
├── simulateur.py                    # Génération de mesures simulées
├── insert_mesure.py                 # Insertion des mesures dans la base
├── read_data.py                     # Lecture et extraction des données
├── visualisation.py                 # Graphiques et analyses
└── main.py                          # Point d’entrée du projet
```

---

## Base de données

Le fichier **DATABASE Projet Industriel.sql** contient :

- La création de la base `projet_industriel`
- La création de la table `mesures`
- Les types de données utilisés
- Les contraintes nécessaires

---

## ⚙️ Fonctionnement du projet

### Créer la base MySQL  
Importer le fichier SQL dans MySQL Workbench ou via la ligne de commande :

```sql
SOURCE 'DATABASE Projet Industriel.sql';
```

### Configurer la connexion dans `db.py`  
Adapter si nécessaire :

```python
host="localhost",
user="root",
password="mot_de_passe",
database="projet_industriel"
```

### Lancer la simulation et l’insertion

```bash
python main.py
```

Le script :
- génère des mesures
- les insère dans MySQL
- affiche un résumé

### Visualiser les données

```bash
python visualisation.py
```

---

## Exemple de données générées

- Température (°C)
- Pression (bar)
- Vitesse (m/s)
- Horodatage automatique

---

## Compétences mises en œuvre

- Python (modules, architecture, scripts)
- MySQL (création de base, insertion, requêtes)
- Visualisation (matplotlib)
- Gestion de projet data
- Versioning Git & GitHub

---

## Améliorations possibles

- Ajout d’une API Flask pour exposer les données
- Tableau de bord interactif (Streamlit / Dash)
- Ajout de tests unitaires
- Automatisation via un scheduler

---

## Auteur

**Ezekiel Houabaloukou**  
Étudiant Master en Data Enginnering / Cloud & passionné par les projets industriels et analytiques.
