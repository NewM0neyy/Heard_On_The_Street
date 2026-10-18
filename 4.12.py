import numpy as np
def shuffle(trials=100000):
  deck=[0]*48+[1]*4 
  fav_outcome=0# four kings are represented by 1 and others are represented by 0
  for _ in range(trials):
    
   shuffled_deck=np.random.permutation(deck)
   cards=shuffled_deck[:2]
   if cards[0]==1 and cards[1]==1:
     fav_outcome+=1
  return fav_outcome/trials
print(shuffle())
  
