import pylahman
import pandas as pd


def test_allstar_full():
    allstar_full = pylahman.allstar_full()
    assert isinstance(allstar_full, pd.DataFrame)


def test_appearances():
    appearances = pylahman.appearances()
    assert isinstance(appearances, pd.DataFrame)


def test_awards_managers():
    awards_managers = pylahman.awards_managers()
    assert isinstance(awards_managers, pd.DataFrame)


def test_awards_players():
    awards_players = pylahman.awards_players()
    assert isinstance(awards_players, pd.DataFrame)


def test_awards_share_managers():
    awards_share_managers = pylahman.awards_share_managers()
    assert isinstance(awards_share_managers, pd.DataFrame)


def test_awards_share_players():
    awards_share_players = pylahman.awards_share_players()
    assert isinstance(awards_share_players, pd.DataFrame)


def test_batting():
    batting = pylahman.batting()
    assert isinstance(batting, pd.DataFrame)


def test_batting_post():
    batting_post = pylahman.batting_post()
    assert isinstance(batting_post, pd.DataFrame)


def test_college_playing():
    college_playing = pylahman.college_playing()
    assert isinstance(college_playing, pd.DataFrame)


def test_fielding():
    fielding = pylahman.fielding()
    assert isinstance(fielding, pd.DataFrame)


def test_fielding_of():
    fielding_of = pylahman.fielding_of()
    assert isinstance(fielding_of, pd.DataFrame)


def test_fielding_of_split():
    fielding_of_split = pylahman.fielding_of_split()
    assert isinstance(fielding_of_split, pd.DataFrame)


def test_fielding_post():
    fielding_post = pylahman.fielding_post()
    assert isinstance(fielding_post, pd.DataFrame)


def test_hall_of_fame():
    hall_of_fame = pylahman.hall_of_fame()
    assert isinstance(hall_of_fame, pd.DataFrame)


def test_home_games():
    home_games = pylahman.home_games()
    assert isinstance(home_games, pd.DataFrame)


def test_managers():
    managers = pylahman.managers()
    assert isinstance(managers, pd.DataFrame)


def test_managers_half():
    managers_half = pylahman.managers_half()
    assert isinstance(managers_half, pd.DataFrame)


def test_parks():
    parks = pylahman.parks()
    assert isinstance(parks, pd.DataFrame)


def test_people():
    people = pylahman.people()
    assert isinstance(people, pd.DataFrame)


def test_pitching():
    pitching = pylahman.pitching()
    assert isinstance(pitching, pd.DataFrame)


def test_pitching_post():
    pitching_post = pylahman.pitching_post()
    assert isinstance(pitching_post, pd.DataFrame)


def test_salaries():
    salaries = pylahman.salaries()
    assert isinstance(salaries, pd.DataFrame)


def test_schools():
    schools = pylahman.schools()
    assert isinstance(schools, pd.DataFrame)


def test_series_post():
    series_post = pylahman.series_post()
    assert isinstance(series_post, pd.DataFrame)


def test_teams():
    teams = pylahman.teams()
    assert isinstance(teams, pd.DataFrame)


def test_teams_franchises():
    teams_franchises = pylahman.teams_franchises()
    assert isinstance(teams_franchises, pd.DataFrame)


def test_teams_half():
    teams_half = pylahman.teams_half()
    assert isinstance(teams_half, pd.DataFrame)


if __name__ == "__main__":
    test_allstar_full()
    test_appearances()
    test_awards_managers()
    test_awards_players()
    test_awards_share_managers()
    test_awards_share_players()
    test_batting()
    test_batting_post()
    test_college_playing()
    test_fielding()
    test_fielding_of()
    test_fielding_of_split()
    test_fielding_post()
    test_hall_of_fame()
    test_home_games()
    test_managers()
    test_managers_half()
    test_parks()
    test_people()
    test_pitching()
    test_pitching_post()
    test_salaries()
    test_schools()
    test_series_post()
    test_teams()
    test_teams_franchises()
    test_teams_half()
    print("All tests passed.")
