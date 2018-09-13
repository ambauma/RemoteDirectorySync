#!/usr/bin/env python
"""
A utility to synchronize directories across a local network.
"""
import hashlib
import shutil

def main():
    """
    Main entry to the application.
    """
    print("Hello World!")

def _sync_trees(system_of_record, backup_system):
    """
    This method will compare the children of these two directories and then recursively call itself for their children.
    :param system_of_record:
    :param backup_system:
    :return:
    """
    backup_system_children = list(backup_system.iterdir());
    system_of_record_children = list(system_of_record.iterdir())
    for sor_child in system_of_record_children:
        found = False
        for bs_child in backup_system_children:
            if sor_child.is_file():
                if _is_file_same(sor_child, bs_child):
                    found = True
                    break
            else:
                if _is_dir_same(sor_child, bs_child):
                    found = True
                    _sync_trees(sor_child, bs_child)
        if not found:
            if sor_child.is_file():
                shutil.copy(str(sor_child), str(backup_system.absolute()) + "/" + sor_child.name)
            else:
                shutil.copytree(str(sor_child), str(backup_system.absolute()) + "/" + sor_child.name)





def _is_file_same(left, right):
    """
    Must have the same name and the same hash
    :param left:
    :param right:
    :return:
    """
    left_name = left.name
    left_hash = _hash(left.absolute)
    right_name = right.name
    right_hash = _hash(right.absolute)
    return left_name == right_name and left_hash == right_hash

def _is_dir_same(left, right):
    return left.name == right.name

def _hash(filename):
    with open(filename, 'rb') as file:
        bytes = file.read()
        readable_hash = hashlib.sha256(bytes).hexdigest()
        return readable_hash


if __name__ == '__main__':
    main()
