def atm_operation(balance: int, action: str, amount: int) -> dict:
    if amount < 0:
        return {"Error": "Manfiy summa kiritish mumkin emas"}
    if action == "deposit":
        balance += amount
    elif action == "withdraw":
        if amount > balance:
            return {"Error": "Balans yetarli emas"}
        balance -= amount
    else:
        return {"Error": "Noto'g'ri amal"}
    return {"balance": balance}

print(atm_operation(100000, "deposit", 50000))   
print(atm_operation(100000, "withdraw", 20000))  
