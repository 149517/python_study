from socket import *

def main():
	# 1 创建套接字
	ss = socket(AF_INET, SOCK_STREAM)

	# 2 绑定本地信息
	ss.bind(("",7788))

	# 3 将套接字转为被动
	ss.listen(128)

	# 4 等待客户端连接
	new_socket, sock_addr = ss.accept()

	# 5 接收请求
	recv_data = new_socket.recv(1024).encode("utf-8")
	print("客户端想要下载："+ recv_data)

	# 6 回复
	file = ''
	try:
		file_1 = open("../000.txt","rb")
		file = file_1.read()
		new_socket.send(file)
	except:
		print("没有这个文件")
		new_socket.send("没有这个文件")	
	
	# 关闭套接字
	new_socket.close()
	ss.close()

if __name__ == "__main__":
	main()