#Establishing a file as a default hitting enter key
fname = input('Enter a file name: ')
if len(fname) < 1 : fname ='my-captain.txt'
hand = open(fname)

for lin in hand :
    #Taking the white spaces off the right hand side
    lin = lin.rstrip()
    print(lin)
    #Going horizontally across those lines
    wds = lin.split()
    print(wds)
    for w in wds :
        #Making sure you are going through all the words
        print(w)