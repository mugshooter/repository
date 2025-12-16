#include <stdio.h>
#include <stdlib.h>

union ByteConverter {
    unsigned long num;
    unsigned char bytes[sizeof(unsigned long)];
};

int main() {
    union ByteConverter converter;
    converter.num = 0x123456789;

    printf("Number: %lu\n", converter.num);
    printf("Bytes: ");
    for (int i = 0; i < sizeof(unsigned long); i++) {
        printf("%02X ", converter.bytes[i]);
    }
    printf("\n");

    return 0;
}