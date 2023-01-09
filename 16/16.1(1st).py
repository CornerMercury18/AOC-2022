from os.path import dirname, join


def brute(current_edge, activated=set(), visited=set(), time=0, max_flow=0, current_flow=0):
    if time == 30:
        if current_flow > max_flow:
            max_flow = current_flow
        return max_flow, activated
    
    if current_edge not in activated:
        activated.add(current_edge)
        flow = valves[current_edge][0]
        max_flow, activated = brute(current_edge, activated, visited, time + 1, max_flow, current_flow + flow*(30-time+1))
        activated.discard(current_edge)
    
    visited.add(current_edge)
    
    for edge in valves[current_edge][1]:
        if edge not in visited:
            max_flow, activated = brute(edge, activated, visited, time + 1, max_flow, current_flow)
    
    visited.discard(current_edge)
    return max_flow, activated

current_dir = dirname(__file__)
path = join(current_dir, "./16i.txt")

with open(path, 'r') as f:
  data = [line.strip('\n') for line in f.readlines()]


valves = {}
for line in data:
    s = line.split()
    name = s[1]
    flow_rate = int(s[4].split('=')[1][:-1])
    edges = ''.join(s[9:]).split(',')
    valves[name] = (flow_rate, edges)

print(valves)


max_flow, activated = brute('AA') 
print(max_flow)