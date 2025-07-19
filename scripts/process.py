import os
import pandas as pd


raw_data_dir = os.path.join(os.path.dirname(__file__), "..", "data-raw")
processed_data_dir = os.path.join(os.path.dirname(__file__), "..", "src/pylahman/data")


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
                    dtype_backend="pyarrow",
                    engine="pyarrow",
                )
            else:
                df = pd.read_csv(
                    csv_path,
                    dtype_backend="pyarrow",
                    engine="pyarrow",
                )
            df.to_parquet(parquet_path, index=False)
            print(f"Converted {csv_path} to {parquet_path}")


if __name__ == "__main__":
    process_raw_csv_files()
