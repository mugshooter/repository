# include <stdio.h>
# include <stdlib.h>
# include <math.h>

struct vector{
int x;
int y;
int z;
};

int main(void){
struct vector A= {1,2,3};
struct vector B= {0,5,10};

int SY = (A.x*B.x)+(A.y*B.y)+(A.z*B.z);
printf("%d\n", SY);

int i = (A.y*B.z)-(A.z*B.y);
int j = (A.x*B.z)-(A.z*B.x);
int k = (A.x*B.y)-(A.y*B.x);
printf("%d\t%d\t%d\n",i,j,k);

double d = sqrt(A.x*A.x+A.y*A.y+A.z*A.z);
printf("%f\n", d);

double c = sqrt(B.x*B.x+B.y*B.y+B.z*B.z);
printf("%f\n", c);

printf("{%d,%d,%d}\n",A.x,A.y,A.z);
printf("{%d,%d,%d}\n",B.x,B.y,B.z);

return 0;
}