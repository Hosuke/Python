#By Huang Geyang

'''
The program works as follows: 
    you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
    The computer makes guesses, and you give it input - is its guess too high or too low? 
    Using bisection search, the computer will guess the user's secret number!
'''
print 'Please think of a number between 0 and 100!'

low = 0
high = 100
n=50

while True:
    print 'Is your secret number '+str(n)+'?'
    print "Enter 'h' to indicate the guess is too high.",
    print "Enter 'l' to indicate the guess is too low.",
    print "Enter 'c' to indicate I guessed correctly.",
    indicator = raw_input();
    if indicator == 'c':
        print 'Game over. Your secret number was: '+str(n)
        break
    elif indicator == 'l':
        low = n
        n = (low+high)/2
    elif indicator == 'h':
        high = n
        n = (low+high)/2
    else:
        print 'Sorry, I did not understand your input.'
        