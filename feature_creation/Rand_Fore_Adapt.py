import numpy as np
import pandas as pd
from typing import Union
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from feature_selection import get_rf_feature_selection_pipeline, get_rf_feature_selection_grid # type: ignore

def train_rf_model(X_train: Union[np.ndarray, pd.DataFrame], y_train, 
                   externally_selected_features: Union[None, list] = None, 
                   time_based_weights: Union[None, bool] = None) -> GridSearchCV:
    """
    Trains a random forest model using the given training data and hyperparameters.

    Args:
        X_train (numpy.ndarray): The training data features.
        y_train (numpy.ndarray): The training data labels.
        externally_selected_features (list, optional): A list of feature names to use for training. Defaults to None.
        time_based_weights (numpy.ndarray, optional): A 1D array of weights to apply to each sample in X_train. Defaults to None.

    Returns:
        sklearn.model_selection.GridSearchCV: A trained random forest model.
    """
    pipeline = get_rf_pipeline()
    grid = get_rf_grid()

    grid = GridSearchCV(pipeline, n_jobs=-1, param_grid=grid, 
                        scoring='neg_mean_squared_error', cv=5, verbose=1, 
                        refit=True)
    if time_based_weights is not False:
        grid.fit(X_train, y_train, estimator__sample_weight=time_based_weights)
    else:
        grid.fit(X_train, y_train)

    return grid

def get_rf_pipeline() -> Pipeline:
    """
    Returns a pipeline for training a random forest model.

    Returns:
        sklearn.pipeline.Pipeline: A pipeline for training a random forest model.
    """
    pipeline_steps = [('imputer', SimpleImputer())]
    pipeline_steps.extend(get_rf_feature_selection_pipeline())
    pipeline_steps.append(
        ('estimator', RandomForestRegressor())
    )

    return Pipeline(pipeline_steps)

def get_rf_grid() -> dict:
    """
    Returns a dictionary of hyperparameters to use for training a random forest model that
    is used in a grid search.

    Returns:
        dict: A dictionary of hyperparameters to use for training a random forest model.
    """
    rf_grid = {}
    rf_grid.update(get_rf_feature_selection_grid())
    rf_grid.update(get_rf_model_grid())

    return rf_grid

def get_rf_model_grid() -> dict:
    """
    Returns a dictionary of hyperparameters to use for training a random forest model that
    is used in a grid search.

    Returns:
        dict: A dictionary of hyperparameters to use for training a random forest model.
    """
    return {
        'estimator__n_estimators': [200],
        'estimator__max_depth': [None, 10, 20],
        'estimator__max_features': [None, 'sqrt', 'log2'],
        'estimator__min_samples_split': [5, 10],
        'estimator__min_samples_leaf': [1, 2, 4],
    }

# Load the dataset
file_path = 'TUR_combined_with_discharge_SAMPLE_DATA.csv'
data = pd.read_csv(file_path)

# Identify target variables
y_columns = [col for col in data.columns if 'turbidity' in col and 'load' in col]

# Identify feature variables
x_columns = [col for col in data.columns if 'pwna' in col or 'wmth' in col or 'discharge' in col]

# Split data into X and y
X = data[x_columns]
y = data[y_columns[0]]

# Train the model
rf_model = train_rf_model(X, y)

# Return the best parameters and score
print("Best parameters found: ", rf_model.best_params_)
print("Best score: ", -rf_model.best_score_)
