from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def patients_data():
  with open('patients.json', 'r') as file:
    data = json.load(file)
  return data

# Endpoint GET /patients to retrieve the patients
@app.get("/patients")
def get_patients():
    try:
        data = patients_data()
        return data["patients"]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Patients data file not found.")


# Endpoint GET /patients/{id} to retrieve the patient by id
@app.get("/patients/{id}")
def get_patient_by_id(id: int):
    data = patients_data()
    patient = next((patient for patient in data["patients"] if patient["id"] == id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient