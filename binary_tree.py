__author__ = 'john'
import copy
import logging

class BinaryTree:
    # Construct from a dict.
    def __init__(self, tree_dict):
        if tree_dict:
            self.tree_dict = tree_dict
        else:
            raise Exception("tree_dict cannot be null")

    # Returns an in order traversal of the tree.
    def in_order(self):
        return self.__in_order(self.tree_dict)

    # Returns an pre-order traversal of the tree.
    def pre_order(self):
        return self.__pre_order(self.tree_dict)

    # Returns an post-order traversal of the tree.
    def post_order(self):
        return self.__post_order(self.tree_dict)

    # Returns path from the root to node with "to_value"
    def path(self, to_value):
        path = self.__path(self.tree_dict, to_value, {"to_node_found": False})
        path.reverse()
        return path

    def as_dict(self):
        return copy.deepcopy(self.tree_dict)

    def __in_order(self, dict):
        list = []
        if "left" in dict:
            list.extend(self.__in_order(dict["left"]))
        list.append(dict.get("value", None))
        if "right" in dict:
            list.extend(self.__in_order(dict["right"]))
        return list

    def __pre_order(self, dict):
        list = []
        list.append(dict.get("value", None))
        if "left" in dict:
            list.extend(self.__pre_order(dict["left"]))
        else:
            list.append("NULL") # Add terminal node indicator
        if "right" in dict:
            list.extend(self.__pre_order(dict["right"]))
        else:
            list.append("NULL")  # Add terminal node indicator

        return list

    def __post_order(self, dict):
        list = []
        if "left" in dict:
            list.extend(self.__post_order(dict["left"]))
        if "right" in dict:
            list.extend(self.__post_order(dict["right"]))

        list.append(dict.get("value", None))

        return list

    # Recursively searches for the to node.
    def __path(self, dict, to_value, state):
        list = []
        if not state["to_node_found"]:
            if to_value == dict.get("value", None):
                state["to_node_found"] = True
            else:
                if "left" in dict:
                    list.extend(self.__path(dict["left"], to_value, state))

                if "right" in dict:
                    list.extend(self.__path(dict["right"], to_value, state))

        if state["to_node_found"]:
            list.append(dict.get("value", None))

        return list