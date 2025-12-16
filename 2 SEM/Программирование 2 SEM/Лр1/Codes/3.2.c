#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    int M[10], n;
    printf("%s", "Inpunt n ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        printf("%s%d%s", "input M", i + 1, "\n");
        scanf("%d", &M[i]);
    }

    int A;
    for (int i = 0; i < (n / 2); i++)
    {
        A = M[i];
        M[i] = M[n - i - 1];
        M[n - i - 1] = A;
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d", M[i]);
    }
    return 0;
}