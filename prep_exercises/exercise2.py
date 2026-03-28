from typing import Dict

def open_account(balances: Dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount

def sum_balances(accounts: Dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = total_pence // 100
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

# All balances are in pence
balances: Dict[str, int] = {
    "Sima": 700,   # £7.00
    "Linn": 545,   # £5.45
    "Georg": 831,  # £8.31
}

# Add new accounts (amounts in pence)
open_account(balances, "Tobi", 913)  # £9.13
open_account(balances, "Olya", 713)  # £7.13

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")
