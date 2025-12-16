#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    unsigned int id;
    char name[50];
    char faculty[50];
    float rating;
};

int main() {
    int num_students;
    printf("Enter number of students: ");
    scanf("%d", &num_students);

    struct Student students[num_students];
    for (int i = 0; i < num_students; i++) {
        printf("Enter data of students %d:\n", i+1);
        printf("ID: ");
        scanf("%u", &students[i].id);
        printf("Name: ");
        getchar(); 
        fgets(students[i].name, 50, stdin);
        printf("Faculty: ");
        fgets(students[i].faculty, 50, stdin);
        printf("Rating: ");
        scanf("%f", &students[i].rating);
    }

    FILE *f = fopen("students.bin", "wb");
    if (f == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    fwrite(students, sizeof(struct Student), num_students, f);
    fclose(f);

    struct Student new_students[num_students];
    f = fopen("students.bin", "rb");
    if (f == NULL) {
        printf("Error opening file\n");
        return 1;
    }
    fread(new_students, sizeof(struct Student), num_students, f);
    fclose(f);

    for (int i = 0; i < num_students; i++) {
        printf("\nID: %u\nName: %sFaculty: %sRating: %.1f\n", new_students[i].id, new_students[i].name, new_students[i].faculty, new_students[i].rating);
    }

    return 0;
}