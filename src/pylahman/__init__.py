import pandas as pd
import importlib.resources

# functions to load the tables as data frames ----------------------------------


def _read_parquet(filename: str) -> pd.DataFrame:
    try:
        data_path = importlib.resources.files(__package__) / "data" / filename
        with importlib.resources.as_file(data_path) as f:
            return pd.read_parquet(f, engine="pyarrow")
    except FileNotFoundError:
        print(f"File data/{filename} not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading data/{filename}: {e}")
        raise


def AllstarFull() -> pd.DataFrame:
    return _read_parquet("AllstarFull.parquet")


def Appearances() -> pd.DataFrame:
    return _read_parquet("Appearances.parquet")


def AwardsManagers() -> pd.DataFrame:
    return _read_parquet("AwardsManagers.parquet")


def AwardsPlayers() -> pd.DataFrame:
    return _read_parquet("AwardsPlayers.parquet")


def AwardsShareManagers() -> pd.DataFrame:
    return _read_parquet("AwardsShareManagers.parquet")


def AwardsSharePlayers() -> pd.DataFrame:
    return _read_parquet("AwardsSharePlayers.parquet")


def Batting() -> pd.DataFrame:
    return _read_parquet("Batting.parquet")


def BattingPost() -> pd.DataFrame:
    return _read_parquet("BattingPost.parquet")


def CollegePlaying() -> pd.DataFrame:
    return _read_parquet("CollegePlaying.parquet")


def Fielding() -> pd.DataFrame:
    return _read_parquet("Fielding.parquet")


def FieldingOF() -> pd.DataFrame:
    return _read_parquet("FieldingOF.parquet")


def FieldingOFsplit() -> pd.DataFrame:
    return _read_parquet("FieldingOFsplit.parquet")


def FieldingPost() -> pd.DataFrame:
    return _read_parquet("FieldingPost.parquet")


def HallOfFame() -> pd.DataFrame:
    return _read_parquet("HallOfFame.parquet")


def HomeGames() -> pd.DataFrame:
    return _read_parquet("HomeGames.parquet")


def Managers() -> pd.DataFrame:
    return _read_parquet("Managers.parquet")


def ManagersHalf() -> pd.DataFrame:
    return _read_parquet("ManagersHalf.parquet")


def Parks() -> pd.DataFrame:
    return _read_parquet("Parks.parquet")


def People() -> pd.DataFrame:
    """
    Returns the `People` table as a `pandas` `DataFrame`.

    | Column         | Description                                                        |
    |----------------|--------------------------------------------------------------------|
    | `playerID`     | A unique code assigned to each player. Links data across files.    |
    | `birthYear`    | Year player was born                                               |
    | `birthMonth`   | Month player was born                                              |
    | `birthDay`     | Day player was born                                                |
    | `birthCountry` | Country where player was born                                      |
    | `birthState`   | State where player was born                                        |
    | `birthCity`    | City where player was born                                         |
    | `deathYear`    | Year player died                                                   |
    | `deathMonth`   | Month player died                                                  |
    | `deathDay`     | Day player died                                                    |
    | `deathCountry` | Country where player died                                          |
    | `deathState`   | State where player died                                            |
    | `deathCity`    | City where player died                                             |
    | `nameFirst`    | Player's first name                                                |
    | `nameLast`     | Player's last name                                                 |
    | `nameGiven`    | Player's given name (typically first and middle)                   |
    | `weight`       | Player's weight in pounds                                          |
    | `height`       | Player's height in inches                                          |
    | `bats`         | Player's batting hand (left, right, or both)                       |
    | `throws`       | Player's throwing hand (left or right)                             |
    | `debut`        | Date that player made first major league appearance                |
    | `finalGame`    | Date that player made last major league appearance                 |
    | `retroID`      | ID used by Retrosheet                                              |
    | `bbrefID`      | ID used by Baseball Reference website                              |
    """
    return _read_parquet("People.parquet")


def Pitching() -> pd.DataFrame:
    return _read_parquet("Pitching.parquet")


def PitchingPost() -> pd.DataFrame:
    return _read_parquet("PitchingPost.parquet")


def Salaries() -> pd.DataFrame:
    return _read_parquet("Salaries.parquet")


def Schools() -> pd.DataFrame:
    return _read_parquet("Schools.parquet")


def SeriesPost() -> pd.DataFrame:
    return _read_parquet("SeriesPost.parquet")


def Teams() -> pd.DataFrame:
    return _read_parquet("Teams.parquet")


def TeamsFranchises() -> pd.DataFrame:
    return _read_parquet("TeamsFranchises.parquet")


def TeamsHalf() -> pd.DataFrame:
    return _read_parquet("TeamsHalf.parquet")


# functions to get player names from id and vice versa -------------------------

_people_df = People()[["playerID", "nameFirst", "nameLast"]]


def get_player_names(player_ids, last_only=False):
    if isinstance(player_ids, str):
        return _get_player_name(player_ids, last_only=last_only)
    return [_get_player_name(pid, last_only=last_only) for pid in player_ids]


def _get_player_name(player_id, last_only=False):
    row = _people_df[_people_df["playerID"] == player_id]
    if row.empty:
        raise ValueError(f"playerID '{player_id}' not found in People table.")
    if last_only:
        return row["nameLast"].iloc[0]
    return f"{row['nameFirst'].iloc[0]} {row['nameLast'].iloc[0]}"


def get_player_ids(last_name, first_name):
    if isinstance(last_name, str) and isinstance(first_name, str):
        return _get_player_id(last_name, first_name)
    return [_get_player_id(ln, fn) for ln, fn in zip(last_name, first_name)]


def _get_player_id(last_name, first_name):
    row = _people_df[
        (_people_df["nameFirst"] == first_name) & (_people_df["nameLast"] == last_name)
    ]
    if row.empty:
        raise ValueError(f"Player '{first_name} {last_name}' not found in People table.")
    return row["playerID"].iloc[0]
