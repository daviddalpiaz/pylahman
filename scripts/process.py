import os
import pandas as pd

raw_data_dir = os.path.join(os.path.dirname(__file__), "..", "data-raw")
processed_data_dir = os.path.join(os.path.dirname(__file__), "..", "src/pylahman/data")


def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def preprocess_csv(input_file, output_file):
    with (
        open(input_file, "r", newline="", encoding="utf-8") as infile,
        open(output_file, "w", newline="", encoding="utf-8") as outfile,
    ):
        for line in infile:
            processed_line = []
            in_field = False
            length = len(line)
            i = 0
            while i < length:
                char = line[i]
                if char == ",":
                    # check if comma is followed by a space
                    if i + 1 < length and line[i + 1] == " ":
                        # comma followed by space is part of the field
                        if not in_field:
                            processed_line.append('"')
                            in_field = True
                        processed_line.append(char)
                    else:
                        # comma not followed by a space is a field separator
                        if in_field:
                            processed_line.append('"')
                            in_field = False
                        processed_line.append(char)
                elif char == "\n":
                    # end of the line, close the last field if open
                    if in_field:
                        processed_line.append('"')
                    processed_line.append("\n")
                    in_field = False
                elif char == "\r":
                    pass
                else:
                    if not in_field:
                        processed_line.append('"')
                        in_field = True
                    processed_line.append(char)
                i += 1
            if in_field:
                processed_line.append('"')
            outfile.write("".join(processed_line))


def convert_csv_to_parquet(csv_file, parquet_file):
    encodings = ["utf-8", "ISO-8859-1"]
    for encoding in encodings:
        try:
            df = pd.read_csv(csv_file, encoding=encoding)
            df.to_parquet(parquet_file, index=False)
            print(f"Converted {csv_file} to {parquet_file} using {encoding}")
            break
        except UnicodeDecodeError:
            print(f"Failed to read {csv_file} with encoding {encoding}")
            continue
        except Exception as e:
            print(f"Error processing {csv_file}: {e}")
            break


def process_all_files():
    ensure_directory_exists(processed_data_dir)
    for file_name in os.listdir(raw_data_dir):
        if file_name.endswith(".csv"):
            csv_path = os.path.join(raw_data_dir, file_name)
            if file_name == "Schools.csv":
                preprocessed_csv = os.path.join(raw_data_dir, file_name.replace(".csv", "_preprocessed.csv"))
                preprocess_csv(csv_path, preprocessed_csv)
                parquet_path = os.path.join(processed_data_dir, file_name.replace(".csv", ".parquet"))
                convert_csv_to_parquet(preprocessed_csv, parquet_path)
                os.remove(preprocessed_csv)
            else:
                parquet_path = os.path.join(processed_data_dir, file_name.replace(".csv", ".parquet"))
                convert_csv_to_parquet(csv_path, parquet_path)


if __name__ == "__main__":
    process_all_files()
