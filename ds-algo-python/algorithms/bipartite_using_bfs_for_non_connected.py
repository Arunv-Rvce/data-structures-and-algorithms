"""
A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.
A bipartite graph is possible if the graph coloring is possible using two colors such that vertices in a set are colored with the same color. Note that it is possible to color a cycle graph with even cycle using two colors. For example, see the following graph.
"""
from enum import Enum
from typing import List


def is_bipartite(v: int, graph: List[List[int]], color_arr: List[int], src: int):
    class Color(Enum):
        RED = 1
        BLUE = 0

    color_arr[src] = Color.RED.value
    visited = [src]
    next_color = Color.BLUE
    while len(visited):
        u = visited.pop()

        if graph[u][u] == 1:
            return False

        for i in range(v):
            if graph[u][i] == 1 and color_arr[i] == -1:
                color_arr[i] = next_color.value
                next_color = next_color.BLUE if next_color == next_color.RED else next_color.RED
            elif graph[u][i] == 1 and color_arr[i] == color_arr[u]:
                return False
    return True


def check_all_the_subgraph_bipartite(v: int, graph: List[List[int]], color_arr: List[int]):
    for i in range(len(color_arr)):
        if color_arr[i] == -1:
            print(is_bipartite(v, graph, color_arr, i))


if __name__ == '__main__':
    V = 4
    graph = [[0, 1, 0, 1],
             [1, 0, 1, 0],
             [0, 1, 0, 1],
             [1, 0, 1, 0]]
    color_arr = [-1 for i in range(V)]
    check_all_the_subgraph_bipartite(V, graph, color_arr)

