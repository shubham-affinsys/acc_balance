from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
#deployed on https://acc-balance.vercel.app/
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory data store
accounts = [
    {
        "title": "101xxxx1001",
        "account_no": "1001",
        "balance": 892322.03,
        "payload": 1001,
        "type": "payload"
    },
    {
        "title": "101xxxx1002",
        "account_no": "1002",
        "balance": 4363.02,
        "payload": 1002,
        "type": "payload"
    },
    {
        "title": "101xxxx1003",
        "account_no": "1003",
        "balance": 4662.02,
        "payload": 1003,
        "type": "payload"
    },
    {
        "title": "101xxxx1004",
        "account_no": "1004",
        "balance": 8903.56,
        "payload": 1004,
        "type": "payload"
    },
    {
        "title": "101xxxx1005",
        "account_no": "1005",
        "balance": 234.4,
        "payload": 1005,
        "type": "payload"
    },
    {
        "title": "101xxxx1006",
        "account_no": "1006",
        "balance": 765.54,
        "payload": 1006,
        "type": "payload"
    },
]

class Account(BaseModel):
    balance: float

@app.get("/accounts")
def get_all_accounts():
    return accounts

@app.get("/accounts/{account_number}")
def get_balance(account_number: str):
    for account in accounts:
        if account["account_no"] == account_number:
            return {"account_number": account_number, "balance": account["balance"]}
    raise HTTPException(status_code=404, detail="Account not found")

@app.post("/accounts/{account_number}")
def create_account(account_number: str, account: Account):
    if any(acc["account_no"] == account_number for acc in accounts):
        raise HTTPException(status_code=400, detail="Account already exists")
    new_account = {
        "title": f"101xxxx{account_number[-4:]}",
        "account_no": account_number,  
        "balance": account.balance,
        "payload": account_number,
        "type": "payload"
    }
    accounts.append(new_account)
    return {"message": "Account created", "account_number": account_number, "balance": account.balance}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
