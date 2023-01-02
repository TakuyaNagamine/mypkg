#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 Takuya Nagamine 　　　　　
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():          #ヘッダの下にTalkerというクラスを作成
    def __init__(self):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
rclpy.init()
node = Node("talker")
talker = Talker()

def cb():              #関数内のnやpubをtalkerのものに変更
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)
    talker.n += 1

srv = node.create_service(0.5, cb)
rclpy.spin(node)
