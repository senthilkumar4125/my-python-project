import shutil
import os

source = "./build"
destination = "/tmp/deployed_app"

os.makedirs(source, exist_ok=True)
os.makedirs(destination, exist_ok=True)

with open(f"{source}/output.txt", "w") as f:
    f.write("Build artifact for deployment")

shutil.copytree(source, destination, dirs_exist_ok=True)
print("Deployment successful! Files copied to:", destination)
