def main():
    print("This is a monthly payment loan calculator")
    print(" ")


    principal=float(input("Input the loan amount:"))
    apr=float(input("Input the annual interest rate:"))
    years=int(input("Amount of year:"))

    monthly_interest_rate=apr/1200
    amount_of_months=years*12
    payment=principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this loan is: %2.f"%payment)
main()