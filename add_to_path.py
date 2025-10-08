from pathlib import Path
import os
import subprocess

folder = Path(__file__).resolve().parent
current_path = os.environ.get("PATH", "")

if str(folder) not in current_path:
    subprocess.run(f'setx PATH "{current_path};{folder}"', shell=True)
    print(f"Successfully added folder to PATH: {folder}")
else:
    print("Already in PATH.")

input("Press Enter to continue...")