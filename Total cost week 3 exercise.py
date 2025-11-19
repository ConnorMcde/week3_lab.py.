"""Summing a list"""

costs = [15.00, 12.50, 3.75, 40.25, 6.99]
total_cost = 0

for i in range(4):
     total_cost = total_cost + costs[i]
     
     
print(f"{total_cost:.2f}")