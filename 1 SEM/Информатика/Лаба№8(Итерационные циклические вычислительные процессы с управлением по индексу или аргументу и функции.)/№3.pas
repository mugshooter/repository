program pr3;
var k,a:integer;
    U,S,x,e:real;
function f(x:integer):integer;
var i,n:integer;
begin
  n:=1;
  for i:=1 to x do
    n:=n*i;
    f:=n;
    end;
begin
  x:=Pi/6;
  U:=x;
  S:=x;
  k:=1;
  e:=0.0001;
  while abs(U)>e do
  begin
    a:=2*k+1;
    if (k div 2<>0) then
      U:=(-1)*(exp(a*ln(x))/f(a))
    else
      U:=(exp(a*ln(x))/f(a));
    s:=S+U;
    k:=k+1;
  end;
  writeln('sin(x)=',s:0:6);
end. 