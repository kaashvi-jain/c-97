def swap():
    file1= input("enter the file 1  ")
    file2= input("enter the file 2  ")
    f1=open(file1,'r')
    f2=open(file2,'r')
    data1=f1.read()
    data2=f2.read()
    f1=open(file1,'w')
    f1.write(data2)
    f2=open(file2,'w')
    f2.write(data1)
    f1.close()
    f2.close()
swap()