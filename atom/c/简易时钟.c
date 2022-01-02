#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void Update();
void Display();
void Delay();

typedef struct clock {
    int hour;
    int minute;
    int second;
}Clock;
Clock clock;
int main()
{
    long i;
    for (i = 0; i < 100000; i++)
    {
        Update();
        Display();
        Delay();
    }


}
void Update()
{
    clock.second++;
    clock.hour = 21;
    clock.minute = 23;

    if (clock.second == 60)
    {
        clock.minute++;
        clock.second = 0;
    }
    if (clock.minute == 60)
    {
        clock.hour++;
        clock.minute = 0;
    }
    if (clock.hour == 24)
        clock.hour = 0;
   
}
void Display()
{
    printf("%02d:%02d:%02d", clock.hour, clock.minute, clock.second);
    Sleep(1000);
}
void Delay()
{
    Sleep(1000);
    system("cls");
}