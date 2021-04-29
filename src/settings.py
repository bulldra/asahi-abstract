import os
import json

def load_json_setting(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    conf = open(path, 'r')
    return json.load(conf)

asahi_abstract＿dict = load_json_setting('../secrets/asahi_abstract.json')

# 文字列として保持
asahi_abstract_url = asahi_abstract＿dict['url']
asahi_abstract_token = asahi_abstract＿dict['token']
asahi_abstract_rate= str(asahi_abstract＿dict['rate']),
asahi_abstract_auto_paragraph = str(asahi_abstract＿dict['auto_paragraph']).lower()
