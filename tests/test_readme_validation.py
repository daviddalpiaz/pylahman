"""
Tests to validate that docstring documentation matches the official README documentation
for all pylahman data loading functions.
"""

import inspect
import re
import pandas as pd
import pytest
import pylahman


def parse_readme_table(table_name):
    """Extract column information from the README file for a specific table."""
    readme_path = "/Users/dmd/Documents/pylahman/lahman-readme.txt"

    with open(readme_path, "r") as f:
        content = f.read()

    # Find the table section
    table_pattern = rf"^{table_name.upper()} TABLE\s*$"
    match = re.search(table_pattern, content, re.MULTILINE | re.IGNORECASE)

    if not match:
        return {}

    # Extract text from table header to next table or end
    start_pos = match.end()

    # Find next table section or end of file
    next_table_pattern = r"^[A-Z][A-Z\s]+ TABLE\s*$"
    next_match = re.search(next_table_pattern, content[start_pos:], re.MULTILINE)

    if next_match:
        end_pos = start_pos + next_match.start()
        table_text = content[start_pos:end_pos]
    else:
        table_text = content[start_pos:]

    # Parse column definitions
    columns = {}
    lines = table_text.split("\n")

    for line in lines:
        line = line.strip()
        if not line or line.startswith("-"):
            continue

        # Look for column definitions (word followed by description)
        parts = line.split(None, 1)  # Split on first whitespace
        if len(parts) == 2:
            col_name = parts[0].strip()
            description = parts[1].strip()

            # Skip lines that don't look like column definitions
            if col_name and description and not col_name.startswith("("):
                columns[col_name] = description

    return columns


def extract_docstring_columns(docstring):
    """Extract column information from numpy-style docstring."""
    if not docstring:
        return {}

    # Find the Returns section with column definitions
    lines = docstring.split("\n")
    in_returns_section = False
    columns = {}

    for line in lines:
        line = line.strip()

        # Start of Returns section
        if line == "Returns" or line.startswith("Returns"):
            in_returns_section = True
            continue

        # Skip the "-------" line after Returns
        if in_returns_section and line.startswith("---"):
            continue

        # End of Returns section
        if in_returns_section and (
            line.startswith("Examples")
            or line.startswith("Notes")
            or line.startswith("See Also")
            or line.startswith("Raises")
            or line.startswith("Parameters")
            or (line == "" and not any(c.isalnum() for c in line))
        ):
            if line == "" and not any(c.isalnum() for c in line):
                continue
            else:
                break

        # Parse column definitions (skip non-column lines)
        if (
            in_returns_section
            and " : " in line
            and not line.startswith("pd.DataFrame")
            and not line.startswith("`DataFrame`")
        ):
            parts = line.split(" : ", 1)
            if len(parts) == 2:
                col_name = parts[0].strip()
                col_type = parts[1].strip()
                columns[col_name] = col_type

    return columns


# Map function names to README table names
TABLE_NAME_MAP = {
    "AllstarFull": "ALL STAR FULL",
    "Appearances": "APPEARANCES",
    "AwardsManagers": "AWARDS MANAGERS",
    "AwardsPlayers": "AWARDS PLAYERS",
    "AwardsShareManagers": "AWARDS SHARE MANAGERS",
    "AwardsSharePlayers": "AWARDS SHARE PLAYERS",
    "Batting": "BATTING",
    "BattingPost": "BATTING POST",
    "CollegePlaying": "COLLEGE PLAYING",
    "Fielding": "FIELDING",
    "FieldingOF": "FIELDING OF",
    "FieldingOFsplit": "FIELDING OF SPLIT",
    "FieldingPost": "FIELDING POST",
    "HallOfFame": "HALL OF FAME",
    "HomeGames": "HOME GAMES",
    "Managers": "MANAGERS",
    "ManagersHalf": "MANAGERS HALF",
    "Parks": "PARKS",
    "People": "PEOPLE",
    "Pitching": "PITCHING",
    "PitchingPost": "PITCHING POST",
    "Salaries": "SALARIES",
    "Schools": "SCHOOLS",
    "SeriesPost": "SERIES POST",
    "Teams": "TEAMS",
    "TeamsFranchises": "TEAM FRANCHISES",
    "TeamsHalf": "TEAMS HALF",
}


# Get all data loading functions
DATA_FUNCTIONS = []
for name in dir(pylahman):
    obj = getattr(pylahman, name)
    if (
        callable(obj)
        and not name.startswith("_")
        and name not in ["get_player_names", "get_player_ids"]
        and hasattr(obj, "__annotations__")
        and obj.__annotations__.get("return") == pd.DataFrame
    ):
        DATA_FUNCTIONS.append((name, obj))


@pytest.mark.readme
@pytest.mark.parametrize("func_name,func", DATA_FUNCTIONS, ids=[name for name, _ in DATA_FUNCTIONS])
def test_docstring_matches_readme(func_name, func):
    """Test that docstring column documentation matches the official README."""
    # Skip functions that don't have README counterparts
    if func_name not in TABLE_NAME_MAP:
        pytest.skip(f"No README table mapping for {func_name}")

    readme_table_name = TABLE_NAME_MAP[func_name]
    readme_columns = parse_readme_table(readme_table_name)

    if not readme_columns:
        pytest.skip(f"Could not parse README table for {readme_table_name}")

    docstring = inspect.getdoc(func)
    assert docstring, f"No docstring found for {func_name}"

    docstring_columns = extract_docstring_columns(docstring)
    assert docstring_columns, f"No columns found in docstring for {func_name}"

    # Get actual data to see what we're working with
    df = func()
    actual_columns = set(df.columns)

    readme_cols = set(readme_columns.keys())
    docstring_cols = set(docstring_columns.keys())

    # Check for columns documented in README but missing from docstring
    missing_from_docstring = readme_cols - docstring_cols

    # Check for columns in docstring but not in README
    extra_in_docstring = docstring_cols - readme_cols

    # Report discrepancies
    issues = []

    if missing_from_docstring:
        issues.append(f"In README but missing from docstring: {sorted(missing_from_docstring)}")

    if extra_in_docstring:
        issues.append(f"In docstring but missing from README: {sorted(extra_in_docstring)}")

    if issues:
        pytest.fail(f"Docstring vs README mismatch for {func_name}: " + " | ".join(issues))


@pytest.mark.readme
def test_readme_parser_works():
    """Test that the README parser can extract at least some tables."""
    people_columns = parse_readme_table("PEOPLE")
    assert people_columns, "README parser should extract People table columns"
    assert "playerID" in people_columns, "People table should contain playerID"

    teams_columns = parse_readme_table("TEAMS")
    assert teams_columns, "README parser should extract Teams table columns"
    assert "yearID" in teams_columns, "Teams table should contain yearID"


@pytest.mark.readme
def test_all_functions_have_readme_mapping():
    """Test that all data loading functions have corresponding README table mappings."""
    missing_mappings = []

    for func_name, func in DATA_FUNCTIONS:
        if func_name not in TABLE_NAME_MAP:
            missing_mappings.append(func_name)

    if missing_mappings:
        pytest.fail(f"Functions missing README table mappings: {missing_mappings}")
