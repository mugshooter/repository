program pr1;
var i,j,S,m:integer;
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
begin
  for j:=1 to 3 do
  begin
    S:=S+A[i,j];
    if A[i,j]>m then
      m:=A[i,j];
    end;
  end;
  writeln('S = ',S,' m = ',m);
end.