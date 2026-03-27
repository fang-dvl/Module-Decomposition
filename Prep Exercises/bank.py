from typing import Dict

# balances is a Dict mapping account names(str) to balances (int)
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


balances: Dict[str, int] = {
    "Sima": 700,
    "Linn": 545,
    "George": 831,
}

open_account(balances, "Tobi", 913)
open_account(balances, "Ola", 713)

total_pence: int = sum_balances(balances)
total_string: str = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")
