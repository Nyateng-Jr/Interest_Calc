def main():
    print("This is a monthly payment loan calculator" + "\n")

    principle = float(input("Enter the loan amount: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter years: "))

    monthly_interest_rate = apr / 1200
    months = years * 12
    monthly_payment = principle * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months))

    print("The monthly_payment of this loan is: %.2f" % monthly_payment)


main()