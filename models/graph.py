# Represents a path through a graph. Internally it holds a list of nodes,
class Path:
        def __init__(self, node_list):
            if node_list:
                self.node_list = node_list
            else:
                raise Exception("node_list cannot be null")

        # Calculates path cost  given a map of values to costs. If no map is provided, the cost is the length.
        def cost(self, value_cost_map=None):
            if value_cost_map:
                cost = 0.0
                for node in self.node_list:
                    node_cost = value_cost_map.get(node["value"], 0)
                    cost += node_cost
                return cost
            else:
                return len(self.node_list)

        def get_node_list(self):
            return self.node_list

        def __str__(self):
            return "cost: %s, path: %s"  % (self.cost(), self.get_node_list().__str__())

class Graph:
        def __init__(self, graph_dict):
            if graph_dict:
                self.graph_dict = graph_dict
            else:
                raise Exception("graph_dict cannot be null")

        def find_path(self,start, end):
            return Path(self.__find_path(self.graph_dict, start, end))

        def find_all_paths(self, start ,end):
            return [Path(node_list) for node_list in self.__find_all_paths(self.graph_dict, start, end)]

        def find_shortest_path(self, start, end):
            return Path(self.__find_shortest_path(self.graph_dict, start, end))

        # Returns list of paths that have the lowest cost based on the provided value_cost_map
        def find_lowest_cost_paths(self, start, end, value_cost_map):
            all_paths = self.find_all_paths(start, end)
            # Only return paths that the same lowest cost.
            lowest_cost_paths = []
            lowest_cost = None

            # Note: The operation below has complexity O(2n) which is O(n).
            # First find lowest cost.
            for path in all_paths:
                path_cost = path.cost(value_cost_map)
                if not lowest_cost or path_cost < lowest_cost:
                    lowest_cost = path_cost

            # Now build list of paths with above lowest costs.
            for path in all_paths:
                path_cost = path.cost(value_cost_map)
                if path_cost == lowest_cost:
                    lowest_cost_paths.append(path)

            return lowest_cost_paths

        def as_dict(self):
            return self.graph_dict

        # The following methods adapted from https://www.python.org/doc/essays/graphs/ :
        def __find_path(self, graph, start, end, path=[]):
            path = path + [graph[start]]
            if start == end:
                return path
            if not graph.has_key(start):
                return None
            for node in graph[start].get("arcs", []):
                if node not in path:
                    newpath = self.__find_path(graph, node, end, path)
                    if newpath: return newpath
            return None

        def __find_all_paths(self, graph, start, end, path=[]):
            path = path + [graph[start]]
            if start == end:
                return [path]
            if not graph.has_key(start):
                return []
            paths = []
            for node in graph[start].get("arcs", []):
                if node not in path:
                    newpaths = self.__find_all_paths(graph, node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths

        def __find_shortest_path(self, graph, start, end, path=[]):
            path = path + [graph[start]]
            if start == end:
                return path
            if not graph.has_key(start):
                return None
            shortest = None
            for node in graph[start].get("arcs", []):
                if node not in path:
                    newpath = self.__find_shortest_path(graph, node, end, path)
                    if newpath:
                        if not shortest or len(newpath) < len(shortest):
                            shortest = newpath
            return shortest

