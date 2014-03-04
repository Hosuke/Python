#MIT 6.00.1x Problem Set 1 Q2
#By Huang Geyang
#s = 'azcbobobegghakl'
i = 0
count = 0
for i in range(len(s)-2):
    subs = s[i:i+3]
    #print subs
    if subs == 'bob':
        count += 1
print 'Number of times bob occurs is: '+str(count)