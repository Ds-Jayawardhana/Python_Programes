acc_num = 0

accounts = {
    77493843: {"balance_acc": 10000},
    20110159: {"balance_acc": 15000},
    41920784: {"balance_acc": 1000},
    16340262: {"balance_acc": 34000},
    27323237: {"balance_acc": 43567}
}

def balance():
    print("Account balance is $:", accounts[acc_num]["balance_acc"])

def withdraw():
    with_amount = int(input("Enter an Amount to withdraw:$ "))
    while with_amount > accounts[acc_num]["balance_acc"]:
        
        print("Sorry, You can't Withdraw Money")
        print("Withdraw amount should be less than Account Balance")
        with_amount = int(input("Enter an Amount to withdraw:$ "))
    accounts[acc_num]["balance_acc"]-=with_amount
def deposit():
    depo_amount = int(input("Enter an Amount to Deposit:$ "))
    accounts[acc_num]["balance_acc"]+=depo_amount

def main():
    global acc_num
    acc_num = int(input("Enter your account Number: "))
    while True:
        if acc_num in accounts:
            print("Enter option 1: To check the Balance")
            print("Enter option 2: To Withdraw Money")
            print("Enter option 3: To Deposit Money")
            print("Enter option 0: To exit The Programe")
            
            option = int(input("Choose one of the 4 Options: "))
            
            if option == 1:
                balance()
            elif option == 2:
                withdraw()
            elif option == 3:
                deposit()
            elif option==0:
                print("Exiting the programe....")
                exit()    
            else:
                print("Please Enter a Number between 1 and 3")
                continue
        else:
            print("Invalid account number. Please try again.")
            acc_num = int(input("Enter your account Number: "))
            continue

main()
