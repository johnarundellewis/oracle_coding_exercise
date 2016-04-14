from serializers import SerializerFactory

# Author: John Lewis. Email: john.arundel.lewis@gmail.com
if __name__ == "__main__":

    # Get an instance of the serializer factory.
    serializer_factory = SerializerFactory.get_instance()

    json_serializer = serializer_factory.get_serializer("json")
    prefix_serializer = serializer_factory.get_serializer("prefix")

    # Loads the sample map from a JSON file.
    file = open("maps/sample.json")
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