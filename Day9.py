#Python
from colorsys import yiq_to_rgb
from pathlib import Path
from Common import read_grid

INPUT = Path('day9_input.txt')

if __name__ == '__main__':

    red = read_grid(INPUT)
    # find largest rectangle
    max_area = 0
    for c1 in range(len(red)-1):
        for c2 in range(c1+1,len(red)):
            area = (abs(red[c1][0]-red[c2][0])+1) * (abs(red[c1][1]-red[c2][1])+1)
            if area > max_area:
                max_area = area
    print(f'Part 1: {max_area}')

    # part 2 - find largest rectangle that does not include any uncolored locations

    # Big Idea: topologically compress the puzzle so it is tractable
    # map each x,Y coordinate to 0..n ordered coordinates skipping every other number
    # e.g., if you had points (1,1), (1,4), (100,4), (100,200), ...
    # you would map x=1 to 10, x=100 to 2, y=1 to 0, y=4 to 2, y=200 to 4
    # This preserves the relative locations of all points, but compresses the space

    # Then we can flood fill the uncolored locations starting from outside the min/max x/y
    # Any location not reached by flood fill is colored

    #extract a list of unique x and y coordinates
    xs = set()
    ys = set()
    for r in red:
        xs.add(r[0])
        ys.add(r[1])
    xs = sorted(xs)
    ys = sorted(ys)
    index = 0
    x_map = {}
    y_map = {}
    for x in xs:
        x_map[x] = index
        index += 2
    max_x = index-1
    for y in ys:
        y_map[y] = index
        index += 2
    max_y = index-1

    # now connect pairs of compressed coordinates
    colored: set[tuple[int,int]] = set()
    last_red = red[len(red)-1]
    for r in red:
        for x in range(min(x_map[r[0]],x_map[last_red[0]]), max(x_map[r[0]],x_map[last_red[0]])+1):
            for y in range(min(y_map[r[1]],y_map[last_red[1]]), max(y_map[r[1]],y_map[last_red[1]])+1):
                colored.add((x,y))
        last_red = r

    # flood fill from outside min/max x/y
    list_to_visit: list[tuple[int,int]] = [(-1,-1)]
    uncolored: set[tuple[int,int]] = set()
    while len(list_to_visit) > 0:
        loc = list_to_visit.pop()
        if loc[0] < -1 or loc[1] < -1 or loc[0] > max_x or loc[1] > max_y:
            continue
        if loc in colored or loc in uncolored:
            continue
        uncolored.add(loc)
        # add neighbors
        list_to_visit.append((loc[0]-1, loc[1]))
        list_to_visit.append((loc[0]+1, loc[1]))
        list_to_visit.append((loc[0], loc[1]-1))
        list_to_visit.append((loc[0], loc[1]+1))

    # now find largest rectangle that does not include any uncolored locations
    max_area = 0
    for c1 in range(len(red) - 1):
        for c2 in range(c1 + 1, len(red)):
            # check if any uncolored locations are inside the rectangle
            has_uncolored = False
            for x in range(min(x_map[red[c1][0]], x_map[red[c2][0]]), max(x_map[red[c1][0]], x_map[red[c2][0]]) + 1):
                for y in range(min(y_map[red[c1][1]], y_map[red[c2][1]]), max(y_map[red[c1][1]], y_map[red[c2][1]]) + 1):
                    if (x, y) in uncolored:
                        has_uncolored = True
                        break
                if has_uncolored:
                    break
            if has_uncolored:
                continue
            area = (abs(red[c1][0] - red[c2][0]) + 1) * (abs(red[c1][1] - red[c2][1]) + 1)
            if area > max_area:
                max_area = area
    print(f'Part 2: {max_area}')
