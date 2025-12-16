#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

void swap(int* a, int size) {
    for (int i = 0; i < size - 1; i += 2) {
        int temp = a[i];
        a[i] = a[i + 1];
        a[i + 1] = temp;
    }
}

int main() {
    int* a = (int*)malloc(12 * sizeof(int));
    for (int i = 0; i < 12; i++) {
        a[i] = i + 1;
    }

    printf("Bef swap: ");
    for (int i = 0; i < 12; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    swap(a, 12);

    printf("Aft swap: ");
    for (int i = 0; i < 12; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    free(a);
    
    return 0;
}