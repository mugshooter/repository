program pr2;
var i,j,Sg,Sp:integer;
A: array[1..3,1..3] of integer;
begin
  for i:=1 to 3 do
  begin
    for j:=1 to 3 do
    begin
      A[i,j]:= random(100);
      writeln('  A[',i,',',j,'] = ',A[i,j]);
    end;
  end;
  for i:=1 to 3 do
    Sg:=Sg+A[i,i];
  writeln('Sg = ',Sg);
  for i:=1 to 3 do
    Sp:=Sp+A[i,3-i+1];
  writeln('Sp = ', Sp)
  end.