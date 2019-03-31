class InsufficientFundsError(Exception):
    pass

bal=10000
amount=float(input("Enter Amount"))
if(bal<amount):
    try:
        raise InsufficientFundsError
    except(InsufficientFundsError):
        print("Balance is not sufficient")

    finally:
        print("Bye")

else:
    print("Transaction Success")

