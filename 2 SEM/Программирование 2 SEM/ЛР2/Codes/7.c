#include <stdio.h>
#include <stdlib.h>

int main() {
    int n_rows, n_cols, i, j;
    int **arr;
    printf("Number of rows: ");
    scanf("%d", &n_rows);
    printf("Number of columns: ");
    scanf("%d", &n_cols);

    arr = (int**)malloc(n_rows * sizeof(int*));

    for (i = 0; i < n_rows; i++) {
        arr[i] = (int*)malloc(n_cols * sizeof(int));
    }

    for (i = 0; i < n_rows; i++) {
        for (j = 0; j < n_cols; j++) {
            arr[i][j] = i * j;
        }
    }

    printf("Array:\n");
    for (i = 0; i < n_rows; i++) {
        for (j = 0; j < n_cols; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    for (i = 0; i < n_rows; i++) {
        free(arr[i]);
    }

    free(arr);

    return 0;
}