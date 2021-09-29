def count():
    filename=input("enter the file  ")
    number=0
    f=open(filename,'r')
    for line in f :
        words=line.split()
        number= number+len(words)
    print("number of words  ",number)
count()    