def open_account(balances:dict[str, float], name:str, amount:float)-> None:
    balances[name] = amount

def sum_balances(accounts:dict[str, float])->float:
    total = 0.00
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence:float) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances = {
    "Sima": 7.00,
    "Linn": 5.45,
    "Georg": 8.31,
}

open_account(balances, "Tobi", 9.13)
open_account(balances, "Olya", 7.13)

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")