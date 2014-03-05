#MIT 6.00.1x Problem Set 2 Q1
#By Huang Geyang

#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

monthInterestRate = annualInterestRate/12
totalPaid = 0

for i in range(1,13):
    print 'Month: ' + str(i)
    print 'Minimum monthly payment: ' + str(round(balance*monthlyPaymentRate,2))
    totalPaid += balance*monthlyPaymentRate
    balance -= balance*monthlyPaymentRate
    balance += balance*monthInterestRate
    print 'Remaining balance: ' + str(round(balance,2))

print 'Total paid: ' + str(round(totalPaid,2))
print 'Remaining balance: ' + str(round(balance,2))