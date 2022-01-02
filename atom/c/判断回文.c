#define _CRT_SECURE_NO_WARNINGS 1 
#include <stdio.h>
int noae(int* ar, int sz);

int main()
{
	//把第一个数子删除，紧接着将第二个数放到这串数字的末尾，
	//再将底三个数字删除，第4 个数字放到这串数字的末...
	//最后取得是删除的顺序
	int ar[20] = { 6,3,1,7,5,8,9,2,4 };
	int sz = sizeof(ar) / sizeof(ar[0]);
	int head, tail;
	head = 0;
	tail = noae(ar, sz);	//元素计算
	int a[20] = { 0 };
	//核心
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

	//判断回文
	char bo[] = "aha";
	int len = strlen(bo);
	printf("\n%d\n", len);
	int min = len / 2 ;
	int top = len-1;
	for (int i = 0; i < min && top >= min; i++)
	{
		if (bo[i] != bo[top])
		{
			printf("%s 不是回文数。\n", bo);
			break;
		}
		top--;
	}
	if (top == min)
	{
		printf("%s 是回文数\n", bo);
	}


	return 0;
}
int noae(int* ar, int sz)	
//计算数组内元素，最多计算数组内含有 2个0，末尾为0时候不能得出正确结果
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
