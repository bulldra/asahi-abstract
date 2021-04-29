import sys
import json
import requests
import settings

args = sys.argv
if len(args) != 2:
    raise ValueError('処理対象ファイルがコマンド引数に指定されていません')
text_file = args[1]
text = open(text_file, 'r', encoding='UTF-8').read()

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',   
    'x-api-key': settings.asahi_abstract['token']
}

payload = json.dumps({
    'text': text, 
    'rate': str(settings.asahi_abstract['rate']),
    'auto_paragraph': str(settings.asahi_abstract['auto_paragraph']).lower()
}).encode('utf-8')

r = requests.post(settings.asahi_abstract['url'], headers=headers, data=payload)
r.raise_for_status()

for x in r.json()['result']:
    print(x)
