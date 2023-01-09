from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./18i.txt")

with open(path) as f:
  data = [[int(n) for n in line.strip('\n').split(',')] for line in f.readlines()]

cubes = set()
for x, y, z in data:
    cubes.add((x, y, z))

total = len(cubes) * 6
for x, y, z in cubes:
    if (x-1, y, z) in cubes:
        total -= 1
    if (x+1, y, z) in cubes:
        total -= 1
    if (x, y-1, z) in cubes:
        total -= 1
    if (x, y+1, z) in cubes:
        total -= 1
    if (x, y, z-1) in cubes:
        total -= 1
    if (x, y, z+1) in cubes:
        total -= 1

print(total)
