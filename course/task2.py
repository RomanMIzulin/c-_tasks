from os import listdir

def readOne(file):
    lis = []
    with open(file,'rb') as f:
        
        while(True):
            t = f.read(1)
            if t =='':
                break
            else:
                lis.extend(t)
    return lis

def readFiles(direc):
    fileNames =  [f for f in listdir(direc)]
    return fileNames
l=[]

l.extend(readFiles('./pics'))
print(l)
print(readOne('./pics/'+l[0]))
print(l[0])


