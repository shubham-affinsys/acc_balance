import requests    
import pprint
url = f"https://acc-balance.vercel.app/accounts/"
response = requests.get(url)

data = response.json()
accounts=[]
for data_acc in data:
    account=dict()
    account["title"] = data_acc["account_number"]
    account["balance"] = data_acc["balance"]
    account["payload"] = data_acc["account_number"]

    accounts.append(account)

pprint.pprint(accounts)



    #make request to server to get account balance 
    #account balnce is already stored in slot_accounts
    # try:
    #     url = f"https://acc-balance.vercel.app/accounts/{slot_account_no}"
    #     response = requests.get(url)
    #     data = response.json()
    #     if "balance" in data.keys():
    #         slot_balance = data["balance"]
    #     else:
    #         slot_balance = "not found"
    # except Exception as e:
    #     logging.error("Error occured while fetching account balance"+e)