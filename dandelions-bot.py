import os
import time
import random
import subprocess
from datetime import datetime

def git_push():
    os.chdir("./dandelions/")
    subprocess.run(["git", "pull"])
    subprocess.run(["git", "add", "--all"])
    subprocess.run(["git", "commit", "-m", "dandelions"])

    # Git push with username and password input
    git_process = subprocess.Popen(["git", "push"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = git_process.communicate(input=b"<GITHUB_USERNAME>\n<PERSONAL_ACCESS_TOKEN>\n")
    print(stdout.decode(), stderr.decode())

    os.chdir("..")

def main():
    folder_path = "./dandelions/"
    files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    files.sort()  # Sort files for consistent rotation order

    while True:
        if not files:  # If no files are found in the folder, skip the rotation
            print("Error: No PNG files in the folder.")
            continue

        # Remove previous dandelions.png
        os.system(f'rm "./dandelions/dandelions.png"')
        git_push()

        # Select a random file from the list
        random_file = random.choice(files)

        # Copy the randomly selected file to dandelions.png
        os.system(f'cp "{os.path.join(folder_path, random_file)}" "{os.path.join(folder_path, "dandelions.png")}"')

        # Git commands
        git_push()

        # Wait for 30 minutes
        time.sleep(14400)

if __name__ == "__main__":
    main()
