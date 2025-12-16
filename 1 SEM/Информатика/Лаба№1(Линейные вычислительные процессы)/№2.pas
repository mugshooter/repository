program pr2;
var
  a : integer;
  b,c,d,x : real;
begin
  read(a);
  d:=(a mod 10)* 100; 
  c:= (a -(a mod 100)) / 100; 
  b:=((a mod 100)-( a mod 10));     
  x:= d + c +b;
  write(x);                  
end.