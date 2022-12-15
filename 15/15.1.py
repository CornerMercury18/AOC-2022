from os.path import dirname, join


def get_distance(sensor, coords):
  return abs(sensor[0] - coords[0]) + abs(sensor[1] - coords[1])

current_dir = dirname(__file__)
path = join(current_dir, "./15i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

y = 2000000
beacons = []
empty = set()
for line in data:
  sensor = (int(line.split()[2].split('=')[1][:-1]), int(line.split()[3].split('=')[1][:-1]))
  beacon = (int(line.split()[-2].split('=')[1][:-1]), int(line.split()[-1].split('=')[1]))
  beacons.append(beacon)

  distance = get_distance(sensor, beacon)
  for i in range(int(distance) + 1):
    coords = (sensor[0] + i, y)
    if get_distance(sensor, coords) > distance:
      break
    else:
      empty.add(coords)

  for i in range(int(distance) + 1):
    coords = (sensor[0] - i, y)
    if get_distance(sensor, coords) > distance:
      break
    else:
      empty.add(coords)
  
  

for beacon in beacons:
  empty.discard(beacon)

print(len(empty))