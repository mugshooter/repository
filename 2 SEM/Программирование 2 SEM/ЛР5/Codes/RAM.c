#include <stdlib.h>

int **allocate_matrix(int n, int m) {
    int **matrix = (int **) malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) {
        matrix[i] = (int *) malloc(m * sizeof(int));
    }
    return matrix;
}

void deallocate_matrix(int **matrix, int n) {
    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);
}