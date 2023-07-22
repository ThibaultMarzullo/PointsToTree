from typing import Optional


class Node:
    name: str
    children: list("Node")
    parent: "Node"

    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, name):
        child = Node(name=name, parent=self)
        self.children.append(child)

        return child

    def get_child(self, name) -> Optional["Node"]:
        return next((c for c in self.children if c.name == name), None)

    def add_to_tree(self, path: list[str]):
        if len(path) == 0:
            return

        v = path.pop(0)
        child = self.get_child(v)
        if child is None:
            child = self.add_child(v)

        child.add_to_tree(path)

    def print_tree(self, depth=0):
        result = "  " * depth + self.name + "\n"
        for child in self.children:
            result += child.print_tree(depth + 1)

        return result

    def get_all_descendants(self):
        descendants = []
        for child in self.children:
            descendants.append(child)
            descendants += child.get_all_descendants()

        return descendants

    def get_path(self):
        if self.parent is None:
            return []
        else:
            return self.parent.get_path() + [self.name]


class PointTree:
    root: Node

    def __init__(self):
        self.root = Node("--")

    def add_to_tree(self, path: list[str]):
        self.root.add_to_tree(path)

    def __repr__(self):
        return self.root.print_tree()

    def get_all_nodes(self):
        return self.root.get_all_descendants()
