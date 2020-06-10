### Date created
June 10th, 2020

### Project Title
Puzzle Search

### Description
Python code  to perform a set of algorithmic searches in order to find the solution to an 8-puzzle game.
The code searches for a search-path to reach any target 8-puzzle configuration starting from
any source configuration. It uses and compares 3 algorithms for this purpose
* Breadth-first-search (BFS)
* Depth-first-search (DFS)
* A* search, with a cost function
Note that this code is WIP
* BFS and DFS work - but with some source-target combinations they do not reach a result in a reasonable amount if iterations (200,000)
* A* is still in debug mode

### Files used
puzzle_search.py
Can be run from any Python capable console - code does not use Numpy or Panda, nor external files

### Credits
This code originates from an assignment which is part of the CSMM101x course (Artificial intelligence) from Columbia University, delivered via EDX.ORG
