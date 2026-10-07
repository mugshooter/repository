   // Демонстрация:
   //  (1) алгоритма Евклида для вычисления НОД двух на-
   //      туральных чисел;
   //  (2) расширенного (обобщённого) алгоритма Евклида
   //      для вычисления НОД двух натуральных чисел;
   //  (3) вычисления мультипликативно обратного  нату-
   //      ральному числу a по заданному модулю m
   // *******************************************
   #include<iostream>
   #include<stdlib.h>
   #include<cmath>
   #include<time.h>
   #include<conio.h>
      using namespace std;
      int gcd (int, int);
      int ext_gcd (int, int, int&, int&);

   // =======
   int main()
   {
      int a, b, x, y;
      int m;
      // printf("Введите a и b      : "); 
      // scanf("%d",&a); scanf("%d",&b);
      srand(time(NULL));
      a=rand(), b=rand(); printf("a= %d, b= %d\n\n",a,b);
      ext_gcd(a,b,x,y);
      printf("Результаты         : "); printf("x=%d, y=%d\n",x, y);
      printf("Проверка вычислений: a*x+b*y=%d, gcd(a,b)= %d\n\n",
             a*x + b*y, gcd(a,b));
      // ------------------------------------------------
      printf("Вычисление мультипликативно обратного:\n");
      printf("Введите a и модуль (a*x=1 (mod m)): ");
      a=rand(), m=rand()%100;
      while (!(gcd(a,m)==1) && !(m==1))
      {
        a=rand(), m=rand()%100; 
      }
      printf("a= %d, m= %d\n\n",a,m);
      ext_gcd(a,m,x,y);
      printf("Мультипликативно обратное: "); 
      printf("a= %d => a^(-1)=%d\n",a, m + x % m);
      printf("Проверка вычислений      : a*a^(-1) (mod m)= %d\n\n ",
             (a * (m+ x % m)) % m);
      getch();
      return 0;
   }

   // ===================
   int gcd (int a, int b) 
   {
      int t;
      while (b) 
      {
        t=a%b; a=b; b=t;        
      }
      return abs(a);
   }
   // =======================================
   int ext_gcd (int a, int b, int& x, int& y)
   {
      int q, r, x1, x2, y1, y2, d;
      if (b==0) 
      {
        d=a, x=1, y=0;
        return d;
      }
      x2=1, x1=0, y2=0, y1=1;
      while (b>0) 
      {
        q=a/b, r=a-q*b; x=x2-q*x1, y=y2-q*y1; 
        a=b, b=r; x2=x1, x1=x, y2=y1, y1=y;
      }
      d=a, x=x2, y=y2;
      return abs(d);
   }
