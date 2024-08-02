# Création d'un Modèle d'IA pour la Gestion des Files d'Attente

## Introduction

Ce projet vise à créer un modèle d'intelligence artificielle capable de prédire les temps d'attente dans un contexte médical ou administratif. Ce document décrit les étapes de création du modèle, l'entraînement, la prédiction et la sauvegarde des résultats, en utilisant des scripts Python. 

## Structure du Répertoire

Voici la structure des fichiers du projet :

```
Ai Model :
|-- data.csv
|-- main.py
|-- predict_and_save.py
|-- requirements.txt
|-- train_model.py
```

- **`data.csv`** : Fichier contenant les données d'entrée pour l'entraînement et les prédictions.
- **`main.py`** : Script principal pour exécuter les processus d'entraînement et de prédiction.
- **`predict_and_save.py`** : Script pour effectuer des prédictions avec le modèle entraîné et sauvegarder les résultats dans un fichier CSV.
- **`requirements.txt`** : Liste des dépendances Python nécessaires.
- **`train_model.py`** : Script pour entraîner le modèle et sauvegarder le modèle et l'encodeur.

## Préparation et Traitement des Données

Les données utilisées pour entraîner le modèle doivent être au format CSV et inclure les colonnes suivantes :

- Horaires d'arrivée des patients
- Horaires de départ des patients
- Type de service ou de consultation
- Durée des consultations
- Variables contextuelles (jour de la semaine, heure de la journée, etc.)

**Exemple de structure de données :**

```csv
Patient_ID,Arrivée,Départ,Type_Service,Durée,Jour_Semaine,Heure
1,08:00,08:30,Consultation,30,Lundi,Matin
2,08:15,08:45,Urgence,30,Lundi,Matin
```

## Scripts Python

### Entraînement du Modèle

**`train_model.py`** : Ce script entraîne le modèle en utilisant les données contenues dans `data.csv`. Il prépare les données, entraîne un modèle de régression avec RandomForest, évalue le modèle, et sauvegarde le modèle ainsi que l'encodeur pour les variables catégorielles.

### Prédictions et Sauvegarde

**`predict_and_save.py`** : Ce script charge le modèle et l'encodeur sauvegardés, effectue des prédictions sur les données de `data.csv`, et sauvegarde les résultats dans `predictions_results.csv`.

### Script Principal

**`main.py`** : Ce script exécute les processus d'entraînement et de prédiction en appelant les scripts `train_model.py` et `predict_and_save.py` respectivement.

## Installation des Dépendances

### Dépendances Python

Créez un fichier `requirements.txt` pour lister les dépendances nécessaires :

```txt
pandas
scikit-learn
joblib
```

Pour installer les dépendances, exécutez la commande suivante dans votre terminal :

```bash
pip install -r requirements.txt
```

### Installation de Python

Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez créer un environnement virtuel et installer les modules nécessaires comme suit :

```bash
# Créez et activez un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`

# Installez les dépendances
pip install -r requirements.txt
```

## Utilisation

Pour entraîner le modèle, faire des prédictions et sauvegarder les résultats, exécutez le script principal :

```bash
python main.py
```

Ce script exécute les deux étapes suivantes :

1. **Entraîne le modèle** : En exécutant `train_model.py` pour entraîner et sauvegarder le modèle.
2. **Effectue des prédictions** : En exécutant `predict_and_save.py` pour prédire les temps d'attente et sauvegarder les résultats.

## Conclusion

Ce projet fournit une solution complète pour la création et l'utilisation d'un modèle d'IA pour la gestion des files d'attente. Suivez les instructions pour préparer les données, entraîner le modèle, effectuer des prédictions, et installer les dépendances nécessaires pour exécuter les scripts Python. Assurez-vous que vos données sont correctement formatées et adaptées au modèle pour obtenir les meilleurs résultats.
```

Ce `README.md` décrit de manière concise les étapes nécessaires pour utiliser le projet, les scripts impliqués, et les dépendances nécessaires, tout en restant pertinent avec les dernières modifications apportées.