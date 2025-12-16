#include <stdio.h>
#include <stdlib.h>

double **C_M(int rows, int cols) {
    double **M = (double **) malloc(rows * sizeof(double *));
    for (int i = 0; i < rows; i++) {
        M[i] = (double *) malloc(cols * sizeof(double));
    }
    return M;
}

void F_M(double **M, int rows) {
    for (int i = 0; i < rows; i++) {
        free(M[i]);
    }
    free(M);
}

void W_M(double **M, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%lf", &M[i][j]);
        }
    }
}

void P_M(double **M, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%lf ", M[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int rows, cols;
    printf("Enter number of rows: ");
    scanf("%d", &rows);
    printf("Enter number of columns: ");
    scanf("%d", &cols);

    double **M = C_M(rows, cols);
    W_M(M, rows, cols);
    printf("Matrix:\n");
    P_M(M, rows, cols);
    F_M(M, rows);

    return 0;
}