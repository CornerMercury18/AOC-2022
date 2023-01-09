from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./i.txt")

with open(path) as f:
  data = [line.strip('\n') for line in f.readlines()]