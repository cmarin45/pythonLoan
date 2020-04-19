from classes import credit
from classes.bankConditions import BankConditions


class loanType(BankConditions):

    ctypeList = []

    def choices(self):
        self.ctypeList = {1: 'Personal', 2: 'Auto', 3: 'Mortgage'}
        print("Please choose the type of the loan: ")
        print(self.ctypeList)
        choice = input("Choice: ")
        if choice is '1':
            credit.BankConditions.interest = 0.10
            print("Personal loan with 10% interest")
        elif choice is '2':
            credit.BankConditions.interest = 0.07
            print("Auto loan with 7% interest")
        elif choice is '3':
            credit.BankConditions.interest = 0.05
            print("Mortgage with 5% interest")
        else:
            print("Please choose option 1:Personal,2:Auto or 3:Mortgage")
