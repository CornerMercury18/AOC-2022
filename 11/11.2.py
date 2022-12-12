from os.path import dirname, join
from time import time

class Monkey():
  def __init__(self, items, operation, division, on_true=None, on_false=None):
    self.items = items
    if operation[-1] == 'old':
      if operation[-2] == '+':
        self.operation = lambda x: 2*x
      else:
        self.operation = lambda x: x**2
    else:
      if operation[-2] == '+':
        self.operation = lambda x: x + int(operation[-1])
      else:
        self.operation = lambda x: x * int(operation[-1])
    self.division = division
    self.on_true = on_true
    self.on_false = on_false
    self.inspections = 0

  def catch(self, item):
    self.items.append(item)
  
  def set_true(self, m):
    self.on_true = m

  def set_false(self, m):
    self.on_false = m
  
  def round(self):
    while len(self.items) > 0:
      worry = self.items.pop(0)
      for key, value in worry.items():
        worry[key] = self.operation(value) % key
      
      if worry[self.division] == 0:
        self.on_true.catch(worry)
      else:
        self.on_false.catch(worry)
      
      self.inspections += 1


def create_mod(num):
  dict_ = {}
  dict_[2] = num % 2
  dict_[3] = num % 3
  dict_[5] = num % 5
  dict_[7] = num % 7
  dict_[11] = num % 11
  dict_[13] = num % 13
  dict_[17] = num % 17
  dict_[19] = num % 19

  return dict_


current_dir = dirname(__file__)
path = join(current_dir, "./11i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

t1 = time()
monkeys = []
links = []
for i in range(0, len(data), 7):
  items = [create_mod(int(num)) for num in data[i+1].split(':')[1].split(', ')]
  operation = data[i+2].split()[-2:]
  div = int(data[i+3].split()[-1])
  t = int(data[i+4].split()[-1])
  f = int(data[i+5].split()[-1])
  links.append((t,f))
  monkeys.append(Monkey(items, operation, div))

for i, monkey in enumerate(monkeys):
  monkey.set_true(monkeys[links[i][0]])
  monkey.set_false(monkeys[links[i][1]])


for f in range(10000):
  for monkey in monkeys:
    monkey.round()


inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
print(inspections[0] * inspections[1])
print(time() - t1)