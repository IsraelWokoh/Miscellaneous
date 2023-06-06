class BankAccount:
    accounts = 0
    
    def __init__(self, account_no, forename, surname):
        BankAccount.accounts +=1
        self.account_no = account_no
        self.forename = forename
        self.surname = surname

    @ classmethod
    def getAccounts(cls):
        return BankAccount.accounts

    def getName(self):
        return self.forename + " " + self.surname

class Mortgage(BankAccount):
    def __init__(self, account_no, forename, surname, duration, loanAmount):
        self.duration = duration
        self.loanAmount = loanAmount
        BankAccount.__init__(self,account_no, forename, surname)

class Savings(BankAccount):
    balance = 0
    intRate = 0

    def mortgagePayment(self):
        paymentTry = False
        while not paymentTry
        try:
            amount = int(input('How much would you like to pay in?\n'))
            paymentTry = True
        except ValueError:
            print('Please enter a valid number.')
        self.balance += amount
        print(f'Your current balance is now: {balance}.')
 
if __name__ == "__main__":
   account1 = Mortgage("0189272","Charles","Hall",48,100000)
   account2 = Mortgage("1729239","Sasha","Miles",36,120000)
   print(BankAccount.getAccounts())
   print(account1.getName())

