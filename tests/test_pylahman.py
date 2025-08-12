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


def test_Batting_includes_2024():
    df = pylahman.Batting()
    assert 2024 in df["yearID"].values, "2024 not found in Batting table yearID column"


def test_Pitching_includes_2024():
    df = pylahman.Pitching()
    assert 2024 in df["yearID"].values, "2024 not found in Pitching table yearID column"


def test_people_birthYear_is_int64():
    df = pylahman.People()
    assert (
        df["birthYear"].dtype == "Int64"
    ), f"birthYear dtype is {df['birthYear'].dtype}, expected Int64"
    assert (
        df["deathYear"].dtype == "Int64"
    ), f"deathYear dtype is {df['deathYear'].dtype}, expected Int64"


def test_dates_are_dates():
    df = pylahman.People()
    assert (
        df["debut"].dtype == "datetime64[ns]"
    ), f"debut dtype is {df['deathYear'].dtype}, expected datetime64[ns]"
