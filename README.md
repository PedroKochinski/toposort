# Topological Sorting of Directed Acyclic Graphs using Depth-First Search

This is a project for implementing topological sorting on Directed Acyclic Graphs (DAGs) using the Depth-First Search (DFS) algorithm in Python. Topological sorting is a common operation in graph theory, involving determining a linear order of vertices in a DAG. This implementation uses the NetworkX and Pygraphviz libraries to represent the DAG and perform topological sorting based on the DFS algorithm.

## Summary

Topological sorting is a fundamental operation in graph theory with various practical applications, including project task scheduling, resolving dependencies in software systems, and detecting cycles in directed graphs. In this project, we present an approach based on the Depth-First Search (DFS) algorithm to solve the topological sorting problem in a DAG.

## Implementation Details

The implementation of this topological sorting algorithm using DFS is done in Python and follows these key steps:

### 1. Representation of the DOT Graph

The input graph is read from the standard input using the NetworkX and Pygraphviz libraries. The input is expected to be in the DOT format, which describes the vertices and edges of the DAG.

### 2. Topological Sorting

The topological sorting algorithm encapsulates the depth-first search algorithm. At the beginning of the algorithm, data structures are defined, including a set of visited vertices and a list called "ordering." For each vertex in the graph, it checks if it has been visited. If it has not been visited, the depth-first search is called for that vertex. The topological ordering is obtained in the "ordering" list.

```python
def topological_sort_dfs(graph):
    visited = set()
    ordering = []
    for vertex in graph.nodes():
        if vertex not in visited:
            dfs_post_order(graph, vertex, visited, ordering)
    return ordering
```

### 3. Depth-First Search (DFS)

The `dfs_post_order` function performs depth-first search on the graph. It visits each unvisited vertex, explores its neighbors, and stores the post-order of the vertices at the beginning of the "ordering" list, thereby obtaining the topological ordering.

```python
def dfs_post_order(graph, vertex, visited, ordering):
    visited.add(vertex)
    for neighbor in graph.successors(vertex):
        if neighbor not in visited:
            dfs_post_order(graph, neighbor, visited, ordering)
    ordering.insert(0, vertex)
```

## Execution Instructions

To run the program, follow these steps:

1. Execute the `make` command to compile the program, if necessary.
2. Run the program using the command `./toposort < input.txt`, where `input.txt` is a file containing input data in the format described in the assignment, representing a graph in DOT format.
3. The result of the topological sorting will be saved in the `output.txt` file.

Ensure that the input and output files are correctly configured for the program to execute correctly.

This project provides an efficient solution for topological sorting of Directed Acyclic Graphs using depth-first search in Python. We hope it proves useful for your DAG topological sorting needs.
