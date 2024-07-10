import requests
import pandas as pd
import joblib

# Step 1: Fetch the latest entry data from the API
def fetch_latest_entry(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            latest_entry = data[-1]  # Assuming the latest entry is the last in the list
            return latest_entry
        else:
            raise ValueError("Invalid data format received from API")
    else:
        raise ConnectionError(f"Failed to fetch data: Status code {response.status_code}")

# Step 2: Load the pre-trained machine learning model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Step 3: Prepare input data for prediction
def prepare_data_for_prediction(latest_entry):
    # Convert the latest entry to a DataFrame
    input_data = pd.DataFrame([latest_entry])
    # Example: if you need to scale features
    # scaler = joblib.load('scaler.pkl')
    # input_data_scaled = scaler.transform(input_data)
    return input_data

# Step 4: Make predictions
def make_predictions(model, input_data):
    predictions = model.predict(input_data)
    return predictions

if __name__ == "__main__":
    api_url = "https://api.yourservice.com/data"  # Replace with your API endpoint
    model_path = "C:\Users\Lenovo\Downloads\model.ipynb"

    try:
        latest_entry = fetch_latest_entry(api_url)
        model = load_model(model_path)
        input_data = prepare_data_for_prediction(lateages ast_entry)
        predictions = make_predictions(model, input_data)

        print("Predictions:", predictions)
    except Exception as e:
        print("An error occurred:", str(e))
