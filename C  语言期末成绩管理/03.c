#include "03.h"


int num = 0;	//人数

int Register()
{
	Ap Initial = { '\0' }, Current = { '\0' };
	FILE* fp;
	fp = fopen("000.dat", "r");
	if (fp == NULL)
	{
		fp = fopen("000.dat", "w");
		fclose(fp);
		fp = fopen("000.dat", "r");
		if (fp == NULL)
		{
			printf("error\n");
			printf("无法找到读取的文件,\n");
		}
	}
	fread(&Initial.Racc, sizeof(Initial.Racc), 1, fp);
	fread(&Initial.Rpas, sizeof(Initial.Rpas), 1, fp);
	fclose(fp);

	if (strlen(Initial.Racc) == 0)
	{
		printf("初始化账号：\n");
		gets(Initial.Racc);
		printf("初始化密码:\n");
		gets(Initial.Rpas);
		fp = fopen("000.dat", "w");
		if (fp == NULL)
		{
			printf("error");
			exit(0);
		}
		fwrite(&Initial.Racc, sizeof(Initial.Racc), 1, fp);
		fwrite(&Initial.Rpas, sizeof(Initial.Rpas), 1, fp);
		fclose(fp);
	}


	printf("输入账号：\n");
	gets(Current.Racc);
	printf("输入密码：\n");
	gets(Current.Rpas);
	if (strcmp(Initial.Racc, Current.Racc) == 0 && strcmp(Initial.Rpas, Current.Rpas) == 0)
	{
		printf("输入正确。\n");
		return 1;
	}
	else
	{
		printf("输入错误\n");
		return 0;
	}

}

void didplayMune()
{

	printf("===========================================\n");
	printf("===========================================\n");
	printf("==           1.录入学生信息              ==\n");
	printf("==           2.增加学生信息              ==\n");
	printf("==           3.删除学生信息              ==\n");
	printf("==           4.查找学生信息              ==\n");
	printf("==           5.修改学生信息              ==\n");
	printf("==           6.将当前信息储存至文件       ==\n");
	printf("==           7.输出所有学生信息           ==\n");
	printf("==           8.读取文件中的学生信息       ==\n");
	printf("==           0.退出                      ==\n");
	printf("\n\n");
	printf("首次进入程序请先录入信息后操作             ==\n\n");
	printf("===========================================\n");



}

void Inputstu()
{
	int add = 0;	//后续增加的人数
	int i = 0;		//循环控制
	printf("输入需要录入或者增加信息的人数：\n");
	if (num == 0)
	{
		scanf("%d", &add);
		num = add;
	}
	else
	{
		scanf("%d", &add);
		num = add+num;
	}
	getchar();
	for (i = 0; i < add; i++);
	{
		printf("第 %d 个：\n", i+1);
		printf("姓名：\n");
		scanf("%s", &stu[i].name);
		printf("学号：\n");
		scanf("%d", &stu[i].stunum);
		printf("班级:\n");
		scanf("%s", &stu[i].Class);
		printf("性别:\n");
		scanf("%s", &stu[i].sex);
		printf("专业:\n");
		scanf("%s", &stu[i].major);
		printf("综合成绩\n");
		scanf("%d", &stu[i].result);
	}
	if (i == num)
		printf("输入完成！");
	system("pause");
}

void Lookstu()
{
	if (num == 0)
	{
		printf("当前没有学生信息。\n");
		system("pause");
		return 0;
	}
	int i = 0;
	int nstu = 0;
	printf("输入将要查找的学号：\n");
	scanf("%d", &nstu);
	for (i = 0; i < num; i++)
	{
		if (nstu == stu[i].stunum)
		{
			printf("学生信息：\n");
			printf("%s\n", stu[i].name);
			printf("%d\n", stu[i].stunum);
			printf("%s\n", stu[i].Class);
			printf("%s\n", stu[i].sex);
			printf("%s\n", stu[i].major);
			printf("%d\n\n", stu[i].result);
		}
		else
		{
			printf("没有该学生！");
		}
	}
}

void  Delstu()
{
	if (num < 1)
	{
		printf("没有学生信息！");
		system("pause");
		return 0;
	}
	int sz;
	sz = num;
	char name[20] = { 0 };
	int i = 0;
	int s = 0;
	printf("输入将要删除的名字：\n");
	scanf("%s", &name);
	for (i = 0; i < sz; i++)
	{
		if (strcmp(name, stu[i].name) == 0)
		{
			printf("学生信息：\n");
			printf("%s", name);
			printf("%d\n", stu[i].stunum);
			printf("%s\n", stu[i].Class);
			printf("%s\n", stu[i].sex);
			printf("%s\n", stu[i].major);
			printf("%d\n\n", stu[i].result);
			printf("确认删除？(1/0)\n");
			scanf("%d", &s);
			if (s == 1)
			{
			//这里的方法（因为每个学生都输入了学号等信息，每个学生都是独立的）
			//是将最后一个学生的信息移到当前删除的位置，将最后一位的信息都变为0；
			//再将所有学生的个数减去1
				*stu[i].name = stu[sz].name;
				stu[i].stunum = stu[sz].stunum;
				*stu[i].Class = stu[sz].Class;
				*stu[i].sex = stu[sz].sex;
				*stu[i].major = stu[sz].major;
				stu[i].result = stu[sz].result;

				*stu[sz].name = 0;
				stu[sz].stunum = 0;
				*stu[sz].Class = 0;
				*stu[sz].sex = 0;
				*stu[sz].major = 0;
				stu[sz].result = 0;


				num = num - 1;
			}
			else
			{
				printf("退出。\n");
				break;
			}
		}
		else
		{
			printf("没有该学生！");
			break;
		}
	}
}

void modifystu()
{
	if (num < 1)
	{
		printf("没有学生信息可以修改。");
		return 0;
	}
	int i = 0;
	int s = 0;

	//储存修改信息的变量
	char name[20];
	char Nname[20];
	int Nstunum;
	char NClass[20];
	char Nsex[10];
	char Nmajor[20];
	char Nresult;
	
	//按名字修改
	printf("输入将要修改的学生的姓名：\n");
	scanf("%d", &name);
	for (i = 0; i < num; i++)
	{
		if (strcmp(name, stu[i].name) == 0)
		{
			//先输出信息
			printf("学生信息：\n");
			printf("%s", stu[i].name);
			printf("%d\n", stu[i].stunum);
			printf("%s\n", stu[i].Class);
			printf("%s\n", stu[i].sex);
			printf("%s\n", stu[i].major);
			printf("%d\n\n", stu[i].result);

			system("pause");//暂停后继续

			printf("   1.名字修改     2.学号修改   3.班级修改\n");
			printf("   4.性别修改     5.专业修改   6.成绩修改\n");
			printf("输入你的选择, 0则退出\n");
			scanf("%d", &s);
			switch (s)
			{
			case 1:
				scanf("%s", &Nname);
				*stu[i].name = Nname;
				break;
			case 2:
				scanf("%d", &Nstunum);
				stu[i].stunum = Nstunum;
				break;
			case 3:
				scanf("%s", &NClass);
				*stu[i].Class = NClass;
				break;
			case 4:
				scanf("%s", &Nsex);
				*stu[i].sex = Nsex;
				break;
			case 5:
				scanf("%s", &Nmajor);
				*stu[i].major = Nmajor;
				break;
			case 6:
				scanf("%d", &Nresult);
				stu[i].result = Nresult;
				break;
			default:
				printf("退出删除\n");
				break;
			}
		}
		else
		{
			printf("没有该学生！");
		}
	}
}
void save()
{
	if (num == 0)
	{
		printf("当前没有学生信息！");
		system("pause");
		return 0;
	}
	int i = 0;
	FILE* fp;
	fp = open("stu.txt", "wb");
	if (fp == NULL)
	{
		printf("file_error");
		system("pause");
	}
	for (i = 0; i < num; i++)
		if (fwrite(&stu[i], sizeof(Stu), 1, fp) != 1)
			printf("保存失败!!\n");
		printf("保存成功！\n");
		fclose(fp);
		system("pause");

}

void Print()
{
	if (num == 0)
	{
		printf("当前没有学生信息\n");
		system("pause");
		return 0;
	}
	int i = 0;
	for (i = 0; i < num; i++);
	{
		printf("第 %d 个学生信息：\n",i+1);
		printf("%s\n", stu[i].name);
		printf("%d\n", stu[i].stunum);
		printf("%s\n", stu[i].Class);
		printf("%s\n", stu[i].sex);
		printf("%s\n", stu[i].major);
		printf("%d\n\n", stu[i].result);
	}
}


void Update()
{
	int i = 0;
	int m = 0;	//读取后的人数
	FILE* fp;
	fp = fopen("stu.txt", "rb");
	if (fp == NULL)
	{
		printf("file_error\n");
		system("pause");
		return 0;
	}
	for (i = 0; i < N; i++)	//N为最大学生数（预处理）
	{
		if (fread(&stu[i], sizeof(Stu), 1,fp) == 1)
			m++;
	}
	if (m == 0)
		printf("读取失败！\n");
	else
	{
		printf("读取成功！\n");
		num = m;	//将读取后的人数赋给num
	}
	fclose(fp);
	system("pause");
}



