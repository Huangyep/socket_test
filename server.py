# -*- coding: UTF-8 -*-
import socket

s = socket.socket()          # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 777                   # 设置端口,端口被占用修改端口或是关闭任务管理器
s.bind((host,port))          # 绑定端口
s.listen(5)                  # 等待客户端连接

while True:
    c,addr = s.accept()      # 建立客户端连接。
    print ('连接地址: ',addr)
    msg = '来自服务端的消息：你好'
    c.send(bytes(msg,encoding="utf-8"))#向客户端发送消息
    while True:
        accept_msg = str(c.recv(1024),encoding="utf-8")
        print("".join(["客户端：", accept_msg,"   端口：", str(addr[1])]))
        if accept_msg == "断开连接":
            break
        send_msg = input("服务端：")
        c.sendall(bytes(send_msg,encoding="utf-8"))
    c.close()                # 关闭连接
