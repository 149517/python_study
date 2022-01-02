#include "03.h"

int main()
{
	if (Register())
	{
		
		int xz = 0;//选择控制变量
		while (1)
		{
			//菜单
			didplayMune();
			scanf("%d", &xz);
			switch (xz)
			{
			case 1:
				printf("            录入学生信息\n");
				Inputstu();
				system("pause");
				system("cls");
				break;
			case 2:
				printf("            增加学生信息\n");
				Inputstu();
				system("pause");
				system("cls");
				break;
			case 3:
				printf("            删除学生信息\n");
				Delstu();
				system("pause");
				system("cls");
				break;
			case 4:
				printf("            查找学生信息\n");
				Lookstu();
				system("pause");
				system("cls");
				break;
			case 5:
				printf("            修改学生信息\n");
				modifystu();
				system("pause");
				system("cls");
				break;
			case 6:
				printf("      将学生信息储存至文件\n");
				save();
				system("pause");
				system("cls");
				break;
			case 7:
				printf("        输出所有学生的信息\n");
				Print();
				system("pause");
				system("cls");
				break;
			case 8:
				printf("      读取文件中的学生信息\n");
				Update();
				system("pause");
				system("cls");
				break;
			case 0:
				exit(0);
				break;
			default:
				printf("输入错误！\n");
				system("pause");
				system("cls");
			}
		}
	}
	return 0;

}