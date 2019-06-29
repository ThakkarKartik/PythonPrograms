
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''
#plt.plot([1,2,3,4])
plt.xlabel('Real Number')
plt.ylabel('Estimation')
#plt.plot([1, 2, 3, 4], [1, 4, 9, 10])

plt.plot([1,2,3,4], [1,4,9,16], 'gs')
plt.axis([0, 6, 0, 20])
plt.show()
'''
plt.plot([1,2,3,4], [1,4,9,16], 'g^')
plt.plot([3,4,5,6], [3,6,2,10], 'r--')
plt.axis([0, 6, 0, 16])

plt.show()

t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

names =['Dingos','Wild Cats','Tigers']
values = [1,11,111]

#plt.figure(1,figsize=(9,3))
plt.subplot(2,2,1)
plt.bar(names,values,linewidth=4.0)
plt.subplot(2,2,2)
plt.plot(names,values,dashes=[10,10,4,4])
plt.subplot(2,2,3)
plt.barh(names,values,color='green',linewidth=4.0)
plt.subplot(2,2,4)
plt.pie(values,values)

plt.plot(names,values,linestyle='steps', marker='o', markeredgecolor='blue', markerfacecolor='black', markersize=15)
plt.show()

plt.hist(values,10)

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.annotate('Best Place',xy=(1,1))
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
