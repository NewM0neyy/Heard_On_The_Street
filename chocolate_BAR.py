import random
import numpy as np
import matplotlib.pyplot as plt
def breaking_bad(num_of_pieces=100):
  L=1
  pieces_count=0
  while L<=num_of_pieces:
    X=random.randint(1,num_of_pieces)
    if X>=L:
      L=X+1
    else:
      L=L+1
    pieces_count+=1
  return pieces_count
trials=100000
prob=[breaking_bad()  for n in range(100000)]
counts=np.bincount(prob)
pieces=np.arange(len(counts))
plt.plot(pieces,counts,color='blue')
plt.xlabel("Number of pieces")
plt.ylabel("Prob of breaking into k pieces")
plt.show()
