from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"phase": 0, "day": 3, "status": "ok"}
