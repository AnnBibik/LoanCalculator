import math
import argparse
import inspect

parser = argparse.ArgumentParser()
parser.add_argument('-i1', '--type', type=str, choices=['annuity', 'diff'])
parser.add_argument('-i2', '--principal', type=int)
parser.add_argument('-i3', '--periods', type=int)
parser.add_argument('-i4', '--interest', type=float)
parser.add_argument('-i5', '--payment', type=int)

args = parser.parse_args()
arguments = [args.type, args.principal, args.periods, args.interest, args.payment]


def calculate_interest_rate(loan_interest):
    return loan_interest / (12 * 100)


def calculating_differentiated_paymants(principal, periods, interest):
    sum_of_payment = 0
    nominal_interest_rate = calculate_interest_rate(interest)
    for month in range(1, periods + 1):
        result = math.ceil(
            principal / periods + nominal_interest_rate * (principal - (principal * (month - 1)) / periods))
        sum_of_payment += result
        print(f'Month {month}: payment is {result}')
    if sum_of_payment > principal:
        overpayment = sum_of_payment - principal
        print(f'Overpayment = {overpayment}')


def get_loan_principal(payment, periods, interest):
    nominal_interest_rate = calculate_interest_rate(interest)

    loan_principal = round(payment / (
            (nominal_interest_rate * math.pow(1 + nominal_interest_rate, periods)) / (
            math.pow(1 + nominal_interest_rate, periods) - 1)))

    print(f'Your loan principal = {loan_principal}!')

    if (payment * periods) > loan_principal:
        overpayment = payment * periods - loan_principal
        print(f'Overpayment = {overpayment}')


def convert_month_to_year(months):
    if months == 1:
        print(f'It will take {months} month to repay this loan!')
    elif 1 < months <= 12:
        print(f'It will take {months} months to repay this loan!')
    elif months > 12:
        year = int(months / 12)
        months = math.ceil(months - year * 12)
        print(f'It will take {year} years and {months} months to repay this loan!')


def get_monthly_payments(principal, payment, interest):
    nominal_interest_rate = calculate_interest_rate(interest)
    res = payment / (payment - nominal_interest_rate * principal)
    number_of_month = math.ceil(math.log(res, 1 + nominal_interest_rate))
    convert_month_to_year(number_of_month)
    if payment * number_of_month > principal:
        overpayment = payment * number_of_month - principal
        print(f'Overpayment = {overpayment}')


def get_annuity_montly_payment(principal, periods, interest):
    nominal_interest_rate = calculate_interest_rate(interest)
    annyity_paiment = math.ceil(
        principal * ((nominal_interest_rate * (1 + nominal_interest_rate) ** periods) / (
                ((1 + nominal_interest_rate) ** periods) - 1)))
    print(f'Your monthly payment = {annyity_paiment}!')


def is_function_args_less_four(func):
    if len(inspect.getfullargspec(func)) < 4:
        print('Incorrect parameters')
        return


if args.type == 'diff':
    is_function_args_less_four(calculating_differentiated_paymants)
    if args.interest is None:
        print('Incorrect parameters')
    elif args.payment is not None:
        print('Incorrect parameters')
    else:
        calculating_differentiated_paymants(int(args.principal), int(args.periods), float(args.interest))
elif args.type == 'annuity':
    is_function_args_less_four(get_loan_principal)
    if args.interest is None:
        print('Incorrect parameters')
    elif args.principal is None:
        get_loan_principal(int(args.payment), int(args.periods), float(args.interest))
    elif args.periods is None:
        is_function_args_less_four(get_monthly_payments)
        get_monthly_payments(int(args.principal), int(args.payment), float(args.interest))
    elif args.payment is None:
        is_function_args_less_four(get_annuity_montly_payment)
        get_annuity_montly_payment(int(args.principal), int(args.periods), float(args.interest))
else:
    print('Incorrect parameters')
