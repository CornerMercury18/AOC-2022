from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./12i.txt")

with open(path, 'r') as f:
  grid = [[char for char in line.strip('\n')] for line in f.readlines()]

def flood(pos, last_char, steps, solution):
  if steps >= solution:
    return solution
  if not(0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])):
    return solution
  if not(ord(last_char) >= ord(grid[pos[0]][pos[1]]) - 1):
    return solution
  if pos == end_pos:
    return steps
  if visited.get(pos) == None or visited[pos] > steps:
    visited[pos] = steps
    solution = flood((pos[0] + 1, pos[1]), grid[pos[0]][pos[1]], steps + 1, solution)
    solution = flood((pos[0] - 1, pos[1]), grid[pos[0]][pos[1]], steps + 1, solution)
    solution = flood((pos[0], pos[1] + 1), grid[pos[0]][pos[1]], steps + 1, solution)
    solution = flood((pos[0], pos[1] - 1), grid[pos[0]][pos[1]], steps + 1, solution)
  
  return solution



visited = {}
more = []
for i, row in enumerate(grid):
  for j, char in enumerate(row):
    if char == 'S':
      start_pos = (i, j)
      grid[i][j] = 'a'
    elif char == 'E':
      end_pos = (i, j)
      grid[i][j] = 'z'
    elif char == 'a':
      more.append((i, j))


max_steps = 377
for m in more:
  solve = flood(m, 'a', 0, max_steps)
  if solve < max_steps:
    max_steps = solve 

print(max_steps)


