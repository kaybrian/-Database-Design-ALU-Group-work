from sys import implementation
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import database.py

app = FastAPI()

class WaterQuality(BaseModel):
    ph: float
    hardness: float
    solids: float
    chloramines: float
    sulfate: float
    conductivity: float
    organic_carbon: float
    trihalomethanes: float
    turbidity: float
    created_at: datetime = None

class Prediction(BaseModel):
    water_quality_id: str
    prediction: int
    created_at: datetime = None

@app.post('/water_quality', response_model=dict)
def add_water_quality(entry: WaterQuality):
    entry_id = database.add_water_quality(entry.dict())
    return {"message": "Water quality entry added", "id": entry_id}

@app.get('/water_quality', response_model=list)
def get_water_quality():
    entries = database.get_water_quality()
    return entries

@app.get('/water_quality/{id}', response_model=dict)
def get_water_quality_entry(id: str):
    entry = database.get_water_quality_entry(id)
    if entry:
        return entry
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

@app.put('/water_quality/{id}', response_model=dict)
def update_water_quality(id: str, entry: WaterQuality):
    updated_entry = database.update_water_quality(id, entry.dict())
    return {"message": "Water quality entry updated", "entry": updated_entry}

@app.delete('/water_quality/{id}', response_model=dict)
def delete_water_quality(id: str):
    success = database.delete_water_quality(id)
    if success:
        return {"message": "Water quality entry deleted"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

@app.post('/prediction', response_model=dict)
def add_prediction(entry: Prediction):
    entry_id = database.add_prediction(entry.dict())
    return {"message": "Prediction added", "id": entry_id}

@app.get('/prediction', response_model=list)
def get_predictions():
    entries = database.get_predictions()
    return entries

@app.get('/prediction/{id}', response_model=dict)
def get_prediction(id: str):
    entry = database.get_prediction(id)
    if entry:
        return entry
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

@app.put('/prediction/{id}', response_model=dict)
def update_prediction(id: str, entry: Prediction):
    updated_entry = database.update_prediction(id, entry.dict())
    return {"message": "Prediction updated", "entry": updated_entry}

@app.delete('/prediction/{id}', response_model=dict)
def delete_prediction(id: str):
    success = database.delete_prediction(id)
    if success:
        return {"message": "Prediction deleted"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")