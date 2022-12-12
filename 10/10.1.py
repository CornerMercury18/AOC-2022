from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./10i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]


x = 1
cycles = [1, 1]
for line in data:
  # if 179 <= len(cycles) <= 225:
  #   print(x, line) 
  cycles.append(x)
  if line != 'noop':
    x += int(line.split()[1])
    cycles.append(x)

total = 0
for i in [20, 60, 100, 140, 180, 220]:
  total += (i)*cycles[i]

print(total)