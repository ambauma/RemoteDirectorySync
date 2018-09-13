import pytest
import os
import shutil
from pathlib import Path
from rds import rds


class TestRdsMethods():

    def setup_method(self, test_method):
        Path('./tests/test_data/a').mkdir(parents=True, exist_ok=True)
        Path('./tests/test_data/b').mkdir(parents=True, exist_ok=True)

    def teardown_method(self, test_method):
        shutil.rmtree(Path('./tests/test_data/'), True)

    def test_main(self):
        rds.main()

    def test_sync_empty_directories(self):
        rds._sync_trees(Path('./tests/test_data/a'), Path('./tests/test_data/b'))
        assert Path('./tests/test_data/a').is_dir()
        assert Path('./tests/test_data/a').exists()
        assert Path('./tests/test_data/b').is_dir()
        assert Path('./tests/test_data/b').exists()
        assert 0 == len(list(Path('./tests/test_data/a').iterdir()))
        assert 0 == len(list(Path('./tests/test_data/b').iterdir()))

    def test_sync_trees_file_exists_on_a_but_not_b(self):
        child1 = Path('./tests/test_data/a/childA')
        child1.touch()
        rds._sync_trees(Path('./tests/test_data/a'), Path('./tests/test_data/b'))
        assert 1 == len(list(Path('./tests/test_data/a').iterdir()))
        assert 1 == len(list(Path('./tests/test_data/b').iterdir()))

    def test_sync_trees_file_exists_on_a_and_b(self):
        pass

    def test_sync_trees_file_exists_on_b_but_not_a(self):
        pass

