import pylahman
import pandas as pd
import pytest


@pytest.mark.parametrize(
    "func",
    [
        pylahman.allstar_full,
        pylahman.appearances,
        pylahman.awards_managers,
        pylahman.awards_players,
        pylahman.awards_share_managers,
        pylahman.awards_share_players,
        pylahman.batting,
        pylahman.batting_post,
        pylahman.college_playing,
        pylahman.fielding,
        pylahman.fielding_of,
        pylahman.fielding_of_split,
        pylahman.fielding_post,
        pylahman.hall_of_fame,
        pylahman.home_games,
        pylahman.managers,
        pylahman.managers_half,
        pylahman.parks,
        pylahman.people,
        pylahman.pitching,
        pylahman.pitching_post,
        pylahman.salaries,
        pylahman.schools,
        pylahman.series_post,
        pylahman.teams,
        pylahman.teams_franchises,
        pylahman.teams_half,
    ],
)
def test_returns_dataframe(func):
    df = func()
    assert isinstance(df, pd.DataFrame)


def test_batting_includes_2024():
    df = pylahman.batting()
    assert (
        2024 in df["yearID"].values
    ), "2024 not found in batting table yearID column"


def test_pitching_includes_2024():
    df = pylahman.pitching()
    assert (
        2024 in df["yearID"].values
    ), "2024 not found in pitching table yearID column"
