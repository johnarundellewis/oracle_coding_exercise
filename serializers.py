import json
from binary_tree import BinaryTree

# Base class (ie. interface) for TreeSerializers
class TreeSerializer:
    def serialize(cls, tree):
        pass

    def deserialize(cls, source):
        pass

# Serializes a binary tree to JSON.
class JSONSerializer(TreeSerializer):

    def serialize(self, tree):
        return json.dumps(tree.as_dict())

    def deserialize(self, source):
        return BinaryTree(json.loads(source))

# Serializes the tree into a custom (but concise) text format.
class PrefixSerializer(TreeSerializer):

    symbol_map = {
        "ENTRANCE": "E",
        "EXIT": "X",
        "MONSTER": "M",
        "TREASURE": "T",
        "EMPTY": "_",
        "NULL": "."
    }

    reverse_symbol_map = dict(reversed(item) for item in symbol_map.items())

    def serialize(self, tree):
        str = ""
        values = tree.pre_order()
        for value in values:
            symbol = self.symbol_map.get(value, None)
            str += symbol
        return str

    def deserialize(self, source):
        dict = self.__build_dict(source, {"index": 0})
        return BinaryTree(dict)

    def __build_dict(self, source, state):
            dict = {}
            if state["index"] < len(source):
                c = source[state["index"]]
                state["index"] += 1

                if c != ".":
                    node_value = self.reverse_symbol_map[c]
                    dict["value"]  = node_value
                    lhs = self.__build_dict(source, state)
                    if lhs:
                        dict["left"] = lhs

                    rhs = self.__build_dict(source, state)
                    if rhs:
                        dict["right"] = rhs
                    return dict
                else:
                    return None
            else:
                return None


# Factory for providing serializers
class SerializerFactory:
    __instance = None

    def __init__(self):
        self.serializers = { "json": JSONSerializer(),  "prefix":  PrefixSerializer()}

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SerializerFactory()
        return cls.__instance

    def get_serializer(self, type):
        if type in self.serializers:
            return self.serializers[type]
        else:
            raise Exception("No such serializer")
