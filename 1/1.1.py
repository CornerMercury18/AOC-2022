from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./1i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

cals = []
cur = 0
for item in data:
  if item == '':
    cals.append(cur)
    cur = 0
  else:
    cur += int(item)

print(max(cals))
print(sum(sorted(cals, reverse=True)[:3]))