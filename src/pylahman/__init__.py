import pandas as pd
import importlib.resources


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


def fielding_post() -> pd.DataFrame:
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
