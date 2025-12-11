# python
from pathlib import Path
from Common import read_grid

INPUT = Path('day8_input.txt')

if __name__ == '__main__':
    junctions = read_grid(INPUT)

    # find linear distance between each pair of junctions
    distance: list[tuple[int,int,float]] = []
    for j1 in range(len(junctions)-1):
        for j2 in range(j1+1, len(junctions)):
            x1, y1, z1 = junctions[j1]
            x2, y2, z2 = junctions[j2]
            dist = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
            distance.append((j1,j2,dist))

    # connect the 1000 closest junctions
    distance.sort(key=lambda t: t[2])   # sort by the 3rd element (the distance)
    circuits: list[set[int]] = []      # list of circuits
    found: list[set[int]] = []

    def add_junctions_to_circuits(d: tuple[int,int,float]):
        found = []
        j1, j2, dist = d
        for circuit in circuits:
            if j1 in circuit or j2 in circuit:
                found.append(circuit)
                circuit.add(j1)
                circuit.add(j2)
        if not found:
            new_circuit = set()
            new_circuit.add(j1)
            new_circuit.add(j2)
            circuits.append(new_circuit)
        if len(found) > 1:
            first = found[0]
            for other in found[1:]:
                for junc in other:
                    first.add(junc)
                circuits.remove(other)

    for d in distance[:1000]:  # connect the 1000 closest junctions
        add_junctions_to_circuits(d)

    # sort circuits by size
    circuits.sort(key=lambda c: len(c), reverse=True)
    product = 1
    for circuit in circuits[:3]: # find product of sizes of 3 largest circuits
        product *= len(circuit)
    print(f'Part 1: {product}')

    # part 2
    # Continue adding connections until all junctions are connected
    for d in distance[1000:len(distance)]:
        add_junctions_to_circuits(d)
        if len(circuits) == 1 and len(circuits[0]) == len(junctions):
            print(f'connection {d}')
            print(f'junctions connected  {junctions[d[0]]} and {junctions[d[1]]}')
            break
    print(f'Part 2: {junctions[d[0]][0] * junctions[d[1]][0]}')