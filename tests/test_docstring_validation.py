"""
Tests to validate that docstring documentation matches actual data structure
for all pylahman data loading functions.
"""

import inspect
import re
import pandas as pd
import pytest
import pylahman


def extract_docstring_columns(docstring):
    """Extract column information from numpy-style docstring."""
    if not docstring:
        return {}

    # find the Returns section with column definitions
    lines = docstring.split("\n")
    in_returns_section = False
    columns = {}

    for line in lines:
        line = line.strip()

        # start of Returns section
        if line == "Returns" or line.startswith("Returns"):
            in_returns_section = True
            continue

        # skip the "-------" line after Returns
        if in_returns_section and line.startswith("---"):
            continue

        # end of Returns section
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

        # parse column definitions (skip non-column lines)
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


def get_pandas_dtype_category(dtype):
    """Categorize pandas dtype into basic types."""
    dtype_str = str(dtype).lower()

    if "int" in dtype_str:
        return "int"
    elif "float" in dtype_str:
        return "float"
    elif "object" in dtype_str or "string" in dtype_str:
        return "str"
    elif "bool" in dtype_str:
        return "bool"
    elif "datetime" in dtype_str:
        return "datetime"
    else:
        return str(dtype)


# get all data loading functions
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


@pytest.mark.parametrize("func_name,func", DATA_FUNCTIONS, ids=[name for name, _ in DATA_FUNCTIONS])
def test_docstring_columns_exist(func_name, func):
    """Test that all columns documented in docstring exist in the actual data."""
    docstring = inspect.getdoc(func)
    assert docstring, f"No docstring found for {func_name}"

    expected_columns = extract_docstring_columns(docstring)
    assert expected_columns, f"No columns found in docstring for {func_name}"

    df = func()
    actual_columns = set(df.columns)
    expected_cols = set(expected_columns.keys())

    missing_in_data = expected_cols - actual_columns

    # Any inconsistency should fail - no exceptions
    if missing_in_data:
        pytest.fail(
            f"Columns documented in {func_name} docstring but missing from data: Missing={sorted(missing_in_data)}"
        )


@pytest.mark.parametrize("func_name,func", DATA_FUNCTIONS, ids=[name for name, _ in DATA_FUNCTIONS])
def test_data_columns_documented(func_name, func):
    """Test that all data columns are documented in the docstring."""
    docstring = inspect.getdoc(func)
    expected_columns = extract_docstring_columns(docstring)

    df = func()
    actual_columns = set(df.columns)
    expected_cols = set(expected_columns.keys())

    extra_in_data = actual_columns - expected_cols

    # Any undocumented columns should fail
    if extra_in_data:
        pytest.fail(
            f"Columns in {func_name} data but not documented in docstring: Undocumented={sorted(extra_in_data)}"
        )


@pytest.mark.parametrize("func_name,func", DATA_FUNCTIONS, ids=[name for name, _ in DATA_FUNCTIONS])
def test_docstring_types_match_data(func_name, func):
    """Test that documented column types match actual data types where possible."""
    docstring = inspect.getdoc(func)
    expected_columns = extract_docstring_columns(docstring)

    df = func()

    type_mismatches = []
    for col_name, expected_type in expected_columns.items():
        if col_name in df.columns:
            actual_dtype = get_pandas_dtype_category(df[col_name].dtype)

            # Clean up expected type
            expected_clean = expected_type.lower().strip()

            # check for type compatibility - be flexible with known conversions
            if expected_clean == "str" and actual_dtype == "datetime":
                type_mismatches.append(f"{col_name}: expected str, got {actual_dtype}")
            elif expected_clean == "str" and actual_dtype != "str":
                type_mismatches.append(f"{col_name}: expected str, got {actual_dtype}")
            elif expected_clean == "int" and actual_dtype not in ["int", "float"]:
                # float is OK for int with NaNs
                type_mismatches.append(f"{col_name}: expected int, got {actual_dtype}")
            elif expected_clean == "float" and actual_dtype not in ["float", "int"]:
                type_mismatches.append(f"{col_name}: expected float, got {actual_dtype}")

    # Use pytest.fail for consistency with other tests
    if type_mismatches:
        pytest.fail(f"Type mismatches in {func_name}: {' | '.join(type_mismatches)}")


def test_all_functions_have_docstrings():
    """Test that all data loading functions have docstrings."""
    missing_docstrings = []

    for func_name, func in DATA_FUNCTIONS:
        docstring = inspect.getdoc(func)
        if not docstring:
            missing_docstrings.append(func_name)

    if missing_docstrings:
        pytest.fail(f"Functions missing docstrings: {missing_docstrings}")


def test_all_docstrings_have_returns_section():
    """Test that all docstrings have a Returns section with column documentation."""
    missing_returns = []

    for func_name, func in DATA_FUNCTIONS:
        docstring = inspect.getdoc(func)
        if docstring:
            expected_columns = extract_docstring_columns(docstring)
            if not expected_columns:
                missing_returns.append(func_name)

    if missing_returns:
        pytest.fail(f"Functions missing Returns section with columns: {missing_returns}")


def test_functions_return_dataframes():
    """Test that all data loading functions return DataFrames."""
    for func_name, func in DATA_FUNCTIONS:
        df = func()
        assert isinstance(df, pd.DataFrame), f"{func_name} should return a DataFrame"
        assert not df.empty, f"{func_name} should return non-empty DataFrame"


def test_docstring_format_consistency():
    """Test that all docstrings follow consistent format."""
    format_issues = []

    for func_name, func in DATA_FUNCTIONS:
        docstring = inspect.getdoc(func)
        if docstring:
            lines = docstring.split("\n")

            # Check for Returns section
            has_returns = any("Returns" in line for line in lines)
            if not has_returns:
                format_issues.append(f"{func_name}: missing Returns section")

            # Check for column format (var : type description)
            expected_columns = extract_docstring_columns(docstring)
            if not expected_columns:
                format_issues.append(f"{func_name}: no columns found in Returns section")

    if format_issues:
        pytest.fail(f"Docstring format issues: {format_issues}")
