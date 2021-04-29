import sys
import os
import json
import requests
import settings

def main():
    text = open(build_input_text_path(), 'r', encoding='UTF-8').read()
    r = get_abstract_text(text)
    for x in r:
        print(x)

def build_input_text_path():
    args = sys.argv
    if len(args) != 2:
        raise ValueError('処理対象ファイルがコマンド引数に指定されていません')
    path = args[1]
    if os.path.isfile(path) != True:
        raise ValueError('処理対象ファイルの指定が誤っています')
    return path

def get_abstract_text(text):
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': settings.asahi_abstract_token
    }

    payload = json.dumps({
        'text': text,
        'rate': settings.asahi_abstract_rate,
        'auto_paragraph': settings.asahi_abstract_auto_paragraph
    }).encode('utf-8')

    r = requests.post(settings.asahi_abstract_url, headers=headers, data=payload)
    r.raise_for_status()
    return r.json()['result']

if(__name__ == '__main__'):
    main()
