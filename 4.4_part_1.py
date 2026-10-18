import numpy as np
"""
 using backward induction
 the expected value of the last round is 3.5 that of the second round is 4.25 and that 
 of first round is 4.625
 so if i get >=5 on first round i will stop 
 if i get >=4 in the second round we will stop 
 
 """


def rollin(trials=100000):
  expected_payout=[]
  for _ in range(trials):
    roll_1=np.random.randint(1,7)
    if roll_1>=5:
        expected_payout.append(roll_1)
        continue
    roll_2=np.random.randint(1,7)
    if roll_2>=4:
        expected_payout.append(roll_2)
        continue
    roll_3=np.random.randint(1,7)
    expected_payout.append(roll_3)
  return np.mean(expected_payout)
print(rollin())
  
    
        
        
  
  
  
