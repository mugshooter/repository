#include <stdio.h>
#include <stdlib.h>

enum DOW
{
Mo=1,
Tu=2,
We=3,
Th=4,
Fr=5,
Sa=6,
Su=7
};

int main(void)
{
printf("Monday %d\n", Mo);
printf("Tuesday %d\n", Tu);
printf("Wensday %d\n", We);
printf("Thursday %d\n", Th);
printf("Friday %d\n", Fr);
printf("Saturday %d\n", Sa);
printf("Sunday %d\n", Su);

return 0;
}