from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./2i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n').split() for line in f.readlines()]

con = {
  'A': 'r',
  'B': 'p',
  'C': 's',
  'X':  0,
  'Y': 1,
  'Z': 2
}

wins = {
  'r': ['p', 'r', 's'],
  'p': ['s', 'p', 'r'],
  's': ['r', 's', 'p']
}

c = ['r', 'p', 's']

total = 0
for item in data:
  opponent = con[item[0]]
  total += c.index(wins[opponent][2 - con[item[1]]]) + 1 + con[item[1]] * 3


print(total)