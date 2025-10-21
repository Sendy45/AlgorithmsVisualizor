from visualization import render_frame, Cell, Maze, DisplayText
from random import shuffle

def depth_first_search(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:

    if current is None:
        current = maze.get_cell(0, 0)

    current.visited = True
    render_frame([maze], delay) if visualize else None

    neighbors = maze.get_neighbors(current)
    shuffle(neighbors)

    for neighbor in neighbors:
        if not neighbor.visited:
            current.del_walls(neighbor)
            depth_first_search(maze, neighbor, visualize, delay)

    return maze

def right_wall_follower(maze: Maze, current: Cell | None = None, visualize: bool = True, delay: float = 0.0) -> Maze | None:
    if current is None:
        current = maze.get_cell(0, 0)
    direction = 1  # Start facing RIGHT
    goal = maze.get_cell(maze.rows - 1, maze.cols - 1)

    while current != goal:
        current.visited = True
        if visualize:
            render_frame([maze], delay)

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
                current = next_cell
        elif not front_wall:
            # Move forward
            next_cell = maze.get_next_cell(current, FRONT)
            if next_cell is not None:
                current = next_cell
        else:
            # Turn left (or turn around if blocked)
            direction = LEFT

    return maze