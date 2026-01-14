import random


class Bank:
    
    __holder_details = []

    def create_acc(self):
        new_acc = {}

        print("""
            =====   Welcome Sir / Madam   =====
               """)

        new_acc["name"] = input("Enter Holder Name : ")
        age = int(input("Enter Holder Age : "))
        if age < 18:
            print("Come again After 18 Years .")
            return
        new_acc["age"] = age

        mobile = int(input("Enter Holder Mobile Number : "))
        if len(str(mobile)) != 10:
            print("May Given Mobile Number Invalide.")
            return
        new_acc["mobile"] = mobile

        pinn = int(input("Set Your Pin : "))
        if len(str(pinn)) != 4:
            print("Please Set Your Pin Only 4 Digits ")
            return
        new_acc["pin"] = pinn

        aadhar = int(input("Enter Holder Aadhar Number : "))
        if len(str(aadhar))!=12:
            print('Please Enter Valide Aadhar Number.')
            return
        new_acc["aadhar"] = aadhar

        new_acc["IFSC"]="SBIG0019"
        new_acc["account_number"]=random.randint(0000000000000,9999999999999)

        # accoutType
        print("Choice Account Type : ")
        print("                      1) Savings Account")
        print("                      2) Zero Balance Account")
        acctype = int(input("Option : "))
       

        while True:
            if acctype==1:
                print(("You Selected Saving Account So you have to Add Minimum Balance 1000rs : "))
                n1 = int(input("Enter Amount : "))
                if n1>=1000:
                    new_acc["balance"]=n1
                    break
                    
                else:
                    print("Please make Sure Minimum Amount 1000rs !")
                
            elif acctype==2:
                print("You Selected Zero Balance Account So you have to Add Minimum Balance 500rs : ")
                n2 = int(input("Enter Amount : "))
                if n2>=500:
                    new_acc["balance"]=n2
                    break
                else:
                    print("Please make Sure Minimum Amount 500rs !")
            else:
                print("Please Enter Valide Option ! ")
        Bank.__holder_details.append(new_acc)

        print("---  Your Account Created Successfully.   ---")

    def deposit(self):
        print("   ---   Amount Deposit   --- ")
        u_name = input("Enter User name : ")
        up = int(input("Enter Pin : "))
        for x in Bank.__holder_details:
            if x["name"]==u_name and x['pin']==up:
                dep = int(input("Enter Deposite Amount : "))
                if dep>0:
                    x["balance"]+=dep
                    print("Your Amount Creadited SuccessFully.")
                    return
                else:
                    print("Please Enter Valide Amount !")
                    return
                
                    
        print("Invalide User Details ! . ( If Your New User Please Create Account First.)")
                
        
    def withdraw(self):
        print('''   ---   Amount WithDraw   --- 
        ''')
        u_name = input("Enter User name : ")
        up = int(input("Enter Pin : "))
        for x in Bank.__holder_details:
            if x["name"]==u_name and x['pin']==up:
                dep = int(input("Enter WithDraw Amount : "))
                if dep>0 and x["balance"]>=dep:
                    x["balance"]-=dep
                    print("Your Amount debited SuccessFully.")
                    return
                else:
                    print("Please Enter Valide Amount !")
                    return
                
        print("Invalide User Details ! . ( If Your New User Please Create Account First.)")
                
        
    def check_balance(self):
        print('''   ---   Balance checking   --- 
        ''')
        u_name = input("Enter User name : ")
        up = int(input("Enter Pin : "))
        for x in Bank.__holder_details:
            if x["name"]==u_name and x['pin']==up:
                print("Your Current Balance is : ",x["balance"])
                return
        print("Invalide User Details ! . ( If Your New User Please Create Account First.)")

    def details(self):
        un = input("Enter User Name : ")
        up = int(input("Enter Pin : "))
        for x in Bank.__holder_details:
            if un==x['name'] and x['pin']==up:
                for a,b in x.items():
                    print(a,' : ',b)
                    return
        print("Invalid Details. Please Enter Details again !. ( If Your New User Please Create Account First.)")



obj = Bank()

while True:
    print("\n====== BANK MENU ======")
    print("1) Create Account")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Check Balance")
    print("5) Details")
    print("6) Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        obj.create_acc()
    elif choice == 2:
        obj.deposit()
    elif choice == 3:
        obj.withdraw()
    elif choice == 4:
        obj.check_balance()
    elif choice == 5:
        obj.details()
    elif choice == 6:
        print(" ===  Thank You for Banking With Us.  ===")
        break
    else:
        print("Please Enter a Valid Option")