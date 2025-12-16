#include <stdio.h>
#include <math.h>

typedef struct {
    double real;
    double imag;
} complex;

complex add(complex a, complex b) {
    complex result;
    result.real = a.real + b.real;
    result.imag = a.imag + b.imag;
    return result;
}

complex multiply(complex a, complex b) {
    complex result;
    result.real = a.real * b.real - a.imag * b.imag;
    result.imag = a.real * b.imag + a.imag * b.real;
    return result;
}

complex exp_c(complex z, int n) {
    complex result = {1, 0};
    complex term = {1, 0};
    int i;
    for (i = 1; i <= n; i++) {
        term = multiply(term, z);
        term.real /= i;
        term.imag /= i;
        result = add(result, term);
    }
    return result;
}

int main() {
    complex z = {1, 2}; 
    int n = 10; 
    complex exp_z = exp_c(z, n); 
    printf("exp(z) = %f + %fi\n", exp_z.real, exp_z.imag);
    return 0;
}