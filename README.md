A Comprehensive Measure of Well-Being (HDI Prediction)

Overview

This project leverages Machine Learning to predict the Human Development Index (HDI) based on key socio-economic indicators such as income, education, and life expectancy. The goal is to move beyond GDP-based rankings and provide a more comprehensive, data-driven measure of a country's well-being using a trained regression model.

The project follows a structured SDLC-style workflow — from ideation through deployment and demonstration — with each phase documented in its own folder.

Live Application

🔗 https://hdiproject.onrender.com

Key Features


Predictive Modeling – Trained regression model estimates HDI scores from socio-economic inputs.
User-Friendly Interface – Simple, responsive web form for entering indicator values.
Dynamic Results – Real-time prediction of HDI score and corresponding development category (Low / Medium / High / Very High).
Cloud Deployment – Fully deployed and publicly accessible via Render.


Tech Stack

LayerTechnologyModeling & AnalysisPython, Jupyter Notebook, Scikit-Learn, Pandas, NumPyBackendPython (Flask)FrontendHTML5, CSS3, JavaScriptDeploymentRender

Repository Structure

This repository documents the project across its full development lifecycle:

├── 1.Brainstorming & Ideation/     # Problem statement, idea generation
├── 2.Requirement Analysis/         # Functional & non-functional requirements
├── 3.Project Design Phase/         # Data flow diagrams, architecture, UI design
├── 4.Project Planning Phase/       # Sprint/milestone planning
├── 5.Project Development Phase/    # Model training notebooks & app code
├── 6.Project Testing/              # Test cases and validation results
├── 7.Project Documentation/        # Final project report and supporting docs
├── 8.Project Demonstration/        # Demo video / screenshots
└── README.md


Note: Model training and experimentation are primarily carried out in Jupyter Notebooks under the Development phase folder; the deployable web app (Flask backend + HTML/CSS frontend) is built from the resulting trained model.



Getting Started

Clone the repository:

bashgit clone https://github.com/uryapraveen/A-Comprehensive-Measure-of-Well-Being
cd A-Comprehensive-Measure-of-Well-Being

Explore the notebooks in the Development Phase folder to see the data preprocessing, model training, and evaluation steps. To run the web application locally, install the dependencies listed for the Flask app (see the Development Phase folder) and run:

bashpython app.py

Performance

The trained model achieved an R² score of 0.981, indicating high predictive accuracy against actual HDI values. The deployed application was stress-tested using Postman to confirm stable response times under concurrent load.
