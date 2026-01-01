#!/usr/bin/env python3
"""Compare column names between parquet data, lahman-readme.txt, and R package."""

import json
import os
import re

import pandas as pd

SCRIPT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "src/pylahman/data")
README_PATH = os.path.join(SCRIPT_DIR, "..", "lahman-readme.txt")
R_PACKAGE_JSON = os.path.join(SCRIPT_DIR, "r-package-columns.json")
DOCS_OUTPUT_JSON = os.path.join(SCRIPT_DIR, "..", "docs", "compare-tables.json")

# map parquet file names to README table names
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


def parse_readme_table(table_name: str) -> dict[str, str]:
    """Extract column information from the README file for a specific table."""
    with open(README_PATH) as f:
        content = f.read()

    # find the table section
    table_pattern = rf"^{table_name.upper()} TABLE\s*$"
    match = re.search(table_pattern, content, re.MULTILINE | re.IGNORECASE)

    if not match:
        return {}

    start_pos = match.end()

    # find next table section, section divider, or end of file
    next_table_pattern = r"^[A-Z][A-Z\s]+ TABLE\s*$"
    section_divider_pattern = r"^-{20,}\s*$"
    numbered_section_pattern = r"^\d+\.\d+\s"

    next_table_match = re.search(next_table_pattern, content[start_pos:], re.MULTILINE)
    divider_match = re.search(section_divider_pattern, content[start_pos:], re.MULTILINE)
    numbered_match = re.search(numbered_section_pattern, content[start_pos:], re.MULTILINE)

    end_positions = []
    if next_table_match:
        end_positions.append(next_table_match.start())
    if divider_match:
        end_positions.append(divider_match.start())
    if numbered_match:
        end_positions.append(numbered_match.start())

    if end_positions:
        end_pos = start_pos + min(end_positions)
        table_text = content[start_pos:end_pos]
    else:
        table_text = content[start_pos:]

    # parse column definitions
    columns = {}
    for line in table_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("-"):
            continue

        parts = line.split(None, 1)
        if len(parts) == 2:
            col_name = parts[0].strip()
            description = parts[1].strip()
            if col_name and description and not col_name.startswith("("):
                columns[col_name] = description

    return columns


def get_parquet_columns(table_name: str) -> list[str]:
    """Get column names from a parquet file."""
    parquet_path = os.path.join(DATA_DIR, f"{table_name}.parquet")
    if not os.path.exists(parquet_path):
        return []
    df = pd.read_parquet(parquet_path)
    return list(df.columns)


def get_r_package_columns() -> dict[str, list[str]]:
    """Load R package column data from cached JSON."""
    if not os.path.exists(R_PACKAGE_JSON):
        return {}
    with open(R_PACKAGE_JSON) as f:
        return json.load(f)


def find_case_mismatches(set1: set[str], set2: set[str]) -> list[tuple[str, str]]:
    """Find columns that match case-insensitively but not exactly."""
    lower_map1 = {c.lower(): c for c in set1}
    lower_map2 = {c.lower(): c for c in set2}

    mismatches = []
    for lower, col1 in lower_map1.items():
        if lower in lower_map2:
            col2 = lower_map2[lower]
            if col1 != col2:
                mismatches.append((col1, col2))
    return mismatches


def normalize_r_column(col: str) -> str:
    """Normalize R column name for matching.

    - strip leading X from numeric columns (X2B -> 2B)
    - remove dots (park.key -> parkkey)
    """
    # strip leading X from numeric columns
    if col.startswith("X") and len(col) > 1 and col[1].isdigit():
        col = col[1:]
    # remove dots
    col = col.replace(".", "")
    return col


def build_column_table(
    data_cols: set[str], readme_cols: set[str], r_cols: set[str]
) -> list[tuple[str, str, str]]:
    """Build a unified table showing how each column appears in each source."""
    # build lowercase -> original mappings
    data_map = {c.lower(): c for c in data_cols}
    readme_map = {c.lower(): c for c in readme_cols}
    # for R, also create normalized mapping (X2B -> 2B)
    r_map = {c.lower(): c for c in r_cols}
    r_normalized_map = {normalize_r_column(c).lower(): c for c in r_cols}

    # get all unique column names (case-insensitive), using normalized R keys
    all_keys = set(data_map.keys()) | set(readme_map.keys()) | set(r_normalized_map.keys())

    rows = []
    for key in sorted(all_keys):
        py_col = data_map.get(key, "")
        readme_col = readme_map.get(key, "")
        r_col = r_normalized_map.get(key, "")
        rows.append((py_col, readme_col, r_col))

    return rows


def has_differences(rows: list[tuple[str, str, str]]) -> bool:
    """Check if any row has differences between sources."""
    for py, readme, r in rows:
        # check if any are missing or differ
        present = [c for c in (py, readme, r) if c]
        if len(present) < 3 or len(set(present)) > 1:
            return True
    return False


def print_table(table_name: str, rows: list[tuple[str, str, str]]):
    """Print a formatted comparison table. Returns True if there were differences."""
    # only show rows with differences
    diff_rows = [
        r for r in rows
        if not (r[0] and r[1] and r[2] and r[0] == r[1] == r[2])
    ]

    if not diff_rows:
        return False

    # calculate column widths based on diff rows only
    py_width = max(len("Python"), max((len(r[0]) for r in diff_rows), default=0))
    readme_width = max(len("README"), max((len(r[1]) for r in diff_rows), default=0))
    r_width = max(len("R"), max((len(r[2]) for r in diff_rows), default=0))

    print(f"\n{table_name} " + "-" * (78 - len(table_name)))
    print()
    header = f"  {'Python':<{py_width}}  {'README':<{readme_width}}  {'R':<{r_width}}"
    print(header)
    print(f"  {'-' * py_width}  {'-' * readme_width}  {'-' * r_width}")

    for py, readme, r in diff_rows:
        py_str = py if py else "-"
        readme_str = readme if readme else "-"
        r_str = r if r else "-"
        print(f"  {py_str:<{py_width}}  {readme_str:<{readme_width}}  {r_str:<{r_width}}")

    return True


def collect_all_comparisons() -> dict:
    """Collect all table comparison data."""
    r_package_data = get_r_package_columns()

    results = {
        "has_r_data": bool(r_package_data),
        "tables": {},
    }

    for table_name, readme_name in sorted(TABLE_NAME_MAP.items()):
        data_cols = set(get_parquet_columns(table_name))
        readme_cols = set(parse_readme_table(readme_name).keys())
        r_cols = set(r_package_data.get(table_name, []))

        if not data_cols:
            continue

        rows = build_column_table(data_cols, readme_cols, r_cols)

        # only keep rows with differences
        diff_rows = [
            {"python": r[0], "readme": r[1], "r": r[2]}
            for r in rows
            if not (r[0] and r[1] and r[2] and r[0] == r[1] == r[2])
        ]

        results["tables"][table_name] = {
            "differences": diff_rows,
            "has_differences": len(diff_rows) > 0,
        }

    return results


def save_to_docs(results: dict):
    """Save comparison results to docs/ for use by quarto."""
    with open(DOCS_OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Saved comparison data to {DOCS_OUTPUT_JSON}")


def main():
    r_package_data = get_r_package_columns()
    has_r_data = bool(r_package_data)

    print("=" * 70)
    print("TABLE COMPARISON: Python vs README vs R")
    print("=" * 70)

    if not has_r_data:
        print("\nNote: R package data not found. Run 'Rscript scripts/extract-r-columns.R'")

    any_differences = False
    for table_name, readme_name in sorted(TABLE_NAME_MAP.items()):
        data_cols = set(get_parquet_columns(table_name))
        readme_cols = set(parse_readme_table(readme_name).keys())
        r_cols = set(r_package_data.get(table_name, []))

        if not data_cols:
            print(f"\n{table_name}: NO PARQUET FILE FOUND")
            continue

        rows = build_column_table(data_cols, readme_cols, r_cols)
        if print_table(table_name, rows):
            any_differences = True

    if not any_differences:
        print("\nAll tables match!")

    print("\n" + "=" * 70)

    # save results to docs/
    results = collect_all_comparisons()
    save_to_docs(results)


if __name__ == "__main__":
    main()
