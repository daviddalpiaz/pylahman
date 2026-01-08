# PyLahman


`pylahman` is a Python package for accessing the [**Lahman** Baseball
Database](https://sabr.org/lahman-database/) via `pandas`.

> The **data** used in this package is provided by
> [SABR](https://sabr.org/) and is licensed under [CC BY-SA
> 3.0](https://creativecommons.org/licenses/by-sa/3.0/). The data was
> last updated based on the source data available from
> <https://sabr.org/lahman-database/> on 2026-01-08.
>
> The surrounding **software** is licensed under the [MIT
> License](https://opensource.org/licenses/MIT).

## Installation

The `pylahman` package is available on
[PyPI](https://pypi.org/project/pylahman/) and can be installed via
`pip`.

``` bash
pip install pylahman
```

## Documentation and Usage

Each table in the Lahman Baseball Database has a corresponding data
loading function in `pylahman` with the same name. For example, the
`Pitching` table is accessed via the `Pitching()` function. Descriptions
of each data table can be found in the documentation for the
corresponding data loading function in the [API Reference](reference/).

``` python
import pylahman

Pitching = pylahman.Pitching()
print(Pitching.head())
```

        playerID  yearID  stint teamID lgID  W  L   G  GS  CG  ...  IBB  WP  HBP  \
    0  aardsda01    2004      1    SFN   NL  1  0  11   0   0  ...    0   0    2   
    1  aardsda01    2006      1    CHN   NL  3  0  45   0   0  ...    0   1    1   
    2  aardsda01    2007      1    CHA   AL  2  1  25   0   0  ...    3   2    1   
    3  aardsda01    2008      1    BOS   AL  4  2  47   0   0  ...    2   3    5   
    4  aardsda01    2009      1    SEA   AL  3  6  73   0   0  ...    3   2    0   

       BK  BFP  GF   R  SH  SF  GIDP  
    0   0   61   5   8   0   1     1  
    1   0  225   9  25   1   3     2  
    2   0  151   7  24   2   1     1  
    3   0  228   7  32   3   2     4  
    4   0  296  53  23   2   1     2  

    [5 rows x 30 columns]
