program pr1;
var 
  x,y,a,b,c:integer;
begin
  repeat 
  write('Введите число ');
  read(x);
  a:=x mod 10;
  b:= (x mod 100)div 10;
  c:= x div 100;
  y:=a+b+c;
  writeln(y)
  until y<=10;
  
end.