from visualization import render_frame, Cell, Maze, DisplayText
from random import choice

# Made non recursive to prevent max recursion limit
def depth_first_search_generation(maze: Maze, start: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:

    if start is None:
        start = maze.get_cell(0, 0)

    start.visited = True
    stack = [start]

    while stack:
        current = stack[-1]
        neighbors = [n for n in maze.get_neighbors(current) if not n.visited]

        if neighbors:
            neighbor = choice(neighbors)
            current.del_walls(neighbor)
            neighbor.visited = True
            stack.append(neighbor)
        else:
            stack.pop()

        render_frame([maze], delay) if visualize else None

    return maze

def prims_simple_generation(maze: Maze, start: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze:
    if start is None:
        start = maze.get_cell(0, 0)

    start.visited = True
    cells = [start]

    while cells:
        render_frame([maze], delay) if visualize else None

        # Pick a random visited cell
        cell = choice(cells)
        unvisited_neighbors = [n for n in maze.get_neighbors(cell) if not n.visited]

        if unvisited_neighbors:
            neighbor = choice(unvisited_neighbors)
            cell.del_walls(neighbor)
            neighbor.visited = True
            cells.append(neighbor)
        else:
            # No unvisited neighbors, remove cell
            cells.remove(cell)

    return maze

def prims_cell_based_generation(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze:
    if current is None:
        current = maze.get_cell(0, 0)

    current.visited = True
    frontiers = maze.get_neighbors(current)

    while frontiers:
        render_frame([maze], delay) if visualize else None

        # Pick a random frontier cell
        current = choice(frontiers)
        frontiers.remove(current)

        # Find visited neighbors
        visited_neighbors = [n for n in maze.get_neighbors(current) if n.visited]

        if visited_neighbors:
            neighbor = choice(visited_neighbors)
            current.del_walls(neighbor)
            current.visited = True

            # Add its unvisited neighbors to frontier
            for next_neighbor in maze.get_neighbors(current):
                if not next_neighbor.visited and next_neighbor not in frontiers:
                    frontiers.append(next_neighbor)

    return maze


def right_wall_follower(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    if current is None:
        current = maze.get_cell(0, 0)
    direction = 1  # Start facing RIGHT
    goal = maze.get_cell(maze.rows - 1, maze.cols - 1)

    while current != goal:
        current.highlight()
        current.visited = True
        render_frame([maze], delay) if visualize else None

        # Determine the direction indices for walls
        RIGHT, FRONT, LEFT = (direction + 1) % 4, direction, (direction - 1) % 4

        # Check walls relative to current direction
        right_wall = current.walls[RIGHT]
        front_wall = current.walls[FRONT]

        if not right_wall:
            # Turn right and move forward
            direction = RIGHT
            next_cell = maze.get_next_cell(current, direction)
            if next_cell is not None:
                current.unhighlight()
                current = next_cell
        elif not front_wall:
            # Move forward
            next_cell = maze.get_next_cell(current, FRONT)
            if next_cell is not None:
                current.unhighlight()
                current = next_cell
        else:
            # Turn left (or turn around if blocked)
            direction = LEFT

    current.highlight()
    current.visited = True
    render_frame([maze], delay) if visualize else None

    return maze

def dead_end_filling(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    # TODO implement dead end filling algorithm
    raise NotImplementedError

def dijkstra(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    if current is None:
        current = maze.get_cell(0, 0)

    goal = maze.get_cell(maze.rows - 1, maze.cols - 1)
    start = current # for later backtracking

    current.visited = True
    render_frame([maze], delay) if visualize else None

    distances = {cell: float("inf") for cell in maze.all_cells()}
    current_distance = 0

    distances[current] = current_distance
    neighbors = maze.navigable_neighbors(current)

    while current != goal:
        current_distance += 1
        next_neighbors = []
        for neighbor in neighbors:
            neighbor.visited = True

            distances[neighbor] = current_distance

            # Add all unvisited, navigable neighbors of this neighbor
            for n in maze.navigable_neighbors(neighbor):
                if not n.visited and n not in next_neighbors:
                    next_neighbors.append(n)

            if neighbor == goal:
                current = neighbor

        neighbors = next_neighbors
        render_frame([maze], delay) if visualize else None

    while current != start:
        current.highlight()
        render_frame([maze], delay) if visualize else None

        neighbors = maze.navigable_neighbors(current)

        current = min(neighbors, key=lambda n: distances[n])

    current.highlight()
    render_frame([maze], delay) if visualize else None

    return maze


def a_star(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    # TODO implement A* algorithm
    raise NotImplementedError