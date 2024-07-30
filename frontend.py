import requests    
import pprint

url = f"https://acc-balance.vercel.app/users/user_id_1"
response = requests.get(url).json()

accounts=[]
for acc in response["accounts"]:
    account = dict()
    account["title"] = acc
    account["payload"] = acc
    account["balance"] = response["accounts"][acc]["balance"]
    #adding account to list
    accounts.append(account)

pprint.pprint(accounts)
# pprint.pprint(accounts)
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