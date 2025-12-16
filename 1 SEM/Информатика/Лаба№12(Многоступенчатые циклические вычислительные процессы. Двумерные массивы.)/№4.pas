program pr1;
var i,j,s:integer;
A: array[1..3,1..3] of integer;
B:array[1..3] of integer;
begin
  for i:=1 to 3 do
  begin
    for j:=1 to 3 do
    begin
      A[i,j]:= random(100);
      writeln('  A[',i,',',j,'] = ',A[i,j]);
      B[i]+= A[i,j];
    end;
  end;
  writeln('Суммы 1, 2 и 3 строки',B);
  writeln('Отсортированный массив сумм');
  for i := 1 to 3 - 1 do
    for j := 1 to 3 - i do
      if B[j] > B[j + 1] then begin
        s := B[j];
        B[j] := B[j + 1];
        B[j + 1] := s;
      end;
      for i:=1 to 3 do
         write(B[i],' ');
end.
