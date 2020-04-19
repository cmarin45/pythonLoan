class BankConditions:
    # Bank conditions
    # for giving any loan
    # to any type of client
    interest = 0.09 
    openingTax = 20
    creditAnalysisTax = 30
    loanEligibilityLevel = 1.8
    currency = 'USD'

    # Method to print Bank conditions
    def printBankConditions(self):
        print('Interest: ' + str(self.interest * 100) + " %")
        print('Opening tax: ' + str(self.openingTax) + " " + self.currency)
        print('Credit analysis tax: ' + str(self.creditAnalysisTax) + " " + self.currency)
        print('Loan eligibility level: Installments = maximum ' + str(self.loanEligibilityLevel * 33) + " % of income")
