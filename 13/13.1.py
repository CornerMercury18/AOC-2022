from os.path import dirname, join

current_dir = dirname(__file__)
path = join(current_dir, "./13i.txt")

def is_in_order(left, right):
    for l, r in zip(left, right):
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return True
            elif l > r:
                return False
        else:
            if isinstance(l, int):
                l = [l]
            elif isinstance(r, int):
                r = [r]
                
            outcome = is_in_order(l, r)
            if outcome != None:
                return outcome
    
    if len(left) < len(right):
        return True
    elif len(right) < len(left):
        return False


with open(path, 'r') as f:
    data = [line.strip('\n') for line in f.readlines()]

sum = 0
for i in range(0, len(data), 3):
    if is_in_order(eval(data[i]), eval(data[i+1])):
        sum += i // 3 + 1
    

print(sum)

