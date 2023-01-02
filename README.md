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
[INFO] [1672681160.505342700] [listener]: Listen: 0
[INFO] [1672681160.981315600] [listener]: Listen: 1
[INFO] [1672681161.481508700] [listener]: Listen: 2
[INFO] [1672681161.981015500] [listener]: Listen: 3
[INFO] [1672681162.480755200] [listener]: Listen: 4
[INFO] [1672681162.981241400] [listener]: Listen: 5
[INFO] [1672681163.481100400] [listener]: Listen: 6
[INFO] [1672681163.980468500] [listener]: Listen: 7
[INFO] [1672681164.481511900] [listener]: Listen: 8
[INFO] [1672681164.981227600] [listener]: Listen: 9
[INFO] [1672681165.481212700] [listener]: Listen: 10
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
