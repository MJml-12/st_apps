# プロファイル予測アプリ (st_apps)

Streamlit製のシンプルなWebアプリ。氏名を入力すると、登録済みユーザーIDの照合と、外部APIを使った年齢・性別・国籍の予測を行います。

## 構成

```
st_apps/
├── index.py              # トップページ
├── pages/
│   └── test.py           # プロファイル予測ページ
├── assets/
│   └── known_people.json # 既知ユーザーのID照合用データ
├── requirements.txt
└── README.md
```

## 利用している外部API

- [Agify.io](https://agify.io/) — 名前から年齢を予測
- [Genderize.io](https://genderize.io/) — 名前から性別を予測
- [Nationalize.io](https://nationalize.io/) — 名前から国籍を予測

無料プランはリクエスト数に制限があるため、上限を超えるとエラー（`{"error": ...}`）が返ります。

## セットアップ

1. (任意) 仮想環境を作成

   ```bash
   conda create -n st_apps_2026 python=3.12
   conda activate st_apps_2026
   ```

2. 依存パッケージをインストール

   ```bash
   pip install -r requirements.txt
   ```

## 実行方法

```bash
streamlit run index.py
```

ブラウザで `http://localhost:8501` が開きます。サイドバーから「test」ページを選択し、名字・名前を入力して「終了する」ボタンを押すと、ユーザーID照合とAPIによる予測結果が表示されます。

## 既知ユーザーの登録

`assets/known_people.json` に以下の形式でユーザーを追加すると、入力した氏名がID付きで照合されます。

```json
[
  { "id": 1, "first_name": "jamal", "family_name": "muhamad" }
]
```
