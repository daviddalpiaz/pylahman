import os
import pandas as pd

script_path = os.path.dirname(__file__)
raw_data_dir = os.path.join(script_path, "..", "data-raw")
processed_data_dir = os.path.join(script_path, "..", "src/pylahman/data")


def process_raw_csv_files():
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
    for filename in os.listdir(raw_data_dir):
        if filename.endswith(".csv"):
            csv_path = os.path.join(raw_data_dir, filename)
            parquet_path = os.path.join(
                processed_data_dir,
                filename.replace(".csv", ".parquet"),
            )
            if filename == "Schools.csv":
                df = pd.read_csv(
                    csv_path,
                    quotechar='"',
                    dtype_backend="numpy_nullable",
                    engine="pyarrow",
                )
            else:
                df = pd.read_csv(
                    csv_path,
                    dtype_backend="numpy_nullable",
                    engine="pyarrow",
                )
            if filename == "People.csv":
                df["debut"] = pd.to_datetime(df["debut"])
                df["finalGame"] = pd.to_datetime(df["finalGame"])
            if filename == "HomeGames.csv":
                df["spanfirst"] = pd.to_datetime(df["spanfirst"])
                df["spanlast"] = pd.to_datetime(df["spanlast"])
            if filename == "Batting.csv":
                cols_to_drop = [col for col in ["G_batting", "G_old"] if col in df.columns]
                if cols_to_drop:
                    df = df.drop(columns=cols_to_drop)
            df.to_parquet(parquet_path, index=False, engine="pyarrow", compression="zstd")
            print(f"Converted {csv_path} to {parquet_path}")


if __name__ == "__main__":
    process_raw_csv_files()
