from os.path import dirname, join


def add(coords):
  if coords not in trees:
    trees.append(coords)


current_dir = dirname(__file__)
path = join(current_dir, "./8i.txt")

trees = []

with open(path, 'r') as f:
  grid = [[int(char) for char in line.strip('\n')] for line in f.readlines()]

for i, row in enumerate(grid):
  prev = -1
  for j, item in enumerate(row):
    if item > prev:
      add((i, j))
      prev = item
  
  prev = -1
  for j, item in enumerate(reversed(row)):
    if item > prev:
      add((i, (len(row) - 1) - j))
      prev = item


for i in range(len(grid[0])):
  prev = -1
  for j in range(len(grid)):
    if grid[j][i] > prev:
      add((j, i))
      prev = grid[j][i]
  
  prev = -1
  for j in reversed(range(len(grid))):
    if grid[j][i] > prev:
      add((j, i))
      prev = grid[j][i]

# for i in range(len(grid)):
#   add((i, 0))
#   add((i, len(grid[0]) - 1))

# for i in range(len(grid[0])):
#   add((0, i))
#   add((len(grid) - 1, i))


  
print(len(trees), len(grid) * len(grid[0]))

empty_grid = [[str(0) for _ in range(len(grid[0]))] for _ in range(len(grid))]

# print(trees)
for coord in trees:
  empty_grid[coord[0]][coord[1]] = str(1)

print([print(''.join(l)) for l in empty_grid])
