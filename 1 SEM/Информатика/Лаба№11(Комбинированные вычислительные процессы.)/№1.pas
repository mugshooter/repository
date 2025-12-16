program pr1;
const
a=4;
k=7;
n=6;
var
  X:array[1..n] of integer;
  y:real;
  d1,d2,d3,i:integer;
function f(x:real):real;
var 
  z:integer;
  s:real;
  begin
    while z<=10 do
      begin
        s:=s+(exp(ln(z)*x))/3628800;
        z:=z+2;
      end;
    f:=s;
  end;
begin
  d1:=3;
  d2:=10;
  d3:=20;
  for i:=1 to n do
  begin
    X[i]:= random(20);
    writeln('X[',i,'] = ',X[i]);
  end;
  for i:=1 to n do
  begin
    if (X[i]>=d1) and (X[i]<d2) then
    begin
      y:= exp(ln(a+X[i]) * (1/k));
      writeln('Значение y = ',y ,'при X[',i,'] = ',X[i]);
    end
    else
      if (X[i]>d2) and (X[i]<=d3) then
      begin
        y:=f(X[i]);
        writeln('Значение y = ',y ,'при X[',i,'] = ',X[i]);
      end;
  end;
end.

    