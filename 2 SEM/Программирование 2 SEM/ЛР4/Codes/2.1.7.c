#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

#define MY_SIZE 20

int main() 
{
    char* my_string = (char*)malloc(MY_SIZE * sizeof(char));
    fgets(my_string, MY_SIZE, stdin);

    char* lowercase_string = (char*)malloc(strlen(my_string) * sizeof(char));
    strcpy(lowercase_string, my_string);
    for (int i = 0; i < strlen(lowercase_string); i++) {
        if (lowercase_string[i] >= 'A' && lowercase_string[i] <= 'Z') {
            lowercase_string[i] += 32;
        }
    }
    printf("%s\n", lowercase_string);

    char* uppercase_string = (char*)malloc(strlen(my_string) * sizeof(char));
    strcpy(uppercase_string, my_string);
    for (int i = 0; i < strlen(uppercase_string); i++) {
        if (uppercase_string[i] >= 'a' && uppercase_string[i] <= 'z') {
            uppercase_string[i] -= 32;
        }
    }
    printf("%s\n", uppercase_string);

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
    free(lowercase_string);
    free(uppercase_string);
    free(result);

    return 0;
}