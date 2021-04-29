import os
import json

def build_setting_path(path):
    return os.path.dirname(os.path.abspath(__file__)) + '/' + path

def load_json_setting(path):
    path = open(build_setting_path(path), 'r')
    return json.load(path)

asahi_abstract = load_json_setting('../secrets/asahi_abstract.json')
