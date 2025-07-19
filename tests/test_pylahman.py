import pylahman
import pandas as pd
import pytest


@pytest.mark.parametrize(
    "func",
    [
        pylahman.AllstarFull,
        pylahman.Appearances,
        pylahman.AwardsManagers,
        pylahman.AwardsPlayers,
        pylahman.AwardsShareManagers,
        pylahman.AwardsSharePlayers,
        pylahman.Batting,
        pylahman.BattingPost,
        pylahman.CollegePlaying,
        pylahman.Fielding,
        pylahman.FieldingOF,
        pylahman.FieldingOFsplit,
        pylahman.fielding_post,
        pylahman.HallOfFame,
        pylahman.HomeGames,
        pylahman.Managers,
        pylahman.ManagersHalf,
        pylahman.Parks,
        pylahman.People,
        pylahman.Pitching,
        pylahman.PitchingPost,
        pylahman.Salaries,
        pylahman.Schools,
        pylahman.SeriesPost,
        pylahman.Teams,
        pylahman.TeamsFranchises,
        pylahman.TeamsHalf,
    ],
)
def test_returns_dataframe(func):
    df = func()
    assert isinstance(df, pd.DataFrame)


def test_batting_includes_2024():
    df = pylahman.Batting()
    assert 2024 in df["yearID"].values, "2024 not found in Batting table yearID column"


def test_pitching_includes_2024():
    df = pylahman.Pitching()
    assert 2024 in df["yearID"].values, "2024 not found in Pitching table yearID column"
