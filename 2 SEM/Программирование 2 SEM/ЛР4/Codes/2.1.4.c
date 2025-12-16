#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

#define MY_SIZE 20

int main() 
{
    char* my_string = (char*)malloc(MY_SIZE * sizeof(char));
    fgets(my_string, MY_SIZE, stdin);

    char* my_string_copy = (char*)malloc(MY_SIZE * sizeof(char));
    strcpy(my_string_copy, my_string);

    printf("Original string: %s\n", my_string);
    printf("Copied string: %s\n", my_string_copy);

    free(my_string);
    free(my_string_copy);

    return 0;
}