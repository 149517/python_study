#define _CRT_SECURE_NO_WARNINGS 1 
#include <stdio.h>
int noae(int* ar, int sz);

int main()
{
	//�ѵ�һ������ɾ���������Ž��ڶ������ŵ��⴮���ֵ�ĩβ��
	//�ٽ�����������ɾ������4 �����ַŵ��⴮���ֵ�ĩ...
	//���ȡ����ɾ����˳��
	int ar[20] = { 6,3,1,7,5,8,9,2,4 };
	int sz = sizeof(ar) / sizeof(ar[0]);
	int head, tail;
	head = 0;
	tail = noae(ar, sz);	//Ԫ�ؼ���
	int a[20] = { 0 };
	//����
	for (int i=0;i<20 && head < tail;i++)
	{
		a[i] = ar[head];
		head++;
		ar[tail] = ar[head];
		head++;
		tail++;
	}
	int s = noae(a, 20);
	for (int i = 0; i < s; i++)
	{
		printf("%d  ", a[i]);
	}

	//�жϻ���
	char bo[] = "aha";
	int len = strlen(bo);
	printf("\n%d\n", len);
	int min = len / 2 ;
	int top = len-1;
	for (int i = 0; i < min && top >= min; i++)
	{
		if (bo[i] != bo[top])
		{
			printf("%s ���ǻ�������\n", bo);
			break;
		}
		top--;
	}
	if (top == min)
	{
		printf("%s �ǻ�����\n", bo);
	}


	return 0;
}
int noae(int* ar, int sz)	
//����������Ԫ�أ������������ں��� 2��0��ĩβΪ0ʱ���ܵó���ȷ���
{
	int count = 0;
	for (int i = 0; i + 2 < sz; i++)
	{
		if (ar[i] != 0)
		{
			count++;
		}
		if (ar[i] == 0)
		{
			if (ar[i + 1] != 0)
			{
				count++;
			}
			if (ar[i + 1] == 0)
			{
				if (ar[i + 2] != 0)
				{
					count++;
				}
			}
		}
	}
	//printf("%d", count);
	return count;
}
