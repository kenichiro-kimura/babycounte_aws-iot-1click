# AWS IoT 1-click Buttonを使った赤ちゃんの活動記録

## 概要

赤ちゃんが小さいときは、排泄や授乳の記録をつけるのはとても大切です。
しかし、実際にやろうとしても小さい赤ちゃんの相手をしながらマメにノートに書くのはとても大変です。
そこで、せめてボタン1クリックでイベントとその時間だけでも記録できればとの思いから作成しました

ボタンクリックが「おしっこ」、ダブルクリックが「うんち」、ロングクリックが「ミルク」に対応しており、押した時間とイベント名をgoogleスプレッドシートに記録します。

また、家族との情報共有として、それぞれのイベント時に「(赤ちゃん名)おしっこした！」「(赤ちゃん名)うんちした！」「(赤ちゃん名)ミルク飲んだ！」とLINEのグループ等に投稿します。これが不要な場合は該当のソースを削って下さい。

## 使い方概要

AWSのアカウントの作り方などの詳細は適宜調べてください。

LINEへの投稿が不要であればMessagin APIの契約やそれに付随する設定は不要です。

逆に、googleスプレッドシートへの登録が不要であればそれに付随する設定は不要ですし、該当のコードを削除してお使い下さい。


- python2.7をインストールする
- AWSのアカウントを作り、aws cliが動くようにする
- [この辺](https://aws.amazon.com/jp/iot-1-click/devices/)を見てデバイスを入手する
  - 個人的には接続が簡単で電池も変えられる[SORACOM LTE-M Button powered by AWS](https://pages.soracom.jp/LP_SORACOM-LTE-M-Button.html)がお勧めです。
- このプロジェクトをgit cloneする
- serverless frameworkをインストールする
  ```bash
  %pip install serverless
  ```
- 必要なライブラリを入れる
  ```bash
  %pip install -r requirements.txt -t ./
  ```
- クリック()  
- 取りあえずデプロイする
  ```bash
  %sls deploy
  ```
- LINE Messaging APIのDeveloper Trial(無償)を契約してボットアカウントを作る
- デプロイ時に表示されたAPI GatewayのURLを、Messaging APIのコールバックに登録する
- ボットアカウントとLINEで友達になり、適当なグループを作成してそこに招待する
- AWSのコンソールから、Lambda関数「babycounter-hello-dev」のCloudWatch Logsを見るとグループ招待のイベントログが出てるはずなので「groupId」の部分を取得してconfig.iniに記載する
- googleのcredentialを取得する
  - https://console.developers.google.com/project にアクセス
  - [プロジェクト作成] にてプロジェクトを作成
  - 作成したプロジェクトの API Manager から [Drive API] をクリック
  - Google Drive API にて [有効にする] をクリック
  - API Manager のメニューから [認証情報] をクリック
  - [サービス アカウント] プルダウンより [新しいサービスアカウント] をクリック
  - [サービス アカウント名] に任意の名前を入力
  - [役割] にて [Project] の [編集者] をクリック
  - [キーのタイプ] は [JSON] を選択
  - 最後に [作成] ボタンをクリック
  これで取得したファイルを適当な名前でgit cloneしたディレクトリに置き、ファイル名をconfig.iniに記載する
- googleスプレッドシートの新規ファイルを作成し、上記のcredentialに含まれるメールアドレスに対して共有を出す
- googleスプレッドシートのシート名と、ID(URLがhttps://docs.google.com/spreadsheets/d/hogehoge/...となっていると思うので、この「hogehoge」の部分)を取得してconfig.iniに書く
- もう1回デプロイする
  ```bash
  %sls deploy
  ```
- ボタンをひもづける
  - AWSのコンソールないしはCLIで、作成されたLambda関数「babycounter-sendmsg-dev」にボタンをひもづける


 
