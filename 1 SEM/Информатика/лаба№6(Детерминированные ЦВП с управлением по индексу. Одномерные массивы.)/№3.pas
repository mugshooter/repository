program pr3;
var
  i:integer;
  A:array[1..5] of integer;
  B:array[1..5] of integer;
  C:array[1..10] of integer;
begin
  for i :=1 to 5 do begin
    writeln('Введите значение элеманта №' ,i,' массива A');
    readln(A[i]);
  end;
  for i :=1 to 5 do begin
    writeln('Введите значение элеманта №' ,i,' массива B');
    readln(B[i]);
  end;
  for i:= 1 to 5 do begin
    C[i]:=A[i];
    C[i+5]:=B[i];
  end;
  write('Массив C = ',C)  
end.