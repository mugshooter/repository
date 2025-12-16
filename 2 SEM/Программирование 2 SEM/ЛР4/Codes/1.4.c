#include <stdio.h>

void Vec_Proiz(double *a, double *b, double *result) {
    result[0] = a[1] * b[2] - a[2] * b[1];
    result[1] = a[2] * b[0] - a[0] * b[2];
    result[2] = a[0] * b[1] - a[1] * b[0];
}

int main() {
    double a[3], b[3], result[3];

    printf("Vector A (x, y, z): ");
    scanf("%lf %lf %lf", &a[0], &a[1], &a[2]);

    printf("Vector B (x, y, z): ");
    scanf("%lf %lf %lf", &b[0], &b[1], &b[2]);

    Vec_Proiz(a, b, result);

    printf("A*B: (%lf, %lf, %lf)\n", result[0], result[1], result[2]);

    return 0;
}