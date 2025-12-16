program pr2;
var
  n,i,a:integer;
  F:array[1..100] of integer;
begin
  writeln('Введите кол-во элементов массива');
  read(n);
  for i:= 1 to n do begin
    writeln('элемент массива №',i);
    read(F[i]);
  end;
  i:=1;
  while i<=n do begin
    a :=F[i];
    F[i]:=F[i+1];
    F[i+1]:=a;
    i:=i+2;
  end;
  writeln('Результат');
  for i:= 1 to n do
    write(F[i]);
end.