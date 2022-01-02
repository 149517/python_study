#define _CRT_SECURE_NO_WARNINGS 1 
#include <stdio.h>

//快速排序，冒泡排序，简单桶排序

//快速排序
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
	printf("输入  00  时停止：\n");
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
	//冒泡排序
	/*int a[100] = {0};		//数组声明的时候必须给定大小，否则肯定会出错，你这里没出错，
							//是因为int a[] = { 0 };这么写的时候，相当于数组a中就1个元素，
							//相当于int a[1]; a[0] = 0;所以编译器不会报错，
							//但是下面for循环录入数据的时候，数组就越界了
	int b=0;
	printf("输入数字：\n");
	printf("输入  00  停止\n");
	for (int i = 0;; i++)
	{
		scanf("%d", &a[i]);
		if (a[i] == 00)
		{
			b = i;
			break;
		}
	}
	printf("  %d  个数的排序结果：\n",b);
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

	//简单桶排序
	/*
	int ab[100];
	printf("输入的数字：\n");
	printf("输入  00 时停止：\n");
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
			printf("%d   ", i);	//输出的是桶的数字，而不是数组
		}
	}
	*/