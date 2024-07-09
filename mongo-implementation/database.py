from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.water_quality_db

def add_water_quality(entry: dict):
    entry['created_at'] = datetime.utcnow()
    result = db.water_quality.insert_one(entry)
    return str(result.inserted_id)

def get_water_quality():
    entries = list(db.water_quality.find())
    for entry in entries:
        entry['_id'] = str(entry['_id'])
    return entries

def get_water_quality_entry(id: str):
    entry = db.water_quality.find_one({'_id': ObjectId(id)})
    if entry:
        entry['_id'] = str(entry['_id'])
    return entry

def update_water_quality(id: str, entry: dict):
    db.water_quality.update_one({'_id': ObjectId(id)}, {'$set': entry})
    return db.water_quality.find_one({'_id': ObjectId(id)})

def delete_water_quality(id: str):
    result = db.water_quality.delete_one({'_id': ObjectId(id)})
    return result.deleted_count > 0

def add_prediction(entry: dict):
    entry['created_at'] = datetime.utcnow()
    result = db.predictions.insert_one(entry)
    return str(result.inserted_id)

def get_predictions():
    entries = list(db.predictions.find())
    for entry in entries:
        entry['_id'] = str(entry['_id'])
        entry['water_quality_id'] = str(entry['water_quality_id'])
    return entries

def get_prediction(id: str):
    entry = db.predictions.find_one({'_id': ObjectId(id)})
    if entry:
        entry['_id'] = str(entry['_id'])
        entry['water_quality_id'] = str(entry['water_quality_id'])
    return entry

def update_prediction(id: str, entry: dict):
    db.predictions.update_one({'_id': ObjectId(id)}, {'$set': entry})
    return db.predictions.find_one({'_id': ObjectId(id)})

def delete_prediction(id: str):
    result = db.predictions.delete_one({'_id': ObjectId(id)})
    return result.deleted_count > 0
