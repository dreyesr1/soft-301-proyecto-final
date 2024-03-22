import pytest

from testbook import testbook

@pytest.fixture(scope='module')
def notebook():
    with testbook('index.ipynb', execute=True) as tb:
        yield tb

def test_execute_cell00(notebook):
    assert notebook.cell_output_text(0) == '2'

def test_execute_cell01(notebook):
    assert notebook.cell_output_text(1) == '144'