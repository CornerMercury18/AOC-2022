from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./4i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]


total = 0
for item in data:
  e1, e2 = item.split(',')
  l1, r1 = [int(n) for n in e1.split('-')]
  l2, r2 = [int(n) for n in e2.split('-')]
  if (l1 >= l2 and r1 <= r2) or (l2 >= l1 and r2 <= r1):
    total += 1

print(total) 