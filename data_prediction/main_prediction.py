import requests
import numpy as np
import joblib

# Step 1: Fetch Data from the API
def fetch_latest_entry(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        latest_entry = data[-1]  # Assuming the latest entry is the last in the list
        return latest_entry
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Step 2: Prepare Data for Prediction
def preprocess_data(data):
    # Example preprocessing steps
    feature_order = ['feature1', 'feature2', 'feature3']  # Replace with your feature names
    input_data = np.array([data[feature] for feature in feature_order])
    input_data = input_data.reshape(1, -1)  # Reshape for a single prediction
    return input_data

# Step 3: Load the Pre-trained Model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Step 4: Make Predictions
def make_prediction(model, data):
    prediction = model.predict(data)
    return prediction

# Main script
api_url = "https://example.com/api/latest"  # Replace with your API endpoint
model_path = "path/to/your/model.pkl"  # Replace with your model's path

latest_entry = fetch_latest_entry(api_url)
prepared_data = preprocess_data(latest_entry)
model = load_model(model_path)
prediction = make_prediction(model, prepared_data)

print(f"Prediction: {prediction}")
