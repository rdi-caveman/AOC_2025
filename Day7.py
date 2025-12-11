#Python
from pathlib import Path

from Common import read_char_array

INPUT = Path('day7_input.txt')

if __name__ == '__main__':
    # read manifold, find start
    manifold = read_char_array(INPUT)
    for col in range (len(manifold[0])):
        if manifold[0][col] == 'S':
            start = col
            break

    beams = set()
    beams.add(start)
    splits = 0
    for row in range (1, len(manifold)):
        new_beams = set(beams)
        for col in beams:
            if manifold[row][col] == '^':
                splits += 1
                new_beams.remove(col)
                new_beams.add(col-1)
                new_beams.add(col+1)
        beams = new_beams
    print(f'Part 1: {splits}')

    # part 2
    total_timelines = 0
    row = 1
    particles = {start: 1}
    while row < len(manifold):
        new_particles = {}
        for col in particles.keys():
            count = particles.get(col)
            if manifold[row][col] == '^':
                new_particles[col-1] = new_particles.get(col-1, 0) + count
                new_particles[col+1] = new_particles.get(col+1, 0) + count
            else:
                new_particles[col] = new_particles.get(col, 0) + count
        particles = new_particles.copy()
        row += 1
    total_timelines = 0
    for col in particles.keys():
        total_timelines += particles.get(col)
    print(f'Part 2: {total_timelines}')
