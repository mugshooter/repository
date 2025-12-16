# include <stdio.h>
# include <stdlib.h>

union IF
{
int i;
float f;
};

int main(void)
{
union IF u;
u.i = 15;
printf("integer i:%d\n", u.i);

union IF *p = &u;
p->f = 3.14;
printf("float f:%f\n", p->f);

return 0;
}