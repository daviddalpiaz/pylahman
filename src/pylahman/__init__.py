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
    """
    Returns the `AllstarFull` table as a `DataFrame`.

    The `AllstarFull` table contains information about All-Star game appearances.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    gameNum : int
        Game number (zero if only one All-Star game played that season)
    gameID : str
        Retrosheet ID for the game
    teamID : str
        Team
    lgID : str
        League
    GP : int
        1 if Played in the game
    startingPos : str
        If player was game starter, the position played
    """
    return _read_parquet("AllstarFull.parquet")


def Appearances() -> pd.DataFrame:
    """
    Returns the `Appearances` table as a `DataFrame`.

    The `Appearances` table contains information about player appearances by position.
    The columns of the table are documented as the function returns.

    Returns
    -------
    yearID : int
        Year
    teamID : str
        Team
    lgID : str
        League
    playerID : str
        Player ID code
    G_all : int
        Total games played
    GS : int
        Games started
    G_batting : int
        Games in which player batted
    G_defense : int
        Games in which player appeared on defense
    G_p : int
        Games as pitcher
    G_c : int
        Games as catcher
    G_1b : int
        Games as first baseman
    G_2b : int
        Games as second baseman
    G_3b : int
        Games as third baseman
    G_ss : int
        Games as shortstop
    G_lf : int
        Games as left fielder
    G_cf : int
        Games as center fielder
    G_rf : int
        Games as right fielder
    G_of : int
        Games as outfielder (if a player appeared in a single game at multiple OF positions, this will count as one g_OF game)
    G_dh : int
        Games as designated hitter
    G_ph : int
        Games as pinch hitter
    G_pr : int
        Games as pinch runner
    """
    return _read_parquet("Appearances.parquet")


def AwardsManagers() -> pd.DataFrame:
    """
    Returns the `AwardsManagers` table as a `DataFrame`.

    The `AwardsManagers` table contains information about awards won by managers.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Manager ID code
    awardID : str
        Name of award won
    yearID : int
        Year
    lgID : str
        League
    tie : str
        Award was a tie (Y or N)
    notes : str
        Notes about the award
    """
    return _read_parquet("AwardsManagers.parquet")


def AwardsPlayers() -> pd.DataFrame:
    """
    Returns the `AwardsPlayers` table as a `DataFrame`.

    The `AwardsPlayers` table contains information about awards won by players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    awardID : str
        Name of award won
    yearID : int
        Year
    lgID : str
        League
    tie : str
        Award was a tie (Y or N)
    notes : str
        Notes about the award
    """
    return _read_parquet("AwardsPlayers.parquet")


def AwardsShareManagers() -> pd.DataFrame:
    """
    Returns the `AwardsShareManagers` table as a `DataFrame`.

    The `AwardsShareManagers` table contains voting information for manager awards.
    The columns of the table are documented as the function returns.

    Returns
    -------
    awardID : str
        Name of award votes were received for
    yearID : int
        Year
    lgID : str
        League
    playerID : str
        Manager ID code
    pointsWon : int
        Number of points received
    pointsMax : int
        Maximum number of points possible
    votesFirst : int
        Number of first place votes
    """
    return _read_parquet("AwardsShareManagers.parquet")


def AwardsSharePlayers() -> pd.DataFrame:
    """
    Returns the `AwardsSharePlayers` table as a `DataFrame`.

    The `AwardsSharePlayers` table contains voting information for player awards.
    The columns of the table are documented as the function returns.

    Returns
    -------
    awardID : str
        Name of award votes were received for
    yearID : int
        Year
    lgID : str
        League
    playerID : str
        Player ID code
    pointsWon : int
        Number of points received
    pointsMax : int
        Maximum number of points possible
    votesFirst : int
        Number of first place votes
    """
    return _read_parquet("AwardsSharePlayers.parquet")


def Batting() -> pd.DataFrame:
    """
    Returns the `Batting` table as a `DataFrame`.

    The `Batting` table contains yearly batting statistics for all players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    stint : int
        Player's stint (order of appearances within a season)
    teamID : str
        Team
    lgID : str
        League
    G : int
        Games
    AB : int
        At Bats
    R : int
        Runs
    H : int
        Hits
    2B : int
        Doubles
    3B : int
        Triples
    HR : int
        Homeruns
    RBI : int
        Runs Batted In
    SB : int
        Stolen Bases
    CS : int
        Caught Stealing
    BB : int
        Base on Balls
    SO : int
        Strikeouts
    IBB : int
        Intentional walks
    HBP : int
        Hit by pitch
    SH : int
        Sacrifice hits
    SF : int
        Sacrifice flies
    GIDP : int
        Grounded into double plays
    """
    return _read_parquet("Batting.parquet")


def BattingPost() -> pd.DataFrame:
    """
    Returns the `BattingPost` table as a `DataFrame`.

    The `BattingPost` table contains postseason batting statistics for all players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    yearID : int
        Year
    round : str
        Level of playoffs
    playerID : str
        Player ID code
    teamID : str
        Team
    lgID : str
        League
    G : int
        Games
    AB : int
        At Bats
    R : int
        Runs
    H : int
        Hits
    2B : int
        Doubles
    3B : int
        Triples
    HR : int
        Homeruns
    RBI : int
        Runs Batted In
    SB : int
        Stolen Bases
    CS : int
        Caught stealing
    BB : int
        Base on Balls
    SO : int
        Strikeouts
    IBB : int
        Intentional walks
    HBP : int
        Hit by pitch
    SH : int
        Sacrifices
    SF : int
        Sacrifice flies
    GIDP : int
        Grounded into double plays
    """
    return _read_parquet("BattingPost.parquet")


def CollegePlaying() -> pd.DataFrame:
    """
    Returns the `CollegePlaying` table as a `DataFrame`.

    The `CollegePlaying` table contains information about players' college careers.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    schoolID : str
        School ID code
    yearID : int
        Year
    """
    return _read_parquet("CollegePlaying.parquet")


def Fielding() -> pd.DataFrame:
    """
    Returns the `Fielding` table as a `DataFrame`.

    The `Fielding` table contains yearly fielding statistics for all players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    stint : int
        Player's stint (order of appearances within a season)
    teamID : str
        Team
    lgID : str
        League
    POS : str
        Position
    G : int
        Games
    GS : int
        Games Started
    InnOuts : int
        Time played in the field expressed as outs
    PO : int
        Putouts
    A : int
        Assists
    E : int
        Errors
    DP : int
        Double Plays
    PB : int
        Passed Balls (by catchers)
    WP : int
        Wild Pitches (by catchers)
    SB : int
        Opponent Stolen Bases (by catchers)
    CS : int
        Opponents Caught Stealing (by catchers)
    ZR : float
        Zone Rating
    """
    return _read_parquet("Fielding.parquet")


def FieldingOF() -> pd.DataFrame:
    """
    Returns the `FieldingOF` table as a `DataFrame`.

    The `FieldingOF` table contains outfield position information for players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    stint : int
        Player's stint (order of appearances within a season)
    Glf : int
        Games played in left field
    Gcf : int
        Games played in center field
    Grf : int
        Games played in right field
    """
    return _read_parquet("FieldingOF.parquet")


def FieldingOFsplit() -> pd.DataFrame:
    """
    Returns the `FieldingOFsplit` table as a `DataFrame`.

    The `FieldingOFsplit` table contains detailed outfield fielding statistics.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    stint : int
        Player's stint (order of appearances within a season)
    teamID : str
        Team
    lgID : str
        League
    POS : str
        Position
    G : int
        Games
    GS : int
        Games Started
    InnOuts : int
        Time played in the field expressed as outs
    PO : int
        Putouts
    A : int
        Assists
    E : int
        Errors
    DP : int
        Double Plays
    CS : int
        Caught Stealing
    PB : int
        Passed Balls
    SB : int
        Stolen Bases
    WP : int
        Wild Pitches
    ZR : int
        Zone Rating
    """
    return _read_parquet("FieldingOFsplit.parquet")


def FieldingPost() -> pd.DataFrame:
    """
    Returns the `FieldingPost` table as a `DataFrame`.

    The `FieldingPost` table contains postseason fielding statistics for all players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    teamID : str
        Team
    lgID : str
        League
    round : str
        Level of playoffs
    POS : str
        Position
        Position
    G : int
        Games
    GS : int
        Games Started
    InnOuts : int
        Time played in the field expressed as outs
    PO : int
        Putouts
    A : int
        Assists
    E : int
        Errors
    DP : int
        Double Plays
    TP : int
        Triple Plays
    PB : int
        Passed Balls
    SB : int
        Stolen Bases allowed (by catcher)
    CS : int
        Caught Stealing (by catcher)
    """
    return _read_parquet("FieldingPost.parquet")


def HallOfFame() -> pd.DataFrame:
    """
    Returns the `HallOfFame` table as a `DataFrame`.

    The `HallOfFame` table contains information about Hall of Fame voting and inductions.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year of ballot
    votedBy : str
        Method by which player was voted upon
    ballots : int
        Total ballots cast in that year
    needed : int
        Number of votes needed for selection in that year
    votes : int
        Total votes received
    inducted : str
        Whether player was inducted by that vote or not (Y or N)
    category : str
        Category in which candidate was honored
    needed_note : str
        Explanation of qualifiers for special elections, revised in 2023 to include important notes about the record
    """
    return _read_parquet("HallOfFame.parquet")


def HomeGames() -> pd.DataFrame:
    """
    Returns the `HomeGames` table as a `DataFrame`.

    The `HomeGames` table contains information about home games played by teams.
    The columns of the table are documented as the function returns.

    Returns
    -------
    yearkey : int
        Year
    leaguekey : str
        League
    teamkey : str
        Team ID
    parkkey : str
        Ballpark ID
    spanfirst : datetime
        First date of operation (yyyy-mm-dd)
    spanlast : datetime
        Last date of operation (yyyy-mm-dd)
    games : int
        Total number of games
    openings : int
        Total number of paid dates played (games with attendance, note that doubleheaders may make the openings less than games)
    attendance : int
        Total attendance
    """
    return _read_parquet("HomeGames.parquet")


def Managers() -> pd.DataFrame:
    """
    Returns the `Managers` table as a `DataFrame`.

    The `Managers` table contains information about team managers.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID Number
    yearID : int
        Year
    teamID : str
        Team
    lgID : str
        League
    inseason : int
        Managerial order, in order of appearance during the year. One if the individual managed the team the entire year
    G : int
        Games managed
    W : int
        Wins
    L : int
        Losses
    rank : int
        Team's final position in standings that year
    plyrMgr : str
        Player Manager (denoted by 'Y')
    """
    return _read_parquet("Managers.parquet")


def ManagersHalf() -> pd.DataFrame:
    """
    Returns the `ManagersHalf` table as a `DataFrame`.

    The `ManagersHalf` table contains managerial information by half-season.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Manager ID code
    yearID : int
        Year
    teamID : str
        Team
    lgID : str
        League
    inseason : int
        Managerial order, in order of appearance during the year, 1 if the individual managed the team the entire year
    half : int
        First or second half of season
    G : int
        Games managed
    W : int
        Wins
    L : int
        Losses
    rank : int
        Team's position in standings for the half
    """
    return _read_parquet("ManagersHalf.parquet")


def Parks() -> pd.DataFrame:
    """
    Returns the `Parks` table as a `DataFrame`.

    The `Parks` table contains information about ballparks.
    The columns of the table are documented as the function returns.

    Returns
    -------
    parkkey : str
        Ballpark ID code
    parkname : str
        Name of ballpark
    parkalias : str
        Alternate names of ballpark, separated by semicolon
    city : str
        City
    state : str
        State
    country : str
        Country
    """
    return _read_parquet("Parks.parquet")


def People() -> pd.DataFrame:
    """
    Returns the `People` table as a `DataFrame`.

    The `People` table contains biographical information for all players, managers,
    umpires, and executives in the database.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    birthYear : int
        Year player was born
    birthMonth : int
        Month player was born
    birthDay : int
        Day player was born
    birthCountry : str
        Country where player was born
    birthState : str
        State where player was born
    birthCity : str
        City where player was born
    deathYear : int
        Year player died
    deathMonth : int
        Month player died
    deathDay : int
        Day player died
    deathCountry : str
        Country where player died
    deathState : str
        State where player died
    deathCity : str
        City where player died
    nameFirst : str
        Player's first name
    nameLast : str
        Player's last name
    nameGiven : str
        Player's given name (typically first and middle)
    weight : int
        Player's weight in pounds
    height : int
        Player's height in inches
    bats : str
        Player's batting hand (left, right, or both)
    throws : str
        Player's throwing hand (left or right)
    debut : datetime
        Date that player made first major league appearance
    finalGame : datetime
        Date that player made last major league appearance
    retroID : str
        ID used by Retrosheet
    bbrefID : str
        ID used by Baseball Reference website
    """
    return _read_parquet("People.parquet")


def Pitching() -> pd.DataFrame:
    """
    Returns the `Pitching` table as a `DataFrame`.

    The `Pitching` table contains yearly pitching statistics for all players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    stint : int
        Player's stint (order of appearances within a season)
    teamID : str
        Team
    lgID : str
        League
    W : int
        Wins
    L : int
        Losses
    G : int
        Games
    GS : int
        Games Started
    CG : int
        Complete Games
    SHO : int
        Shutouts
    SV : int
        Saves
    IPOuts : int
        Outs Pitched (innings pitched x 3)
    H : int
        Hits
    ER : int
        Earned Runs
    HR : int
        Homeruns
    BB : int
        Walks
    SO : int
        Strikeouts
    BAOpp : float
        Opponent's Batting Average
    ERA : float
        Earned Run Average
    IBB : int
        Intentional Walks
    WP : int
        Wild Pitches
    HBP : int
        Batters Hit By Pitch
    BK : int
        Balks
    BFP : int
        Batters faced by Pitcher
    GF : int
        Games Finished
    R : int
        Runs Allowed
    SH : int
        Sacrifices by opposing batters
    SF : int
        Sacrifice flies by opposing batters
    GIDP : int
        Grounded into double plays by opposing batter
    """
    return _read_parquet("Pitching.parquet")


def PitchingPost() -> pd.DataFrame:
    """
    Returns the `PitchingPost` table as a `DataFrame`.

    The `PitchingPost` table contains postseason pitching statistics for all players.
    The columns of the table are documented as the function returns.

    Returns
    -------
    playerID : str
        Player ID code
    yearID : int
        Year
    round : str
        Level of playoffs
    teamID : str
        Team
    lgID : str
        League
    W : int
        Wins
    L : int
        Losses
    G : int
        Games
    GS : int
        Games Started
    CG : int
        Complete Games
    SHO : int
        Shutouts
    SV : int
        Saves
    IPOuts : int
        Outs Pitched (innings pitched x 3)
    H : int
        Hits
    ER : int
        Earned Runs
    HR : int
        Homeruns
    BB : int
        Walks
    SO : int
        Strikeouts
    BAOpp : float
        Opponents' batting average
    ERA : float
        Earned Run Average
    IBB : int
        Intentional Walks
    WP : int
        Wild Pitches
    HBP : int
        Batters Hit By Pitch
    BK : int
        Balks
    BFP : int
        Batters faced by Pitcher
    GF : int
        Games Finished
    R : int
        Runs Allowed
    SH : int
        Sacrifice Hits allowed
    SF : int
        Sacrifice Flies allowed
    GIDP : int
        Grounded into Double Plays
    """
    return _read_parquet("PitchingPost.parquet")


def Salaries() -> pd.DataFrame:
    """
    Returns the `Salaries` table as a `DataFrame`.

    The `Salaries` table contains player salary information.
    The columns of the table are documented as the function returns.

    Returns
    -------
    yearID : int
        Year
    teamID : str
        Team
    lgID : str
        League
    playerID : str
        Player ID code
    salary : int
        Salary
    """
    return _read_parquet("Salaries.parquet")


def Schools() -> pd.DataFrame:
    """
    Returns the `Schools` table as a `DataFrame`.

    The `Schools` table contains information about schools and colleges.
    The columns of the table are documented as the function returns.

    Returns
    -------
    schoolID : str
        School ID code
    nameFull : str
        School name
    city : str
        City where school is located
    state : str
        State where school is located
    country : str
        Country where school is located
    """
    return _read_parquet("Schools.parquet")


def SeriesPost() -> pd.DataFrame:
    """
    Returns the `SeriesPost` table as a `DataFrame`.

    The `SeriesPost` table contains information about postseason series results.
    The columns of the table are documented as the function returns.

    Returns
    -------
    yearID : int
        Year
    round : str
        Level of playoffs
    teamIDwinner : str
        Team ID of the team that won the series
    lgIDwinner : str
        League ID of the team that won the series
    teamIDloser : str
        Team ID of the team that lost the series
    lgIDloser : str
        League ID of the team that lost the series
    wins : int
        Wins by team that won the series
    losses : int
        Losses by team that won the series
    ties : int
        Tie games
    """
    return _read_parquet("SeriesPost.parquet")


def Teams() -> pd.DataFrame:
    """
    Returns the `Teams` table as a `DataFrame`.

    The `Teams` table contains yearly team statistics and standings information
    for all major league teams.
    The columns of the table are documented as the function returns.

    Returns
    -------
    yearID : int
        Year
    lgID : str
        League
    teamID : str
        Team
    franchID : str
        Franchise (links to TeamsFranchise table)
    divID : str
        Team's division
    Rank : int
        Position in final standings
    G : int
        Games played
    GHome : int
        Games played at home
    W : int
        Wins
    L : int
        Losses
    DivWin : str
        Division Winner (Y or N)
    WCWin : str
        Wild Card Winner (Y or N)
    LgWin : str
        League Champion (Y or N)
    WSWin : str
        World Series Winner (Y or N)
    R : int
        Runs scored
    AB : int
        At bats
    H : int
        Hits by batters
    2B : int
        Doubles
    3B : int
        Triples
    HR : int
        Homeruns by batters
    BB : int
        Walks by batters
    SO : int
        Strikeouts by batters
    SB : int
        Stolen bases
    CS : int
        Caught stealing
    HBP : int
        Batters hit by pitch
    SF : int
        Sacrifice flies
    RA : int
        Opponents runs scored
    ER : int
        Earned runs allowed
    ERA : float
        Earned run average
    CG : int
        Complete games
    SHO : int
        Shutouts (team level)
    SV : int
        Saves
    IPOuts : int
        Outs Pitched (innings pitched x 3)
    HA : int
        Hits allowed
    HRA : int
        Homeruns allowed
    BBA : int
        Walks allowed
    SOA : int
        Strikeouts by pitchers
    E : int
        Errors
    DP : int
        Double Plays (team level)
    FP : float
        Fielding percentage
    name : str
        Team's full name
    park : str
        Name of team's home ballpark
    attendance : int
        Home attendance total
    BPF : int
        Three-year park factor for batters
    PPF : int
        Three-year park factor for pitchers
    teamIDBR : str
        Team ID used by Baseball Reference website
    teamIDlahman45 : str
        Team ID used in Lahman database version 4.5
    teamIDretro : str
        Team ID used by Retrosheet
    """
    return _read_parquet("Teams.parquet")


def TeamsFranchises() -> pd.DataFrame:
    """
    Returns the `TeamsFranchises` table as a `DataFrame`.

    The `TeamsFranchises` table contains information about team franchises.
    The columns of the table are documented as the function returns.

    Returns
    -------
    franchID : str
        Franchise ID
    franchName : str
        Franchise name
    active : str
        Whether team is currently active or not (Y or N)
    NAassoc : str
        ID of National Association team franchise played as
    """
    return _read_parquet("TeamsFranchises.parquet")


def TeamsHalf() -> pd.DataFrame:
    """
    Returns the `TeamsHalf` table as a `DataFrame`.

    The `TeamsHalf` table contains team statistics by half-season.
    The columns of the table are documented as the function returns.

    Returns
    -------
    yearID : int
        Year
    lgID : str
        League
    teamID : str
        Team
    half : int
        First or second half of season
    divID : str
        Division
    DivWin : str
        Won Division (Y or N)
    rank : int
        Team's position in standings for the half
    G : int
        Games played
    W : int
        Wins
    L : int
        Losses
    """
    return _read_parquet("TeamsHalf.parquet")


# functions to get player names from id and vice versa -------------------------

_people_df = People()[["playerID", "nameFirst", "nameLast"]]


def get_player_names(player_ids, last_only=False):
    """
    Get player names from player IDs.

    Parameters
    ----------
    player_ids : str or list of str
        Single player ID or list of player IDs
    last_only : bool, default False
        If True, return only last names. If False, return "First Last" format.

    Returns
    -------
    str or list of str
        Player name(s) corresponding to the input ID(s)

    Raises
    ------
    ValueError
        If a playerID is not found in the People table
    """
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
    """
    Get player IDs from player names.

    Parameters
    ----------
    last_name : str or list of str
        Player's last name(s)
    first_name : str or list of str
        Player's first name(s)

    Returns
    -------
    str or list of str
        Player ID(s) corresponding to the input name(s)

    Raises
    ------
    ValueError
        If a player name combination is not found in the People table
    """
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
