import requests
import pandas as pd
import pickle as pk 
import numpy as np
from sklearn.preprocessing import StandardScaler


# Step 1: Fetch the latest entry data from the API
def fetch_latest_entry(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            latest_entry = data[0]  
            return latest_entry
        else:
            raise ValueError("Invalid data format received from API")
    else:
        raise ConnectionError(f"Failed to fetch data: Status code {response.status_code}")




# Step 3: Prepare input data for prediction
def prepare_data_for_prediction(latest_entry):
    # Convert the latest entry to a DataFrame
    input_data = pd.DataFrame([latest_entry]).drop(columns=['_id', 'created_at'])

    # Convert DataFrame to NumPy array
    input_data_array = input_data.to_numpy()
     
    return input_data_array

# Step 4: Make predictions
def make_predictions(model, input_data):
    # Standardize the features
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(input_data)

            # Make a prediction
    prediction = model.predict(data_scaled)
    prediction = np.round(prediction).astype(int)
    prediction = prediction[0][0]

    return prediction

    
    # predictions = model.predict(input_data)
    # return predictions



if __name__ == "__main__":
    api_url = "http://localhost:8000/water_quality" 
    model_path = "./water_potability_model.pkl"

    # call api to get data  (step 1 )
    data = fetch_latest_entry(api_url)

    # Opening saved model step 2
    with open(model_path, "rb") as file:
        model = pk.load(file)
    
    # preparing data for prediction step 3
    mod_data = prepare_data_for_prediction(data)

    # make prediction step 4
    prediction = make_predictions(model, mod_data)

    # if the prediction is 1, the water is potable; otherwise, it is not potable
    if prediction == 1:
        prediction = "Potable"
    else:
        prediction = "Not Potable"
     


    print(prediction)


