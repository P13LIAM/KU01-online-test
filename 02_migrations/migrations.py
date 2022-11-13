from collections import defaultdict

class Graph:
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
  
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
    """
    A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]
    """
    def printAllPathsUtil(self, u, d, visited, path, all_path):
 
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            all_path.append(path.copy())
            # print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPathsUtil(i, d, visited, path, all_path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
 
        # Create an array to store paths
        path = []
        all_path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path, all_path)
        
        return all_path


def form_shape(coor_dict):
    H = max([k[0] for k in coor_dict.keys()]) + 1
    W = max([k[1] for k in coor_dict.keys()]) + 1

    mat3 = ""
    for i in range(H):
        for j in range(W):
            mat3 += coor_dict[(i, j)]
        mat3 += '\n'
        
    return mat3[:-1]


def matrixstr2coordict(mat):
    mat2 = mat.split('\n')[1:-1]

    H = len(mat2)
    W = len(mat2[0])

    coor_dict = {}
    nodes = {}
    for i, seq in enumerate(mat2):
        for j, symbol in enumerate(seq):
            coor_dict[(i, j)] = symbol
            nodes[i*W + j] = symbol
    
    return coor_dict, nodes, H, W


def patient_filtered(coor_dict, nodes, start_point, L, W = None):
    
    if W is None:
        W = max([k[1] for k in coor_dict.keys()]) + 1

    for k, v in coor_dict.items():
        if abs(k[0] - start_point[0]) > L:
            coor_dict[k] = '#'
            nodes[k[0]*W + k[1]] = '#'
    
    return coor_dict, nodes


def createGraph(nodes, W):
    G = Graph(len(nodes))

    for node, v in nodes.items():
        if v == '#':
            continue
        else:
            neighbors_nodes = [node + 1, node - 1, node + W, node - W]
            for node2 in neighbors_nodes:
                if nodes.get(node2, "#") != "#":
                    G.addEdge(node, node2)
    
    return G


def findpaths_Graph(G, node1, node2, W):
    node1_int = node1[0]*W + node1[1]
    node2_int = node2[0]*W + node2[1]
        
    all_paths = G.printAllPaths(node1_int, node2_int)

    all_paths_node = [[(e//W, e%W) for e in path] for path in all_paths]
    
    return all_paths_node, all_paths


def check_reachable(coor_dict, nodes, W, node1, node2, L):
    coor_dict2 = coor_dict.copy()
    nodes2 = nodes.copy()
    coor_dict2, nodes2 = patient_filtered(coor_dict2, nodes2, node1, L, W)

    print("Matrix_filtered:\n", form_shape(coor_dict2), "\n")
    
    G = createGraph(nodes2, W)
    
    all_paths_node, all_paths = findpaths_Graph(G, node1, node2, W)
    
    return int(len(all_paths_node) != 0)


if __name__ == "__main__":
    mat = f"""
##......##
##.####.##
#....##...
#.##....##
..####.###
##...#...#
"""

    coor_dict, nodes, H, W = matrixstr2coordict(mat)
    print("Matrix:\n", form_shape(coor_dict), "\n")

    list_input_check = ["5 1 3 10 10", "5 1 6 3 10", "5 1 6 9 1", "5 1 6 9 2", "4 2 3 9 2"]
    list_reachable = []
    for input_check in list_input_check:
        print("input: ", input_check, '\n')
        i1, j1, i2, j2, L = [int(e) for e in input_check.split(' ')]
        node1 = (i1-1, j1-1)
        node2 = (i2-1, j2-1)
        output = check_reachable(coor_dict, nodes, W, node1, node2, L)
        list_reachable.append(output)
        print("reachable: ", output, '\n')

    print("list_reachable: ", list_reachable)


    mat = f"""
.....
.....
.....
.....
.....
"""

    coor_dict, nodes, H, W = matrixstr2coordict(mat)
    print("Matrix:\n", form_shape(coor_dict), "\n")

    list_input_check = ["2 1 1 5 0", "2 1 2 5 0", "2 1 3 5 1", "2 1 4 5 1", "2 1 5 5 3"]
    list_reachable = []
    for input_check in list_input_check:
        print("input: ", input_check, '\n')
        i1, j1, i2, j2, L = [int(e) for e in input_check.split(' ')]
        node1 = (i1-1, j1-1)
        node2 = (i2-1, j2-1)
        output = check_reachable(coor_dict, nodes, W, node1, node2, L)
        list_reachable.append(output)
        print("reachable: ", output, '\n')

    print("list_reachable: ", list_reachable)