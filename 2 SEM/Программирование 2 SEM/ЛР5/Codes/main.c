#include <stdio.h>
#include "RAM.h"
#include "matrix.h"

int main() {
    int **a, **b, **c;
    int n = 3, m = 3, p = 3;

    a = allocate_matrix(n, m);
    b = allocate_matrix(m, p);
    c = allocate_matrix(n, p);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            a[i][j] = i + j;
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            b[i][j] = i * j;
        }
    }

    multiply_matrices(a, b, c, n, m, p);

    printf("Result:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < p; j++) {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }

    deallocate_matrix(a, n);
    deallocate_matrix(b, m);
    deallocate_matrix(c, n);

    return 0;
}