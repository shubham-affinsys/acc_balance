from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from data import accounts,users_by_id,phone_to_user_id,account_to_user_id,cif_to_user_id

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


class Account(BaseModel):
    balance: float

@app.get("/accounts")
def get_all_accounts():
    # return accounts
    all_accs = []
    for usr in users_by_id:
        accs = users_by_id[usr]["accounts"]
        for acc in accs:
            all_accs.append(acc)
    return all_accs


@app.get("/accounts/{account_number}")
def get_balance(account_number: str):
    for account in accounts:
        if account["account_number"] == account_number:
            return {"account_number": account_number, "balance": account["balance"]}
    raise HTTPException(status_code=404, detail="Account not found")



# create new account not using it
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
