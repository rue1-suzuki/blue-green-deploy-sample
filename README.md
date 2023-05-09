# docker-swarmを利用したブルーグリーンデプロイ

サンプルのためブルーグリーンの2世代のみ。

3世代以上の世代管理も可能です。

## ./*/docker-compose.yml

replicasは2以上にすることでコンテナを複数起動

コンテナ起動準備中のダウンタイムを解消(軽減)する

```yml
deploy:
    replicas: 3
```

新しいサービスに切り替える際には、

1. 新しいコンテナを作成
2. 古いコンテナを1つ停止
3. 新しいコンテナを開始

を古いサービスがなくなるまで繰り返す。

## スタックのデプロイ

```bash
bash switchStack.bash blue
```

*blueはディレクトリ名

## スタックの切り替え

```bash
bash switchStack.bash green
```

*greenはディレクトリ名

## https-portal

証明書はホストマシンのディレクトリをマウントして利用する

初回以降は新規発行不要

```yaml
volumes:
    - ../https-portal-data/:/var/lib/https-portal/
```
