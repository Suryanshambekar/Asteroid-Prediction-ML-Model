from flask import Flask, request, render_template
import pickle
import pandas as pd

# Load the model
model = pickle.load(open("model.pkl", "rb"))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prediction_text=None)  # Pass None for first load

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint for making predictions.
    Accepts form input from the website.
    """
    try:
        # Get form data from the request
        data = request.form
        
        # Extract feature values into a dictionary
        input_data = {key: float(value) for key, value in data.items()}
        
        # Convert the dictionary to a DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Make predictions
        prediction = model.predict(input_df)
        
        # Map prediction to human-readable output
        result = "Hazardous" if prediction[0] else "Not Hazardous"
        
        return render_template('index.html', prediction_text=f'The asteroid is: {result}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

