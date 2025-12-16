#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;
    int *ptr1, *ptr2;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    ptr1 = &a;
    ptr2 = &b;

    if (*ptr1 > *ptr2) {
        printf("%d > %d \n", *ptr1, *ptr2);
    } else if (*ptr2 > *ptr1) {
        printf("%d > %d \n", *ptr2, *ptr1);
    } else {
        printf("%d = %d \n", *ptr1, *ptr2);
    }

    return 0;
}