# Création d'un Modèle d'IA pour la Gestion des Files d'Attente

## Introduction

Ce projet vise à créer un modèle d'intelligence artificielle capable de prédire les temps d'attente et d'optimiser la gestion des files d'attente dans un contexte médical ou administratif. Ce document présente les différentes étapes de la création du modèle, ainsi que des exemples de données et de traitement, tout en utilisant le framework Symfony pour le développement et le déploiement.

## Plateformes Recommandées

Pour développer et déployer votre modèle d'IA, voici quelques plateformes recommandées :

1. **Google Colab** : Une plateforme gratuite offrant un environnement de développement en Python avec des GPU pour accélérer l'entraînement des modèles.
2. **Amazon SageMaker** : Un service de machine learning complet et entièrement géré pour construire, entraîner et déployer des modèles ML.
3. **Microsoft Azure Machine Learning** : Un service qui permet de créer et déployer des modèles d'apprentissage automatique rapidement.
4. **IBM Watson Studio** : Une plateforme de data science et de machine learning pour collaborer, créer et déployer des modèles.
5. **Kaggle** : Une plateforme de data science offrant des environnements de codage et des compétitions pour améliorer vos compétences en ML.

## Exemples de Données

Les données utilisées pour entraîner le modèle doivent inclure les informations suivantes :

- Horaires d'arrivée des patients
- Horaires de départ des patients
- Type de service ou de consultation
- Durée des consultations
- Nombre de patients en attente
- Personnel médical disponible
- Variables contextuelles (jour de la semaine, heure de la journée, etc.)

**Exemple de structure de données :**

```csv
Patient_ID,Arrivée,Départ,Type_Service,Durée,Patients_Attente,Personnel_Dispo,Jour_Semaine,Heure
1,08:00,08:30,Consultation,30,5,3,Lundi,Matin
2,08:15,08:45,Urgence,30,6,3,Lundi,Matin
...
```

## Préparation et Traitement des Données

Voici un exemple de script Python pour préparer et traiter les données avant de les utiliser pour entraîner un modèle d'IA :

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Charger les données
data = pd.read_csv('data.csv')

# Encodage des variables catégorielles
encoder = OneHotEncoder()
encoded_features = encoder.fit_transform(data[['Type_Service', 'Jour_Semaine', 'Heure']])

# Ajouter les nouvelles features encodées au DataFrame
data = pd.concat([data, pd.DataFrame(encoded_features.toarray())], axis=1)
data.drop(['Type_Service', 'Jour_Semaine', 'Heure'], axis=1, inplace=True)

# Séparer les features et la cible
X = data.drop(['Durée'], axis=1)
y = data['Durée']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner le modèle
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prédire et évaluer
y_pred = model.predict(X_test)
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')

# Sauvegarder le modèle
joblib.dump(model, 'model.joblib')
```

## Déploiement et Intégration avec Symfony

Pour intégrer et déployer le modèle d'IA avec Symfony, vous pouvez créer un service Symfony pour charger le modèle et créer une API pour les prédictions.

### Installation des Dépendances

Installez les dépendances nécessaires pour interagir avec Python et charger le modèle :

```bash
composer require symfony/process
```

### Création du Service

Créez un service Symfony pour charger le modèle et effectuer des prédictions. Voici un exemple de service :

```php
// src/Service/PredictService.php
namespace App\Service;

use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;

class PredictService
{
    private $modelPath;

    public function __construct(string $modelPath)
    {
        $this->modelPath = $modelPath;
    }

    public function predict(array $features): float
    {
        $process = new Process(['python3', 'predict.py', json_encode($features), $this->modelPath]);
        $process->run();

        if (!$process->isSuccessful()) {
            throw new ProcessFailedException($process);
        }

        return floatval($process->getOutput());
    }
}
```

### Script de Prédiction Python

Créez un script Python pour charger le modèle et effectuer des prédictions :

```python
# predict.py
import sys
import json
import joblib

def main():
    features = json.loads(sys.argv[1])
    model_path = sys.argv[2]

    model = joblib.load(model_path)
    prediction = model.predict([features])

    print(prediction[0])

if __name__ == "__main__":
    main()
```

### Contrôleur Symfony

Créez un contrôleur pour exposer une API de prédiction :

```php
// src/Controller/PredictController.php
namespace App\Controller;

use App\Service\PredictService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;

class PredictController extends AbstractController
{
    private $predictService;

    public function __construct(PredictService $predictService)
    {
        $this->predictService = $predictService;
    }

    /**
     * @Route("/predict", name="predict", methods={"POST"})
     */
    public function predict(Request $request): JsonResponse
    {
        $data = json_decode($request->getContent(), true);
        $features = $data['features'];

        $prediction = $this->.predictService->predict($features);

        return new JsonResponse(['predicted_wait_time' => $prediction]);
    }
}
```

## Conclusion

Ce document présente une approche complète pour la création d'un modèle d'IA de gestion des files d'attente, depuis la collecte et la préparation des données jusqu'au déploiement du modèle avec Symfony. Utilisez les plateformes recommandées pour développer et déployer votre modèle, et suivez les exemples de données et de traitement pour assurer une intégration réussie.
