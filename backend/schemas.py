from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    country: str
    home_country: str
    device_new: bool
    timestamp: datetime
