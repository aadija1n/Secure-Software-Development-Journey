
from pathlib import Path
import platform

def main() -> None:
	print("Journey Started !!!")
	print(f"Python version : {platform.python_version()}")
	print(f"Running on : {platform.system()}")
	print(f"File Location : {Path(__file__).resolve()}")

if __name__ == "__main__":
	main()
