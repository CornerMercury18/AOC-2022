from os.path import dirname, join


class Node:
    def __init__(self, value, original_value, prev_node=None, next_node=None):
        self.value = value
        self.original_value = original_value
        self.prev_node = prev_node
        self.next_node = next_node

    def mix(self):
        if self.value == 0:
            return

        self.prev_node.next_node = self.next_node
        self.next_node.prev_node = self.prev_node
        new_prev_node = self
        for _ in range(self.value):
            new_prev_node = new_prev_node.next_node
        
        new_next_node = new_prev_node.next_node

        new_prev_node.next_node = self
        self.prev_node = new_prev_node
        new_next_node.prev_node = self
        self.next_node = new_next_node

    def __str__(self):
        return f'Node({self.prev_node.original_value} -> _{self.original_value}_ -> {self.next_node.original_value})'



current_dir = dirname(__file__)
path = join(current_dir, "./20i.txt")

with open(path) as f:
  data = [int(line.strip('\n')) for line in f.readlines()]

nodes = []
for num in data:
    node = Node(num % (len(data)-1), num)
    if num == 0:
        start_node = node
    nodes.append(node)

for i, node in enumerate(nodes):
    node.prev_node = nodes[i-1]
    node.next_node = nodes[(i+1) % len(nodes)]


for node in nodes:
    node.mix()


next_node = start_node
total = 0
for _ in range(3):
    for _ in range(1000):
        next_node = next_node.next_node
    
    total += next_node.original_value

print(total)