#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>
#include <stdlib.h>
#include <conio.h> 
#include <windows.h>

int displayMenu(void);
int AccountPassword();
int j_c(a);
int l_j(a);


int main()
{

	if (AccountPassword())
	{
		do
		{
			if (displayMenu() != 0)
			{
				getchar();
				printf("��������������������س��˳�\n");
				while (getchar() != '\n')
				{
					printf("\n--------------------------------------------\n");
					displayMenu();
					printf("��������������������س��˳�\n");
					getchar();
				}
				exit(0);
			}
			exit(0);

		} while (_getch() != '\n');

	}
}

int displayMenu(void)
{
	int m = 0;
	int a = 0, b = 0;
	char op = 0;
	printf("1���ӷ� 2������ 3���˷� 4������ 5������ 6���׳� 7���ۼ� 8������\n");
	while(scanf("%d", &m) == 1 && m <= 8)//��ֹ��������
	{
		if (m <= 5)
		{
			printf("�򵥼�����\n");
			printf("�������ֺ�������ţ�\n");
			//scanf("%d %c %d", &a, &op, &b);
			//��ֹ��������
			if (scanf("%d", &a) == 1 && scanf("%c", &op) == 1 && scanf("%d", &b) == 1)
			{
				switch (op)
				{
				case'+':
					printf("%d+%d=%d\n", a, b, a + b);
					break;
				case'-':
					printf("%d-%d=%d\n", a, b, a - b);
					break;
				case'*':
					printf("%d*%d=%d\n", a, b, a * b);
					break;
				case'/':
					printf("%d/%d=%d\n", a, b, a / b);
					break;
				case'%':
					printf("%d %% %d=%d\n", a, b, a % b);
					break;
				default:
					printf("�������\n");
					return 0;
				}
			}
			else
			{
				printf("�������\n");
				printf("��������\n");
				printf("1���ӷ� 2������ 3���˷� 4������ 5������ 6���׳� 7���ۼ� 8������\n");
			}
		}
		else
		{
			if (m == 8)
			{
				printf("�˳�\n");
				exit(0);
			}
			else
			{
				printf("�������������ֵ���ڵ�����\n");
				//��ֹ��������
				if (scanf("%d", &a) == 1)
				{
					switch (m)
					{
					case 6:
						j_c(a);
						break;
					case 7:
						l_j(a);
						break;
					default:
						printf("�������\n");
					}
				}
				else
				{
					printf("�������\n");
					printf("��������\n");
					printf("1���ӷ� 2������ 3���˷� 4������ 5������ 6���׳� 7���ۼ� 8������\n");

				}
			}
		}
		printf("1���ӷ� 2������ 3���˷� 4������ 5������ 6���׳� 7���ۼ� 8������\n");
		printf("������󽫻��˳���\n");

	}
	printf("�������\n");
	printf("�����˳�\n");
	return 0;

}
int j_c(int a)
{
	int i = 1;
	int sum = 1;

	for (i = 1; i <= a; i++)
	{
		sum = sum * i;
	}
	printf("%d���ڵĽ׳�=%d\n", a, sum);
	return 0;
}
int l_j(int a)
{
	int i = 0;
	int sum = 0;
	for (i = 1; i <= a; i++)
	{
		sum = sum + i;
	}
	printf("%d���ڵ��ۼ�=%d\n", a, sum);
	return 0;
}
int AccountPassword(void)
{
	char AccountName[] = "zhangxiao1230";
	char Password[] = "1234560789";

	char yhzh[20] = "0";
	char yhmm[20] = "0";
	int count = 0;
	while (1)
	{
		printf("�����˺���Ϣ��\n");
		scanf("%s", &yhzh);
		if (strcmp(yhzh, AccountName) == 0)
		{
			printf("������ȷ\n\n");
			break;
		}
		else
		{
			printf("�������\n\n");
			count++;
		}
		if (count >= 5)
		{
			printf("�������������ࣺ�Զ��˳�\n");
			return 0;
			break;
		}
	}
	if (count < 5)
	{
		count = 0;
		while (1)
		{
			printf("�������룺\n");
			scanf("%s", &yhmm);
			if (strcmp(yhmm, Password) == 0)
			{
				printf("������ȷ;\n\n");
				break;
			}
			else
			{
				printf("�������\n\n");
				count++;
			}
			if (count >= 5)
			{
				printf("�������������ࣺ�Զ��˳�\n");
				return 0;
				break;
			}
		}
		return 1;
	}
}
