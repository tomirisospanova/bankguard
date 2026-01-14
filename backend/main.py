from fastapi import FastAPI
from schemas import Transaction
from fraud_engine import fraud_decision

app = FastAPI(title="BankGuard Anti-Fraud System")

@app.post("/transaction/check")
def check_transaction(tx: Transaction):
    result = fraud_decision(tx)
    return {
        "transaction_id": tx.transaction_id,
        "result": result
    }
