# HDI Prediction Web Application — Implementation Tasks

## Epic 1: Environment Setup and Package Installation

- [ ] 1.1 Create project directory structure (`data/`, `models/`, `templates/`, `static/`)
- [ ] 1.2 Create `requirements.txt` with pinned versions of all dependencies
- [ ] 1.3 Verify Python 3.8+ is available and create a virtual environment

## Epic 2: Importing Required Libraries

- [ ] 2.1 Create `train.py` with all required imports (pandas, numpy, sklearn, joblib)
- [ ] 2.2 Create `app.py` with all required imports (flask, numpy, joblib)

## Epic 3: Dataset Download and Understanding

- [ ] 3.1 Obtain or prepare the HDI dataset CSV with columns: `life_expectancy`, `mean_years_schooling`, `expected_years_schooling`, `gni_per_capita`, `hdi_tier`
- [ ] 3.2 Place dataset at `data/hdi_dataset.csv`
- [ ] 3.3 Add EDA block in `train.py`: print shape, dtypes, null counts, and class distribution

## Epic 4: Data Preprocessing and Label Encoding

- [ ] 4.1 Drop rows with null values in `train.py`
- [ ] 4.2 Apply `LabelEncoder` to the `hdi_tier` target column
- [ ] 4.3 Select the four feature columns and scale with `StandardScaler`

## Epic 5: Dividing the Model into Train and Test Data

- [ ] 5.1 Implement stratified train/test split (80/20) with `random_state=42`

## Epic 6: Fitting the Model

- [ ] 6.1 Instantiate and train a `RandomForestClassifier` on training data
- [ ] 6.2 Predict on test data and print accuracy score
- [ ] 6.3 Print full classification report with class names
- [ ] 6.4 Print confusion matrix

## Epic 7: Saving the Model

- [ ] 7.1 Save trained model to `models/hdi_model.pkl` using `joblib`
- [ ] 7.2 Save fitted scaler to `models/scaler.pkl`
- [ ] 7.3 Save fitted label encoder to `models/label_encoder.pkl`

## Epic 8: Building the Flask Web Application

- [ ] 8.1 Implement `GET /` route that renders `templates/index.html`
- [ ] 8.2 Create `templates/index.html` with a form containing four numeric inputs and a submit button
- [ ] 8.3 Implement `POST /predict` route that loads model artifacts, scales input, predicts, and decodes the label
- [ ] 8.4 Create `templates/result.html` that displays the predicted HDI tier and a back link
- [ ] 8.5 Add input validation and error handling to the predict route
- [ ] 8.6 Add basic CSS styling in `static/style.css`
- [ ] 8.7 Test all three scenarios: Very High, Medium, and Low HDI inputs

## Conclusion

- [ ] 9.1 Write `README.md` with setup, training, and run instructions
- [ ] 9.2 Verify end-to-end flow: train model → start Flask app → submit form → see prediction
