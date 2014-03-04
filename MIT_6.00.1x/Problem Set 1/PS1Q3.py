#MIT 6.00.1x Problem Set 1 Q3
#By Huang Geyang

#s = 'zyxwvutsrqponmlkjihgfedcba'
i = 1
subs = s[0]
maxsubs = s[0]

while i < len(s):
    if s[i] >= subs[len(subs)-1] :
        subs = subs + s[i]
    else :
        subs = s[i]

    if len(subs) > len(maxsubs) :
        maxsubs = subs

    i+=1
    #print subs

print 'Longest substring in alphabetical order is: '+maxsubs