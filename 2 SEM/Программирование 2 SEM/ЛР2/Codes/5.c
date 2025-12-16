#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    int *arr, *ptr;

    printf("Enter size: ");
    scanf("%d", &n);

    arr = (int*)malloc(n * sizeof(int)); 

    printf("Enter elements:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", arr + i); 
    }

    printf("The reverse:\n");
    for (ptr = arr + n - 1; ptr >= arr; ptr--) {
        printf("%d ", *ptr); 
    }

    free(arr); 

    return 0;
}