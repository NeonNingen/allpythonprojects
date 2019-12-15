class Account:
    def __init__(self, accountNumber, openingDate, currentBalance, interestRate):
        self.accountNumber = accountNumber
        self.openingDate = openingDate
        self.currentBalance = currentBalance
        self.interestRate = interestRate

    def getAccountNumber(self):
        return self.accountNumber

    def getCurrentBalance(self):
        return self.currentBalance

    def addInterest(self):
        interest = self.currentBalance * self.interestRate
        self.currentBalance += interest

    def setInterestRate(self, interestRate):
        self.interestRate = interestRate


class Current(Account):
    def __init__(self, accountNumber, openingDate, currentBalance, interestRate, paymentType, overdraft):
        Account.__init__(self, accountNumber, openingDate, currentBalance, interestRate)
        self.paymentType = paymentType
        self.overdraft = overdraft

    def setPaymentType(self, paymentType):
        self.paymentType = paymentType

    def setOverdraft(self, overdraft):
        self.overdraft = overdraft

    def getOverdraft(self):
        return self.overdraft


a = Account("2121", "21/02/2002", 5000, 20.2)
print(a.getCurrentBalance())
