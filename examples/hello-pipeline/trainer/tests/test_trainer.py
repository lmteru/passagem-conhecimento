import pytest
from unittest.mock import MagicMock
from os.path import exists

import trainer

@pytest.mark.parametrize('path, expect_saved', [
    ('', False),
    ('pickle', True),
    ('teste.pkl', True),
    ('proof/test.pkl', False),
    ('assets/teste.pkl', True)
])
def test_pickler(path, expect_saved):
    is_saved = trainer.pickler([], path)

    assert is_saved == expect_saved

    if expect_saved:
        assert exists(path)