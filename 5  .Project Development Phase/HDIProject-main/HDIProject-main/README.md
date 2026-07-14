# 🌍 Human Development Index (HDI) Predictor

A machine learning web application that predicts a country's **Human Development Index (HDI) score** and classifies it into one of four tiers — **Very High, High, Medium, or Low** — based on real-world development indicators.

Built with Python, Scikit-learn, Flask, and Jupyter Notebook.

---

## 📸 Screenshots

| Home Page | Result Page |
|-----------|-------------|
| Input form with 4 indicators | Predicted HDI score with tier, score bar, and description |

---

## 🧠 What is HDI?

The Human Development Index is a composite statistic of:
- **Life Expectancy** — how long people live
- **Education** — mean and expected years of schooling
- **Income** — Gross National Income (GNI) per capita (PPP $)

| Tier | HDI Score Range |
|------|----------------|
| 🌟 Very High | ≥ 0.800 |
| ✅ High | 0.700 – 0.799 |
| 📈 Medium | 0.550 – 0.699 |
| ⚠️ Low | < 0.550 |

---

## 🗂️ Project Structure

```
mlproject/
├── app.py                          # Flask web application
├── hdi_prediction.ipynb            # Jupyter notebook (all ML epics)
├── requirements.txt                # Python dependencies
├── data/
│   └── hdi_dataset.csv             # HDI dataset (UNDP)
├── models/
│   ├── hdi_model.pkl               # Trained Linear Regression model
│   ├── scaler.pkl                  # Fitted StandardScaler
│   └── label_encoder.pkl           # Fitted LabelEncoder
├── templates/
│   ├── index.html                  # Input form page
│   └── result.html                 # Prediction result page
├── static/
│   └── style.css                   # Dark-themed responsive UI
└── specs/
    └── hdi-prediction/
        ├── requirements.md         # Project requirements
        ├── design.md               # Technical design
        └── tasks.md                # Implementation tasks
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/hdi-prediction.git
cd hdi-prediction
```

### 2. Create and activate virtual environment
```bash
python -m venv hdi_env

# Windows
hdi_env\Scripts\activate

# macOS / Linux
source hdi_env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### Option A — Run the Flask web app directly
> Use this if the model files already exist in `models/`

```bash
python app.py
```
Open your browser at **http://127.0.0.1:5000**

### Option B — Train the model first (Jupyter Notebook)
```bash
jupyter notebook
```
Open `hdi_prediction.ipynb` and run all cells top to bottom. This will:
- Perform EDA and visualization
- Preprocess the data
- Train the Linear Regression model
- Save model artifacts to `models/`

Then run `python app.py`.

---

## 🔍 How It Works

1. User enters 4 indicators on the web form
2. Flask passes inputs to the loaded model
3. Inputs are scaled using the saved `StandardScaler`
4. Linear Regression predicts the HDI score (0–1)
5. Score is mapped to a development tier
6. Result is displayed with a score bar and explanation

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Linear Regression |
| Features | Life Expectancy, Mean Years Schooling, Expected Years Schooling, GNI Per Capita |
| Target | HDI Score (continuous, 0–1) |
| Train/Test Split | 80% / 20% |
| Evaluation | R² Score, MSE, MAE |

---

## 💡 Example Inputs

| Country | Life Exp | Mean School | Exp School | GNI PPP | Expected Tier |
|---------|----------|-------------|------------|---------|---------------|
| Norway-like | 82.4 | 13.0 | 18.2 | 64,660 | Very High |
| Brazil-like | 76.2 | 10.5 | 14.8 | 18,000 | High |
| India-like | 68.5 | 6.8 | 11.2 | 6,500 | Medium |
| Low HDI | 54.3 | 3.2 | 7.5 | 1,800 | Low |

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| pandas, numpy | Data manipulation |
| matplotlib, seaborn | Visualization (EDA) |
| scikit-learn | ML model, preprocessing |
| flask | Web application |
| joblib | Model serialization |
| jupyter, notebook | Interactive development |

---

## 📁 Dataset

- **Source:** UNDP Human Development Report
- **File:** `data/hdi_dataset.csv`
- **Coverage:** 191 countries, multiple years
- **Key columns used:** Life Expectancy (2021), Mean Years of Schooling (2021), Expected Years of Schooling (2021), GNI Per Capita (2021), Human Development Groups

---

## 📄 License

This project is for educational purposes. Dataset sourced from [UNDP Human Development Reports](https://hdr.undp.org/).
