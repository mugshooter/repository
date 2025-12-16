program pr1;
var
  A,B,C: integer;
  x,y:real;
begin
  A:=3;
  B:=4;
  C:=2;
  x:=(A*C-sqrt(A*A+B*B-C*C))/(A*A+B*B);
  y:=Arctan(x/sqrt(1-sqrt(x)));
  write(y)
end.