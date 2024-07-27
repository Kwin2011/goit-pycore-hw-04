import sys
from pathlib import Path
from colorama import init, Fore

def visualize_directory_structure(directory_path):
    init(autoreset=True)
    try:
        path = Path(directory_path)
        if not path.exists() or not path.is_dir():
            print(f"Error: Path '{directory_path}' does not exist or is not a directory.")
            return

        def walk_directory(current_path, prefix=""):

            for item in current_path.iterdir():
                if item.name != ".git":
                    if item.is_dir():
                        print(Fore.BLUE + prefix + "📂 " + item.name)
                        walk_directory(item, prefix + "    ")
                    else:
                        print(Fore.GREEN + prefix + "📜 " + item.name)

        walk_directory(path)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("___Usage: python task_3.py <directory_path>")
        visualize_directory_structure("C:/Users/Stefan-Main/Documents/My-repo/goit-pycore-hw-04/picture")
        # python task_3.py

    else:
        visualize_directory_structure(sys.argv[1])
        # python task_3.py C:/Users/Stefan-Main/Documents/My-repo/goit-pycore-hw-04


