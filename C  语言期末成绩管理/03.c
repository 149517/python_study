#include "03.h"


int num = 0;	//����

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
			printf("�޷��ҵ���ȡ���ļ�,\n");
		}
	}
	fread(&Initial.Racc, sizeof(Initial.Racc), 1, fp);
	fread(&Initial.Rpas, sizeof(Initial.Rpas), 1, fp);
	fclose(fp);

	if (strlen(Initial.Racc) == 0)
	{
		printf("��ʼ���˺ţ�\n");
		gets(Initial.Racc);
		printf("��ʼ������:\n");
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


	printf("�����˺ţ�\n");
	gets(Current.Racc);
	printf("�������룺\n");
	gets(Current.Rpas);
	if (strcmp(Initial.Racc, Current.Racc) == 0 && strcmp(Initial.Rpas, Current.Rpas) == 0)
	{
		printf("������ȷ��\n");
		return 1;
	}
	else
	{
		printf("�������\n");
		return 0;
	}

}

void didplayMune()
{

	printf("===========================================\n");
	printf("===========================================\n");
	printf("==           1.¼��ѧ����Ϣ              ==\n");
	printf("==           2.����ѧ����Ϣ              ==\n");
	printf("==           3.ɾ��ѧ����Ϣ              ==\n");
	printf("==           4.����ѧ����Ϣ              ==\n");
	printf("==           5.�޸�ѧ����Ϣ              ==\n");
	printf("==           6.����ǰ��Ϣ�������ļ�       ==\n");
	printf("==           7.�������ѧ����Ϣ           ==\n");
	printf("==           8.��ȡ�ļ��е�ѧ����Ϣ       ==\n");
	printf("==           0.�˳�                      ==\n");
	printf("\n\n");
	printf("�״ν����������¼����Ϣ�����             ==\n\n");
	printf("===========================================\n");



}

void Inputstu()
{
	int add = 0;	//�������ӵ�����
	int i = 0;		//ѭ������
	printf("������Ҫ¼�����������Ϣ��������\n");
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
		printf("�� %d ����\n", i+1);
		printf("������\n");
		scanf("%s", &stu[i].name);
		printf("ѧ�ţ�\n");
		scanf("%d", &stu[i].stunum);
		printf("�༶:\n");
		scanf("%s", &stu[i].Class);
		printf("�Ա�:\n");
		scanf("%s", &stu[i].sex);
		printf("רҵ:\n");
		scanf("%s", &stu[i].major);
		printf("�ۺϳɼ�\n");
		scanf("%d", &stu[i].result);
	}
	if (i == num)
		printf("������ɣ�");
	system("pause");
}

void Lookstu()
{
	if (num == 0)
	{
		printf("��ǰû��ѧ����Ϣ��\n");
		system("pause");
		return 0;
	}
	int i = 0;
	int nstu = 0;
	printf("���뽫Ҫ���ҵ�ѧ�ţ�\n");
	scanf("%d", &nstu);
	for (i = 0; i < num; i++)
	{
		if (nstu == stu[i].stunum)
		{
			printf("ѧ����Ϣ��\n");
			printf("%s\n", stu[i].name);
			printf("%d\n", stu[i].stunum);
			printf("%s\n", stu[i].Class);
			printf("%s\n", stu[i].sex);
			printf("%s\n", stu[i].major);
			printf("%d\n\n", stu[i].result);
		}
		else
		{
			printf("û�и�ѧ����");
		}
	}
}

void  Delstu()
{
	if (num < 1)
	{
		printf("û��ѧ����Ϣ��");
		system("pause");
		return 0;
	}
	int sz;
	sz = num;
	char name[20] = { 0 };
	int i = 0;
	int s = 0;
	printf("���뽫Ҫɾ�������֣�\n");
	scanf("%s", &name);
	for (i = 0; i < sz; i++)
	{
		if (strcmp(name, stu[i].name) == 0)
		{
			printf("ѧ����Ϣ��\n");
			printf("%s", name);
			printf("%d\n", stu[i].stunum);
			printf("%s\n", stu[i].Class);
			printf("%s\n", stu[i].sex);
			printf("%s\n", stu[i].major);
			printf("%d\n\n", stu[i].result);
			printf("ȷ��ɾ����(1/0)\n");
			scanf("%d", &s);
			if (s == 1)
			{
			//����ķ�������Ϊÿ��ѧ����������ѧ�ŵ���Ϣ��ÿ��ѧ�����Ƕ����ģ�
			//�ǽ����һ��ѧ������Ϣ�Ƶ���ǰɾ����λ�ã������һλ����Ϣ����Ϊ0��
			//�ٽ�����ѧ���ĸ�����ȥ1
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
				printf("�˳���\n");
				break;
			}
		}
		else
		{
			printf("û�и�ѧ����");
			break;
		}
	}
}

void modifystu()
{
	if (num < 1)
	{
		printf("û��ѧ����Ϣ�����޸ġ�");
		return 0;
	}
	int i = 0;
	int s = 0;

	//�����޸���Ϣ�ı���
	char name[20];
	char Nname[20];
	int Nstunum;
	char NClass[20];
	char Nsex[10];
	char Nmajor[20];
	char Nresult;
	
	//�������޸�
	printf("���뽫Ҫ�޸ĵ�ѧ����������\n");
	scanf("%d", &name);
	for (i = 0; i < num; i++)
	{
		if (strcmp(name, stu[i].name) == 0)
		{
			//�������Ϣ
			printf("ѧ����Ϣ��\n");
			printf("%s", stu[i].name);
			printf("%d\n", stu[i].stunum);
			printf("%s\n", stu[i].Class);
			printf("%s\n", stu[i].sex);
			printf("%s\n", stu[i].major);
			printf("%d\n\n", stu[i].result);

			system("pause");//��ͣ�����

			printf("   1.�����޸�     2.ѧ���޸�   3.�༶�޸�\n");
			printf("   4.�Ա��޸�     5.רҵ�޸�   6.�ɼ��޸�\n");
			printf("�������ѡ��, 0���˳�\n");
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
				printf("�˳�ɾ��\n");
				break;
			}
		}
		else
		{
			printf("û�и�ѧ����");
		}
	}
}
void save()
{
	if (num == 0)
	{
		printf("��ǰû��ѧ����Ϣ��");
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
			printf("����ʧ��!!\n");
		printf("����ɹ���\n");
		fclose(fp);
		system("pause");

}

void Print()
{
	if (num == 0)
	{
		printf("��ǰû��ѧ����Ϣ\n");
		system("pause");
		return 0;
	}
	int i = 0;
	for (i = 0; i < num; i++);
	{
		printf("�� %d ��ѧ����Ϣ��\n",i+1);
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
	int m = 0;	//��ȡ�������
	FILE* fp;
	fp = fopen("stu.txt", "rb");
	if (fp == NULL)
	{
		printf("file_error\n");
		system("pause");
		return 0;
	}
	for (i = 0; i < N; i++)	//NΪ���ѧ������Ԥ����
	{
		if (fread(&stu[i], sizeof(Stu), 1,fp) == 1)
			m++;
	}
	if (m == 0)
		printf("��ȡʧ�ܣ�\n");
	else
	{
		printf("��ȡ�ɹ���\n");
		num = m;	//����ȡ�����������num
	}
	fclose(fp);
	system("pause");
}



