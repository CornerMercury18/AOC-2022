from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./2i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n').split() for line in f.readlines()]

con = {
  'A': 'r',
  'B': 'p',
  'C': 's',
  'X': 'r',
  'Y': 'p',
  'Z': 's'
}

wins = {
  'r': ['p', 'r', 's'],
  'p': ['s', 'p', 'r'],
  's': ['r', 's', 'p']
}

c = ['r', 'p', 's']

total = 0
for item in data:
  total += 3 * wins[con[item[1]]].index(con[item[0]])
  total += c.index(con[item[1]]) + 1

print(total)