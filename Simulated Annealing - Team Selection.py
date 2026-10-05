import random

teams = [40, 50, 30, 70, 60]

current = random.choice(teams)

for i in range(10):
    new = random.choice(teams)

    if new > current or random.random() < 0.2:
        current = new

print("Best Team Score:", current)
