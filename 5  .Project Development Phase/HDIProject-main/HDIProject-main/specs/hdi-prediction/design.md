# HDI Prediction Web Application — Technical Design

## Project Structure

```
hdi-prediction/
├── data/
│   └── hdi_dataset.csv          # Raw dataset with HDI indicators and tier labels
├── models/
│   ├── hdi_model.pkl            # Trained classifier
│   ├── scaler.pkl               # Fitted StandardScaler
│   └── label_encoder.pkl        # Fitted LabelEncoder
├── templates/
│   ├── index.html               # Input form page
│   └── result.html              # Prediction result page
├── static/
│   └── style.css                # Basic styling
├── train.py                     # ML pipeline: preprocess, train, save
├── app.py                       # Flask web application
├── requirements.txt             # Python dependencies
└── README.md
```

---

## Entity-Relationship Diagram

```
+------------------+         +-------------------+         +------------------+
|   User Input     |         |    ML Model        |         |  HDI Prediction  |
+------------------+         +-------------------+         +------------------+
| life_expectancy  |──────►  | hdi_model.pkl      |──────►  | predicted_tier   |
| mean_yrs_school  |         | scaler.pkl         |         | (Very High /     |
| exp_yrs_school   |         | label_encoder.pkl  |         |  High / Medium / |
| gni_ppp          |         +-------------------+         |  Low)            |
+------------------+                                        +------------------+
         │
         ▼
+------------------+
|   Dataset (CSV)  |
+------------------+
| country          |
| life_expectancy  |
| mean_yrs_school  |
| exp_yrs_school   |
| gni_ppp          |
| hdi_tier (label) |
+------------------+
```

---

## Epic 1: Environment Setup

**Pre-requisites:** Python 3.8+, pip

`requirements.txt`:
```
pandas==2.1.0
numpy==1.25.0
scikit-learn==1.3.0
flask==3.0.0
joblib==1.3.1
matplotlib==3.7.2
seaborn==0.12.2
```

---

## Epic 2: Importing Required Libraries

**train.py imports:**
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
```

**app.py imports:**
```python
from flask import Flask, render_template, request
import numpy as np
import joblib
```

---

## Epic 3: Dataset Download and Understanding

- Dataset source: UNDP HDI data (or a prepared CSV)
- Key columns: `life_expectancy`, `mean_years_schooling`, `expected_years_schooling`, `gni_per_capita`, `hdi_tier`
- EDA steps:
  - `df.shape`, `df.dtypes`, `df.isnull().sum()`
  - `df['hdi_tier'].value_counts()` for class distribution

---

## Epic 4: Data Preprocessing and Label Encoding

```python
# Drop nulls
df.dropna(inplace=True)

# Encode target
le = LabelEncoder()
df['hdi_encoded'] = le.fit_transform(df['hdi_tier'])

# Features and target
X = df[['life_expectancy', 'mean_years_schooling', 'expected_years_schooling', 'gni_per_capita']]
y = df['hdi_encoded']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## Epic 5: Train/Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)
```

---

## Epic 6: Fitting the Model

```python
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=le.classes_))
```

---

## Epic 7: Saving the Model

```python
joblib.dump(model, 'models/hdi_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(le, 'models/label_encoder.pkl')
```

---

## Epic 8: Flask Web Application

### Routes

| Method | Route      | Description                          |
|--------|------------|--------------------------------------|
| GET    | `/`        | Render input form                    |
| POST   | `/predict` | Accept inputs, return HDI prediction |

### app.py logic

```python
model = joblib.load('models/hdi_model.pkl')
scaler = joblib.load('models/scaler.pkl')
le = joblib.load('models/label_encoder.pkl')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        float(request.form['life_expectancy']),
        float(request.form['mean_years_schooling']),
        float(request.form['expected_years_schooling']),
        float(request.form['gni_per_capita'])
    ]
    scaled = scaler.transform([features])
    prediction = model.predict(scaled)
    label = le.inverse_transform(prediction)[0]
    return render_template('result.html', prediction=label)
```

### index.html (form)
- Four numeric input fields for the HDI indicators
- Submit button that POSTs to `/predict`

### result.html
- Displays the predicted HDI tier
- Link to go back and try another prediction

---

## Data Flow Summary

```
User fills form (4 inputs)
    │
    ▼
POST /predict
    │
    ├─ Load model, scaler, label_encoder from models/
    ├─ Scale input using scaler.transform()
    ├─ Predict class using model.predict()
    └─ Decode class using le.inverse_transform()
    │
    ▼
Render result.html with predicted HDI tier
```
