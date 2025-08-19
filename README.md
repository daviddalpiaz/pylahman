# pylahman

`pylahman` is a Python package for accessing the [**Lahman** Baseball Database](https://sabr.org/lahman-database/) via `pandas`.

> [!IMPORTANT]
> The **data** used in this package is provided by [SABR](https://sabr.org/) and is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
> The data was last updated based on the source data available from <https://sabr.org/lahman-database/> on 2025-07-18.
>
> The surrounding software is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Installation

`pylahman` can be installed via `pip`:

```bash
pip install pylahman
```

## Usage

```python
>>> import pylahman
>>> pylahman.Pitching().columns
Index(['playerID', 'yearID', 'stint', 'teamID', 'lgID', 'W', 'L', 'G', 'GS',
       'CG', 'SHO', 'SV', 'IPouts', 'H', 'ER', 'HR', 'BB', 'SO', 'BAOpp',
       'ERA', 'IBB', 'WP', 'HBP', 'BK', 'BFP', 'GF', 'R', 'SH', 'SF', 'GIDP'],
      dtype='object')
```

## Documentation

Like the package itself, data documentation is still a work in progress.
The [`lahman-readme.txt`](lahman-readme.txt) file contains the documentation for the source data.
The functions available in this package correspond to the table names listed in that documentation.
The full list of available functions is:

- `AllstarFull`
- `Appearances`
- `AwardsManagers`
- `AwardsPlayers`
- `AwardsShareManagers`
- `AwardsSharePlayers`
- `Batting`
- `BattingPost`
- `CollegePlaying`
- `Fielding`
- `FieldingOF`
- `FieldingOFsplit`
- `FieldingPost`
- `HallOfFame`
- `HomeGames`
- `Managers`
- `ManagersHalf`
- `Parks`
- `People`
- `Pitching`
- `PitchingPost`
- `Salaries`
- `Schools`
- `SeriesPost`
- `Teams`
- `TeamsFranchises`
- `TeamsHalf`
