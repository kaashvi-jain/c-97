import os 
import shutil
path = input("please enter the folder  ")
lof=os.listdir(path)
#print(lof)
for file in lof :
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext== '':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
