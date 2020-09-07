import math, sys, argparse

if len(sys.argv) < 4:
    print('Incorrect parameters.')
else:
    parser = argparse.ArgumentParser()
    parser.add_argument('--type')
    parser.add_argument('--payment', type = int)
    parser.add_argument('--principal', type = int) 
    parser.add_argument('--periods', type = int)
    parser.add_argument('--interest', type = float)
    args = parser.parse_args()
    
def diff(periods, interest, principal):
    all_payment = 0
    for i in range(1, periods + 1):
        normal = interest / (12 * 100)
        D_i = principal / periods + normal * (principal - principal * (i - 1) / periods)
        print('Month ' + str(i) + ': paid out ' + str(int(math.ceil(D_i))))
        all_payment += math.ceil(D_i)
        
    over_payment = all_payment - principal
    print('Overpayment = ' + str(int(over_payment)))
        
def annual_principal(periods, payment, interest):
    i = interest / (12 * 100)
    P = payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    print('Your credit principal = ' + str(int(math.floor(P))) + '!')
    over_payment = payment * period - math.floor(P)
    print('Overpayment = ' + str(int(over_payment)))
    
def annual_periods(principal, payment, interest):
    M = payment
    P = principal
    nominal_interest = interest / (12 * 100)
    n = math.log(M / (M - P * nominal_interest), 1 + nominal_interest)
    n = int(math.ceil(n))
    if n == 1:
        print('You need ' + str(n) + ' month to repay the credit.')
    elif 1 < n < 12:
        print('You need ' + str(n) + ' months to repay the credit.')
    elif n == 12 :
        print('You need 1 year to repay the credit.')
    elif n % 12 == 0 and n != 12:
        print('You need ' + str(n // 12) + ' years to repay the credit.')
    elif n % 12 == 1:
        print('You need ' + str(n // 12) + ' years and 1 month to repay the credit')
    else:
        print('You need ' + str(n // 12) + ' years and ' + str(n % 12) + ' months to repay the credit')
    over_payment = payment * n - principal
    print('Overpayment = ' + str(int(over_payment)))
    
def annual_payment(principal, periods, interest):
    i = interest / (12 * 100)
    A = principal * (i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    print('Your annuity payment = ' + str(int(math.ceil(A))) + '!')
    over_payment = math.ceil(A) * periods - principal
    print('Overpayment = ' + str(int(over_payment)))
    
if args.type == 'annuity':
    if not (args.periods and args.payment and args.interest) is not None:
        if args.periods > 0 and args.payment > 0 and args.interest > 0:
            annual_principal(args.periods, args.payment, args.interest)
        else:
            print('Incorrect parameters')
    elif (args.principal and args.payment and args.interest) is not None:
        if args.principal > 0 and args.payment > 0 and args.interest > 0:
            annual_periods(args.principal, args.payment, args.interest)
        else:
            print('Incorrect parameters')
    elif (args.principal and args.periods and args.interest) is not None:
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            annual_payment(args.principal, args.periods, args.interest)
        else:
            print('Incorrect parameter')
    else:
        print('Incorrect parameter')
elif args.type == 'diff':
    if not args.payment:
        if args.periods > 0 and args.interest > 0 and args.principal > 0:
            diff(args.periods, args.interest, args.principal)
        else:
            print('Incorrect parameter')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')