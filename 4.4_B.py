import numpy as np
def rollin(trials=100000):
  expected_payoff=[]
  for _ in range(trials):
    roll_1=np.random.randint(1,7)
    roll_2=np.random.randint(1,7)
    roll_3=np.random.randint(1,7)
    roll=[roll_1,roll_2,roll_3]
    expected_payoff.append(np.max(roll))
    
  return np.mean(expected_payoff)
print(rollin())
