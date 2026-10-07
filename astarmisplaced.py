import heapq

def misplaced_tiles(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3
    moves = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors


def a_star(start, goal):
    pq = []
    h = misplaced_tiles(start, goal)
    heapq.heappush(pq, (h, 0, start, [start]))
    visited = set()
    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                h = misplaced_tiles(next_state, goal)
                new_f = new_g + h
                heapq.heappush(
                    pq,
                    (new_f, new_g, next_state, path + [next_state])
                )
    return None


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

path = a_star(start, goal)

for state in path:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()