program pr2;
function f(x:real):real;
begin 
  f:=2*exp(x)-5*(x*x*x)-2;
end;

function f1(x:real):real;
begin 
  f1:=2*exp(x)-15*(x*x);
end;

var
  t,a,b,x,x1:real;
begin
  t:=Power(10,-6);
  a:=-10;
  b:=10;
  x1:=a;
  repeat
    x:=x1;
    x1:= x- f(x)/f1(x);
  until abs(x1-x)<=t ;
  writeln('Ответ, корень нижней границы ',x);
  x1:=b;
  repeat
    x:=x1;
    x1:=x-f(x)/f1(x);
  until abs(x1-x)<=t;
  writeln('Ответ, корень верхней границы ',x)
end.