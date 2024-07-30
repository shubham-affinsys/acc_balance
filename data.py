accounts =  [
    {"account_number": "HDFC10009234556", "balance": 500.75},
    {"account_number": "SBI00094567291", "balance": 1500.20},
    {"account_number": "YES10008282626", "balance": 250.00},
    {"account_number": "ACC10007802727", "balance": 3200.45},
    {"account_number": "KTK10098373628", "balance": 780.80}
]



users_by_id={
    "user_id_1":{
        "phone":"+91 1234322221",
        "cif":32323223,
        "accounts":{
            "HDFC1427987491378":{"balance":98383.63},
            "SBI8489203884932":{"balance":683937.51}
        }
    },
    "user_id_2":{
        "phone":"+91 1876556322",
        "cif":95857282,
        "accounts":{
            "PNB3877382920837":{"balance":73737.98},
            "SBI0475985847842":{"balance":6267292.75}
        }
    }
}

cif_to_user_id={
    32323223:"user_id_1",
    95857282:"user_id_2"
}

phone_to_user_id={
    "+91 1234322221":"user_id_1",
   "+91 1876556322":"user_id_2"
}

account_to_user_id={
    "HDFC1427987491378":"user_id_1",
    "SBI8489203884932":"user_id_1",
    "PNB3877382920837":"user_id_2",
    "SBI0475985847842":"user_id_2"
}
account_no="HDFC1427987491378"
print(users_by_id[account_to_user_id[account_no]]["accounts"][account_no]["balance"])