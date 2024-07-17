from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
dataset = {
    1: {
        'name': 'Sukanth',
        'reg_no': 50,
        'height': 170.0,
        'age': 20
    },
    2: {
        'name': 'Soorya',
        'reg_no': 45,
        'height': 165.45,
        'age': 21
    }
}

class Student(BaseModel):
    name : str | None = None
    reg_no : int | None = None
    height : float | None = None
    age : int | None = None

@app.get("/")
def home():
    return {"message":"This is homepage"}

@app.get("/student/{id}")
def get_data(id: int):
    if dataset.get(id):
        return dataset[id]
    else:
        raise HTTPException(status_code=404, detail="Data not Available")

@app.post("/student/{id}")
def add_data(id: int, obj: Student):
    if id not in dataset:
        dataset[id] = obj
        return {'message': 'Data Added Successfully',
                'dataset': dataset}
    else:
        raise HTTPException(status_code=404, detail="Data already available")
    
@app.put("/student/{id}")
def put_data(id: int, obj: Student):
    if id in dataset:
        dataset[id] = obj
        return {'message': 'Data Updated Successfully', 'dataset': dataset}
    else:
        raise HTTPException(status_code=404, detail="Data not Available")
    
@app.patch("/student/{id}")
def patch_data(id: int, obj: Student):
    if id in dataset:
        update_data = obj.model_dump(exclude_unset=True)
        dataset[id].update(update_data)
        return {'message': 'Data Updated in Patch Successfully', 'dataset': dataset}
    else:
        return HTTPException(status_code=404, detail="Data not Available")

    