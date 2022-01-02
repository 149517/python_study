from socket import *
def main():
	# 1 创建套接字
	ss = socket(AF_INET,SOCK_STREAM)

	# 2 获取服务器的 ip和 port
	sever_ip = input("输入服务器的ip:")
	sever_port = int(input("输入服务器的port："))

	# 3 连接服务器
	ss.connect((sever_ip,sever_port))

	# 4 获取下载的文件名
	down_name = input("输入将要下载的文件名：")

	# 5 将文件名发送到服务器
	ss.send(down_name.encode("utf-8"))

	# 6 接收文件中的数据
	down_ = ss.recv(1024)

	# 7 将收到的数据储存到一个文件中
	if down_:
		with open("new"+down_name,'wb') as file_1:
			file_1.write(down_)
	else:
		print("没有找到文件")

	# 8 关闭套接字
	ss.close()

if __name__ == "__main__":
	main()