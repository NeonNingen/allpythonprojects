studentResults = [ ['Name','HW1','HW2','HW3','HW4'],
                   ['Steven',8,7,9,4],
                   ['Lauren',7,9,8,6]
                   ]
header = studentResults[0]

for each in header:
    print('{0:8}'.format(each),end = '')

data = studentResults[1:4]
print('\n')


for a,b,c,d,e in data:
    print('{0:<8}{1:<8d}{2:<8d}{3:<8d}{4:<8d}'.format(a,b,c,d,e))
    
