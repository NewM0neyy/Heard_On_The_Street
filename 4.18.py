import numpy as np
import matplotlib.pyplot as plt
def spin(trials=100000,bet_money=1.5):
  spin=[1]*1+[0]*4
  outcome=np.random.choice(spin,size=(trials))
  
  payoff=np.where(outcome==1,5-bet_money,1-bet_money)
  return np.mean(payoff)
print(spin())
trials=np.arange(1,100000)
payoff=[spin(trials=i) for i in trials]
plt.figure(figsize=(10,6))
plt.plot(trials,payoff,color='red')
plt.xlabel("No of trials")
plt.ylabel("Payoff")
plt.show()
    
    
