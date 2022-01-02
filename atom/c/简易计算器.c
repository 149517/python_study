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
				printf("按任意键继续。。。。回车退出\n");
				while (getchar() != '\n')
				{
					printf("\n--------------------------------------------\n");
					displayMenu();
					printf("按任意键继续。。。。回车退出\n");
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
	printf("1－加法 2－减法 3－乘法 4－除法 5－求余 6－阶乘 7－累加 8－结束\n");
	while(scanf("%d", &m) == 1 && m <= 8)//防止错误输入
	{
		if (m <= 5)
		{
			printf("简单计算器\n");
			printf("输入数字和运算符号：\n");
			//scanf("%d %c %d", &a, &op, &b);
			//防止错误输入
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
					printf("输入错误；\n");
					return 0;
				}
			}
			else
			{
				printf("输入错误\n");
				printf("重新输入\n");
				printf("1－加法 2－减法 3－乘法 4－除法 5－求余 6－阶乘 7－累加 8－结束\n");
			}
		}
		else
		{
			if (m == 8)
			{
				printf("退出\n");
				exit(0);
			}
			else
			{
				printf("输入期望求出的值以内的数字\n");
				//防止错误输入
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
						printf("输入错误；\n");
					}
				}
				else
				{
					printf("输入错误\n");
					printf("重新输入\n");
					printf("1－加法 2－减法 3－乘法 4－除法 5－求余 6－阶乘 7－累加 8－结束\n");

				}
			}
		}
		printf("1－加法 2－减法 3－乘法 4－除法 5－求余 6－阶乘 7－累加 8－结束\n");
		printf("输入错误将会退出！\n");

	}
	printf("输入错误，\n");
	printf("程序退出\n");
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
	printf("%d以内的阶乘=%d\n", a, sum);
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
	printf("%d以内的累加=%d\n", a, sum);
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
		printf("输入账号信息：\n");
		scanf("%s", &yhzh);
		if (strcmp(yhzh, AccountName) == 0)
		{
			printf("输入正确\n\n");
			break;
		}
		else
		{
			printf("输入错误\n\n");
			count++;
		}
		if (count >= 5)
		{
			printf("输入错误次数过多：自动退出\n");
			return 0;
			break;
		}
	}
	if (count < 5)
	{
		count = 0;
		while (1)
		{
			printf("输入密码：\n");
			scanf("%s", &yhmm);
			if (strcmp(yhmm, Password) == 0)
			{
				printf("输入正确;\n\n");
				break;
			}
			else
			{
				printf("输入错误\n\n");
				count++;
			}
			if (count >= 5)
			{
				printf("输入错误次数过多：自动退出\n");
				return 0;
				break;
			}
		}
		return 1;
	}
}
