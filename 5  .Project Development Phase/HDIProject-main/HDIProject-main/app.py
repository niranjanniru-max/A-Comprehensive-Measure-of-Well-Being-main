from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load model artifacts once at startup
model   = joblib.load('models/hdi_model.pkl')
scaler  = joblib.load('models/scaler.pkl')
le      = joblib.load('models/label_encoder.pkl')

def classify_hdi(score):
    """Convert predicted HDI score to a human development tier."""
    if score >= 0.800:
        return 'Very High'
    elif score >= 0.700:
        return 'High'
    elif score >= 0.550:
        return 'Medium'
    else:
        return 'Low'

def get_tier_info(tier):
    """Return description and color class for each tier."""
    info = {
        'Very High': {
            'color': 'very-high',
            'emoji': '🌟',
            'description': 'This country ranks among the most developed nations with strong health, education, and income indicators.'
        },
        'High': {
            'color': 'high',
            'emoji': '✅',
            'description': 'This country demonstrates strong human development with good performance across most indicators.'
        },
        'Medium': {
            'color': 'medium',
            'emoji': '📈',
            'description': 'This country is developing. Targeted improvements in healthcare, education, or income could significantly boost its HDI.'
        },
        'Low': {
            'color': 'low',
            'emoji': '⚠️',
            'description': 'This country faces significant development challenges. Investments in health, education, and economic growth are critical.'
        }
    }
    return info.get(tier, info['Low'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        life_expectancy          = float(request.form['life_expectancy'])
        mean_years_schooling     = float(request.form['mean_years_schooling'])
        expected_years_schooling = float(request.form['expected_years_schooling'])
        gni_per_capita           = float(request.form['gni_per_capita'])

        # Validate ranges
        if not (20 <= life_expectancy <= 90):
            raise ValueError('Life expectancy must be between 20 and 90 years.')
        if not (0 <= mean_years_schooling <= 20):
            raise ValueError('Mean years of schooling must be between 0 and 20.')
        if not (0 <= expected_years_schooling <= 25):
            raise ValueError('Expected years of schooling must be between 0 and 25.')
        if not (100 <= gni_per_capita <= 200000):
            raise ValueError('GNI per capita must be between 100 and 200,000.')

        features = pd.DataFrame([[life_expectancy, mean_years_schooling,
                                   expected_years_schooling, gni_per_capita]],
                                 columns=['Life_Expectancy', 'Mean_Years_Schooling',
                                          'Expected_Years_Schooling', 'GNI_Per_Capita'])
        scaled      = scaler.transform(features)
        hdi_score   = model.predict(scaled)[0]
        hdi_score   = round(float(np.clip(hdi_score, 0, 1)), 3)
        tier        = classify_hdi(hdi_score)
        tier_info   = get_tier_info(tier)

        return render_template('result.html',
            hdi_score   = hdi_score,
            tier        = tier,
            color       = tier_info['color'],
            emoji       = tier_info['emoji'],
            description = tier_info['description'],
            life_expectancy          = life_expectancy,
            mean_years_schooling     = mean_years_schooling,
            expected_years_schooling = expected_years_schooling,
            gni_per_capita           = gni_per_capita
        )

    except ValueError as e:
        return render_template('index.html', error=str(e))
    except Exception as e:
        return render_template('index.html', error='Something went wrong. Please check your inputs.')

if __name__ == '__main__':
    app.run(debug=True)
