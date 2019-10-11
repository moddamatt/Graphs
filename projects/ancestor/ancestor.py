
def earliest_ancestor(ancestors, starting_node):

    # If starting node has no parents return -1

    # else
    # Write a function that, given the dataset and the ID of an individual in the dataset,
    # returns their earliest known ancestor – the one at the farthest distance from the 
    # input individual. If there is more than one ancestor tied for "earliest", return 
    # the one with the lowest numeric ID.

    #  The input will not be empty.
    #  There are no cycles in the input.
    #  There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
    #  IDs will always be positive integers.
    #  A parent may have any number of children.

    # ancestors is and array of pairs order as [parent, child]
    # From starting_node we have to find a parent if any
    # If parent is found restart the loop
    # else return that parent

    # Step one create a graph of all points
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        # build edges in reverse
        graph.add_edge(pair[1], pair[0])

    q = Queue()
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if(len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor


    """ 
        Example input
        6

        1 3
        2 3
        3 6
        5 6
        5 7
        4 5
        4 8
        8 9
        11 8
        10 1
        Example output
        10
    """
    pass

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex]= set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can not create edge based on given vertices")

        """        
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 not in self.vertices:
            self.add_vertex(v1)
        elif v2 not in self.vertices:
            self.add_vertex(v2)
        """

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
