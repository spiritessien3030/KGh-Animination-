import bpy
import json
from datetime import datetime

CONFIG_PATH = "//pipeline/config.json"

def load_config():
    with open(bpy.path.abspath(CONFIG_PATH)) as f:
        return json.load(f)

def setup_render(config):
    scene = bpy.context.scene

    scene.render.image_settings.file_format = 'PNG'
    scene.render.filepath = "//renders/frames/"

    scene.render.resolution_x = config["resolution"][0]
    scene.render.resolution_y = config["resolution"][1]

    scene.render.fps = config["fps"]

    scene.frame_start = config["frame_range"][0]
    scene.frame_end = config["frame_range"][1]

def render():
    bpy.ops.render.render(animation=True)

def log():
    with open(bpy.path.abspath("//pipeline/log.txt"), "a") as f:
        f.write(f"Rendered at {datetime.now()}\n")

if __name__ == "__main__":
    config = load_config()
    setup_render(config)
    render()
    log()
