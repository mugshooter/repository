#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main() {
    char *string = "3Ga- 53F,p";
    int length = strlen(string);

    for (int i = 0; i < length; i++) {
        printf(" Symbol: %c\n", string[i]);
        if (isalpha(string[i])) {
            if (isupper(string[i])) {
                printf("Big letter.");
            } else if (islower(string[i])) {
                printf("Low letter.");
            }
        } else if (isdigit(string[i])) {
            printf("Cifra.");
        } else if (isspace(string[i])) {
            printf("Space.");
        } else if (ispunct(string[i])) {
            printf("Mark.");
        } else {
            printf("This character is not printable.\n");
        }
    }

    return 0;
}