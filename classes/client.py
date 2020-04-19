class Client:
    # Initialize the Client class
    # with the client information
    # @param firstName: string    
    # @param lastName: string    
    # @param age: string    
    # @param income: string    
    # @param needToBorrow: string    
    def __init__(self, name, age, income, needToBorrow):
        self.name = name
        self.age = age
        self.income = income
        self.needToBorrow = needToBorrow

    # Method to print all information
    # related to that Client
    def printClientInfo(self):
        print('Name: ' + str(self.name))
        print('Age: ' + str(self.age))
        print('Income: ' + str(self.income))
        print('Need to borrow: ' + str(self.needToBorrow))

    # Methods to update the Client First and Last Name
    def updateClientName(self, name):
        self.name = name

    def updateClientAge(self, age):
        self.age = age

    # Method to update the Client Income
    # if for example the Client income will change
    # over time
    # @param newIncome: String
    def updateIncome(self, income):
        self.income = income

    # Method to update the Client needToBorrow
    # if the Client need will change
    # over time
    # @param newAmountToBorrow: String
    def updateBorrowNeed(self, needToBorrow):
        self.needToBorrow = needToBorrow
