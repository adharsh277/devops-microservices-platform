from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"service": "auth", "status": "up"}

@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "admin":
        return {"token": "fake-jwt-token"}
    return {"error": "invalid credentials"}
