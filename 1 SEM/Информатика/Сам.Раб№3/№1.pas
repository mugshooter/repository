function y(x:real):real;
begin
y:=cos(x);
end;
const a=-0.75;
      b=0.75;
      n=10;
var h,s:real;
    i:integer;
begin
h:=(b-a)/n;
s:=(y(a)+y(b))/2;
for i:=1 to n-1 do 
s:=s+y(a+i*h);
s:=s*h;
writeln('значение интеграла S=',s);
end.