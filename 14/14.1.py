from os.path import dirname, join

def get_grid(data):
  grid = {}
  for line in data:
    l = line.split(' -> ')
    len_ = len(l)
    for i, coord in enumerate(l):
      coord = [int(n) for n in coord.split(',')]
      if i + 1 < len_:
        next_coord = [int(n) for n in l[i+1].split(',')]
        change_in_x = next_coord[0] - coord[0]
        if change_in_x != 0:
          if change_in_x >= 0:
            for j in range(change_in_x + 1):
              grid[(coord[1], coord[0] + j)] = '#'
          else:
            for j in range(-change_in_x + 1):
              grid[(coord[1], next_coord[0] + j)] = '#'
        else:
          change_in_y = next_coord[1] - coord[1]
          if change_in_y >= 0:
            for j in range(change_in_y + 1):
              grid[(coord[1] + j, coord[0])] = '#'
          else:
            for j in range(-change_in_y + 1):
              grid[(next_coord[1] + j, coord[0])] = '#'

  return grid


def drop_sand():
  current_coord = (-1, 500)
  while current_coord[0] < max_y:
    if grid.get((current_coord[0] + 1, current_coord[1])) == None:
      current_coord = (current_coord[0] + 1, current_coord[1])
    elif grid.get((current_coord[0] + 1, current_coord[1] - 1)) == None:
      current_coord = (current_coord[0] + 1, current_coord[1] - 1)
    elif grid.get((current_coord[0] + 1, current_coord[1] + 1)) == None:
      current_coord = (current_coord[0] + 1, current_coord[1] + 1)
    else:
      grid[(current_coord[0], current_coord[1])] = 'o'
      return True
    
  return False



current_dir = dirname(__file__)
path = join(current_dir, "./14i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

max_y = -float('inf')

for line in data:
  for coord in line.split(' -> '):
    coord = [int(n) for n in coord.split(',')]
    if coord[1] > max_y:
      max_y = coord[1]


grid = get_grid(data)

count = 0
while True:
  if drop_sand():
    count += 1
  else:
    break


print(count)