from os.path import dirname, join

def update_tail(h, t):
  if abs(t[0] - h[0])  <=  1 and abs(t[1] - h[1]) <= 1:
    return t
  
  if abs(t[0] - h[0]) > 1:
    if abs(t[1] - h[1]) == 1:
      t = [(t[0]+h[0])//2, h[1]]
    else:
      t = [(t[0]+h[0])//2, t[1]]
    if t not in tail_pos:
      tail_pos.append(t)
    return t
  
  if abs(t[1] - h[1]) > 1:
    if abs(t[0] - h[0]) == 1:
      t = [h[0], (t[1]+h[1])//2]
    else:
      t = [t[0], (t[1]+h[1])//2]
    if t not in tail_pos:
      tail_pos.append(t)
    return t



current_dir = dirname(__file__)
path = join(current_dir, "./9i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

h = [0, 0]
t = [0, 0]
tail_pos = [(0, 0)]
for item in data:
  c, n = item.split()
  if c == 'R':
    for _ in range(int(n)):
      h = [h[0] + 1, h[1]]
      t = update_tail(h, t)
  elif c == 'L':
    for _ in range(int(n)):
      h = [h[0] - 1, h[1]]
      t = update_tail(h, t)
  elif c == 'U':
    for _ in range(int(n)):
      h = [h[0], h[1] - 1]
      t = update_tail(h, t)
  else:
    for _ in range(int(n)):
      h = [h[0], h[1] + 1]
      t = update_tail(h, t)


print(len(tail_pos))