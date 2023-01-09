from os.path import dirname, join

activated = set()
visited = set()

def brute(current_edge, time=0, max_flow=0, current_flow=0):
    if time >= 30 or len(visited) == len(nodes):
        if current_flow > max_flow:
            max_flow = current_flow
        return max_flow
    
    if current_edge not in activated and current_edge != 'AA':
        activated.add(current_edge)
        flow = valves[current_edge][0]
        max_flow = brute(current_edge, time + 1, max_flow, current_flow + flow*(30-time-1))
        activated.discard(current_edge)
    
    
    for edge in nodes[current_edge].keys():
        if edge not in visited:
            weight = nodes[current_edge][edge]
            visited.add(edge)
            max_flow = brute(edge, time + weight, max_flow, current_flow)
            visited.discard(edge)
        
    return max_flow

current_dir = dirname(__file__)
path = join(current_dir, "./16i.txt")

with open(path) as f:
    data = [line.strip('\n').split() for line in f.readlines()]

connection_valves = {}
valves = {}
nodes = {}
for line in data:
    name = line[1]
    rate = int(line[4].split('=')[1][:-1])
    connections = ''.join(line[9:]).split(',')
    
    if rate == 0 and name != 'AA':
        connection_valves[name] = connections
    else:
        valves[name] = (rate, connections)
        nodes[name] = {}

    
    
for key, value in valves.items():
    for node in value[1]:
        weight = 1
        last_node = key
        current_node = node
        while current_node not in valves:
            edges = connection_valves[current_node]
            if edges[0] == last_node:
                last_node = current_node
                current_node = edges[1]
            else:
                last_node = current_node
                current_node = edges[0]
            
            weight += 1

        nodes[key][current_node] = weight
        nodes[current_node][key] = weight

print(brute('AA'))
 
        