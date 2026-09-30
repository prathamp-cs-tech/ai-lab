def dfs(start, goal):
    visited = set()

    def search(state, path):
        # Goal reached
        if state == goal:
            return path

        visited.add(state)

        # Find blank tile (0)
        zero = state.index(0)
        row = zero // 3
        col = zero % 3

        # Possible moves: Up, Down, Left, Right
        moves = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for dr, dc in moves:
            new_row = row + dr
            new_col = col + dc

            # Check boundaries
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero = new_row * 3 + new_col

                # Create new state
                new_state = list(state)
                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                # Don't visit an already explored state
                if new_state not in visited:
                    result = search(new_state, path + [new_state])

                    if result is not None:
                        return result

        return None

    return search(tuple(start), [tuple(start)])


# Example
start = [
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
]

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solution = dfs(start, goal)

if solution:
    print("Solution found!")
    for state in solution:
        print()
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
else:
    print("No solution found")
