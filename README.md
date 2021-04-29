# 朝日新聞長文要約APIラッパー

https://cl.asahi.com/api_data/longsum.html

上記の朝日新聞長文要約生成を取り扱うプログラム  
設定ファイルとローカルのテキストファイルを読み込んでDocker上で実行

## ビルド方法

```bash
# docker-compose build
```

secrets/asahi_abstract.json に設定ファイルを作成

```json
{
    "url": "https://clapi.asahi.com/abstract",
    "token": "xxx",
    "rate": 0.5,
    "auto_paragraph": false
}
```

## 実行方法

```bash
# docker-compose run --entrypoint "python /data/src/asahi.py /data/work/test.txt" asahi-abstract
```

