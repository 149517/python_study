import socket
def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# 绑定一个本地信息

	local_addr = ("",7788)
	udp_socket.bind(local_addr)

		# 接受数据
	while True:
		recv_data = udp_socket.recvfrom(1024)

		recv_msg = recv_data[0] 	# 接受的内容信息
		send_addr = recv_data[1]	# 接受的发送者的地址

		# 打印接受的数据
		print(recv_data)
		print("%s:%s"%(str(send_addr),recv_msg.decode("gbk"))) # 解码

	# 关闭套接字
	udp_socket.close()

if __name__ == "__main__":
	main()