import re
## ----open file
f3 = open ("./FECLP30.csv",'r')
## ----- read array
Arr_f3 = f3.readlines() 

num_startline=15
num_inputlines=len(Arr_f3)
num_total_input=num_inputlines - num_startline

M1 = [0 for m in range(num_total_input)]

for l in range (num_startline, num_inputlines):
  Arr_temp = re.split(",", Arr_f3[l])
  #print(Arr_temp)
  
  M1[l-num_startline] = abs(float(Arr_temp[1]))
print(M1)

M2 = [0 for o in range(num_total_input)]

for u in range (num_startline, num_inputlines):
## M1[l]= abs(float(re.split(",", Arr_f3[l]))*10^-5))
  print(u)
  Arr_temp2 = re.split(",", Arr_f3[u])
  M2[u-num_startline] = abs(float(Arr_temp2[2]))
 ## print (Arr_temp[1])
print(M2)

f4 = open ("./FECLP30output.csv",'w')
for y in range(len(M1)):
 f4.write ("{0:.10f},{1:.10f}\n".format(M1[y],M2[y]))
f4.close()

