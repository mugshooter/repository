program pr1;
function f(a,b,c:integer):real;
// a-граница суммы,b-факториал, c-последнее число
var
  i,u,d:integer;
  begin
    d:=1;
    for i:=1 to b do
      d:=d*i;
    u:=0;
    for i:=1 to a do 
      u:=u+(2*i+c);  
    f:=(u/d)
end;
var
  z:real;
  begin
    z:=f(10,3,1)+f(20,5,0)+f(40,8,3);
    writeln(z);
  end.
    