# -*- coding: utf-8 -*-
'''
get_host_by_name.py プログラム
ホスト名をIPアドレスに変換するプログラム
使い方 $ python3 ./gethostbyname.py
'''

import socket


def get_host_by_name():
    while True:
        try:
            hostname = input("Input hostname (end : q) : ")
            if hostname == 'q':
                break
            print(socket.gethostbyname(hostname))
        except:
            print("Don't conversion")


# end get_host_by_name


if __name__ == "__main__":
    get_host_by_name()
