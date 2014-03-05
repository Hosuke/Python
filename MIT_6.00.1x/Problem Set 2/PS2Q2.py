#MIT 6.00.1x Problem Set 2 Q2
#By Huang Geyang

balance = 3329
annualInterestRate = 0.2

monthInterestRate = annualInterestRate / 12

for monthlyPaymentRate in range(10,balance,10):
    totalPaid = 0
    tempBalance = balance

    for i in range(1,13):
        totalPaid += monthlyPaymentRate
        tempBalance -= monthlyPaymentRate
        tempBalance += tempBalance*monthInterestRate

    if tempBalance <= 0 :
        break

print 'Lowest Payment: ' + str(monthlyPaymentRate)