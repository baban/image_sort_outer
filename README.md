

## 使い方

### 画像にタグを付与する

`/mnt/c/cg/`以下に画像をおいている場合、deepdanbooruを使って、以下の様にして画像にタグを付与します。

```sh
deepdanbooru evaluate /mnt/c/cg/*.{jpg,png,webp} --project-path ./train-data --save-txt
```

### タグを参考に画像を分類する

画像と同じディレクトリに、タグを記述したtxtファイルを用意してください。

その状態で以下のコマンドを実行。

```sh
python ./filter.py
```

