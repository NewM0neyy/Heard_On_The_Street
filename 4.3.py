import numpy as np
import matplotlib.pyplot as plt
def coin_toss(trials=100000,no_of_coins=4):
  toss=[0,1]
  your_toss=np.random.choice(toss,size=(trials,no_of_coins+1))
  opp_toss=np.random.choice(toss,size=(trials,no_of_coins))
  your_heads=np.sum(your_toss,axis=1)
  opp_heads=np.sum(opp_toss,axis=1)
  your_win=your_heads>opp_heads
  prob=np.mean(your_win)
  return prob


coins=np.arange(1,21)
coin_toss=[coin_toss(no_of_coins=i) for i in coins]
plt.plot(coins,coin_toss,color='red')
plt.xlabel("No of coin")
plt.ylabel("Prob of winning")
plt.show()
  
