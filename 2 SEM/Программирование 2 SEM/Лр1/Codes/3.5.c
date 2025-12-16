#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int M[5] = {1, 2, 4,5,3};
int n;

int main(void)
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = i; (j > 0) && M[j] < (M[j - 1]); j--)
        {
            n = M[j - 1];
            M[j - 1] = M[j];
            M[j] = n;
        }
    }
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", M[i]);
    }
    return 0;
}