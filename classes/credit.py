from classes.bankConditions import BankConditions


class Credit(BankConditions):
    # Initialize the Credit class
    # and extending the BankConditions Class
    # meaning BankConditions methods will be available
    # in the Credit class as well
    # with the client information
    # @param Client: Dictionary
    def __init__(self, income, needToBorrow, installments):
        self.income = income
        self.needToBorrow = needToBorrow
        self.installments = installments

    def printInfo(self):
        self.income = float(input('Income: '))
        self.needToBorrow = float(input('Need to borrow: '))

    def isClientEligible(self):
        try:
            while self.loanPeriod and self.installments is not None:
                return float(self.income) / float(self.installments) >= self.loanEligibilityLevel
        except AttributeError:
            print("Please set the loan period and monthly installments first! Option 2 and 5")

    def setLoanPeriod(self, loanPeriod):
        self.loanPeriod = loanPeriod

    def creditDetails(self):
        try:
            self.installments = float(round(self.needToBorrow * self.interest / (
                    12 * (1 - (1 + (self.interest / 12)) ** (-1 * self.loanPeriod))), 2))
            print("Client monthly installments: " + str(self.installments))
        except AttributeError:
            print("Please select option 2 to set the load period")
