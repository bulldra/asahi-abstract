#!/usr/bin/env python3

__author__ = "bulldra"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import argparse
import json
import requests
import settings

def main(args):
    path = args.arg1
    if os.path.isfile(path) != True:
        raise ValueError('処理対象ファイルの指定が誤っています')

    text = open(path, 'r', encoding='UTF-8').read()
    r = get_abstract_text(text)
    for x in r:
        print(x)

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
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', help='処理対象ファイル名')
    parser.add_argument("--version", action="version", version="%(prog)s (version {version})".format(version=__version__))
    args = parser.parse_args()
    main(args)
