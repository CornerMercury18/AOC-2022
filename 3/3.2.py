from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./3i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

sum = 0
for a, b, c in zip(*[iter(data)]*3):
  for char in a:
    if char in b and char in c:
      if char.isupper():
        sum += ord(char) - 64 + 26
      else:
        sum += ord(char) - 96
     
      break

print(sum)