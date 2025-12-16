program pr1;
const
  M:array[1..10] of integer = (6,7,3,2,8,5,9,10,1,11);
var
  i,n,s:integer;
begin
  readln(n);
  s:=0;
  for i:=1 to 10 do
    if M[i]>n then
    begin
      s:=s+M[i];
      writeln('Индекс элемента, который больше введёного числа ',i);
    end;
    writeln(s)
end.