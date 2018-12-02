#!/usr/bin/env python
"""
A utility to synchronize directories across a local network.
"""
import hashlib
import os


class Node:
    """
    A class to create a tree structure from.  Nodes should have a link to their parent (or None)
     and links to all children.
    """
    def __init__(self, parent):
        self.name: list = None
        self.hash = None
        self.is_file = None
        self.children = []
        self.parent = parent

    def find(self, path: list):
        """
        Finds a child node by searching down from its current position in the tree.  Does not
        search up the tree.
        """
        if path == self.name:
            return self
        if len(self.children) > 0:
            for child in self.children:
                returned = child.find(path)
                if returned:
                    return returned
        return None

    def __repr__(self):
        return str(self.__dict__)


def map_tree(path, parent=None):
    """
    Reads a filesystem into a data structure.
    :param path:  The PathLib object representing the filesystem to walk
    :param parent:  Option toplevel node, used for recursion.
    :return:  a tree structure that represents all the files.
    """
    here = Node(parent)
    here.name = path.split('/')
    here.is_file = False
    first_time = True
    for root, _, files in os.walk(path):
        # THE FIRST NODE FOUND IS THE ROOT!
        if first_time:
            first_time = False
            continue
        # root is the folder it has walked into.
        # _ are the directories in the root, walk will get to them.
        # files are files in the root directory.
        abs_root = root.split('/')
        parent_node = here.find(abs_root[0:-1])
        current_node = Node(parent_node)
        parent_node.children.append(current_node)
        current_node.name = abs_root
        current_node.is_file = False
        for file in files:
            file_node = Node(current_node)
            file_node.name = os.path.join(root, file).split('/')
            file_node.is_file = True
            file_node.hash = _hash('/'.join(file_node.name))
            current_node.children.append(file_node)
    return here

def _hash(filename: str):
    with open(filename, 'rb') as file:
        file_bytes = file.read()
        readable_hash = hashlib.sha256(file_bytes).hexdigest()
        return readable_hash
