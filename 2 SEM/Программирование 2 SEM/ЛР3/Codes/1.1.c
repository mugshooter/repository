#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void function(int a) {
    printf("%d\n", a*a*a);
}

struct MGD {
    int (*aa)(int); 
};

int main(void) {
    struct MGD avc = {&function};
    avc.aa(15);

    return 0;
}