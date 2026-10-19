import numpy as np
import matplotlib.pyplot as plt
def bet(trials=1000000,odd_ratio=10):
  match=[1,0]
  outcome=np.random.choice(match,size=(trials,4))
  wins=np.sum(outcome,axis=1)==4
  payout=np.where(wins,odd_ratio,-1)
  return np.mean(payout)
odd_ratio=[5,10,15,20]
payoff=[bet(odd_ratio=i) for i in odd_ratio]
plt.plot(odd_ratio,payoff,color='red')
plt.xlabel("odds ratio")
plt.ylabel("Expected payout")
plt.show()
  
    


  
  
