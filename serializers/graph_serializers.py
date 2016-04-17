__author__ = 'john'
import json

from serializers.serializer import Serializer
from models.graph import Graph

# Serializes a graph to JSON.

class JSONSerializer(Serializer):

    def serialize(self, graph):
        return json.dumps(graph.as_dict())

    def deserialize(self, source):
        return Graph(json.loads(source))

# Factory for providing graph serializers
class GraphSerializerFactory:
    __instance = None

    def __init__(self):
        self.serializers = {"json": JSONSerializer()}

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = GraphSerializerFactory()
        return cls.__instance

    def get_serializer(self, type):
        if type in self.serializers:
            return self.serializers[type]
        else:
            raise Exception("No such serializer")

