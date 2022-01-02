#define  _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define N 10
typedef struct Ap{
	char Racc[20];
	char Rpas[20];
}Ap;
//Ap  账号密码结构类型

typedef struct Stu{
	char name[20];
	int  stunum;
	char Class[20];
	char sex[10];
	char major[20];
	int result;
}Stu;
Stu stu[N];


int Register();		//账号注册及登录
void didplayMune();	//菜单
void Inputstu();		//信息录入,增加学生
void Delstu();		//删除学生信息
void Lookstu();		//查找学生信息
void modifystu();	//修改学生信息
void save();		//将学生信息储存至文件
void Print();		//输出所有文件信息
void Update();		//从文件中读取信息