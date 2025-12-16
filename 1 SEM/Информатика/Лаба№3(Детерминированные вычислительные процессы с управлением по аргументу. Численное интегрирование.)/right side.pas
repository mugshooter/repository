program rp;
var
  a,b,h,n,x,s,i:real;
  function f(x:real):real;
  begin
    f:=(sin((1.5*x)+0.3))/(2.3+cos(0.4*(x*x)+1));  
  end;
  begin
    a:=0.4;
    b:=1.2;
    n:=10;
    s:=0;
    h:=(b-a)/n;
    x:=a;
    while x<b-h do begin
      s:=s+f(x);
      x:=x+h;
    end;
    i:=h*s;
    writeln('ответ: ',i,' шаг=',' ', h)
  end.