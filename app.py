#PyDantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Body, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import logic

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Models 
class Data(BaseModel):
    grade: int
    percentages: int


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/finalNote", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("finalNote.html", {"request": request})

@app.get("/finalRequired", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("finalRequired.html", {"request": request})

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
