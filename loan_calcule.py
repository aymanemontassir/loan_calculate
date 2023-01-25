import math as m
loan_principale = 0 
monthly_price = 0
months = 0

def set_loan_principale(value):
    loan_principale = value


def get_months_left(loan, monthly_payment):
    return round((loan / monthly_price))


def get_monthly_price(loan,months):
    return round(loan/months)

# def set_monthly_price(value):
#     monthly_price = value

def run():
    loan_principale = input("Enter the loan principal:")
    set_loan_principale(loan_principale)
    questions()
    if input() == "m":
        result = calcul_months_left(loan_principale)
        return result
    elif input() == "p":
        result = calcul_monthly_payment(loan_principale)
        return result

def calcul_monthly_payment(loan):
    ml = input("Enter the number of months:")
    return round(get_monthly_price(loan,ml))    
    
def calcul_months_left(loan):
    mp = input("enter the monthly payment:")
    return get_months_left(loan,mp)

def questions():
    print("What do you want to calculate?")
    print('type "m" for number of monthly payments,')
    print('type "p" for the monthly payment:')

    run()