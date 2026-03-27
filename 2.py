from typing import Dict, Union

def open_account(balances: Dict[str, int], name: str, amount: Union[int, float, str]) -> None:
    if isinstance(amount, str) and amount.startswith("£"):
        pounds, pence = map(int, amount[1:].split("."))
        amount = pounds * 100 + pence
    elif isinstance(amount, float):
        amount = int(round(amount * 100))
    elif isinstance(amount, int):
        pass
    else:
        raise ValueError("Unsupported amount format")
    balances[name] = amount

def sum_balances(accounts: Dict[str, int]) -> int:
    total: int = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds: int = total_pence // 100
    pence: int = total_pence % 100
    return f"£{pounds}.{pence:02d}"

# Main block
balances: Dict[str, int] = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances, "Tobi", 9.13)       # float input
open_account(balances, "Olya", "£7.13")    # string input

total_pence: int = sum_balances(balances)
total_string: str = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")
