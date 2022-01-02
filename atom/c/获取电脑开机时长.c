//获取电脑开机长
#include <stdio.h>
#include <windows.h>

int main()
{
	DWORD k = GetTickCount64();
	int s = k / 1000;
	
	int h = s / 3600;
	int m = (s-h*3600)/60;

	s = s%60;

	printf("电脑已经开机 %d h %d m %d s\n", h, m, s);

	return 0;
}