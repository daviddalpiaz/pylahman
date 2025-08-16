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


def test__get_player_name():
    player_id = "aaronha01"
    first = "Hank"
    last = "Aaron"
    assert pylahman._get_player_name(player_id) == f"{first} {last}"
    assert pylahman._get_player_name(player_id, last_only=True) == last
    with pytest.raises(ValueError, match="not found in People table"):
        pylahman._get_player_name("not_a_real_id")


def test__get_player_id():
    player_id = "bondsba01"
    first = "Barry"
    last = "Bonds"
    assert pylahman._get_player_id(last, first) == player_id
    with pytest.raises(ValueError, match="not found in People table"):
        pylahman._get_player_id("NotARealLastName", "NotARealFirstName")


def test_get_player_names():
    assert pylahman.get_player_names("aaronha01") == "Hank Aaron"
    assert pylahman.get_player_names("aaronha01", last_only=True) == "Aaron"
    ids = ["aaronha01", "bondsba01"]
    names = pylahman.get_player_names(ids)
    assert names == ["Hank Aaron", "Barry Bonds"]
    last_names = pylahman.get_player_names(ids, last_only=True)
    assert last_names == ["Aaron", "Bonds"]
    with pytest.raises(ValueError):
        pylahman.get_player_names("not_a_real_id")


def test_get_player_ids():
    assert pylahman.get_player_ids("Aaron", "Hank") == "aaronha01"
    last_names = ["Aaron", "Bonds"]
    first_names = ["Hank", "Barry"]
    ids = pylahman.get_player_ids(last_names, first_names)
    assert ids == ["aaronha01", "bondsba01"]
    with pytest.raises(ValueError):
        pylahman.get_player_ids("NotARealLastName", "NotARealFirstName")
