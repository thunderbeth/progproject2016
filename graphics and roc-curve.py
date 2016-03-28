
# coding: utf-8

# In[5]:

get_ipython().magic('matplotlib inline')
# Nosik
import codecs
from numpy import linspace
import matplotlib.pyplot as plt
fig=plt.figure()
f=open('c:/Python34/1.txt','r',encoding='utf-8-sig')
arr=[]
for line in f:
    line=line.split()
    arr.append(float(line[0]))
f.close()
arr.sort()
t=0.67
x=[]
y=[]
for i in arr:
    print (i)
for i in arr:
    
    if i<=(t-0.1):
        y.append(0)
        x.append(i)
    elif i>=(t+0.1):
        y.append(1)
        x.append(i)
    else:
        y.append((i-t+0.1)/0.2)
        x.append(i)

plt.plot(x,y)


# In[8]:

get_ipython().magic('matplotlib inline')
#Lebedev_graphic
import codecs
from numpy import linspace
import matplotlib.pyplot as plt
fig=plt.figure()
f=open('c:/Python34/Lebedev_Lebedev.txt','r',encoding='utf-8-sig')
arr=[]
for line in f:
    line=line.split()
    arr.append(float(line[0]))
f.close()
f=open('c:/Python34/Lebedev_Nosik.txt','r',encoding='utf-8-sig')
for line in f:
    line=line.split()
    arr.append(float(line[0]))
f.close()
arr.sort()
t=0.26
x=[]
y=[]
for i in arr:
    print (i)
for i in arr:
    
    if i<=(t-0.02):
        y.append(1)
        x.append(i)
    elif i>=(t+0.02):
        y.append(0)
        x.append(i)
    else:
        y.append((t+0.02-i)/0.04)
        x.append(i)

plt.plot(x,y)


# In[18]:

get_ipython().magic('matplotlib inline')
#Lebedev_roc-curve
import codecs
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
fig=plt.figure()
f=open('c:/Python34/Lebedev_Lebedev.txt','r',encoding='utf-8-sig')
arr=[]
for line in f:
    line=line.split()
    arr.append(float(line[0]))
f.close()

score=[]
classes=[]
t=0.26
p=0
for i in arr:
    if i<=(t-0.02):
        p=1
        score.append(p)
        classes.append(1)
    elif i>=(t+0.02):
        p=0
        score.append(p)
        classes.append(1)
    else:
        p=(t+0.02-i)/0.04
        score.append(p)
        classes.append(1)
        
f=open('c:/Python34/Lebedev_Nosik.txt','r',encoding='utf-8-sig')
brr=[]
for line in f:
    line=line.split()
    brr.append(float(line[0]))
f.close()

t=0.26
p=0
for i in brr:
    if i<=(t-0.02):
        p=1
        score.append(p)
        classes.append(0)
    elif i>=(t+0.02):
        p=0
        score.append(p)
        classes.append(0)
    else:
        p=(t+0.02-i)/0.04
        score.append(p)
        classes.append(0)
       
fpr, tpr, _ = roc_curve(classes, score)
plt.figure()
plt.plot(fpr, tpr)
print('AUC =', auc(fpr, tpr))
    


# In[ ]:



