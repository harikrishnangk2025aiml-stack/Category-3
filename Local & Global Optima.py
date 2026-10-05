locations = [10, 20, 15, 50, 30, 25]
current = locations[0]
for x in locations[1:]:
    if x > current:
        current = x
print("Local Optimum:", current)
print("Global Optimum:", max(locations))
