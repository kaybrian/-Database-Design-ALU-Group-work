import numpy as np

def preprocess_data(data):
    # Example preprocessing steps
    # Assuming data is a dictionary and your model expects a numpy array with specific features
    feature_order = ['feature1', 'feature2', 'feature3']  # Replace with your feature names
    input_data = np.array([data[feature] for feature in feature_order])
    input_data = input_data.reshape(1, -1)  # Reshape for a single prediction
    return input_data

prepared_data = preprocess_data(latest_entry)
print(prepared_data)
