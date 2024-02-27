
# Dijkstra's Algorithm for Knight's Shortest Path Problem with Docker
This repository contains an implementation of Dijkstra's algorithm to solve the Knight's Shortest Path Problem on a chessboard. The goal is to find the minimum-length path for a knight to traverse from an initial cell to a final cell on an empty chessboard.

# Knight's Shortest Path Problem
Problem Description
The Knight's Shortest Path Problem involves determining the shortest sequence of knight moves (L-shaped) to reach a target cell on a chessboard from a given starting position.

#Input
Initial cell coordinates (e.g., (1, 1))
Final cell coordinates (e.g., (8, 8))

#Output
The minimum-length sequence of moves for the knight to reach the final cell.


#Implementation Details
Dependencies
Python 3.x
** Dockerized Environment
--> ** for implementation in docker environment

# To run the implementation directly in a Python, follow these steps:

1. Install the required dependencies:

pip install -r requirements.txt

2. Run the dijkstra.py script:

python dijkstra.py


3. Enter the initial and final cell coordinates as prompted.

4. View the output:

5. The script prints the minimum-length sequence of moves for the knight.
6. The graph with the highlighted shortest path is saved as shortest_distance.png.
7. The graph structure is saved as shortest_distance.dot



# To run the implementation in a Docker container, follow these steps:

1. Build the Docker image:

docker build -t dijkstra .


2. Run the Docker container:

e.g. docker run -it -v /home/Dijkstra/:/workspace dijkstra
--> Notes: Mention the workpspace location to save the outputs.

3. Follow the prompts to enter the initial and final cell coordinates.

4. View the output:
The script prints the minimum-length sequence of moves for the knight.

# Additional Notes
The script incorporates Dijkstra's algorithm to find the shortest path.
The graph is constructed based on valid knight moves on an 8x8 chessboard.

