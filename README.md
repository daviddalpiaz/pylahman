# pylahman

`pylahman` is a Python package for accessing the [**Lahman** Baseball Database](http://www.seanlahman.com/) via `pandas`.

> [!IMPORTANT]
> The **data** used in this package is provided by [Sean Lahman](http://www.seanlahman.com/) and is licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). The data was last updated based on the source data available from <http://www.seanlahman.com/> on 2024-08-21.
> 
> The surrounding software is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Installation

`pylahman` can be installed via `pip`:

```bash
pip install pylahman
```

## Usage

```python
>>> import pylahman as lbd
>>> lbd.pitching().columns
Index(['playerID', 'yearID', 'stint', 'teamID', 'lgID', 'W', 'L', 'G', 'GS',
       'CG', 'SHO', 'SV', 'IPouts', 'H', 'ER', 'HR', 'BB', 'SO', 'BAOpp',
       'ERA', 'IBB', 'WP', 'HBP', 'BK', 'BFP', 'GF', 'R', 'SH', 'SF', 'GIDP'],
      dtype='object')
```

## Documentation

Like the package itself, data documentation is still a work in progress. The [`lahman-readme.txt`](lahman-readme.txt) file contains the documentation for the source data. The functions available in this package correspond to the table names listed in that documentation, but converted from `CamelCase` to the more popular `snake_case` in Python. For example the source table `AllStarFull` becomes `allstar_full`. The full list of available functions is:

- `allstar_full`
- `appearances`
- `awards_managers`
- `awards_players`
- `awards_share_managers`
- `awards_share_players`
- `batting`
- `batting_post`
- `college_playing`
- `fielding`
- `fielding_of`
- `fielding_of_split`
- `fielding_post`
- `hall_of_fame`
- `home_games`
- `managers`
- `managers_half`
- `parks`
- `people`
- `pitching`
- `pitching_post`
- `salaries`
- `schools`
- `series_post`
- `teams`
- `teams_franchises`
- `teams_half`
