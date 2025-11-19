"""Неорієнтований граф"""

def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
        
         # since the graph is undirected
        adj[v].append(u)
    return adj
  

if __name__ == "__main__":
    V = 3

    # List of edges (u, v)
    edges = [[0, 1], [0, 2], [1, 2]]

    # Build the graph using edges
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):
        
        # Print the vertex
        print(f"{i}:", end=" ")
        for j in adj[i]:
            
            # Print its adjacent
            print(j, end=" ")
        print()

"""Орієнтований граф"""

def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    # Add each edge to the adjacency list
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

    return adj
  

if __name__ == "__main__":
    V = 3

    # List of edges (u, v)
    edges = [[1, 0], [1, 2], [2, 0]]

    # Build the graph using edges
    adj = createGraph(V, edges)

    print("Adjacency List Representation:")
    for i in range(V):
        
        # Print the vertex
        print(f"{i}:", end=" ")
        for j in adj[i]:
            
            # Print its adjacent
            print(j, end=" ")
        print()