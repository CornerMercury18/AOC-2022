from os.path import dirname, join


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./24i.txt")

    blizzards = {}

    with open(path) as f:
        for y, row in enumerate(f.readlines()[1:-1]):
            for x, char in enumerate(row.strip('\n')[1:-1]):
                match char:
                    case 'v':
                        dir = (1, 0)
                    case '>':
                        dir = (0, 1)
                    case '^':
                        dir = (-1, 0)
                    case '<':
                        dir = (0, -1)
                    case _:
                        continue
                
                blizzards[(y, x)] = [dir]


    return blizzards, (y, x)

def get_next_blizzard(blizzards, max_pos):
    new_blizzards = {}
    for pos, blizzard_list in blizzards.items():
        for blizzard_dir in blizzard_list:
            new_pos = (
                (pos[0] + blizzard_dir[0]) % (max_pos[0]+1),
                (pos[1] + blizzard_dir[1]) % (max_pos[1]+1)
            )
            if new_pos not in new_blizzards:
                new_blizzards[new_pos] = [blizzard_dir]
            else:
                new_blizzards[new_pos].append(blizzard_dir)

    return new_blizzards

#also returns current_pos
def get_adjacents(pos, max_pos, start_pos, end_pos):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
    adjacents = []
    for dir in dirs:
        new_pos = tuple(sum(x) for x in zip(pos, dir))
        if 0 <= new_pos[0] <= max_pos[0] and 0 <= new_pos[1] <= max_pos[1]:
            adjacents.append(new_pos)
        elif new_pos == end_pos or new_pos == start_pos:
            adjacents.append(new_pos)
    
    return adjacents

def bfs(blizzards, start_pos, end_pos, max_pos):
    neighbours = {start_pos}
    depth = 0

    while end_pos not in neighbours:
        depth += 1
        blizzards = get_next_blizzard(blizzards, max_pos)
        new_neighbours = set()
        for pos in neighbours:
            for new_neighbour in get_adjacents(pos, max_pos, start_pos, end_pos):
                if new_neighbour not in blizzards:
                    new_neighbours.add(new_neighbour)
        
        neighbours = new_neighbours

    return depth

def output_map(blizzards, max_pos):
    print('#.' + '#' * (max_pos[1] + 1))
    for y in range(max_pos[0]+1):
        print('#', end='')
        for x in range(max_pos[1]+1):
            if (y, x) not in blizzards:
                print('.', end='')
                continue
                
            print(len(blizzards[(y, x)]), end='')
        
        print('#')
    print('#' * (max_pos[1] + 1) + '.#')
    


def main():
    blizzards, max_pos = get_data()
    end_pos = (max_pos[0] + 1, max_pos[1])
    print(bfs(blizzards, (-1, 0), end_pos, max_pos))



if __name__ == '__main__':
    main()