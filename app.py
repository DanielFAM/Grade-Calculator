from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello" : "World"}

def run():
    pass

if __name__ == "__main__":
    pass