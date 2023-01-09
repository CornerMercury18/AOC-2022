from os.path import dirname, join


def get_data():
    current_dir = dirname(__file__)
    path = join(current_dir, "./19i.txt")

    with open(path) as f:
        lines = [[robot.split() for robot in line.strip('\n').split('.')] for line in f.readlines()]
    
    return [
        ((int(blueprint[0][6]), 0, 0), 
        (int(blueprint[1][4]), 0, 0),
        (int(blueprint[2][4]), int(blueprint[2][7]), 0),
        (int(blueprint[3][4]), 0, int(blueprint[3][7])))
        for blueprint in lines
     ]


def eval_blueprint(blueprint, minutes):
    blue = list(reversed(blueprint))
    materials = [0, 0, 0, 0]
    robots = [1, 0, 0, 0]
    for _ in range(minutes):
        index = -1
        for i, robot in enumerate(blue):
            for j, ingredient in enumerate(robot):
                if materials[j] < ingredient:
                    break
            else:
                index = len(blue) - 1 - i
                for k, ingredient in enumerate(robot):
                    materials[k] = materials[k] - ingredient 
                
                break
        
        for i, robot_count in enumerate(robots):
            materials[i] = materials[i] + robot_count

        if index >= 0:
            robots[index] = robots[index] + 1
    
        print(materials)
        print('robots', robots)

    return materials[-1]


def main():
    blueprints = get_data()
    total = 0
    for i, blueprint in enumerate(blueprints):
        total += (i+1) * eval_blueprint(blueprint, 24)

    print(total)

if __name__ == '__main__':
    main()