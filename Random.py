import random
import statistics

result = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    result.append(sum)

mean = statistics.mean(result)
standarddeviation = statistics.stdev(result)

median = statistics.median(result)

mode = statistics.mode(result)

print(mean, standarddeviation, median, mode)
