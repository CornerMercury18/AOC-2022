
from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./6i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()][0]

prev = data[:14]
skip = 0

for i, char in enumerate(data[14:]):
  if len(set(j for j in prev if prev.count(j) > 1)) == 0:
    print(i + 14)
    break

  prev = prev[1:] + char