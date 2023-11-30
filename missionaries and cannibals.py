class State:
    def __init__(self, left_m, left_c, boat, right_m, right_c):
        self.left_m = left_m
        self.left_c = left_c
        self.boat = boat
        self.right_m = right_m
        self.right_c = right_c

    def __eq__(self, other):
        return (
            self.left_m, self.left_c, self.boat, self.right_m, self.right_c
        ) == (
            other.left_m, other.left_c, other.boat, other.right_m, other.right_c
        )

    def __hash__(self):
        return hash((self.left_m, self.left_c, self.boat, self.right_m, self.right_c))

    def __str__(self):
        return f"Left: {self.left_m}M-{self.left_c}C | Boat: {self.boat} | Right: {self.right_m}M-{self.right_c}C"


def is_valid(state):
    if (state.left_m < state.left_c and state.left_m > 0) or (state.right_m < state.right_c and state.right_m > 0):
        return False
    return 0 <= state.left_m <= 3 and 0 <= state.left_c <= 3 and 0 <= state.right_m <= 3 and 0 <= state.right_c <= 3


def generate_successors(current_state):
    successors = []
    for move_m in range(3):
        for move_c in range(3):
            if 0 < move_m + move_c <= 2:
                new_state = State(
                    current_state.left_m - move_m * current_state.boat,
                    current_state.left_c - move_c * current_state.boat,
                    1 - current_state.boat,
                    current_state.right_m + move_m * current_state.boat,
                    current_state.right_c + move_c * current_state.boat
                )
                if is_valid(new_state):
                    successors.append(new_state)
    return successors


def dfs_search_with_path(initial_state, goal_state, visited):
    stack = [(initial_state, [])]
    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return True, path + [current_state]
        visited.add(current_state)
        successors = generate_successors(current_state)
        for successor in successors:
            if successor not in visited:
                stack.append((successor, path + [current_state]))
    return False, []

def solve_missionaries_cannibals_with_path():
    initial_state = State(3, 3, 1, 0, 0)
    goal_state = State(0, 0, 0, 3, 3)
    visited = set()
    found_solution, path = dfs_search_with_path(initial_state, goal_state, visited)
    if found_solution:
        print("Solution found:")
        for state in path:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_missionaries_cannibals_with_path()
