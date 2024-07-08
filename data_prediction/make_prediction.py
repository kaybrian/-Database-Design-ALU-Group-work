def make_prediction(model, data):
    prediction = model.predict(data)
    return prediction

prediction = make_prediction(model, prepared_data)
print(f"Prediction: {prediction}")
