accounts ={
    1001 : ["Zoro","24-03-2000","2406",10000],
    1002 : ["Sanji","12-02-1998","3121",20000],
    1003 : ["Franky","19-12-1199",None,10000],
    1004 : ["Brook","19-12-2002","1234",50000]
    }
print("Welcome !")
while True:
    print("*************************************")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. pin generation")
    print("4. mini statement")
    print("5. Exit")
    x=int(input("Enter your option: "))
    if x > 5:
        print("Choose the Correct option")
    else:
        if x == 1:
            account_no=int(input("Enter your Account number: "))
            if account_no not in accounts:
                print("Enter a vaild Account Number")
            else:
                if accounts[account_no][-2] is None:
                    print("First Generate Your Pin")
                else:                
                    pin=input("Enter Your pin: ")
                    if pin != accounts[account_no][-2]:
                        print("Please Enter Correct pin")
                    else:
                        amt=int(input("Enter Your amount: "))
                        if amt<=accounts[account_no][-1]:
                            accounts[account_no][-1] -= amt
                            print("Withdrawl Successful")
                        else:
                            print("Insufficient Balance")
        elif x == 2:
            account_no=int(input("Enter your Account number: "))
            if account_no not in accounts:
                print("Enter a vaild Account Number")
            else:
                amt=int(input("Enter Your Amount: "))
                amt+=accounts[account_no][-1]
                print("Money Added sucessfully")
            
        elif x == 3:
            account_no=int(input("Enter your Account number: "))
            if account_no not in accounts:
                print("Enter a vaild Account Number")
            else:
                if accounts[account_no][-2] is None:
                    pin=int(input("Enter your new pin: "))
                    confirm_pin=int(input("Re-Enter your New Pin: "))
                    if pin == confirm_pin:
                        accounts[account_no][-2] = pin
                        print("Pin Generated successfully")
                    else:
                        print("Re-enter Your Pin generation was unsucessful")
                else:
                    print("Your pin is already generated")
        elif x == 4:
            account_no=int(input("Enter your Account number: "))
            if account_no not in accounts:
                print("Enter a vaild Account Number")
            else:
                if accounts[account_no][-2] is None:
                    print("First Generate Your Pin")
                else:                
                    pin=input("Enter Your pin: ")
                    if pin != accounts[account_no][-2]:
                        print("Please Enter Correct pin")
                    else:
                        print(f"Account Number: {account_no}")
                        print(f"Name: {accounts[account_no][1]}")
                        print(f"DateofBirth: {accounts[account_no][2]}")
                        print(f"Balance amount: {accounts[account_no][-1]}")
        else:
            print("Thank You!\n Visit Again")
            break
print("*************************************")
    
