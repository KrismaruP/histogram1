#Establishing a file as a default hitting enter key
fname = input('Enter a file name: ')
if len(fname) < 1 : fname ='my-captain.txt'
hand = open(fname)


di = dict()
for lin in hand :
    #Taking the white spaces off the right hand side
    lin = lin.rstrip()
    print(lin)
    #Going horizontally across those lines
    wds = lin.split()
    print(wds)
    for w in wds :
        #Using the idiom .get to retrieve, create, update, counter
        di[w] = di.get(w,0) + 1
    print(di)

#Looking for the maximum and finding the most common word. Doing a maximum loop
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k
print(theword, largest)