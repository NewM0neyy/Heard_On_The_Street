import numpy as np
def rollin(trials=100000):
  payoff=[]
  for _ in range(trials):
    
    while True:
      roll=np.random.randint(1,7)
      if roll!=1:
        
        break
    payoff.append(roll)
  return np.mean(payoff)  
print(rollin())

        
      
