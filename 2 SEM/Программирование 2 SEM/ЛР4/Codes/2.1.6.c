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
    char* str2 = "World!";
    char* result = (char*)malloc((strlen(str1) + strlen(str2) + 1) * sizeof(char));
    strcpy(result, str1);
    strcat(result, str2);
    printf("%s\n", result);

    if (strcmp(my_string, result) == 0) {
        printf("The strings are odinakovo.\n");
    } else {
        printf("The strings are ne odinakovo.\n");
    }

    free(my_string);
    free(result);

    return 0;
}