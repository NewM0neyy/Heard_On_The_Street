import numpy as np
import matplotlib.pyplot as plt
def rollin(trials=100000,n=5):
  success=0
  for _ in range(trials):
    current_roll=0
    while current_roll < n:
      current_roll+=np.random.randint(1,7)
    if current_roll==n:
      success+=1
  return success/trials
n=np.arange(1,51)
p=[rollin(n=i) for i in n]
plt.plot(n,p,color='blue')
plt.xlabel("N")
plt.ylabel("P")
plt.show()
  
      
      
      

  
    
  
