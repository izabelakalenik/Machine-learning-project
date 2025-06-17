# Predicting Film Popularity and Resampling Techniques for Rare Target Values using classification and regression models

This project was developed as part of a master's level Machine Learning course and was completed by a team of two.

## Overview
The project explores the effectiveness of various machine learning models in predicting movie popularity based on descriptive features such as budget, genres, runtime, and user ratings. It investigates both classification and regression approaches, treating popularity as either a discrete class or a continuous variable. Additionally, the study focuses on the impact of resampling techniques to address data imbalance and the use of discretization of regression outputs, analyzing how these strategies influence model performance.


## Dataset

| **Attribute**   | **Description**                                                      |
|-----------------|----------------------------------------------------------------------|
| Instances       | 4,803 movies                                                         |
| Features        | 24 columns including title, budget, genres, release date, revenue, popularity, etc. |
| Target Variable | Popularity (continuous), optionally discretized for classification   |
| Data Types      | Numerical (e.g., budget), Categorical (e.g., genres), Textual (e.g., overview) |
| Languages       | Mostly English (94%), with several other languages                   |
| Source          | Kaggle (public domain), based on TMDB data                           |
| Link to dataset | https://www.kaggle.com/datasets/utkarshx27/movies-dataset                                                                     |



## **Notebooks**

| Notebook Name                                     | Description                                                                                                  |
|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `01_data_preprocessing.ipynb`                    | Cleaning, feature engineering, visualizations, discretization.                                               |
| `02a_classification_no_resample.ipynb`           | Classification models without resampling.                                                                    |
| `02b_classification_simple_resample.ipynb`       | Classification models with RandomOverSampler.                                                                |
| `03a_regression_no_resample.ipynb`               | Regression models without resampling.                                                                        |
| `03b_regression_simple_resample.ipynb`           | Regression models with RandomOverSampler.                                                                    |
| `04a_results_influance_of_simple_resampling.ipynb` | Statistical comparison of models with/without resampling.                                                    |
| `04b_results_classification_vs_regression.ipynb` | Comparison of regression (discretized) vs classification models for data with and without simple resampling. |

---

## Models Used

- **Classification:**
  - SVC (Support Vector Classifier)
  - KNN Classifier
  - Decision Tree Classifier
  - MLP Classifier

- **Regression:**
  - SVR (Support Vector Regressor)
  - KNN Regressor
  - Decision Tree Regressor
  - MLP Regressor

## Evaluation Metrics

- **Regression:**
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² (Coefficient of Determination)

- **Classification (incl. discretized regression):**
  - Accuracy
  - Precision
  - Recall
  - F1-score

Additionally, **Wilcoxon Signed-Rank Test** is used for statistical significance testing.

---

## Technologies

- Python (pandas, NumPy, scikit-learn)
- Jupyter Notebooks
- Matplotlib & Seaborn for data visualization
- `imblearn` for resampling techniques
- **Wilcoxon signed-rank test** for statistical significance testing

## Requirements

Install dependencies:
```bash
pip install -r requirements.txt
