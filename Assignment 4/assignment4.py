"""Assignment 4 - Enoch Leow 30600022"""

from math import inf
class Graph:
    def __init__(self, gfile):
        """
        Initialse Graph
        :time-complexity: function must run in O(V)^2 where V are the number of nodes in graph
        :auxiliary-space: uses O(V)^2 auxiliary-space where V are the number of nodes in graph
        :param gfile: .txt file containing graph data (nodes + weights)
        """
        self.size = 0                                                       # initial parameters
        self.nodes = []
        self.num_edge = 0
        self.edges = []
        self.readfile(gfile)                                                # calls read file function

    def readfile(self, filename):
        """
        Reads file into the graph continer
        :param filename: .txt file containing graph data (nodes + weights)
        :return: None
        """
        file = open(filename, "r")                                          # open file
        self.size = int(file.read(1))                                       # record graph size
        self.edges = [[] for i in range(self.size)]
        for i in file:                                                      # record each node
            if i != "\n":
                self.edges[int(i[0])].append((int(i[2]), int(i[4])))
                self.edges[int(i[2])].append((int(i[0]), int(i[4])))
                self.num_edge += 1
        file.close()
        for i in range(self.size):
            self.nodes.append(i)

    def shallowest_spanning_tree(self):
        """
        Finds the node which gives the shallowest spanning tree
        :time-complexity: O(V)^3 where V is the number of nodes in the graph.
        :return: tuple of (node, depth)
        """
        min = inf
        node = "unassigned"
        for i in range(self.size):                                          # checks each node
            temp = self.nodes.copy()
            temp.remove(i)
            res = self.aux_sst(i)                                           # calls auxiliary function
            if res < min:                                                   # returns node with min depth
                min = res
                node = i
        return node, min

    def aux_sst(self, startnode):
        """
        finds depth needed to reach all nodes from a starting node using
        breadth First Search Algorithm
        :param startnode: node (integer)
        :return: depth from node to reach all nodes
        """
        queue = [startnode, "next"]                                         # initialise queue
        remaining = self.nodes.copy()
        remaining.remove(startnode)
        depth = 1
        while queue != [] and remaining != []:                              # keep running queue
            if queue[0] == "next":                                          # if next depth, add indicator "next"
                depth += 1
                queue.pop(0)
            else:
                available = self.edges[queue[0]]                            # search all paths adjacent to node
                queue.pop(0)
                for node in available:
                    if node[0] in remaining:
                        remaining.remove(node[0])
                        queue.append(node[0])
                queue.append("next")
        return depth                                                        # return depth

    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        """
        Find the quickest path from home to ice to icecream to destination using dijkstra's algorithm
        :time-complexity: O(Elog(V )), where E is the number of edges in the graph and
        V is the number of nodes in the graph.
        :param home: node integer
        :param destination: node integer
        :param ice_locs: list of integers (nodes)
        :param ice_cream_locs: list of integers (nodes)
        :return: tuple (path length, node path)
        """
        routes = []
        for i in ice_locs:                                                  # try all combinations of ice and icecream-
            for j in ice_cream_locs:                                        # locations
                get_ice = self.dijk_route(home, i)
                get_cream = self.dijk_route(i, j)
                goto_party = self.dijk_route(j, destination)
                routes.append((get_ice[0]+get_cream[0]+goto_party[0],get_ice[1]+get_cream[1][1:]+goto_party[1][1:]))
        min = (inf, "idk")
        for i in routes:                                                    # return the one with lowest path length
            if i[0] < min[0]:
                min = i
        return min                                                          # return tuple (path length, node path)


    def dijk_route(self, start, end):
        """
        function for dijkstra's algorithm between 2 nodes
        :param start: integer node
        :param end: integer node
        :return: tuple, (path length, list of path)
        """
        queue = [[start, 0, None]]                                          # initialise queue
        node_status = []                                                    # tracks all node statuses
        dequeue = []
        for x in self.nodes:                                                # initialise status for all nodes
            node_status.append([x, "inactive", inf, None])
        node_status[start][1] = "active"
        while queue != []:                                                  # continues to run till all nodes are done
            current = queue[0][0]
            next = self.edges[current]
            for i in next:                                                  # checks all adjacent nodes to current
                if node_status[i[0]][1] == "inactive":                      # if not visited, add onto queue
                    queue.append([i[0], i[1]+queue[0][1], current])
                    node_status[i[0]][1] = "active"

                elif node_status[i[0]][1] != "ended":                       # checks if not already ended
                    index = 0
                    for a in queue:
                        if a[0] == i[0]:
                            break
                        index += 1
                    if queue[index][1] > queue[0][1] + i[1]:                # if path is quicker, move it in the queue
                        queue.pop(index)
                        insert = 0
                        for b in queue:
                            if b[1] < i[1]+queue[0][1]:
                                break
                            insert += 1
                        queue = queue[:index] + [[i[0], i[1]+queue[0][1], current]] + queue[index:]
            node_status[queue[0][0]] = [current, "ended", queue[0][1], queue[0][2]]
            dequeue.append(queue.pop(0))
        path = [end]
        now = end
        while now != start:                                                 # backtrack for path
            path.insert(0, node_status[now][3])
            now = node_status[now][3]
        walk = node_status[end][2]
        return (walk, path)                                                 # return (path length, list of path)

