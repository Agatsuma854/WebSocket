# -*- coding: utf-8 -*-
'''
client0.pyプログラム
Pythonによるクライアントソケットの利用法をしてす例題プログラム(0)
50000番ポートでサーバに接続します
使い方 $ python3 ./client0.py
'''

import socket

HOST = "localhost"  # HostName which is connected server
# HOST = "127.0.0.1 # 接続先ホストの名前
POST = 50000  # Port number
BUFSIZE = 4096  # RX buffer size

## main ##
# make socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
client.connect((HOST, POST))
# recv msg by server
data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
# close connect
client.close()

# end