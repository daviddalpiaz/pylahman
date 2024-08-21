import pandas as pd
import importlib.resources


def read_parquet(filename: str) -> pd.DataFrame:
    try:
        with importlib.resources.path(__package__, filename) as f:
            return pd.read_parquet(f)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")
        raise


def allstar_full() -> pd.DataFrame:
    return read_parquet("data/AllstarFull.parquet")


def appearances() -> pd.DataFrame:
    return read_parquet("data/Appearances.parquet")


def awards_managers() -> pd.DataFrame:
    return read_parquet("data/AwardsManagers.parquet")


def awards_players() -> pd.DataFrame:
    return read_parquet("data/AwardsPlayers.parquet")


def awards_share_managers() -> pd.DataFrame:
    return read_parquet("data/AwardsShareManagers.parquet")


def awards_share_players() -> pd.DataFrame:
    return read_parquet("data/AwardsSharePlayers.parquet")


def batting() -> pd.DataFrame:
    return read_parquet("data/Batting.parquet")


def batting_post() -> pd.DataFrame:
    return read_parquet("data/BattingPost.parquet")


def college_playing() -> pd.DataFrame:
    return read_parquet("data/CollegePlaying.parquet")


def fielding() -> pd.DataFrame:
    return read_parquet("data/Fielding.parquet")


def fielding_of() -> pd.DataFrame:
    return read_parquet("data/FieldingOF.parquet")


def fielding_of_split() -> pd.DataFrame:
    return read_parquet("data/FieldingOFsplit.parquet")


def fielding_post() -> pd.DataFrame:
    return read_parquet("data/FieldingPost.parquet")


def hall_of_fame() -> pd.DataFrame:
    return read_parquet("data/HallOfFame.parquet")


def home_games() -> pd.DataFrame:
    return read_parquet("data/HomeGames.parquet")


def managers() -> pd.DataFrame:
    return read_parquet("data/Managers.parquet")


def managers_half() -> pd.DataFrame:
    return read_parquet("data/ManagersHalf.parquet")


def parks() -> pd.DataFrame:
    return read_parquet("data/Parks.parquet")


def people() -> pd.DataFrame:
    return read_parquet("data/People.parquet")


def pitching() -> pd.DataFrame:
    return read_parquet("data/Pitching.parquet")


def pitching_post() -> pd.DataFrame:
    return read_parquet("data/PitchingPost.parquet")


def salaries() -> pd.DataFrame:
    return read_parquet("data/Salaries.parquet")


def schools() -> pd.DataFrame:
    return read_parquet("data/Schools.parquet")


def series_post() -> pd.DataFrame:
    return read_parquet("data/SeriesPost.parquet")


def teams() -> pd.DataFrame:
    return read_parquet("data/Teams.parquet")


def teams_franchises() -> pd.DataFrame:
    return read_parquet("data/TeamsFranchises.parquet")


def teams_half() -> pd.DataFrame:
    return read_parquet("data/TeamsHalf.parquet")
