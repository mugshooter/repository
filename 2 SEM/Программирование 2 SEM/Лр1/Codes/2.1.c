#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    long int r1 = 228000000, r2 = 149600000, x[300], y[300];
    int T1 = 365, T2 = 687;
    float w1 = 2 * M_PI / T1, w2 = 2 * M_PI / T2;
    for (int t = 0; t < 300; t++)
    {
        x[t] = r1 * cos(w1 * t) - r2 * cos(w2 * t);
        y[t] = r1 * sin(w1 * t) - r2 * sin(w2 * t);
        printf("%li %li, X Y", x[t], y[t]);
        printf("\n");
    }
    return 0;
}