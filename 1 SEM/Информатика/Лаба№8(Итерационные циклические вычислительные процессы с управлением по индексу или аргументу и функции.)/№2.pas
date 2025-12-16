program pr2;
var x,U,S,e:real;
    k:integer;
function f(i:integer):integer;
var m,n:integer;
begin
  m:=1;
  for n:=1 to i do
    m:=m*n;
  f:=m
end;
begin
  e:=0.0001;
  k:=1;
  U:=1;
  S:=1;
  x:=0.5;
  while U>e do
  begin
    U:=(exp(k*ln(x))/f(k));
    S:=S+U;
    k:=k+1;
  end;
  writeln('e^x=',S:0:6);
end.