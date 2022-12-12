from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./10i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]


x = 1
cycles = [1]
for line in data:
  # if 179 <= len(cycles) <= 225:
  #   print(x, line) 
  cycles.append(x)
  if line != 'noop':
    x += int(line.split()[1])
    cycles.append(x)

grid = [['.' for _ in range(40)] for _ in range(6)]

crt = (0 , 0)
for y in range(6):
  for x in range(40):
    cur = cycles[y*40 + x]
    if cur -1 <= crt[1] <= cur + 1:
      grid[crt[0]][crt[1]] = '@'
    
    if crt[1] + 1 >= 40:
      crt = (crt[0] + 1, 0)
    else:
      crt = (crt[0], crt[1] + 1)


[print(''.join(row)) for row in grid]