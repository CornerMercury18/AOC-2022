from os.path import dirname, join
from time import time

current_dir = dirname(__file__)
path = join(current_dir, "./21i.txt")

with open(path) as f:
  data = [line.strip('\n').split(':') for line in f.readlines()]

while 'root' not in globals():
    for var, exp in data:
        try:
            globals()[var] = eval(exp)
            data.remove([var, exp])
        except:
            pass

print(root)