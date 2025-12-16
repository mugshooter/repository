#include <stdio.h>
#include <stdlib.h>

enum DataType {
    INT,
    FLOAT,
    CHAR
};

union Data {
    int i;
    float f;
    char c;
};

struct Log {
    enum DataType type;
    union Data data;
};
