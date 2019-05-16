import csv
from scipy.stats import chi2
import math
from struct import *
def readData(path):
    with open(path,newline='') as file:
        data = csv.reader(file,delimiter= ' ',quotechar='|',quoting=csv.QUOTE_NONE )
#        print(data.__next__())
#        k = 0
#        for i in data:
#            print(i)
#            k=k+1
#            if k==5:
#                break
    return data 
def readByBytes(path):
    with open(path,'rb') as f:
        l = []
        while(True):
            t= f.read(4)
            if t!='':
                l.append(t)
            else:
                break
        return l
def readByStruck():
    data = open('5.data','rb').read()
    f = unpack('>1000000f',data)
    return f
def takeBorders(data):
    return min(data), max(data)

def devide(data,k):
    l=[]
    n = len(data)
    # m - max  elements in one interval
    m = n // k
    count = 0
    for i in range(k-1):
        ll=[]
        for j in range(m):
            ll.append(data[count+j])
            count = count+1
    l.append(ll)
    return l
teta=12.98
def pj(a,b):
    return (-math.exp(-(b**2/(2*teta**2))) +   math.exp(-(a**2/(2*teta**2))))
dsize = 1000000
def chi(data,k):
    data= list(data)
    data.sort()
    summ=0
    for i in range(k-2):
        le = len(data)//(k)
        summ+=(le-dsize*pj(data[i*le],data[(i+1)*le-1]))**2/(dsize*pj(data[i*le],data[(i+1)*le-1]))
    return summ

def H0(data,k):
    siz = len(data)
    n = 0
    l= []
    if siz%k == 0:
        n=siz/k
        for i in range(k):
            l.append(pj(data[n*k],data[n*2*k-1],n))
        summ =0
        for i in range(k):
            summ+=(n-siz*l[i])**2/(siz*l[i])
        return summ
    else:
        n = (siz+1)/k
        nlast = len(data[siz*(k-1):])    
        for i in range(k-1):
            l.append(pj(data[n*k],data[n*2*k-1],n))
        l.append(pj(data[:-nlast],data[:-1],nlast))
        summ =0
        for i in range(k-1):
            summ+=(n-siz*l[i])**2/(siz*l[i])
        summ+=(nlast-siz*l[i])**2/(siz*l[i])
        return summ 

data=(readByStruck())
print(chi(data,150),chi2.ppf(0.05,2*32),chi2.ppf(0.95,2*32))
print(sum(data)/len(data)*2/(2*math.pi)**(0.5))
