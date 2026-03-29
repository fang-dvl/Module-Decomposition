from typing import Dict
def open_account(balances: Dict[str, int], name: str, amount: int)-> None:
    balances[name] = amount

def sum_balances(accounts:  Dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int)-> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}
#missed balance argument, add balances
open_account(balances,"Tobi", 913)
#3rd argument is an int not a String and format as pence
open_account(balances,"Olya", 713)

total_pence = sum_balances(balances)
#wrong name of function
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")