import argparse
from models.graph import Graph
from serializers.tree_serializers import TreeSerializerFactory
from serializers.graph_serializers import GraphSerializerFactory

# Author: John Lewis. Email: john.arundel.lewis@gmail.com

# The Graph Demo uses a simple directed graph to find multiple paths from entrance ot exit, and also determine
# the safest and most dangerous ones.
class GraphDemo:
    def run(self):

        serializer_factory = GraphSerializerFactory.get_instance()
        json_serializer = serializer_factory.get_serializer("json")

        print "--- Graph Demo ---"
        print

        file = open("maps/multi_path.graph.json")
        graph_obj = json_serializer.deserialize(file.read())

        print "Safest path(s):"
        lowest_cost_paths = graph_obj.find_lowest_cost_paths("ENTRANCE", "EXIT", {"MONSTER": 2, "REWARD": -1})
        for path in lowest_cost_paths:
            for node in path.get_node_list():
                print node["value"]
        print
        print "Most dangerous path(s):"
        lowest_cost_paths = graph_obj.find_lowest_cost_paths("ENTRANCE", "EXIT", {"MONSTER": -2, "REWARD": 1})
        for path in lowest_cost_paths:
            for node in path.get_node_list():
                print node["value"]

# The tree demo makes use of a simple binary tree for traversing the map and finding a path from the entrance to exit.
class TreeDemo:
    def run(self):

        print "--- Tree Demo ---"
        print

        # Get an instance of the serializer factory.
        serializer_factory = TreeSerializerFactory.get_instance()

        json_serializer = serializer_factory.get_serializer("json")
        prefix_serializer = serializer_factory.get_serializer("prefix")

        # Loads the sample map from a JSON file.
        file = open("maps/sample.tree.json")
        tree = json_serializer.deserialize(file.read())

        # Display the path from entrance to exit.
        print "*** Path from ENTRANCE to EXIT:"
        print tree.path("EXIT")

        # Serializes the map using the prefix serializer:
        first_prefix_string = prefix_serializer.serialize(tree)
        print "First serialized prefix string:"
        print first_prefix_string

        # Deserialize the serialized string.
        tree2 = prefix_serializer.deserialize(first_prefix_string)

        # Now serialize it again:
        second_prefix_string = prefix_serializer.serialize(tree)
        print "Second serialized prefix string:"
        print second_prefix_string

        if first_prefix_string == second_prefix_string:
            print "They are equal."

        print "and serialized out back to JSON again:"
        print json_serializer.serialize(tree2)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--graph-demo', help='Run the Graph Demo', action='store_true')
    parser.add_argument('--tree-demo', help='Run the Tree Demo', action='store_true')

    args = parser.parse_args()

    if not (args.tree_demo or args.graph_demo):
      parser.print_help()
    else:
        if args.graph_demo:
            GraphDemo().run()
        if args.tree_demo:
            TreeDemo().run()


