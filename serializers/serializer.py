# Base class (ie. interface) for Serializers
class Serializer:
    def serialize(cls, object):
        pass

    def deserialize(cls, source):
        pass
