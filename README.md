# 第17回 自主課題｜都市の天気検索・比較アプリ

## アプリの目的

日本の都市の現在の気温と湿度を調べ、2都市の気温を比較するアプリです。旅行や移動の前に、行き先と出発地の気温を確かめる用途を想定しています。コンソール版とTkinterのGUI版の両方を作り、天気の取得と気温の比較には共通の処理を使います。

**最初に [課題の手順と完成条件](TASK.md) を読んでください。** 実装と動作確認ができたら、このREADMEに実際の操作方法や確認結果を記録します。

## 対象都市とデータ

札幌・東京・大阪・広島・福岡。各都市の代表地点の緯度・経度は [cities.py](cities.py) に用意してあります。天気を取得するにはインターネット接続が必要です。授業ではAPIキーを使いません。気象データの提供元は [Open-Meteo](https://open-meteo.com/) です。

## 準備

授業で指定された自分の提出用リポジトリをGitでクローンし、README.mdがあるフォルダーをPyCharmで開いてください。Python 3.10以上を使います。PyCharmのインタープリターにも、以下で作る仮想環境を指定します。

**Windows（PowerShell）**

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m tkinter
```

**macOS**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m tkinter
```

小さな確認用ウィンドウが開いたら閉じてください。

## 起動

| 環境 | コンソール版 | GUI版 |
| --- | --- | --- |
| Windows | `.\.venv\Scripts\python.exe cli.py` | `.\.venv\Scripts\python.exe gui.py` |
| macOS | `.venv/bin/python cli.py` | `.venv/bin/python gui.py` |

現在はコンソール版の1都市の天気取得と2都市の気温比較を実装しています。GUIは未実装です。完成後の起動方法は次のとおりです。

## 操作方法と実行例

ここに、両方の起動後の操作方法、実際に入力した都市名とコンソール出力を記入してください。完成したGUIのスクリーンショットをリポジトリに保存し、この場所にMarkdownで表示してください。

## 動作確認

[TASK.mdの確認表](TASK.md#動作確認)をもとに、入力・期待する結果・実際の結果を記録してください。

## Copilotの利用記録

自分が依頼した作業を一つ選び、その提案をどの入力と実行結果で確かめたかを書いてください。
