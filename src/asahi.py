import sys
import os
import json
import requests
import settings


def get_input_text_path():
    args = sys.argv
    if len(args) != 2:
        raise ValueError('処理対象ファイルがコマンド引数に指定されていません')
    path = args[1]
    if os.path.isfile(path) != True:
        raise ValueError('処理対象ファイルの指定が誤っています')
    return path

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'x-api-key': settings.asahi_abstract['token']
}

payload = json.dumps({
    'text': open(get_input_text_path(), 'r', encoding='UTF-8').read(),
    'rate': str(settings.asahi_abstract['rate']),
    'auto_paragraph': str(settings.asahi_abstract['auto_paragraph']).lower()
}).encode('utf-8')

r = requests.post(settings.asahi_abstract['url'], headers=headers, data=payload)
r.raise_for_status()

for x in r.json()['result']:
    print(x)
