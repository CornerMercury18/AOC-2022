from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./3i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]

sum = 0
for item in data:
  l, r = item[0:len(item)//2], item[len(item)//2: len(item)]
  for char in l:
    if char in r:
      if char.isupper():
        sum += ord(char) - 64 + 26
      else:
        sum += ord(char) - 96
     
      break


print(sum)