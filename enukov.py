# import numpy as np
# #Контейнер расчета
# from sympy import *
# k, T, C, L = symbols('k C T L')
# #1 способ
# C_ost=100000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(5):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 100000, T:5, L:0})
#   Am_lst.append(round(Am.subs({C: 100000, T:5, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)

# #2 способ
#Aj=0
#C_ost=100000
#Am_lst_2=[]
#C_ost_lst_2=[]
#for i in range(5):
#  Am = k * 1/T * (C - Aj)
#  C_ost -= Am.subs({C: 100000, T:5, k:2})
#  Am_lst_2.append(round(Am.subs({C: 100000, T:5, k:2}), 2))
#  Aj += Am
#  C_ost_lst_2.append(round(C_ost, 2))
#print('Am_lst_2:', Am_lst_2)
#print('C_ost_lst_2:', C_ost_lst_2)

# #Контейнер табличного вывода
#import pandas as pd
#Y = range(1, 6)
#table1 = list(zip(Y, C_ost_lst, Am_lst))
#table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
#tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
#tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])

#print(tfame)
#print(tfame2)

# #Контейнер визуализации
#from matplotlib import pyplot as plt
# plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
# plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
# plt.show()

# vals = Am_lst
# labels = list(range(1, 9))
# explode = (0.1, 0.1, 0.1, 0.1, 0.1)
# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"}, rotatelabels=True)
# ax.axis("equal")
# plt.show()

# ВАРИАНТ 2

# Первый способ
# from sympy import *
# k, T, C, L = symbols('k C T L')

# C_ost=50000
# Am_lst=[]
# C_ost_lst=[]
# for i in range(9):
#   Am = (C-L)/T
#   C_ost -= Am.subs({C: 50000, T:9, L:0})
#   Am_lst.append(round(Am.subs({C: 50000, T:9, L:0}), 2))
#   C_ost_lst.append(round(C_ost, 2))
# print('Am_lst:', Am_lst)
# print('C_ost_lst:', C_ost_lst)
#Сосед все сделал правильно

#2 способ
# Aj=0
# C_ost=50000
# Am_lst_2=[]
# C_ost_lst_2=[]
# for i in range(9):
#   Am = k * 1/T * (C - Aj)
#   C_ost -= Am.subs({C: 50000, T:9, k:2})
#   Am_lst_2.append(round(Am.subs({C: 50000, T:9, k:2}), 2))
#   Aj += Am
#   C_ost_lst_2.append(round(C_ost, 2))
# print('Am_lst_2:', Am_lst_2)
# print('C_ost_lst_2:', C_ost_lst_2)
#Сосед все сделал правильно
#Контейнер табличного вывода
#import pandas as pd
#Y = range(1, 10)
#table1 = list(zip(Y, C_ost_lst, Am_lst))
#table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
#tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
#tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])

#print(tfame)
#print(tfame2)

# from matplotlib import pyplot as plt
#plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
#plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
#plt.show()

# vals = Am_lst
# labels = list(range(1, 10))
#explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, #wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"}, rotatelabels=True)
#ax.axis("equal")
#plt.show()

#vals = Am_lst_2
#labels = list(range(1, 10))
#explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"}, #rotatelabels=True)
#ax.axis("equal")
#plt.show()

#table1 = list(zip(Y, Am_lst))
#table2 = list(zip(Y, Am_lst_2))
#tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
#tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])

#plt.bar(tfame['Y'], tfame['Am_lst'])
#plt.show()

#сосед все правильно сделал

# Вариант 7
# Первый способ
from sympy import *

k, T, C, L = symbols('k C T L')

C_ost = 70000
Am_lst = []
C_ost_lst = []
for i in range(8):
  Am = (C - L) / T
  C_ost -= Am.subs({C: 70000, T: 8, L: 0})
  Am_lst.append(round(Am.subs({C: 70000, T: 8, L: 0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)

#2 способ
Aj = 0
C_ost = 70000
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(8):
  Am = k * 1 / T * (C - Aj)
  C_ost -= Am.subs({C: 70000, T: 8, k: 2})
  Am_lst_2.append(round(Am.subs({C: 70000, T: 8, k: 2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода
import pandas as pd

Y = range(1, 9)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])

print(tfame)
print(tfame2)

from matplotlib import pyplot as plt
#plt.plot(tfame['Y'], tfame['C_ost_lst'], label = 'Am')
#plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label = 'Am_2')
#plt.show()

vals = Am_lst
labels = list(range(1, 9))
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       autopct='%1.1f%%',
       shadow=True,
       explode=explode,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': "k"
       },
       rotatelabels=True)
ax.axis("equal")
plt.show()

#vals = Am_lst_2
#labels = list(range(1, 9))
#explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"}, #rotatelabels=True)
#ax.axis("equal")
#plt.show()

#table1 = list(zip(Y, Am_lst))
#table2 = list(zip(Y, Am_lst_2))
#tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
#tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])

#plt.bar(tfame['Y'], tfame['Am_lst'])
#plt.show()
