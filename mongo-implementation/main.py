from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')
db = client.water_quality_db

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
    entry.created_at = datetime.utcnow()
    result = db.water_quality.insert_one(entry.dict())
    return {"message": "Water quality entry added", "id": str(result.inserted_id)}

@app.get('/water_quality', response_model=list)
def get_water_quality():
    entries = list(db.water_quality.find())
    for entry in entries:
        entry['_id'] = str(entry['_id'])
    return entries

@app.get('/water_quality/{id}', response_model=dict)
def get_water_quality_entry(id: str):
    entry = db.water_quality.find_one({'_id': ObjectId(id)})
    if entry:
        entry['_id'] = str(entry['_id'])
        return entry
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

@app.put('/water_quality/{id}', response_model=dict)
def update_water_quality(id: str, entry: WaterQuality):
    db.water_quality.update_one({'_id': ObjectId(id)}, {'$set': entry.dict()})
    return {"message": "Water quality entry updated"}

@app.delete('/water_quality/{id}', response_model=dict)
def delete_water_quality(id: str):
    result = db.water_quality.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return {"message": "Water quality entry deleted"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

@app.post('/prediction', response_model=dict)
def add_prediction(entry: Prediction):
    entry.created_at = datetime.utcnow()
    result = db.predictions.insert_one(entry.dict())
    return {"message": "Prediction added", "id": str(result.inserted_id)}

@app.get('/prediction', response_model=list)
def get_predictions():
    entries = list(db.predictions.find())
    for entry in entries:
        entry['_id'] = str(entry['_id'])
        entry['water_quality_id'] = str(entry['water_quality_id'])
    return entries

@app.get('/prediction/{id}', response_model=dict)
def get_prediction(id: str):
    entry = db.predictions.find_one({'_id': ObjectId(id)})
    if entry:
        entry['_id'] = str(entry['_id'])
        entry['water_quality_id'] = str(entry['water_quality_id'])
        return entry
    else:
        raise HTTPException(status_code=404, detail="Entry not found")

@app.put('/prediction/{id}', response_model=dict)
def update_prediction(id: str, entry: Prediction):
    db.predictions.update_one({'_id': ObjectId(id)}, {'$set': entry.dict()})
    return {"message": "Prediction updated"}

@app.delete('/prediction/{id}', response_model=dict)
def delete_prediction(id: str):
    result = db.predictions.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return {"message": "Prediction deleted"}
    else:
        raise HTTPException(status_code=404, detail="Entry not found")
