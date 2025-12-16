program pr3;
var i,j:integer;
A: array[1..3,1..3] of integer;
begin
  writeln('Исходная матрица');
  for i:=1 to 3 do
  begin
    for j:=1 to 3 do
    begin
      A[i,j]:= random(100);
      writeln(' A[',i,',',j,'] = ',A[i,j]);
    end;
  end;
  writeln();
  writeln('Полученная матрица');
  for i:=1 to 3 do
  begin
    for j:=1 to 3 do
    begin
      if i>j then
        A[i,j]:=0;
      writeln(' A[',i,',',j,'] = ',A[i,j]);
      end;     
    end;
  end.
