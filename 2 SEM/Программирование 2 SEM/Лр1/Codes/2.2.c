#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float F(int x)
{
    return ((sin(x - 0.2)) / (0.7 + cos(x * x)));
}

int main(void)
{
    float a = -0.7, b = 0.7, s = 0, n, h, x;
    printf("Input n: ");
    scanf("%f", &n);
    h = (b - a) / n;
    x = a + h;

    while (x < (b - h))
    {
        s = s + ((f(x) + f(x + h)) / 2);
        x = x + h;
    }
    s = h * (((f(a) + f(b)) / 2) + s);
    printf("integ = %.3f", h, s);
    return 0;
}