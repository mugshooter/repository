program lp;
var
  a,b,h,n,x,s,i:real;
  function f(x:real):real;
  begin
    f:=(sin((1.5*x)+0.3))/(2.3+cos(0.4*(x*x)+1));  
  end;
  begin
    a:=0.4;
    b:=1.2;
    n:=10000;
    s:=0;
    h:=(b-a)/n;
    x:=a+h;
    while x<(b-h) do begin
      s:=s+(4*f(x));
      s:=s+(2*f(x+h));
      x:=x+(2*h);
    end;
    i:=(h/3)*(s+f(a)+f(b));
    writeln('ответ: ',i,' шаг=',' ', h)
  end.  