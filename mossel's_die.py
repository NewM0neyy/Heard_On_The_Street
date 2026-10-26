import numpy as np
def rollin(trials=100000):
  valid_roll=[]
  for _ in range(trials):
    is_eve=True
    count=0
    while True:
      roll=np.random.randint(1,7)
      count+=1
      if roll %2!=0:
        is_eve=False
      if roll==6:
        break
    if is_eve:
      valid_roll.append(count)
  return np.mean(valid_roll)
print(rollin())
      
        
  
  
