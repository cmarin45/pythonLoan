import datetime
import sys
from classes.client import Client
from classes.credit import Credit
from classes.creditType import loanType

now = datetime.datetime.now()
line = '-'*50
options = {'[1]': "Determine if client is eligible", '[2]': "Set Loan Period", '[3]': "Client Info",
           '[4]': "Bank Conditions", '[5]': "Client Installments", '[6]': "Update Client Name",
           '[7]': "Update Client Age", '[8]': "Update Client Income", '[9]': "Update Client Amount to Borrow",
           '[0]': "Exit Program"}

def getClientData():
    print(line)
    print('Credit Loan Application')
    print(line)
    print('Today: ' + now.strftime("%Y-%m-%d %H:%M"))
    print(line)
    print('Please input the needed information below! ')
    print(line)
    name = input('Client name: ')
    age = int(input('Client age: '))
    income = int(input('Client income: '))
    needToBorrow = int(input('Client need to borrow: '))
    return {
            'name': name,
            'age': age,
            'income': income,
            'needToBorrow': needToBorrow
        }


def printActionOptions():
    print(line)
    print('Please select an option to continue')
    print('To select an option just type the option number, i.e. 6, and press enter')
    print(line)
    print('\n'.join("{}: {}".format(k, v) for k, v in options.items()))
    print(line)
    option = input('Select an option: ')
    continueProgram(option)


def continueAction():
    print('Type b to go back, anything else to exit')
    goBack = input('Go back? ')

    if (goBack == 'b'):
        print('Return to option choise')
        printActionOptions()
    else:
        print('Exit program...')
        sys.exit()


def caseOption_1(option):
    if option == '1':
        eligibility = credit.isClientEligible()
        if (eligibility):
            levelOfIndebtness = float(clientData['income']) / float(clientData['needToBorrow'])
            print(line)
            print(clientData['name'] + ' is eligible with a level of indebtness of ' + "{0:.2f}".format(
                levelOfIndebtness) + " %")
            continueAction()
        else:
            print(line)
            print('Sorry, ' + clientData['name'] + ' is not eligible!')
            continueAction()


def caseOption_2(option):
    if (option == '2'):
        try:
            loanPeriod = float(input('Client loan period should be (in months): '))
            credit.setLoanPeriod(loanPeriod)
        except ValueError:
            print("Loan period should be only numbers, try again")
        continueAction()


def caseOption_3(option):
    if (option == '3'):
        print(line)
        client.printClientInfo()
        print(line)
        continueAction()


def caseOption_4(option):
    if (option == '4'):
        print(line)
        credit.printBankConditions()
        print(line)
        continueAction()


def caseOption_5(option):
    if (option == '5'):
        print(line)
        ctype.choices()
        credit.creditDetails()
        print(line)
        continueAction()


def caseOption_6(option):
    if (option == '6'):
        print(line)
        try:
            name = str(input('Client name: '))
            if name.isalpha():
                client.updateClientName(name)
            else:
                raise TypeError
        except TypeError:
            print("The name should contain only characters, try again")
        print(line)
        continueAction()


def caseOption_7(option):
    if (option == '7'):
        print(line)
        try:
            age = int(input('Client Age: '))
            client.updateClientAge(age)
        except ValueError:
            print("The age should be between 18 and 65, try again")
        print(line)
        continueAction()


def caseOption_8(option):
    if (option == '8'):
        print(line)
        try:
            income = int(input('Client Income: '))
            client.updateIncome(income)
        except ValueError:
            print("The income should be numerical")
        print(line)
        continueAction()


def caseOption_9(option):
    if (option == '9'):
        print(line)
        try:
            needToBorrow = int(input('Client need to borrow: '))
            client.updateBorrowNeed(needToBorrow)
        except ValueError:
            print("The borrow value should be numerical")
        print(line)
        continueAction()


def continueProgram(option):
    if (option == '0'):
        print('Closing application...')
        print('Aplication closed.')
        sys.exit()
    else:
        caseList = (caseOption_1(option), caseOption_2(option), caseOption_3(option), caseOption_4(option),
                    caseOption_5(option), caseOption_6(option), caseOption_7(option), caseOption_8(option),
                    caseOption_9(option))
        for option in range(1, 10):
            return caseList[option]


# Start the program
clientData = getClientData()

# create a new instace of the Client and Credit class
client = Client(clientData['name'], clientData['age'], clientData['income'], clientData['needToBorrow'])
credit = Credit(clientData['income'], clientData['needToBorrow'], caseOption_5('installments'))
ctype = loanType()

printActionOptions()
