#include <stdio.h>
# include <stdlib.h>

struct DMY{
int day;
int month;
int year;
};

int main(void){
struct DMY BD = {25,12,1993};
printf("Day, Month, Year: %d\t%d\t%d\n", BD.day, BD.month, BD.year);
return 0;
}