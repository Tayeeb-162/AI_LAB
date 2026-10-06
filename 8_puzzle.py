import heapq

GOAL = ("1", "2", "3", "4", "5", "6", "7", "8", "_")


def manhattan_distance(state):
    distance = 0

    for i in range(9):
        if state[i] != "_":
            goal = GOAL.index(state[i])

            current_row = i // 3
            current_col = i % 3

            goal_row = goal // 3
            goal_col = goal % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


def actions(state):
    moves = []

    blank = state.index("_")
    row = blank // 3
    col = blank % 3

    if row > 0:
        moves.append("UP")

    if row < 2:
        moves.append("DOWN")

    if col > 0:
        moves.append("LEFT")

    if col < 2:
        moves.append("RIGHT")

    return moves


def child_node(state, action):
    new_state = list(state)
    blank = new_state.index("_")

    if action == "UP":
        new_blank = blank - 3
    elif action == "DOWN":
        new_blank = blank + 3
    elif action == "LEFT":
        new_blank = blank - 1
    else:
        new_blank = blank + 1

    new_state[blank], new_state[new_blank] = \
        new_state[new_blank], new_state[blank]

    return tuple(new_state)


def solvable(state):
    values = [int(x) for x in state if x != "_"]
    inversions = 0

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                inversions += 1

    return inversions % 2 == 0


def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(state[i:i + 3]))


def a_star(start):
    frontier = []
    counter = 0

    g = 0
    h = manhattan_distance(start)
    f = g + h

    heapq.heappush(
        frontier,
        (f, counter, start, [], g)
    )

    explored = set()

    while frontier:
        f, _, state, path, g = heapq.heappop(frontier)

        if state in explored:
            continue

        explored.add(state)

        if state == GOAL:
            return path, g

        for action in actions(state):
            child = child_node(state, action)

            if child not in explored:
                new_g = g + 1
                h = manhattan_distance(child)
                new_f = new_g + h

                counter += 1

                heapq.heappush(
                    frontier,
                    (
                        new_f,
                        counter,
                        child,
                        path + [(action, child)],
                        new_g
                    )
                )

    return None, None


start = []

for i in range(3):
    start.extend(input().split())

start = tuple(start)

if len(start) != 9 or set(start) != set(GOAL):
    print("Invalid input")

elif not solvable(start):
    print("No solution exists")

else:
    result, cost = a_star(start)

    if result is None:
        print("Failure")

    else:
        print("Initial State:")
        print_state(start)

        for action, state in result:
            print()
            print("Move:", action)
            print_state(state)

        print()
        print("Goal State Reached")
        print("Solution Cost:", cost)
        print("Game Solved")
