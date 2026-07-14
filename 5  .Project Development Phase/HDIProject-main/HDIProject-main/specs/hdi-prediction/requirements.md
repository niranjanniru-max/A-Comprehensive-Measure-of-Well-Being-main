# HDI Prediction Web Application — Requirements

## Overview

A machine learning web application that predicts the Human Development Index (HDI) tier of a country based on life expectancy, education, and income indicators. The application classifies countries into four tiers: **Very High**, **High**, **Medium**, and **Low** human development.

---

## Functional Requirements

### Epic 1: Environment Setup and Package Installation
- REQ-1.1: The project must run in a Python virtual environment.
- REQ-1.2: Required packages must be installable via `requirements.txt`.
- REQ-1.3: Packages include: `pandas`, `numpy`, `scikit-learn`, `flask`, `joblib`, and `matplotlib`/`seaborn` for visualization.

### Epic 2: Importing Required Libraries
- REQ-2.1: The training script must import data manipulation libraries (`pandas`, `numpy`).
- REQ-2.2: The training script must import ML libraries from `scikit-learn` (model, encoders, train/test split, metrics).
- REQ-2.3: The Flask app must import `flask`, `joblib`, and `numpy`/`pandas` for inference.

### Epic 3: Dataset Download and Understanding
- REQ-3.1: The dataset must contain the following input features:
  - Life Expectancy at Birth (years)
  - Mean Years of Schooling (years)
  - Expected Years of Schooling (years)
  - Gross National Income (GNI) per capita (PPP $)
- REQ-3.2: The dataset must contain a target column representing the HDI tier: `Very High`, `High`, `Medium`, `Low`.
- REQ-3.3: The dataset must be stored as a CSV file in the `data/` directory.
- REQ-3.4: An exploratory data analysis (EDA) step must summarize shape, data types, null values, and class distribution.

### Epic 4: Data Preprocessing and Label Encoding
- REQ-4.1: The pipeline must handle missing values by either dropping or imputing them.
- REQ-4.2: The target variable (HDI tier) must be label-encoded to integer classes before training.
- REQ-4.3: Input features must be scaled using `StandardScaler` or `MinMaxScaler`.
- REQ-4.4: The label encoder and scaler must be saved as serialized artifacts for use during inference.

### Epic 5: Dividing the Model into Train and Test Data
- REQ-5.1: The dataset must be split into training (80%) and testing (20%) sets.
- REQ-5.2: Splitting must use a fixed `random_state` for reproducibility.
- REQ-5.3: Stratified splitting must be used to preserve class distribution.

### Epic 6: Fitting the Model
- REQ-6.1: A classification algorithm must be trained on the training data (e.g., Random Forest, Decision Tree, or Logistic Regression).
- REQ-6.2: The model must be evaluated on the test set using accuracy, classification report, and confusion matrix.
- REQ-6.3: Evaluation results must be printed or logged during training.

### Epic 7: Saving the Model
- REQ-7.1: The trained model must be serialized and saved using `joblib` to a `models/` directory.
- REQ-7.2: The fitted scaler must be saved alongside the model.
- REQ-7.3: The fitted label encoder must be saved alongside the model.

### Epic 8: Building the Flask Web Application
- REQ-8.1: The Flask app must expose a home route (`GET /`) that renders an input form.
- REQ-8.2: The input form must accept the four HDI indicator values from the user.
- REQ-8.3: The app must expose a predict route (`POST /predict`) that:
  - Accepts form inputs
  - Loads the saved model, scaler, and label encoder
  - Scales the inputs
  - Returns the predicted HDI tier as a human-readable label
- REQ-8.4: The prediction result must be displayed on the result page.
- REQ-8.5: The app must handle invalid or missing inputs gracefully with user-facing error messages.

---

## Non-Functional Requirements

- NFR-1: The web app must respond to a prediction request within 2 seconds.
- NFR-2: The codebase must be organized with clear separation between training (`train.py`), inference, and the Flask app (`app.py`).
- NFR-3: The app must be runnable locally with a single `flask run` or `python app.py` command.

---

## Entity-Relationship Overview

| Entity         | Attributes                                                                 |
|----------------|----------------------------------------------------------------------------|
| Country Input  | life_expectancy, mean_years_schooling, expected_years_schooling, gni_ppp  |
| HDI Prediction | predicted_tier (Very High / High / Medium / Low)                          |
| ML Model       | trained classifier, fitted scaler, fitted label encoder                   |
| Dataset        | CSV file with input features + HDI tier label                             |

---

## Project Flow Summary

```
Dataset (CSV)
    └─► EDA & Preprocessing
            └─► Label Encoding + Scaling
                    └─► Train/Test Split
                            └─► Model Training & Evaluation
                                    └─► Save Model Artifacts
                                            └─► Flask App (form input → prediction → result)
```
