#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

#define MY_SIZE 20

int main() {
    char my_string[MY_SIZE];
    printf(":Write ");
    fgets(my_string, MY_SIZE, stdin);
    printf("%s\n", my_string);

    free(my_string);

    return 0;
}