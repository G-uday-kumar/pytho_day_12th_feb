account_balance=10000
withdrawal=int(input("enter amount to withdrawal it should be a multiple of 100:-"))
#remaining_balance=account_balance

if withdrawal<=account_balance:
    if withdrawal>=100 and withdrawal%100==0:
        print("amount is deducted:- ", withdrawal)
        account_balance=account_balance-withdrawal
        print("remaining balance=",account_balance)
    else:
        print("withdrawal is not possible")
else:
    print("insufficient balance")
