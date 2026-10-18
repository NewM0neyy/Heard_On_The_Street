import numpy as np
#this question is a sub question for 4.8 the strategy ,for 4.8 is to toss the coin twice :
#HH child 1 will get the apple
#TT child 2 will get apple
#TH child 3 will get apple 
#HT retoss
def toss(trials=100000):
  coin_toss=['H','T']
  total_toss=0
  for _ in range(trials):
    while True:
      first=np.random.choice(coin_toss)
      sec=np.random.choice(coin_toss)
      toss=first+sec
      total_toss+=2
      if toss in ['HH' ,'TT','TH']:
        break
      else:
        continue
  return total_toss/trials
print(toss())        
      
      
        
        
      
  
  
