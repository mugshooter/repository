#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int A[3][3] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
int sum = 0;

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        int sum = 0;
        for (int j = 0; j < 3; j++)
        {
            sum += A[i][j];
        }
        A[i][0] = sum / 3;
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    return 0;
}