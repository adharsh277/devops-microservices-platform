from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

class Notification(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"service": "notifications", "status": "up"}

@app.post("/notify")
def send_notification(notification: Notification):
    time.sleep(2)  # simulate slow external system
    print(f"NOTIFICATION SENT: {notification.message}")
    return {"status": "sent"}
