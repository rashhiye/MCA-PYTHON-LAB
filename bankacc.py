class BankAccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount}deposite new balance{self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} withdraw\n remaining balance:{self.balance}")
        else:
            print("insufficiant amount")
    def display(self):
        print(f"account holder:{self.name} \n balance:{self.balance}")
    
    

acc=BankAccount("Allen",1000)
acc.display()
acc.deposit(500)
acc.withdraw(100)
