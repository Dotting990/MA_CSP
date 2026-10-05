# MA, Functions Notes
def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"What is your monthly {money}:"))
            return amount
        except:
            print("That is not a number >:[")


# Write all your variables
income = stupid_prooof("income")
rent = stupid_proof("rent")
utilites = stupid_prooft("utilites")
groceries = stupid_proof("groceries")
transportation = stupid_proof("transportation")
savings = income * .1

# Write any functions you are using
def calc_precent(income, bill):
    return round(bill/income *100)

# Outputs for user
print(f"Your rent is ${rent:.2f} that is {stupid_prooof(income,rent)}% of your income.")
print(f"Your utilities is ${utilities:.2f} that is {stupid_prooof(income,utilites)}% of your income.")
print(f"Your groceries is ${groceries:.2f} that is {stupid_prooof(income,groceries)}% of your income.")
print(f"Your transportation is ${transportation:.2f} that is {stupid_prooof(income,transportation)}% of your income.")
print(f"Your savings is ${savings:.2f} that is {stupid_prooof(income,savings)}% of your income.")
print(f"You have $ {income-rent-utilities-groceries-transportation-savings:.2f} that ")