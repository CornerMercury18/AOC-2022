from os.path import dirname, join


# Set a given data in a dictionary with position provided as a list
def setInDict(dataDict, mapList, key):
    for k in mapList: 
      dataDict = dataDict[k]
    dataDict[key] = {}

def setTotalInDict(dataDict, mapList, value):
    for k in mapList: 
      dataDict = dataDict[k]
    if 'total' not in dataDict:
      dataDict['total'] = 0
    dataDict['total'] += value


def flood(dict, folder=None):
  subtotal = 0
  for key in dict.keys():
    if key != 'total':
      subtotal += flood(dict[key], key)
  
  if 'total' in dict:
    subtotal += dict['total']
  
  totals.append((subtotal, folder))
  #print(subtotal)
  return subtotal
  

current_dir = dirname(__file__)
path = join(current_dir, "./7i.txt")

with open(path, 'r') as f:
  lines = [line.strip('\n') for line in f.readlines()]


files = {}


for line in lines:
  if line.split()[1] == 'cd':
    command = line.split()[2]
    if command == '/':
      dir = []
    elif command == '..':
      dir.pop()
    else:
      dir.append(command)

  elif line.split()[0] == 'dir':
    setInDict(files, dir, line.split()[1])
  
  elif line.split()[0].isnumeric():
    setTotalInDict(files, dir, int(line.split()[0]))



print(files)


totals = []
flood(files)
print(totals)

total = 0
for value in totals:
  if value[0] <= 100000:
    total += value[0]

sort = list(sorted(totals, key=lambda x: x[0]))
print(total)

for item in sort:
  if item[0] >= 30000000 - 21251929:
    print(item)
    break

