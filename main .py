balance=10000
transactions=[]

#check balance function
def check_balance():
    print("\nCurrent balance=",balance)
#deposit function
def deposit():
    global balance
    amount=int(input("Enter the amount you want to deposit="))
    balance+=amount
    transactions.append("Deposited="+str(amount))
    print("Amount deposited succesfully")
#withdraw function
def withdraw():
    global balance
    amount=int(input("Enter the amount you want to withdraw="))
    
    if amount<=balance:
        balance-=amount
        transactions.append("Withdawn="+str(amount))
        print("Collect your Cash")
    else:
        print("Insufficent balance")
#staement function
def statements():
    print("----History")
    if len(transactions)==0:
        print("No transcations yet")
    else:
        for t in transactions:
            print(t)
    

    
#main menu
while(True):
    print("\n-----ATM MENU-----")
    print("1.Check balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Statement")
    print("5.Exit")
    
    choice=int(input("Enter your choice="))
    
    if choice==1:
        check_balance()
    elif choice==2:
        deposit()
    elif choice==3:
        withdraw()
    elif choice==4:
        statements()
    elif choice==5:
        print("THANK YOU FOR USING ATM MACHINE")
        break
    else:
        print("Invalid choice...TRY AGAIN!!!")
