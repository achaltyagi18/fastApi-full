from fastapi import FastAPI , Path ,HTTPException , Query

import json 
app = FastAPI()

@app.get("/")

def load_data():
    with open( 'patients.json' , 'r') as f:
        data = json.load(f)
    return data
def home():
    return{ " message " : " patient management system api "}

@app.get("/home")
def about():
    return { " message " : " a fully functional api to manage your patient recored "}


@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def patient_id(patient_id : str = Path(description = "tell the specific data" , example = " P005")):
    data = load_data()

    if patient_id in data :
        return data[patient_id]
    raise HTTPException(status_code= 404, detail= "Patient is not found ")

@app.get("/sort")
def sort_patients( sort_by: str = Query(..., description= "sort on the baes of height") , order: str = Query('asc' , description="sort in asc or dec") ):
    valid_fields = ["height" , " weight" , "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code= 400 , detail= f"Invalid field selected from the {valid_fields}" )

    if order not in ["asc" , " desc"]:
        raise HTTPException(status_code=400 , detail= " the order is not present in the asc or dec")

    data = load_data()

    