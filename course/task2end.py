import numpy as np
from scipy.stats import chi2
from scipy.stats import chisquare 
from scipy.stats import chi2_contingency as c2 
from bitstring import BitArray as bt
import os
import sys
import matplotlib.pyplot as plt
# bin(int.from_bytes(t.encode(), 'little'))
BYTE_READ=1
def readOne(file):
    lis = list()
    with open(file,'rb') as f:
        lis=[]
        while(True):
            t = f.read(BYTE_READ)
            if t!=b'':
                lis.append(t)
            else:
                break
    return lis

def readFiles(direc):
    d = dict()
    fileNames =  [f for f in os.listdir(direc)]
    for i in fileNames:
        d.update({i:readOne(direc+'/'+i)})
    return d

def emPlot(dic,n):
    lx =[]
    ly=[]
    for key,value in dic.items():
        lx.append(bin(int.from_bytes(key,byteorder='little')))
        ly.append(value)
    ly=np.array(ly)/n
#    for i in (range(1,len(ly))):
#        ly[i]+=ly[i-1]
    plt.plot(lx,ly)
    plt.show()

def analyseOne(lis):
    n = len(lis)
    s = sorted(set(lis))
    d = dict()
    for i in s:
        count = 0
        for j in lis:
            if j<=i:
                count = count+1
        d.update({i:count})
    return d,n



def mean(lis):
    summ = 0
    for i in lis:
        summ +=int.from_bytes(i,byteorder='little')
    return summ/len(lis)


def desp(lis):
    summ = 0
    for i in lis:
        summ +=(int.from_bytes(i,byteorder='little')**2)
    return summ/len(lis)-mean(lis)**2

def showAll(dic):
    ordered  = sorted(dic.items(), key=lambda kv:kv[0])
    global BYTE_READ
    b = BYTE_READ
    BYTE_READ = b*8
    chil=chi2.ppf(0.05,2**BYTE_READ)
    chih=chi2.ppf(0.95,2**BYTE_READ)
    print('name',' ','mean',' ','desp', ' ','chi2',' ','0.05',' ','0.95')
#     f=open('out.txt','a+')
    for i in ordered:
        if BYTE_READ>1:
            print(i[0],' ',format(mean(i[1]),'.2e'), ' ', format(desp(i[1]),'.2e'),' ',Chi((dic[i[0]])),' ',chil,' ',chih)
        else:
            print(i[0],' ',(mean(i[1])), ' ', (desp(i[1])),' ',Chi((dic[i[0]])),' ',chil,' ',chih)
#     for key,value in dic.items():
#         print(key,' ',format(mean(value),'.2e'), ' ', format(desp(value),'.2e'))
    
def pj(a,b,n):
    print(a,' ',b)
    return (int.from_bytes(b,byteorder='little')-int.from_bytes(a,byteorder='little'))/n

def H0(data,k):
    siz = len(data)
    data.sort()
    print(siz)
    print(data[:50])
    n = 1
    l= []
    if siz%k == 0:
        n=siz//k
        for i in range(k-1):
            l.append(pj(data[n*i],data[n*i+n-1],n))
        summ =0
        for i in range(k-1):
            summ+=(n-siz*l[i])**2/(siz*l[i])
        return summ
    else:
        n = (siz+1)//k
        nlast = len(data[n*(k-2)+1:])    
        for i in range(k-2):
            l.append(pj(data[n*i],data[n*i+n-1],n))
            print(l[i])
        l.append(pj(data[-nlast],data[-1],nlast))
        summ =0
        for i in range(k-2):
            summ+=(n-siz*l[i])**2/(siz*l[i])
        summ+=(nlast-siz*l[-1])**2/(siz*l[-1])
        return summ     

def Chi(data):
    d,n = elcounter(data)
    s = set(data)
    dim = len(s)
    summ=0
    con =(n/2**BYTE_READ)
    for i in s:
            summ+=((d[i]-con)**2) / (con)
    return summ

def elcounter(lis):
    n = len(lis)
    s = sorted(set(lis))
    d = dict()
    s.sort()
    lis.sort()
    j=0
#     print(lis[:10])
#     print(s[:50])
    for i in s:
        count = 0 
        while j<n:
            if i!=lis[j]:
                break
            if i==lis[j]:
                j+=1
                count+=1
        d.update({i:count})
    return d,n

print("Native byteorder: ", sys.byteorder)
# print(readOne('./pics/'+l[0]))
# readOne('pics'+'/'+'eee')
data = readFiles('testfiles')
# data['first.png'][0]==data['first.png'][0]
# mean(data['first.png']),mean(data['second.png']),mean(data['eee']),desp(data['first.png']),desp(data['eee'])
#showAll(data)

# print(analyseOne(data['first.png']))
dd,n=analyseOne(data['pexels-photo-257840.jpeg.zip'])
#dd=np.array(data['pexels-photo-257840.jpeg.zip'])
#print(H0(dd,7),' ',chi2.ppf(0.05,7),chi2.ppf(0.95,7))
#dd = [int.from_bytes(d,byteorder='little') for d in dd]
#print(dd[:100])       
#print(int.from_bytes(b'101010101010101010101010',byteorder='little'))
# elcounter(data['pexels-photo-257840.jpeg.zip'])
# print(Chi(dd),' ',chi2.ppf(0.05,2**BYTE_READ-1),chi2.ppf(0.95,2**BYTE_READ-1))
emPlot(dd,n)
