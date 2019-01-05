from collections import deque

def rotate(state, pipe_numbers):

    queue = deque(state)
    rotations = []

    for i in range(len(state)):

        if all([queue[i] == 1 for i in pipe_numbers]):
            rotations.append(i)
        queue.rotate(1)

    return rotations

B = rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1])
if __name__ == '__main__':
     #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"
