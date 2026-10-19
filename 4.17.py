import matplotlib.pyplot as plt
def basketball(trials=100000):
  two_pointer_win=0
  three_pointer_win=0
  for _ in range(trials):
    if random.random()<0.7:
      if random.random()<0.5:
        two_pointer_win+=1
  for _ in range(trials):
    if random.random()<0.4:
      three_pointer_win+=1
  return two_pointer_win/trials,three_pointer_win/trials
two,three=basketball()
y=[two,three]
x=["prob of winning through two pointer","probability of winning through three pointer"]
plt.figure(figsize=(8,5))
plt.bar(x,y)
plt.show()
