from os.path import dirname, join


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./22i.txt")

    with open(path) as f:
        data = [line.strip('\n') for line in f.readlines()]
    
    instructions = data[-1]
    map = []
    row_len = max([len(row) for row in data[:-2]])
    for row in data[:-2]:
        map.append([row[i] if len(row) > i else ' ' for i in range(row_len)])

    return map, instructions + ' '



def move(map, pos, distance, direction):
    for _ in range(distance):
        new_pos = ((pos[0] + direction[0]) % len(map), (pos[1] + direction[1]) % len(map[0]))
        char = map[new_pos[0]][new_pos[1]]
        if char == '.':
            pos = new_pos
            continue
        elif char == '#':
            return pos

        while map[new_pos[0]][new_pos[1]] == ' ':
            new_pos = ((new_pos[0] + direction[0]) % len(map), (new_pos[1] + direction[1]) % len(map[0]))
            
        if map[new_pos[0]][new_pos[1]] == '#':
            return pos
        
        pos = new_pos

    return pos


def main():
    map, instructions = get_data()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d_index = 0
    distance = ''
    for i, char in enumerate(map[0]):
        if char == '.':
            current_pos = (0, i)
            break
    
    for char in instructions:
        if char.isnumeric() == False:
            current_pos = move(map, current_pos, int(distance), directions[d_index])
            distance = ''
            if char == 'R':
                d_index = (d_index + 1) % len(directions)
            elif char == 'L':
                d_index = (d_index - 1) % len(directions)
        else:
            distance += char

    print(1000 * (current_pos[0] + 1) + 4 * (current_pos[1] + 1) + d_index)
    

if __name__ == '__main__':
    main()