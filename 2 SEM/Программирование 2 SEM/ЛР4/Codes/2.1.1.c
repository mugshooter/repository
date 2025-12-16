#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>

#define MY_SIZE 20

int main() 
{
    char* my_string = (char*)malloc(MY_SIZE * sizeof(char));
    fgets(my_string, MY_SIZE, stdin);

    int count = 0;
    for(int i = 0; my_string[i] != '\0'; i++)
    {
        count++;
    }

    printf("%d\n", count -1);

    free(my_string);

    return 0;
}