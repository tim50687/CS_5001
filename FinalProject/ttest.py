import turtle
import time
import glob, os


for file in os.listdir("./slider_puzzle_project_fall2021_assets-2022"):
    if file.endswith(".puz"):
        print(file)
