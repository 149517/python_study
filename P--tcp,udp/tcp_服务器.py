from socket import *

def main():
	# 创建套接字
	tcp_socket = socket(AF_INET,SOCK_STREAM)

	# 绑定本地信息
	tcp_socket.bind(("",7080))

	# 让默认的套接字由主动转为被动
	tcp_socket.listen(128)

	# 等待客户端的连接
	while True:
		print("dengdai")
		new_client_socket, client_addr = tcp_socket.accept()
		print("连接成功")
		print("连接者的地址为：" + str(client_addr))

		# 接收客户端的请求
		while True:
			recv_data = new_client_socket.recv(1024)
			print(recv_data)

			# 回复客户端
			if recv_data:
				new_client_socket.send("hello.___ok___".encode('utf-8'))
			else:
				break

		# 关闭套接字
		new_client_socket.close()
	tcp_socket.close()

if __name__ == "__main__":
	main()