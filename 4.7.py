import numpy as np
wins=4
w=np.zeros((wins+1,wins+1))
for i in range(wins):
  w[wins,i]=200
  w[i,wins]=0
for i in range(wins-1,-1,-1):
  for j in range(wins-1,-1,-1):
    w[i,j]=(w[i+1,j]+w[i,j+1])/2
    print(w[i,j])
#printing how much money u will have on each step
