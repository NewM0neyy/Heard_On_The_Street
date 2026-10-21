import numpy as np
import matplotlib.pyplot as plt
def rollin(trials=100000):
  a_wins=0
  b_wins=0
  roll_a=np.random.randint(1,21,size=(trials))
  roll_b=np.random.randint(1,7,size=(trials,3))
  a_condition = roll_a > np.sum(roll_b, axis=1)
  b_condition = np.sum(roll_b, axis=1) > roll_a
  prob_a=np.mean(a_condition)
  prob_b=np.mean(b_condition)
  plt.figure(figsize=(10,5))
  x=["A wins","B wins"]
  y=[prob_a,prob_b]
  plt.bar(x,y)
  plt.show()
  

rollin()
    
  
