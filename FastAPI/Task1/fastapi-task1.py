from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from linkedlist_sort import LinkedList
from majority_element import majority_element

app = FastAPI()


# Pydantic Models
class MajorityElementModel(BaseModel):
    string: str = "0"

class BubbleSortModel(BaseModel):
    values: str = "0"
    ascending: bool = True

# Endpoints for Majority Element
@app.get("/majority-element")
def get_majority_element(string: str):
    try:
        result = majority_element(string)
        return {"majority_element": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/majority-element")
def post_majority_element(request: MajorityElementModel):
    try:
        result = majority_element(request.string)
        return {"majority_element": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoints for Bubble Sort
@app.get("/bubble-sort")
def get_bubble_sort(values: str, ascending: bool = True):
    try:
        values = list(map(int, values.strip().split(',')))
        ll = LinkedList()
        for val in values:
            ll.insertAtBeginning(val)
        ll.bubbleSort(ll.head, ascending)
        sorted_list = ll.displayLinkedList()
        return {"sorted_list": sorted_list}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/bubble-sort")
def post_bubble_sort(request: BubbleSortModel):
    try:
        values = list(map(int, request.values.strip().split(',')))
        ll = LinkedList()
        for val in values:
            ll.insertAtBeginning(val)
        ll.bubbleSort(ll.head, request.ascending)
        sorted_list = ll.displayLinkedList()
        return {"sorted_list": sorted_list}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


