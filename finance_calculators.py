# This program allows the user to access two different financial calculators
# an investment calculator and a home loan repayment calculator
import math

#first, print out a statement about investment and bond

print("Choose either \'investment\' or \'bond\' from the menu below to proceed:\n")
print("investment -  to calculate the amount of interest you\'ll earn on your investment")
print("bond       -  to calculate the amount you\'ll have to pay on a home loan\n")

#make all the input become lower case, it is easier to later if statement
while True:
    invest_type = input("Please choose between investment or bond: ")
    invest_type = invest_type.lower()

    #error message shown here
    if invest_type != "bond" and invest_type != "investment":
        print("Error, please reenter.")
        continue
    #when the user choose investment
    elif invest_type == "investment":
        deposit = float(input("How much money are you depositing: "))
        interest_rate = float(input("What is the interest rate? eg 8%, please enter 8 : "))
        year = int(input("How many years do you plan on investing: "))
        interest = input("Do you prefer simple or compound interest? ")
        # choose which type of interest and calculation for each choice
        if interest == "simple":
            total = deposit * (1 + (interest_rate/100) * year)
            print(f"After {year} years, your total amount is {round(total, 2)} with a {interest_rate}% interest rate.")
        elif interest == "compound":
            total = deposit * math.pow((1 + interest_rate/100), year)
            print(f"After {year} years, your total amount is {round(total, 2)} with a {interest_rate}% interest rate.")

    # when the user choose bond
    elif invest_type == "bond":
        value = float(input("Please enter the value of the house: "))
        annual_interest_rate = float(input("What is the annual interest rate? eg 8%, please enter 8 : "))
        month_interest_rate = annual_interest_rate/12
        months = int(input("How many months do you plan to repay the bond: "))
        #bond calculation, i dont know why i cant use math.pow
        #repayment = ((month_interest_rate/100)* value)/(1-(1 + month_interest_rate/100)**(-months))
        repayment = ((month_interest_rate / 100) * value) / (1 - math.pow((1 + month_interest_rate / 100), (-months)))
        print(f"In {months} months, your monthly repaymnet is {round(repayment, 2)}", end="")
        print(f" with a {annual_interest_rate}% interest rate.")
