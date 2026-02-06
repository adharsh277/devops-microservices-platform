from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List
import uuid
import requests

app = FastAPI()

# In-memory order store
orders = []

class Order(BaseModel):
    item: str
    quantity: int

class OrderResponse(Order):
    id: str

@app.get("/health")
def health():
    return {"service": "orders", "status": "up"}

@app.post("/orders", response_model=OrderResponse)
def create_order(order: Order):
    order_id = str(uuid.uuid4())
    new_order = {
        "id": order_id,
        "item": order.item,
        "quantity": order.quantity
    }
    orders.append(new_order)
    return new_order

@app.get("/orders", response_model=List[OrderResponse])
def list_orders():
    return orders


# 🔔 Background task helper (NEW for Day 5)
def send_notification(message: str):
    requests.post(
        "http://notifications-service:8004/notify",
        json={"message": message}
    )


# 🔽 UPDATED endpoint (Day 5 version)
@app.post("/orders-with-payment")
def create_order_with_payment(order: Order, background_tasks: BackgroundTasks):
    order_id = str(uuid.uuid4())

    order_data = {
        "id": order_id,
        "item": order.item,
        "quantity": order.quantity
    }
    orders.append(order_data)

    payment_response = requests.post(
        "http://payments-service:8003/pay",
        json={
            "order_id": order_id,
            "amount": 1000
        }
    )

    # 🔥 async background task
    background_tasks.add_task(
        send_notification,
        f"Order {order_id} processed with payment status {payment_response.json().get('status')}"
    )

    return {
        "order": order_data,
        "payment": payment_response.json(),
        "notification": "scheduled"
    }
