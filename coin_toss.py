import random
def single_game(m):
  score=0
  stake=1.0
  while score>-2 and score< 2:
    if score==0 or score==1:
      stake=min(stake*2,m)
    elif score==-1:
      pass
    is_heads=random.choice([True,False])
    if is_heads:
      score+=1
    else:
      score-=1
  if score==2:
    return stake
  else:
    return -stake
def play(m,trials=100000):
  total_payoff=0
  for _ in range(trials):
    total_payoff+=single_game(m)
  avg_payoff=total_payoff/trials
  print(f"Expected payoff:{avg_payoff} ")
play(100000)
