"""
Tests for the rds/rds.py module.
"""
import os
import shutil
from rds import rds


def setup_function():
    """
    Setup before every test case.
    """
    if not os.path.exists('./tests/test_data/a'):
        os.makedirs('./tests/test_data/a', exist_ok=True)
        if not os.path.exists('./tests/test_data/a/some.txt'):
            with open('./tests/test_data/a/some.txt', 'w') as some_file:
                some_file.write("I am writing some things")
    if not os.path.exists('./tests/test_data/b'):
        os.makedirs('./tests/test_data/b', exist_ok=True)
    if not os.path.exists('./tests/test_data/b/c'):
        os.makedirs('./tests/test_data/b/c', exist_ok=True)


def teardown_function():
    """
    Teardown before every test case.
    """
    shutil.rmtree('./tests/test_data/', True)


def test_map_directory():
    """
    Tests building a tree structure off a directory.
    """
    test_data_root = rds.map_tree('tests/test_data')
    assert not test_data_root.is_file
    for child in test_data_root.children:
        print(child)
    assert len(test_data_root.children) == 2
    
    child0 = test_data_root.children[0]
    assert child0 is not None
    assert not child0.is_file
    assert child0.name == ["tests","test_data","a"]
    assert len(child0.children) == 1
    child0child0 = child0.children[0]
    assert child0child0 is not None
    assert child0child0.is_file
    assert 'b078c0263ea4cb856aecf5b3cc9fd79d37b7a5f7d3af9b87726a99095eb674b1' == child0child0.hash
    
    child1 = test_data_root.children[1]
    assert child1 is not None
    assert not child1.is_file
    assert child1.name == ["tests","test_data","b"]
    assert len(child1.children) == 1

    child1child0 = child1.children[0]
    assert child1child0 is not None
    assert not child1child0.is_file
    assert child1child0.name == ["tests","test_data","b","c"]
    assert len(child1child0.children) == 0
