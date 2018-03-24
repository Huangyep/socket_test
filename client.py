# -*- coding: UTF-8 -*-
import socket

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 777                  # 设置端口号
s.connect((host, port))

data= s.recv(1024)
print(str(data,encoding="utf-8"))
msg = "已连接"
s.sendall(bytes(msg,encoding="utf-8"))

while True:
    send_msg = input("客户端：")
    s.sendall(bytes(send_msg,encoding="utf-8"))
    if send_msg == "断开连接":
        break
    accept_msg = str(s.recv(1024),encoding="utf-8")
    print("".join(("服务端：",accept_msg)))

s.close()                      #关闭连接