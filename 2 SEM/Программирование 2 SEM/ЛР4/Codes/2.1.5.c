#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

#define MY_SIZE 20

int main() 
{
    char* my_string = (char*)malloc(MY_SIZE * sizeof(char));
    fgets(my_string, MY_SIZE, stdin);

    char* str1 = "Hello, ";
    char* str2 = "world!";
    char* result = (char*)malloc((strlen(str1) + strlen(str2) + 1) * sizeof(char));
    strcpy(result, str1);
    strcat(result, str2);
    printf("%s\n", result);

    free(my_string);
    free(result);

    return 0;
}