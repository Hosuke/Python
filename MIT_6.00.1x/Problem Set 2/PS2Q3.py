#MIT 6.00.1x Problem Set 2 Q3
#By Huang Geyang

balance = 999999
annualInterestRate = 0.18

monthInterestRate = annualInterestRate / 12.0
low = balance / 12
high = (balance * (1 + monthInterestRate) ** 12) / 12.0
epsilon = 0.01

while True :
    totalPaid = 0
    tempBalance = balance
    monthlyPaymentRate = (low + high) / 2.0

    for i in range(1,13):
        totalPaid += monthlyPaymentRate
        tempBalance -= monthlyPaymentRate
        tempBalance += tempBalance*monthInterestRate

    if (tempBalance-0)**2 <= epsilon :
        break
    elif tempBalance < 0 :
    	high = monthlyPaymentRate
    else :
    	low = monthlyPaymentRate

print 'Lowest Payment: ' + str(round(monthlyPaymentRate,2))