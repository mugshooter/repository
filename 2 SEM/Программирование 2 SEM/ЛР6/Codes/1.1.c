#include <stdio.h>
#include <stdlib.h>

struct Student
{
    unsigned int id;
    char name [50];
    char faculty [50];
    float rating;
};

int main(void)
{
struct Student students[3];
 for (int i = 0; i < 3; i++) 
    {
        printf("Enter data %d:\n", i+1);
        printf("ID: ");
        scanf("%u", &students[i].id);
        printf("Name: ");
        fflush(stdin);
        fgets(students[i].name, 50, stdin);
        students[i].name[strcspn(students[i].name, "\n")] = '\0';
        printf("Faculty: ");
        fflush(stdin);
        fgets(students[i].faculty, 50, stdin);
        students[i].faculty[strcspn(students[i].faculty, "\n")] = '\0';
        printf("Rating: ");
        scanf("%f", &students[i].rating);
    }

FILE* file = fopen("students.csv","a");
for(int i = 0; i < 3; i++)
{
    fprintf(file,"%u,%s,%s,%.1f\n", students[i].id, students[i].name, students[i].faculty, students[i].rating);
}
fclose(file);

file = fopen("students.csv","r");

struct Student readStudents[3];

char line[100];
int i = 0;
while (fgets(line,100,file))
{
    sscanf(line, "%u,%[^,],%[^,],%f", &readStudents[i].id, readStudents[i].name, readStudents[i].faculty, &readStudents[i].rating);
    i++;
}
close(file);

   for (int i = 0; i < 3; i++) {
        printf("Student %d:\n", i+1);
        printf("ID: %u\n", readStudents[i].id);
        printf("Name: %s\n", readStudents[i].name);
        printf("Faculty: %s\n", readStudents[i].faculty);
        printf("Rating: %.1f\n", readStudents[i].rating);
        printf("\n");
    }

    return 0;
}
