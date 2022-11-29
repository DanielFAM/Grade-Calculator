#PyDantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Body
import logic

app = FastAPI()

# Models 
class Data(BaseModel):
    grade: list
    percentages: list


@app.get("/")
def home():
    return {"Hello" : "World"}

#request and response body

@app.post("/calculator/finalNote")
def final_notes(data: Data = Body(...)):

    grades = list(data.grade)
    percentages = list(data.percentages)

    return {"response":logic.nota_final(grades, percentages)}


@app.post("/calculator/missingNote")
def missing_note(data: Data = Body(...)):
    grades = list(data.grade)
    percentages = list(data.percentages)

    return {"response":logic.faltante_final(grades, percentages)}
