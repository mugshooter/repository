#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    double *arr, *ptr;

    printf("Enter size : ");
    scanf("%d", &n);

    arr = (double*)malloc(n * sizeof(double)); 

    printf("Enter elements :\n");
    for (i = 0; i < n; i++) {
        scanf("%lf", arr + i); 
    }

    printf("elements of the array:\n");
    for (ptr = arr; ptr < arr + n; ptr++) {
        printf("%lf ", *ptr); 
    }

    free(arr); 

    return 0;
}