#include <stdio.h>
#include <stdlib.h>

int main() {
    int a = 1234567890;
    char *ptr = (char*)&a;

    printf("Bytes:\n");
    for (int i = 0; i < sizeof(int); i++) {
        printf("%d ", *(ptr + i));
    }

    return 0;
}