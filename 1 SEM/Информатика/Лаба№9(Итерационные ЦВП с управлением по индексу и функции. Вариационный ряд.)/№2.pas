program pr2;
var
  M:array[1..10] of integer = (42069,78,36,21,86,5,9,1043,1,111);
  i,j,n:integer;
  begin
    for i:=1 to 9 do begin
      for j :=(i+1) to 10 do begin
        if M[i]<M[j] then
        begin
          n:=M[i];
          M[i]:=M[j];
          M[j]:=n;
        end;
      end;
  end;
writeln(M);
end.