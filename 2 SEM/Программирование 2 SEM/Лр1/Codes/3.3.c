#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int A[3][3] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
int At[3][3];
int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            At[j][i] = A[i][j];
        }
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", At[i][j]);
        }
        printf("\n");
    }
    return 0;
}
