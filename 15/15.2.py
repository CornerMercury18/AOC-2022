from os.path import dirname, join
from collections import defaultdict

def get_distance(sensor, coords):
  return abs(sensor[0] - coords[0]) + abs(sensor[1] - coords[1])

current_dir = dirname(__file__)
path = join(current_dir, "./15i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

pairs = []
boundary_points = defaultdict(int)
for line in data:
  sensor = (int(line.split()[2].split('=')[1][:-1]), int(line.split()[3].split('=')[1][:-1]))
  beacon = (int(line.split()[-2].split('=')[1][:-1]), int(line.split()[-1].split('=')[1]))

  distance = get_distance(sensor, beacon)
  pairs.append((sensor, distance))
  #count all points on edge of beacon ranges
  for i in range(distance):
    boundary_points[(sensor[0] - distance + i - 1, sensor[1] - i)] += 1
    boundary_points[(sensor[0] + i, sensor[1] - distance + i - 1)] += 1
    boundary_points[(sensor[0] + distance - i + 1, sensor[1] + i)] += 1
    boundary_points[(sensor[0] - i, sensor[1] + distance - i + 1)] += 1


for point, count in boundary_points.items():
  if count >= 2:
    if 0 <= point[0] <= 4000000 and 0 <= point[1] <= 4000000:
      for pair in pairs:
        if get_distance(pair[0], point) <= pair[1]:
          break
      else:
        print(point[0]*4000000 + point[1])
        break