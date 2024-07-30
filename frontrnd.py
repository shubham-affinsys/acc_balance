import requests    
url = f"https://acc-balance.vercel.app/accounts/{1004}"
response = requests.get(url)

data = response.json()
slot_balance = data["balance"]
print(slot_balance)