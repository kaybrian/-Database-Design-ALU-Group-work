import joblib

def load_model(model_path):
    model = joblib.load(model_path)
    return model

model_path = "path/to/your/model.pkl"  # Replace with your model's path
model = load_model(model_path)
