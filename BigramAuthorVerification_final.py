import json
import os
from numpy import linspace
import matplotlib.pyplot as plt

def self_compare(filename, filename2, arr_for_sums):
    with open(filename, 'r') as fp:
        with open(filename2,'r') as fp2:
            fp = fp.read()
            fp2 = fp2.read()
            data = json.loads(fp)
            data2 = json.loads(fp2)
            keys1 = [tuple(item[0]) for item in data]
            values1 = [item[1] for item in data]
            dicdata1 = dict(zip(keys1, values1))
            keys2 = [tuple(item[0]) for item in data2]
            values2 = [item[1] for item in data2]
            dicdata2 = dict(zip(keys2,values2))
            
            suum = 0
            for key1 in dicdata1:
                if key1 in dicdata2:
                    suum += ((2*(dicdata1[key1]-dicdata2[key1])/(dicdata1[key1]+dicdata2[key1]))**2)
            arr_for_sums.append(suum)
        
def new_compare(unknown, filename):
    with open(filename, 'r') as fp:
        with open(unknown,'r') as fp2:
            fp = fp.read()
            fp2 = fp2.read()
            data = json.loads(fp)
            data2 = json.loads(fp2)
            keys1 = [tuple(item[0]) for item in data]
            values1 = [item[1] for item in data]
            dicdata1 = dict(zip(keys1, values1))
            keys2 = [tuple(item[0]) for item in data2]
            values2 = [item[1] for item in data2]
            dicdata2 = dict(zip(keys2,values2))
            
            suum = 0
            for key1 in dicdata1:
                if key1 in dicdata2:
                    suum += ((2*(dicdata1[key1]-dicdata2[key1])/(dicdata1[key1]+dicdata2[key1]))**2)
            m = suum/max_of_sum
            level.append(m)

    
arr_for_sums = []
arr2 = []
level = []        
path = './Nosik_bigramy/'
path_unknown = './unknown_Lebedev/'

files = []
unknown = []
for a, b, c in os.walk(path):
    for filename in os.listdir(path):
        if filename.endswith('.json'):
            files.append(filename)
 
for a, b, c in os.walk(path_unknown):
    for filename in os.listdir(path_unknown):
        if filename.endswith('.json'):
            unknown.append(filename)
           
#unknown = 'unknown_6.json'

results = []         
for c in unknown:
    for a in files:
        for b in files:
            if a != b:
                self_compare(path + a, path + b, arr_for_sums)
        max_of_sum = max(arr_for_sums)
        arr2.append(new_compare(path_unknown + c, path + a))
        arr_for_sums = []
    results.append(sum(level)/len(level))
print (results)
    
'''
results.sort()

#let the graph, results and roc-curve be only for Lebedev
fig = plt.figure()
t = 0.26
x = []
y = []
for i in results:    
    if i<=(t-0.01):
        y.append(1)
        x.append(i)
    elif i>=(t+0.01):
        y.append(0)
        x.append(i)
    else:
        y.append((t+0.01-i)/0.02)
        x.append(i)

plt.plot(x,y)

for i in results:
    if i <= (t-0.01):
        print ('Yes')
    elif i >= (t+0.01):
        print ('No')
    else:
        print ('p='+str((t + 0.01- i)/0.02))

#for a, b, c in os.walk(path_unknown):
#    for unknown in c:
#        if unknown.endswith('.json'):
#new_compare(unknown, path + a)


 #print (sorted(list_of_ms)[len(list_of_ms)//2])         

'''