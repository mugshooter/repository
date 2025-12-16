#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    int x, y;
    float u;

    scanf("%d %d", &x, &y);

    u = (1 + pow(sin(x + y), 2)) / 2 + abs(x - (2 * x * x) / (1 + abs(sin(x + y))));

    printf("%f", u);
    return 0;
}