from typing import Dict

# Function to open a new account where balances is a dictionary with 'string' keys (names) and integer values(pence).'name' of the new account holder as a string, and 'amount' is an integer (balance in pence).
def open_account(balances: Dict[str, int], name: str, amount: int) -> None:
    # Add, update account in the dictionary
    balances[name] = amount

# Function to sum of all balances in the account dictionary
def sum_balances(accounts: Dict[str, int]) -> int:
    total = 0
    # Loop through each name and balance 
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

# Function to format pence as a string
def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = total_pence // 100
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

# Balances dictionary with 'string' as a name and an 'integer' as a pence
balances: Dict[str, int] = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}
# Missed balances argument, added balances
open_account(balances, "Tobi", 913) 
# Pence must be integer, not a string and format as pences
open_account(balances, "Olya", 713)

total_pence = sum_balances(balances)

# Wrong name of the function, changed the name
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")