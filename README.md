# mypkg
![test](https://github.com/TakuyaNagamine/mypkg/actions/workflows/test.yml/badge.svg)
## 本リポジトリについて
このリポジトリには千葉工業大学にて開講されている「ロボットシステム学」の講義内で取り扱われているプログラムを含めたリポジトリである
## パッケージ内容
- talker.py
  - countupというトピックを通じて,16ビットの符号付き整数を送信する.
- litener.py
  - countupというトピックからメッセージを受信し,terminalに出力する. 
- talk_listen.launch.py
  - このパッケージに含まれている２つのノードを一度に立ち上げる事ができる.
## 実行方法
### run
1. ターミナルにて以下のコマンドを実行
  ```
  $ros2 run mypkg talker
  ```
2. 新たにターミナルを起動し,以下のコマンドを実行
  ```
  $ros2 run mypkg listener
  ```
* 実行結果
- 新たに起動したターミナルに以下のような結果が表示される
  ```
  [INFO] [1672680918.309449900] [listener]: Listen: 33
  [INFO] [1672680918.781468700] [listener]: Listen: 34
  [INFO] [1672680919.281392000] [listener]: Listen: 35
  [INFO] [1672680919.781785100] [listener]: Listen: 36
  [INFO] [1672680920.280769100] [listener]: Listen: 37
  [INFO] [1672680920.781184700] [listener]: Listen: 38
  ```
## 動作確認済み環境
- ROS
  - ROS2 foxy
  - ROS2 Humble
- OS
  - Ubuntu 20.04 LTS  
  - Ubuntu 22.04 LTS  
## ライセンス
  - このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。
  - このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです
    - [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
  - © 2022 Takuya Nagamine
