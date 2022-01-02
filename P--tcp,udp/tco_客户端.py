from socket import *
def main():
	# 创建套接字
	tcp_socket = socket(AF_INET,SOCK_STREAM)
	# 链接服务器
	# 输入服务器及端口
	tcp_ip = input("输入服务区ip：")
	tcp_port = int(input("输入port："))
	server_addr = (tcp_ip,tcp_port)
	tcp_socket.connect(server_addr)

	# 发送信息
	data = input("输入发送的信息：")
	tcp_socket.sendall(data.encode('utf-8'))
	# 关闭
	tcp_socket.close()

if __name__ == "__main__":
	main()