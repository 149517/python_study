#define  _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

#define N 10
typedef struct Ap{
	char Racc[20];
	char Rpas[20];
}Ap;
//Ap  �˺�����ṹ����

typedef struct Stu{
	char name[20];
	int  stunum;
	char Class[20];
	char sex[10];
	char major[20];
	int result;
}Stu;
Stu stu[N];


int Register();		//�˺�ע�ἰ��¼
void didplayMune();	//�˵�
void Inputstu();		//��Ϣ¼��,����ѧ��
void Delstu();		//ɾ��ѧ����Ϣ
void Lookstu();		//����ѧ����Ϣ
void modifystu();	//�޸�ѧ����Ϣ
void save();		//��ѧ����Ϣ�������ļ�
void Print();		//��������ļ���Ϣ
void Update();		//���ļ��ж�ȡ��Ϣ