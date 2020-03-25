
# coding: utf-8

# In[4]:


import re
## ----open file
f3 = open ("C:\\Winston\\fileconvert\\FECLP30.csv",'r')


## ----- read array

Arr_f3 = f3.readlines() ## 定義f1 逐行讀資料動作

## for n in range (len(Arr_f3)): # 逐行讀取後逐行顯示
   ## print (n, Arr_f3[n])

M1 = [0 for m in range(55)]

for l in range (17,73):
## M1[l]= abs(float(re.split(",", Arr_f3[l]))*10^-5))
  Arr_temp = re.split(",", Arr_f3[l])
  k= l-17
  M1[k] = abs(float(Arr_temp[1]))
 ## print (Arr_temp[1])
print(M1)

M2 = [0 for o in range(55)]

for u in range (17,78):
## M1[l]= abs(float(re.split(",", Arr_f3[l]))*10^-5))
  Arr_temp2 = re.split(",", Arr_f3[u])
  p= u-17
  M2[p] = abs(float(Arr_temp2[2]))
 ## print (Arr_temp[1])
print(M2)

f4 = open ("C:\\Winston\\fileconvert\\FECLP30output.csv",'w')
for y in range(len(M1)):
 f4.write ("{0:.10f},{1:.10f}\n".format(M1[y],M2[y]))
f4.close()

