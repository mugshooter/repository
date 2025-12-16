program pr1;
var
  a,i,n:integer;
begin
  a:=1;
  read(n);
  for i:=1 to n do
    a:= a*i;
  writeln(a);
end.