#define _CRT_SECURE_NO_WARNINGS 1 
#include <stdio.h>

//��������ð�����򣬼�Ͱ����

//��������
int a[101];
int n = 0;
int quicksort(int left, int right)
{
	int n, m, temp;
	n = left;
	m = right;
	temp = a[left];
	if (n > m)
		return 0;
	while (n != m)
	{

		while (a[m] >= temp && n < m)
			m--;
		while (a[n] <= temp && n < m)
			n++;
		if (n < m)
		{
			int te = a[n];
			a[n] = a[m];
			a[m] = te;
		}

	}
	a[left] = a[n];
	a[n] = temp;

	quicksort(left, n - 1);
	quicksort(n + 1, right);
}
int main()
{
	printf("����  00  ʱֹͣ��\n");
	for (int i = 0;; i++)
	{
		scanf("%d", &a[i]);
		if (a[i] == 00)
		{
			n = i;
			break;
		}
	}
	quicksort(0, n);
	for (int i = 1; i < n+1; i++)
	{
		if (a[i] != a[i - 1])
			printf("%d  ", a[i]);
	}
	return 0;
}



//int abc[20];
//int d = 0;
//int quicksort(int start , int end);
//int main() {
	//ð������
	/*int a[100] = {0};		//����������ʱ����������С������϶������������û����
							//����Ϊint a[] = { 0 };��ôд��ʱ���൱������a�о�1��Ԫ�أ�
							//�൱��int a[1]; a[0] = 0;���Ա��������ᱨ��
							//��������forѭ��¼�����ݵ�ʱ�������Խ����
	int b=0;
	printf("�������֣�\n");
	printf("����  00  ֹͣ\n");
	for (int i = 0;; i++)
	{
		scanf("%d", &a[i]);
		if (a[i] == 00)
		{
			b = i;
			break;
		}
	}
	printf("  %d  ��������������\n",b);
	for (int i = 0; i < b+1; i++)
	{
		for (int j = i; j < b+1; j++)
		{
			if (a[i] < a[j])
			{
				int te = a[i];
				a[i] = a[j];
				a[j] = te;

			}
		}
	}
	for (int i = 0; i < b; i++)
	{
		printf("%d  ", a[i]);
	}
	*/

	//��Ͱ����
	/*
	int ab[100];
	printf("��������֣�\n");
	printf("����  00 ʱֹͣ��\n");
	int c = 0;
	for (int i = 0; i < 100; i++)
	{
		ab[i] = 0;
	}
	for (int i = 0; i < 100; i++)
	{
		scanf("%d", &c);
		if (c == 00)
		{
			break;
		}
		ab[c]++;
	}
	for (int i = 0; i < 100; i++)
	{
		if (ab[i] != 0)
		{
			printf("%d   ", i);	//�������Ͱ�����֣�����������
		}
	}
	*/