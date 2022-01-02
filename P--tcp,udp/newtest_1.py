import socket
def main():

	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	# 手动输入对方的ip和端口
	dest_ip = input("输入对方ip")
	dest_port = int(input("输入对方port"))

	# 循环发送和接收
	while True:

		send_date = input("将要发送的内容：")

	# 发送信息
		udp_socket.sendto(send_date.encode("gbk"),(dest_ip,dest_port))

		#接受
		recv_date = udp_socket.recvfrom(1024)

		recv_msg = recv_date[0] 	# 接受的内容信息
		send_addr = recv_date[1]	# 接受的发送者的地址

		print(recv_date)
		print("%s:%s"%(str(send_addr),recv_msg.decode("gbk"))) # 解码
	udp_socket.close()

if __name__ == "__main__":
	main()