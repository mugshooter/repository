#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    float a, b, c, x, h;
    printf("Input: a,b,c,x \n");
    scanf("%f%f%f%f", &a, &b, &c, &x);
    h = (-1 * ((x - a) / (cbrt(x * x + a * a)) - ((4 * pow(pow(x * x + b * b, 3), 0.25)) / 2 + a + b + cbrt(pow(x - c, 2)))));
    printf("%f", h);
    return 0;
}