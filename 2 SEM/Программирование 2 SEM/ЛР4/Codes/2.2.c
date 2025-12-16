#include <stdio.h>
#include <stdlib.h>

int main() {
    char str_double[] = "3.14159";
    char str_int[] = "42";
    double num_double = atof(str_double);
    int num_int = atoi(str_int);
    printf("num_double = %f\n", num_double);
    printf("num_int = %d\n", num_int);
    return 0;
}