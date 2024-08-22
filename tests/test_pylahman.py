import pylahman
import pandas as pd


def test_load():
    # setup
    batting = pylahman.batting()

    # test fit method
    assert batting is not None
    assert isinstance(batting, pd.DataFrame), "batting is not a pandas DataFrame"
