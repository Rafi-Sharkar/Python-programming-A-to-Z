# Data Encapsulation
import sys
class bank:
    def inpuddata(self):
        self.__acc = int(input("Enter your account no ::"))
        self.__bal = int(input("Enter balance ::"))
    def deposit(self):
        amt = int(input("Enter the amount of deposit ::"))
        self.__bal = self.__bal + amt
    def withdraw(self):
        amt = int(input("Enter the withdrawl amount ::"))
        self.__bal = self.__bal - amt
    def displaybalance(self):
        print(f"Account no {self.__acc}")
        print(f"Balance {self.__bal}")

cust = bank()
while True:
    print("-"*40)
    print("1. Input account detail")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display balance")
    print("5. Exit")
    print("-"*40)
    choice = int( input ("Enter your choice::"))
    if choice == 1:
        cust.inpuddata()
    elif choice == 2:
        cust.deposit()
    elif choice == 3:
        cust.withdraw()
    elif choice == 4:
        cust.displaybalance()
    elif choice == 5:
        continue      # i can also use  sys.exit() which work like  break function
    