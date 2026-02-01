from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import random
import time

app = FastAPI()

class PaymentRequest(BaseModel):
    order_id: str
    amount: float

class PaymentResponse(BaseModel):
    payment_id: str
    status: str

@app.get("/health")
def health():
    return {"service": "payments", "status": "up"}

@app.post("/pay", response_model=PaymentResponse)
def process_payment(payment: PaymentRequest):
    time.sleep(1)  # simulate processing delay
    status = random.choice(["success", "failed"])
    return {
        "payment_id": str(uuid.uuid4()),
        "status": status
    }
