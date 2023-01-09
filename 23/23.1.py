from os.path import dirname, join


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./23i.txt")
    elf_poses = set() 

    with open(path) as f:
        #flipped in y axis so increasing y index is North
        data = list(reversed([[char for char in line.strip('\n')] for line in f.readlines()]))
    
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            if char == '#':
                elf_poses.add((x, y))

    return elf_poses


def round(poses, props):
    new_poses = set()
    poses_to_check = set()
    for x, y in poses:
        adjacents = [(x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1)]
        for adjacent in adjacents:
            if adjacent in poses:
                poses_to_check.add((x, y))
                break
        else:
            new_poses.add((x,y))

    pos_dict = {}
    for x, y in poses_to_check:
        new_pos = (x, y)
        for x_, y_ in props:
            if y_ == 0:
                if ((x + x_, y - 1) not in poses and
                    (x + x_, y) not in poses and
                    (x + x_, y + 1) not in poses):
                    new_pos = (x + x_, y)
                    break
            else:
                if ((x - 1, y + y_) not in poses and
                    (x, y + y_) not in poses and
                    (x + 1, y + y_) not in poses):
                    new_pos = (x , y + y_)
                    break
        
        if pos_dict.get(new_pos) == None:
            pos_dict[new_pos] = [] 

        pos_dict[new_pos].append((x, y))
    
    for new_pos, original_poses in pos_dict.items():
        if len(original_poses) != 1:
            for pos in original_poses:
                new_poses.add(pos)
        else:
            new_poses.add(new_pos)

    return new_poses

def main():
    poses = get_data()
    props = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for _ in range(10):
        poses = round(poses, props)
        props.append(props.pop(0))

    min_x = float('inf')
    max_x = -float('inf')
    min_y = float('inf')
    max_y = -float('inf')
    for x, y in poses:
        min_x = min([x, min_x])
        max_x = max([x, max_x])
        min_y = min([y, min_y])
        max_y = max([y, max_y])
    
    for y in reversed(range(min_y, max_y + 1)):
        for x in range(min_x, max_x + 1):
            if (x,y) in poses:
                print('#', end='')
            else:
                print('.', end='')
        
        print()

    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(poses))

if __name__ == '__main__':
    main()