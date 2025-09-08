# Asteroid Hazard Prediction ML Model

## Overview

This project is a machine learning application designed to predict whether an asteroid is hazardous based on various orbital and physical parameters. The model uses a Decision Tree Classifier trained on NASA's asteroid dataset to classify asteroids as "Hazardous" or "Non-Hazardous."

The project includes two interactive interfaces:
- A Flask-based web application for user-friendly predictions via a web form.
- A Streamlit application that provides model training insights, decision tree visualization, and real-time predictions.

## Features

- **Machine Learning Model**: Decision Tree Classifier for binary classification (Hazardous vs. Non-Hazardous).
- **Data Preprocessing**: Automated cleaning and feature selection from the NASA dataset.
- **Web Interfaces**: 
  - Flask app with HTML template for simple predictions.
  - Streamlit app with interactive widgets, model accuracy display, and decision tree visualization.
- **Deployment Ready**: Includes Dockerfile for containerization and deployed versions on Render and Streamlit Cloud.
- **User Input**: Accepts asteroid parameters like diameter, velocity, distance, etc., for predictions.

## Dataset

The model is trained on the [NASA Asteroids Classification Dataset](https://www.kaggle.com/datasets/shrutimehta/nasa-asteroids-classification) from Kaggle. The dataset includes features such as:
- Estimated Diameter (min/max)
- Relative Velocity
- Miss Distance
- Absolute Magnitude
- And more...

Irrelevant columns (e.g., Neo Reference ID, Name, Orbit ID) are dropped during preprocessing.

## Model Details

- **Algorithm**: Decision Tree Classifier (scikit-learn)
- **Hyperparameters**: max_depth=5, min_samples_split=10
- **Training Split**: 70% train, 30% test
- **Accuracy**: Displayed in the Streamlit app (typically around 90%+ based on the dataset)

The trained model is saved as `model.pkl` for use in the Flask app.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone or download the repository.
2. Navigate to the project directory:
   ```
   cd Asteroid-Prediction-ML-Model
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Ensure the following files are present:
   - `nasa.csv` (dataset)
   - `model.pkl` (pre-trained model)

## Usage

### Flask Web Application
1. Run the Flask app:
   ```
   python app.py
   ```
2. Open your browser and go to `http://localhost:5000`.
3. Fill in the asteroid parameters in the form and click "Predict" to get the result.

### Streamlit Application
1. Run the Streamlit app:
   ```
   streamlit run streamlit_app_1.py
   ```
2. The app will open in your browser.
3. View model accuracy, decision tree visualization, and make predictions using the sidebar inputs.

## Deployment

The project is deployed on:
- **Render**: [https://asteroid-prediction-ml-model.onrender.com](https://asteroid-prediction-ml-model.onrender.com)
- **Streamlit Cloud**: [https://asteroidpredictionmlmodel.streamlit.app](https://asteroidpredictionmlmodel.streamlit.app)

### Docker (Optional)
To run in a container:
1. Build the Docker image:
   ```
   docker build -t asteroid-prediction .
   ```
2. Run the container:
   ```
   docker run -p 5000:5000 asteroid-prediction
   ```
3. Access the Flask app at `http://localhost:5000`.

## Project Structure

```
Asteroid-Prediction-ML-Model/
├── app.py                    # Flask application
├── streamlit_app_1.py        # Streamlit application
├── model.pkl                 # Pre-trained model
├── nasa.csv                  # Dataset
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── templates/
│   └── index.html            # Flask HTML template
├── static/
│   └── style.css             # CSS for Flask app
├── Poster for the Project.pdf
├── Presentation of Project.pptx
└── README.md                 # This file
```

## Author

**Suryansh Ambekar**  
PRN: 202201090042
Mail: suryanshambekar@gmail.com



## Acknowledgments

- Kaggle for hosting the dataset.
- scikit-learn for the machine learning library.
