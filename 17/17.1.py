from os.path import dirname, join

def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./17i.txt")

    with open(path) as f:
        return [char for char in f.readlines()[0].strip('\n')]


def output_grid(grid):
    [print(''.join(line)) for line in reversed(grid)]


def is_colliding(grid, rock, pos):
    for i, row in enumerate(rock):
        if i + pos[1] >= 0:
            return False
        for j, col in enumerate(row):
            # print(len(grid) + i + pos[1], j + pos[0])
            if col == '#' and grid[len(grid) + i + pos[1]][j + pos[0]] == '#':
                return True

def drop(grid, rock, flow, flow_index):
    x = 2
    for _ in range(3):
        if flow[flow_index % len(flow)] == '<':
            if x > 0:
                x -= 1
        else:
            if x + len(rock[0]) - 1 < 6:
                x += 1

        flow_index += 1
    
    y = 0
    went_down = True
    while went_down == True:
        if flow[flow_index % len(flow)] == '<':
            if x > 0:
                if not is_colliding(grid, rock, (x-1, y)):
                    x -= 1
        else:
            if x + len(rock[0]) - 1 < 6:
                if not is_colliding(grid, rock, (x+1, y)):
                    x += 1
        
        flow_index += 1
        if not is_colliding(grid, rock, (x, y-1)):
            y -= 1
        else:
            went_down = False

    increment = 0
    for i, row in enumerate(rock):
        if y + i >= 0:
            grid.append(['.' for _ in range(7)])
        else:
            increment += 1
        for j, col in enumerate(row):
            if col == '#':
                grid[len(grid) - 1 + y + increment][j + x] = '#'

    return grid, flow_index



def main():
    flow = get_data()
    rocks = [
        [
            ['#', '#', '#', '#']
        ],
        [
            ['.', '#', '.'],
            ['#', '#', '#'],
            ['.', '#', '.']
        ],
        [
            ['#', '#', '#'],
            ['.', '.', '#'],
            ['.', '.', '#']
        ],
        [
        
            ['#'],
            ['#'],
            ['#'],
            ['#']
        ],
        [
            ['#', '#'],
            ['#', '#']
        ]
    ]
    grid = [['#' for _ in range(7)]]
    flow_index = 0
    for _ in range(2022):
        grid, flow_index = drop(grid, rocks[0], flow, flow_index)
        rocks.append(rocks.pop(0))

    print(len(grid) - 1)

if __name__ == '__main__':
    main()