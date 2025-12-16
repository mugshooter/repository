#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int n, m;
int main(void)
{
    do
    {
        printf("%s", "n= ");
        scanf("%d", &n);
        m = 0;
        while (n > 0)
        {
            m = m + (n % 10);
            n = n / 10;
        }
        if (m >= 10)
        {
            printf("%s ", "sum >10, repeat \n");
        }
    } while (m >= 10);

    printf("%d", m);

    return 0;
}
