program tr;
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
    while x<b-h do begin
      s:=s+f(x);
      x:=x+h;
    end;  
    i:=h*(((f(a)+f(b))/2)+s);
    writeln('ответ: ',i,' шаг=',' ', h);
  end.