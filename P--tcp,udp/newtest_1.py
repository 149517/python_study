import socket
def main():

	# �����׽���
	udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	# �ֶ�����Է���ip�Ͷ˿�
	dest_ip = input("����Է�ip")
	dest_port = int(input("����Է�port"))

	# ѭ�����ͺͽ���
	while True:

		send_date = input("��Ҫ���͵����ݣ�")

	# ������Ϣ
		udp_socket.sendto(send_date.encode("gbk"),(dest_ip,dest_port))

		#����
		recv_date = udp_socket.recvfrom(1024)

		recv_msg = recv_date[0] 	# ���ܵ�������Ϣ
		send_addr = recv_date[1]	# ���ܵķ����ߵĵ�ַ

		print(recv_date)
		print("%s:%s"%(str(send_addr),recv_msg.decode("gbk"))) # ����
	udp_socket.close()

if __name__ == "__main__":
	main()