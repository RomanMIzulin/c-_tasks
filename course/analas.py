import csv


f = open('5_nrawdata.nrawdata')
data = csv.reader(f,delimiter=' ' )
print(next(data))
