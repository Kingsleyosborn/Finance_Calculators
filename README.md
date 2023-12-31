# Finance_calculators

The user should be allowed to choose which calculation they want
to do. 
1 for investment
2 for bond

If the user selects ‘investment’, do the following:
■ Ask the user to input:
● The amount of money that they are depositing.
● The interest rate (as a percentage). Only the number
of the interest rate should be entered — don’t worry
about having to deal with the added ‘%’, e.g. The user
should enter 8 and not 8%.
● The number of years they plan on investing.
● Then ask the user to input if they want “simple” or
“compound” interest, and store this in a variable called
interest. Depending on whether or not they typed
“simple” or “compound”, output the appropriate
amount that they will get back after the given period,
at the specified interest rate. Look below for the
formula to be used:

Interest formula:
The total amount when simple interest is applied is calculated as
follows: A = P(1 + r * t)
The Python equivalent is very similar: A =P*(1+r*t)
The total amount when compound interest is applied is calculated as
follows: A = P(1 + r) ^ t
The Python equivalent is slightly different: A = P* math.pow((1+r),t)
In the formulae above:
● ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
then r is 0.08.
● ‘P’ is the amount that the user deposits.
● ‘t’ is the number of years that the money is being invested.
● ‘A’ is the total amount once the interest has been applied.

If the user selects ‘bond’, do the following:
■ Ask the user to input:
● The present value of the house. e.g. 100000
● The interest rate. e.g. 7
● The number of months they plan to take to repay the
bond. e.g. 120
Bond repayment formula:
The amount that a person will have to be repaid on a home loan each
month is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))
In the formula above:
● ‘P’ is the present value of the house.
● ‘i’ is the monthly interest rate, calculated by dividing the annual
interest rate by 12.
● ‘n’ is the number of months over which the bond will be repaid.
