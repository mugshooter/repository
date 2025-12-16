#include <stdio.h>
#include <stdlib.h>

int main(void) {
    double *ptr = (double*)malloc(sizeof(double)); 
    *ptr = 2; 
    double **pointer = &ptr; 
    printf("%lf\n", **pointer); 
    free(ptr); 
    return 0;
}