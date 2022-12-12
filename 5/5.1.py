from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./5i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

stacks = {key + 1: [] for key in range(9)}

for i in reversed(range(8)):
  for j in range(1, len(data[i]), 4):
    if data[i][j].isalpha():
      stacks[(j + 3)//4].append(data[i][j])


for i in range(10, len(data)):
  split = data[i].split()
  count = int(split[1])
  c_from = int(split[3])
  to = int(split[5])
  for _ in range(count):
    stacks[to].append(stacks[c_from].pop())

print(stacks)

for i in range(1, 10):
  print(stacks[i][-1], end='')
