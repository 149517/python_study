#include "03.h"

int main()
{
	if (Register())
	{
		
		int xz = 0;//ѡ����Ʊ���
		while (1)
		{
			//�˵�
			didplayMune();
			scanf("%d", &xz);
			switch (xz)
			{
			case 1:
				printf("            ¼��ѧ����Ϣ\n");
				Inputstu();
				system("pause");
				system("cls");
				break;
			case 2:
				printf("            ����ѧ����Ϣ\n");
				Inputstu();
				system("pause");
				system("cls");
				break;
			case 3:
				printf("            ɾ��ѧ����Ϣ\n");
				Delstu();
				system("pause");
				system("cls");
				break;
			case 4:
				printf("            ����ѧ����Ϣ\n");
				Lookstu();
				system("pause");
				system("cls");
				break;
			case 5:
				printf("            �޸�ѧ����Ϣ\n");
				modifystu();
				system("pause");
				system("cls");
				break;
			case 6:
				printf("      ��ѧ����Ϣ�������ļ�\n");
				save();
				system("pause");
				system("cls");
				break;
			case 7:
				printf("        �������ѧ������Ϣ\n");
				Print();
				system("pause");
				system("cls");
				break;
			case 8:
				printf("      ��ȡ�ļ��е�ѧ����Ϣ\n");
				Update();
				system("pause");
				system("cls");
				break;
			case 0:
				exit(0);
				break;
			default:
				printf("�������\n");
				system("pause");
				system("cls");
			}
		}
	}
	return 0;

}