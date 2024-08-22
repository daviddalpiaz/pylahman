import subprocess
import sys


def run_process_script():
    print("Processing raw data...")
    subprocess.check_call([sys.executable, "scripts/process.py"])


def run_build_command():
    print("Building package...")
    subprocess.check_call(
        [
            "uvx",
            "--from",
            "build",
            "pyproject-build",
            "--sdist",
            "--installer",
            "uv",
        ]
    )
    subprocess.check_call(
        [
            "uvx",
            "--from",
            "build",
            "pyproject-build",
            "--wheel",
            "--installer",
            "uv",
        ]
    )


def main():
    run_process_script()
    run_build_command()


if __name__ == "__main__":
    main()
