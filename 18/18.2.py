from os.path import dirname, join

def flood(pos, depth=0, is_open=False):
    if is_open or pos in visited:
        return is_open
    else:
        visited.add(pos)
    #just under recursion limit lmao
    if depth > 950:
        return True
    if pos in cubes:
        return is_open

    x, y, z = pos
    p = [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
    for new_pos in p:
        is_open = flood(new_pos, depth=depth + 1)
        if is_open:
            return is_open

    return False

current_dir = dirname(__file__)
path = join(current_dir, "./18i.txt")

with open(path) as f:
  data = [[int(n) for n in line.strip('\n').split(',')] for line in f.readlines()]

cubes = set()
for x, y, z in data:
    cubes.add((x, y, z))

total = 0
for x, y, z in cubes:
    p = [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]
    for pos in p:
        if pos not in cubes:
            visited = set()
            if flood(pos):
                total += 1
            

print(total)
