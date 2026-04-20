import os

shots = []

shots_dir = "renders/final"

for file in os.listdir(shots_dir):
    if file.endswith(".mp4"):
        shots.append(file)

with open("shots.txt", "w") as f:
    for shot in shots:
        f.write(f"file '{shots_dir}/{shot}'\n")

print("shots.txt created")
