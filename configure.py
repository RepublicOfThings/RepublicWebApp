import os
import yaml

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

config = yaml.load(open(PROJECT_DIR+"/webapp/static/app/config.yml"))

print(config)