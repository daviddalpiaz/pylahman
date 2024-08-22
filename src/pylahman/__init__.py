import pandas as pd
import importlib.resources


def read_parquet(filename: str) -> pd.DataFrame:
    try:
        data_path = importlib.resources.files(__package__) / "data" / filename
        with importlib.resources.as_file(data_path) as f:
            return pd.read_parquet(f)
    except FileNotFoundError:
        print(f"File data/{filename} not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading data/{filename}: {e}")
        raise


def allstar_full() -> pd.DataFrame:
    return read_parquet("AllstarFull.parquet")


def appearances() -> pd.DataFrame:
    return read_parquet("Appearances.parquet")


def awards_managers() -> pd.DataFrame:
    return read_parquet("AwardsManagers.parquet")


def awards_players() -> pd.DataFrame:
    return read_parquet("AwardsPlayers.parquet")


def awards_share_managers() -> pd.DataFrame:
    return read_parquet("AwardsShareManagers.parquet")


def awards_share_players() -> pd.DataFrame:
    return read_parquet("AwardsSharePlayers.parquet")


def batting() -> pd.DataFrame:
    return read_parquet("Batting.parquet")


def batting_post() -> pd.DataFrame:
    return read_parquet("BattingPost.parquet")


def college_playing() -> pd.DataFrame:
    return read_parquet("CollegePlaying.parquet")


def fielding() -> pd.DataFrame:
    return read_parquet("Fielding.parquet")


def fielding_of() -> pd.DataFrame:
    return read_parquet("FieldingOF.parquet")


def fielding_of_split() -> pd.DataFrame:
    return read_parquet("FieldingOFsplit.parquet")


def fielding_post() -> pd.DataFrame:
    return read_parquet("FieldingPost.parquet")


def hall_of_fame() -> pd.DataFrame:
    return read_parquet("HallOfFame.parquet")


def home_games() -> pd.DataFrame:
    return read_parquet("HomeGames.parquet")


def managers() -> pd.DataFrame:
    return read_parquet("Managers.parquet")


def managers_half() -> pd.DataFrame:
    return read_parquet("ManagersHalf.parquet")


def parks() -> pd.DataFrame:
    return read_parquet("Parks.parquet")


def people() -> pd.DataFrame:
    return read_parquet("People.parquet")


def pitching() -> pd.DataFrame:
    return read_parquet("Pitching.parquet")


def pitching_post() -> pd.DataFrame:
    return read_parquet("PitchingPost.parquet")


def salaries() -> pd.DataFrame:
    return read_parquet("Salaries.parquet")


def schools() -> pd.DataFrame:
    return read_parquet("Schools.parquet")


def series_post() -> pd.DataFrame:
    return read_parquet("SeriesPost.parquet")


def teams() -> pd.DataFrame:
    return read_parquet("Teams.parquet")


def teams_franchises() -> pd.DataFrame:
    return read_parquet("TeamsFranchises.parquet")


def teams_half() -> pd.DataFrame:
    return read_parquet("TeamsHalf.parquet")
