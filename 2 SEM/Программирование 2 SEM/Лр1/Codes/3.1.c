#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    int Y[10];
    for (int i = 1; i < 11; i++)
    {
        printf("%s%d%s", "Y", i, "\n");
        scanf("%d", &Y[i]);
    }

    for (int i = 0; i < 10; i++)
    {
        Y[i] = pow(Y[i], 2);
        printf("%d ", Y[i]);
    }
    return 0;
}