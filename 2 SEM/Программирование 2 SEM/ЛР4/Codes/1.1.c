#include <stdio.h>
#include <stdlib.h>

int func1 (int x)
{
int a=1;
for (int i=1;i<=x;i++)
{
a=a*i;
}
return a;
}

int func2 (int x)
{
if (x==1)
{
return 1;
}
else
{
return x*func2(x-1);
}
}

int main(void)
{
printf("V1=%d\n",func1(16));
printf("V2=%d\n",func2(16));
}