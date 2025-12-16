#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int F(int n)
{
    if (n < 3)
    {
        return 1;
    }
    else
    {
        return F(n - 2) + F(n - 3);
    }
}

int main(void)
{
    int m;
    printf("%s", "Input m:");
    scanf("%d", &m);
    for (int i = 0; F(i) < m; i++)
    {
        printf("%d ", F(i));
    }
    return 0;
}