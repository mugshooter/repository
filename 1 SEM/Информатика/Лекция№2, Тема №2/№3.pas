program pr3;
var 
  f1,f2:integer;
  r:real;
begin
  f1:=6;
  f2:=12;
  r:=((f2/f1)*(1+0.707*sqrt(1-f1/f2))-1)*((f2/f1)*(1+0.707*sqrt(1-f1/f2))-1);
  write(r)
end.
